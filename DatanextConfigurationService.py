import ConfigurationService_pb2_grpc
import ConfigurationService_pb2



class DatanextConfigurationService(ConfigurationService_pb2_grpc.DatanextConfigurationServiceServicer):
    def __init__(self):
        pass

    def GetModels(self, request, context):
        ownerid=request.OwnerId
        modelid=request.ModelId
        #return ConfigurationService_pb2.GetModelsReply()

    def GetModel(self, request, context):
        ownerid = request.OwnerId
        modelid = request.ModelId

    def GetEntities(self, request, context):
        ownerid=request.OwnerId
        entityname=request.EntityName
