// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.29.1
// source: github.com/openconfig/gnmi/proto/collector/collector.proto

package gnmi

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	Collector_Reconnect_FullMethodName = "/gnmi.Collector/Reconnect"
)

// CollectorClient is the client API for Collector service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type CollectorClient interface {
	Reconnect(ctx context.Context, in *ReconnectRequest, opts ...grpc.CallOption) (*Nil, error)
}

type collectorClient struct {
	cc grpc.ClientConnInterface
}

func NewCollectorClient(cc grpc.ClientConnInterface) CollectorClient {
	return &collectorClient{cc}
}

func (c *collectorClient) Reconnect(ctx context.Context, in *ReconnectRequest, opts ...grpc.CallOption) (*Nil, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(Nil)
	err := c.cc.Invoke(ctx, Collector_Reconnect_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// CollectorServer is the server API for Collector service.
// All implementations should embed UnimplementedCollectorServer
// for forward compatibility.
type CollectorServer interface {
	Reconnect(context.Context, *ReconnectRequest) (*Nil, error)
}

// UnimplementedCollectorServer should be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedCollectorServer struct{}

func (UnimplementedCollectorServer) Reconnect(context.Context, *ReconnectRequest) (*Nil, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Reconnect not implemented")
}
func (UnimplementedCollectorServer) testEmbeddedByValue() {}

// UnsafeCollectorServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to CollectorServer will
// result in compilation errors.
type UnsafeCollectorServer interface {
	mustEmbedUnimplementedCollectorServer()
}

func RegisterCollectorServer(s grpc.ServiceRegistrar, srv CollectorServer) {
	// If the following call pancis, it indicates UnimplementedCollectorServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&Collector_ServiceDesc, srv)
}

func _Collector_Reconnect_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ReconnectRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(CollectorServer).Reconnect(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Collector_Reconnect_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(CollectorServer).Reconnect(ctx, req.(*ReconnectRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Collector_ServiceDesc is the grpc.ServiceDesc for Collector service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Collector_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "gnmi.Collector",
	HandlerType: (*CollectorServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Reconnect",
			Handler:    _Collector_Reconnect_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "github.com/openconfig/gnmi/proto/collector/collector.proto",
}
