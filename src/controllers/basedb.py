from src.models.basedb import DatabaseModel
from src import app
databaseModel = DatabaseModel()
class DatabaseController():
    def list(self):        
        data = databaseModel.lists()
        return data
    def create(self, base_datos):
        databaseModel.create(base_datos)
    def search(self, basedb):
        data = databaseModel.listTables(basedb)
        return data
