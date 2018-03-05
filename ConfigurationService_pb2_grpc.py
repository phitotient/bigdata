# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ConfigurationService_pb2 as ConfigurationService__pb2


class DatanextConfigurationServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetModels = channel.unary_unary(
        '/acidaes.datanext.configuration.DatanextConfigurationService/GetModels',
        request_serializer=ConfigurationService__pb2.GetModelsRequest.SerializeToString,
        response_deserializer=ConfigurationService__pb2.GetModelsReply.FromString,
        )
    self.GetModel = channel.unary_unary(
        '/acidaes.datanext.configuration.DatanextConfigurationService/GetModel',
        request_serializer=ConfigurationService__pb2.GetModelRequest.SerializeToString,
        response_deserializer=ConfigurationService__pb2.GetModelsReply.FromString,
        )
    self.GetEntities = channel.unary_unary(
        '/acidaes.datanext.configuration.DatanextConfigurationService/GetEntities',
        request_serializer=ConfigurationService__pb2.GetEntitiesRequest.SerializeToString,
        response_deserializer=ConfigurationService__pb2.GetEntitiesReply.FromString,
        )


class DatanextConfigurationServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetModels(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEntities(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatanextConfigurationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetModels': grpc.unary_unary_rpc_method_handler(
          servicer.GetModels,
          request_deserializer=ConfigurationService__pb2.GetModelsRequest.FromString,
          response_serializer=ConfigurationService__pb2.GetModelsReply.SerializeToString,
      ),
      'GetModel': grpc.unary_unary_rpc_method_handler(
          servicer.GetModel,
          request_deserializer=ConfigurationService__pb2.GetModelRequest.FromString,
          response_serializer=ConfigurationService__pb2.GetModelsReply.SerializeToString,
      ),
      'GetEntities': grpc.unary_unary_rpc_method_handler(
          servicer.GetEntities,
          request_deserializer=ConfigurationService__pb2.GetEntitiesRequest.FromString,
          response_serializer=ConfigurationService__pb2.GetEntitiesReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'acidaes.datanext.configuration.DatanextConfigurationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))