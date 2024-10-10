from typing import Callable

def database_mongo(generate: Callable):
    if type == "mongo":
        try:
            import pymongo
        except: 
            raise ImportError("The Strig database function requires you to have pymongo installed. pip install pymongo")

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    return generate()
