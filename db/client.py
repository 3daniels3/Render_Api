from pymongo import MongoClient

#db_client = MongoClient().local base de datos local

db_client = MongoClient(
    "mongodb+srv://api:api@cluster0.izru9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").dbFastapi
      #.test seria la base de datos
