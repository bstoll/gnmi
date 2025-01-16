/*
Copyright 2017 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// Package value provides utility functions for working with gNMI TypedValue
// messages.
package value

import (
	"encoding/json"
	"fmt"
	"math"
	"unicode/utf8"

	gpb "github.com/openconfig/gnmi/proto/gnmi"
)

// FromScalar will convert common scalar types to their TypedValue equivalent.
// It will return an error if the type cannot be mapped to a scalar value.
func FromScalar(i interface{}) (*gpb.TypedValue, error) {
	tv := &gpb.TypedValue{}
	switch v := i.(type) {
	case string:
		if utf8.ValidString(v) {
			tv.Value = &gpb.TypedValue_StringVal{StringVal: v}
		} else {
			return nil, fmt.Errorf("string %q contains non-UTF-8 bytes", v)
		}
	case int:
		tv.Value = &gpb.TypedValue_IntVal{IntVal: int64(v)}
	case int8:
		tv.Value = &gpb.TypedValue_IntVal{IntVal: int64(v)}
	case int16:
		tv.Value = &gpb.TypedValue_IntVal{IntVal: int64(v)}
	case int32:
		tv.Value = &gpb.TypedValue_IntVal{IntVal: int64(v)}
	case int64:
		tv.Value = &gpb.TypedValue_IntVal{IntVal: v}
	case uint:
		tv.Value = &gpb.TypedValue_UintVal{UintVal: uint64(v)}
	case uint8:
		tv.Value = &gpb.TypedValue_UintVal{UintVal: uint64(v)}
	case uint16:
		tv.Value = &gpb.TypedValue_UintVal{UintVal: uint64(v)}
	case uint32:
		tv.Value = &gpb.TypedValue_UintVal{UintVal: uint64(v)}
	case uint64:
		tv.Value = &gpb.TypedValue_UintVal{UintVal: v}
	case float32:
		tv.Value = &gpb.TypedValue_DoubleVal{DoubleVal: float64(v)}
	case float64:
		tv.Value = &gpb.TypedValue_DoubleVal{DoubleVal: v}
	case bool:
		tv.Value = &gpb.TypedValue_BoolVal{BoolVal: v}
	case []string:
		sa := &gpb.ScalarArray{Element: make([]*gpb.TypedValue, len(v))}
		for x, s := range v {
			sa.Element[x] = &gpb.TypedValue{Value: &gpb.TypedValue_StringVal{StringVal: s}}
		}
		tv.Value = &gpb.TypedValue_LeaflistVal{LeaflistVal: sa}
	case []byte:
		tv.Value = &gpb.TypedValue_BytesVal{BytesVal: v}
	case []interface{}:
		sa := &gpb.ScalarArray{Element: make([]*gpb.TypedValue, len(v))}
		var err error
		for x, intf := range v {
			sa.Element[x], err = FromScalar(intf)
			if err != nil {
				return nil, fmt.Errorf("in []interface{}: %v", err)
			}
		}
		tv.Value = &gpb.TypedValue_LeaflistVal{LeaflistVal: sa}
	default:
		return nil, fmt.Errorf("non-scalar type %+v", i)
	}
	return tv, nil
}

// DeprecatedScalar is a scalar wrapper for communicating our desire to remove
// this encoding from gNMI support.
type DeprecatedScalar struct {
	Message string
	Value   interface{}
}

// ToScalar will convert TypedValue scalar types to a Go native type. It will
// return an error if the TypedValue does not contain a scalar type.
func ToScalar(tv *gpb.TypedValue) (interface{}, error) {
	var i interface{}
	switch tv.GetValue().(type) {
	case *gpb.TypedValue_DecimalVal:
		i = decimalToFloat(tv.GetDecimalVal())
	case *gpb.TypedValue_StringVal:
		i = tv.GetStringVal()
	case *gpb.TypedValue_IntVal:
		i = tv.GetIntVal()
	case *gpb.TypedValue_UintVal:
		i = tv.GetUintVal()
	case *gpb.TypedValue_BoolVal:
		i = tv.GetBoolVal()
	case *gpb.TypedValue_FloatVal:
		i = tv.GetFloatVal()
	case *gpb.TypedValue_DoubleVal:
		i = tv.GetDoubleVal()
	case *gpb.TypedValue_LeaflistVal:
		elems := tv.GetLeaflistVal().GetElement()
		ss := make([]interface{}, len(elems))
		for x, e := range elems {
			v, err := ToScalar(e)
			if err != nil {
				return nil, fmt.Errorf("ToScalar for ScalarArray %+v: %v", e.Value, err)
			}
			ss[x] = v
		}
		i = ss
	case *gpb.TypedValue_BytesVal:
		i = tv.GetBytesVal()
	case *gpb.TypedValue_JsonVal:
		v := tv.GetJsonVal()
		if err := json.Unmarshal(v, &i); err != nil {
			return nil, err
		}
		uVal := DeprecatedScalar{
			Message: "Deprecated TypedValue_JsonVal",
			Value:   i,
		}
		return uVal, nil
	case *gpb.TypedValue_JsonIetfVal:
		v := tv.GetJsonIetfVal()
		if err := json.Unmarshal(v, &i); err != nil {
			return nil, err
		}
		uVal := DeprecatedScalar{
			Message: "Deprecated TypedValue_JsonIetfVal",
			Value:   i,
		}
		return uVal, nil
	default:
		return nil, fmt.Errorf("non-scalar type %+v", tv.Value)
	}
	return i, nil
}

// decimalToFloat converts a *gnmi_proto.Decimal64 to a float32. Downcasting to
// float32 is performed as the precision of a float64 is not required.
func decimalToFloat(d *gpb.Decimal64) float32 {
	return float32(float64(d.Digits) / math.Pow(10, float64(d.Precision)))
}

// Equal returns true if the values in a and b are the same.  This method
// handles only the primitive types and ScalarArrays and returns false for all
// other types.
func Equal(a, b *gpb.TypedValue) bool {
	switch av := a.GetValue().(type) {
	case *gpb.TypedValue_StringVal:
		bv, ok := b.GetValue().(*gpb.TypedValue_StringVal)
		if !ok {
			return false
		}
		return av.StringVal == bv.StringVal
	case *gpb.TypedValue_IntVal:
		bv, ok := b.GetValue().(*gpb.TypedValue_IntVal)
		if !ok {
			return false
		}
		return av.IntVal == bv.IntVal
	case *gpb.TypedValue_UintVal:
		bv, ok := b.GetValue().(*gpb.TypedValue_UintVal)
		if !ok {
			return false
		}
		return av.UintVal == bv.UintVal
	case *gpb.TypedValue_BoolVal:
		bv, ok := b.GetValue().(*gpb.TypedValue_BoolVal)
		if !ok {
			return false
		}
		return av.BoolVal == bv.BoolVal
	case *gpb.TypedValue_BytesVal:
		bv, ok := b.GetValue().(*gpb.TypedValue_BytesVal)
		if !ok {
			return false
		}
		return string(av.BytesVal) == string(bv.BytesVal)
	case *gpb.TypedValue_DoubleVal:
		bv, ok := b.Value.(*gpb.TypedValue_DoubleVal)
		if !ok {
			return false
		}
		return av.DoubleVal == bv.DoubleVal
	case *gpb.TypedValue_FloatVal:
		bv, ok := b.GetValue().(*gpb.TypedValue_FloatVal)
		if !ok {
			return false
		}
		return av.FloatVal == bv.FloatVal
	case *gpb.TypedValue_DecimalVal:
		bv, ok := b.GetValue().(*gpb.TypedValue_DecimalVal)
		if !ok {
			return false
		}
		return av.DecimalVal.Digits == bv.DecimalVal.Digits && av.DecimalVal.Precision == bv.DecimalVal.Precision
	case *gpb.TypedValue_LeaflistVal:
		bv, ok := b.GetValue().(*gpb.TypedValue_LeaflistVal)
		if !ok {
			return false
		}
		ae, be := av.LeaflistVal.Element, bv.LeaflistVal.Element
		if len(ae) != len(be) {
			return false
		}
		for i := range ae {
			if !Equal(ae[i], be[i]) {
				return false
			}
		}
		return true
	}
	// Types that are not primitive or ScalarArray are not considered.
	return false
}
