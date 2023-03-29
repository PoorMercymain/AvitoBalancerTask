# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import auth_pb2 as auth__pb2


class AuthStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckAuth = channel.unary_unary(
                '/api.Auth/CheckAuth',
                request_serializer=auth__pb2.AuthRequest.SerializeToString,
                response_deserializer=auth__pb2.AuthResponse.FromString,
                )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckAuth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckAuth': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAuth,
                    request_deserializer=auth__pb2.AuthRequest.FromString,
                    response_serializer=auth__pb2.AuthResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.Auth', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckAuth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Auth/CheckAuth',
            auth__pb2.AuthRequest.SerializeToString,
            auth__pb2.AuthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
