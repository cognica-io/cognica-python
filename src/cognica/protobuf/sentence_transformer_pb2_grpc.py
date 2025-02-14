# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import cognica.protobuf.sentence_transformer_pb2 as sentence__transformer__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in sentence_transformer_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SentenceTransformerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.encode = channel.unary_unary(
                '/cognica.rpc.sentence_transformer.SentenceTransformerService/encode',
                request_serializer=sentence__transformer__pb2.SentenceEncoderRequest.SerializeToString,
                response_deserializer=sentence__transformer__pb2.SentenceEncoderResponse.FromString,
                _registered_method=True)


class SentenceTransformerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def encode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SentenceTransformerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'encode': grpc.unary_unary_rpc_method_handler(
                    servicer.encode,
                    request_deserializer=sentence__transformer__pb2.SentenceEncoderRequest.FromString,
                    response_serializer=sentence__transformer__pb2.SentenceEncoderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cognica.rpc.sentence_transformer.SentenceTransformerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cognica.rpc.sentence_transformer.SentenceTransformerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SentenceTransformerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def encode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cognica.rpc.sentence_transformer.SentenceTransformerService/encode',
            sentence__transformer__pb2.SentenceEncoderRequest.SerializeToString,
            sentence__transformer__pb2.SentenceEncoderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class CrossEncoderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.predict = channel.unary_unary(
                '/cognica.rpc.sentence_transformer.CrossEncoderService/predict',
                request_serializer=sentence__transformer__pb2.CrossEncoderRequest.SerializeToString,
                response_deserializer=sentence__transformer__pb2.CrossEncoderResponse.FromString,
                _registered_method=True)


class CrossEncoderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CrossEncoderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'predict': grpc.unary_unary_rpc_method_handler(
                    servicer.predict,
                    request_deserializer=sentence__transformer__pb2.CrossEncoderRequest.FromString,
                    response_serializer=sentence__transformer__pb2.CrossEncoderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cognica.rpc.sentence_transformer.CrossEncoderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cognica.rpc.sentence_transformer.CrossEncoderService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CrossEncoderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cognica.rpc.sentence_transformer.CrossEncoderService/predict',
            sentence__transformer__pb2.CrossEncoderRequest.SerializeToString,
            sentence__transformer__pb2.CrossEncoderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class CLIPEncoderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.encode = channel.unary_unary(
                '/cognica.rpc.sentence_transformer.CLIPEncoderService/encode',
                request_serializer=sentence__transformer__pb2.CLIPEncoderRequest.SerializeToString,
                response_deserializer=sentence__transformer__pb2.CLIPEncoderResponse.FromString,
                _registered_method=True)


class CLIPEncoderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def encode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CLIPEncoderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'encode': grpc.unary_unary_rpc_method_handler(
                    servicer.encode,
                    request_deserializer=sentence__transformer__pb2.CLIPEncoderRequest.FromString,
                    response_serializer=sentence__transformer__pb2.CLIPEncoderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cognica.rpc.sentence_transformer.CLIPEncoderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cognica.rpc.sentence_transformer.CLIPEncoderService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CLIPEncoderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def encode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cognica.rpc.sentence_transformer.CLIPEncoderService/encode',
            sentence__transformer__pb2.CLIPEncoderRequest.SerializeToString,
            sentence__transformer__pb2.CLIPEncoderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class QAEncoderServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.predict = channel.unary_unary(
                '/cognica.rpc.sentence_transformer.QAEncoderService/predict',
                request_serializer=sentence__transformer__pb2.QAEncoderRequest.SerializeToString,
                response_deserializer=sentence__transformer__pb2.QAEncoderResponse.FromString,
                _registered_method=True)


class QAEncoderServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QAEncoderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'predict': grpc.unary_unary_rpc_method_handler(
                    servicer.predict,
                    request_deserializer=sentence__transformer__pb2.QAEncoderRequest.FromString,
                    response_serializer=sentence__transformer__pb2.QAEncoderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cognica.rpc.sentence_transformer.QAEncoderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cognica.rpc.sentence_transformer.QAEncoderService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class QAEncoderService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cognica.rpc.sentence_transformer.QAEncoderService/predict',
            sentence__transformer__pb2.QAEncoderRequest.SerializeToString,
            sentence__transformer__pb2.QAEncoderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
