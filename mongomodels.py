from pymongo import MongoClient

connectionstring="mongodb://mongodb:acid_123@35.227.40.31:27017/models"
databasename="models"
collectionname="modelidwithguid"
   # def generatemongoclient(self,connectionstring,databasename,collectionname):
client=MongoClient("mongodb://mongodb:acid_123@35.227.40.31:27017/models")
db = client["models"]
table = db["modelidwithguid"]
#return table

    #def findmodelbyid(self,modelid,table):
result=table.find_one({"modelid":2,"ownerid":1})
print(result)

