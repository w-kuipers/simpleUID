from typing import Literal, overload, Optional, Any
from .alpha import alpha
from .alphanumeric import alphanumeric
from .numeric import numeric
from .var import var

types = Literal["mysql", "mongo"]
methods = Literal["alpha", "alphanumeric", "numeric", "var"]

@overload
def database(type: types, method: Literal["numeric"]) -> int: ...

@overload
def database(type: types, method: Literal["alpha", "alphanumeric"]) -> str: ...

@overload
def database(type: types, method: Literal["var"], varstring: str) -> str: ...

def database(type: types, method: methods, varstring: str = "") -> str | int:
    if type == "mysql":
        try: 
            import mysql.connector
        except: 
            raise ImportError("The Strig database function requires you to have mysql-connector-python installed. pip install mysql-connector-python")

    def generate():
        if method == "alpha":
            return alpha()

        if method == "alphanumeric":
            return alphanumeric()

        if method == "numeric":
            return numeric()

        if method == "var":
            return var(varstring)

    generated = generate()
        


    return generated

