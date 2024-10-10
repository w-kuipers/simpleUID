from typing import Callable

def database_mongo(generate: Callable, creds):
    if type == "mysql":
        try: 
            import mysql.connector
        except: 
            raise ImportError("The Strig database function requires you to have mysql-connector-python installed. pip install mysql-connector-python")

    my  

    return generate()
