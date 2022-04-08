import pymongo

class Database:
    def __init__(self,database,collection):
        connectionString = "mongodb+srv://admin:admin@bancoiot.df2gm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]

    def create(self, nome_sensor,valor_sensor,unidade,sensor_alarmado):
        return self.collection.insert_one({"Sensor": nome_sensor,"Temperatura":valor_sensor,"Unidade de medida":unidade,"Sensor Alarmado":sensor_alarmado})
    
    def resetDatabase(self):
        self.db.drop_collection(self.collection)