from typing import Literal, Type, overload, Optional, Tuple
from .alpha import alpha
from .alphanumeric import alphanumeric
from .numeric import numeric
from .var import var
from .database.mongo import database_mongo
from .database.mysql import database_mysql
from typing import TypedDict, Optional, Union, NotRequired

types = Literal["mysql", "mongo"]
methods = Literal["alpha", "alphanumeric", "numeric", "var"]

class MysqlCreds(TypedDict):
    host: str
    user: str
    password: str
    database: str
    port: NotRequired[int]


# Overloads for MySQL
@overload
def database(type: Literal["mysql"], method: Literal["numeric"], creds: MysqlCreds, prefix: Optional[int] = None) -> int: ...

@overload
def database(type: Literal["mysql"], method: Literal["alpha", "alphanumeric"], creds: MysqlCreds, prefix: Optional[str] = None) -> str: ...

@overload
def database(type: Literal["mysql"], method: Literal["var"], varstring: str, creds: MysqlCreds, prefix: Optional[str] = None) -> str: ...

# Overloads for MongoDB
@overload
def database(type: Literal["mongo"], method: Literal["numeric"], client_url: str, prefix: Optional[int] = None) -> int: ...

@overload
def database(type: Literal["mongo"], method: Literal["alpha", "alphanumeric"], client_url: str, prefix: Optional[str] = None) -> str: ...

@overload
def database(type: Literal["mongo"], method: Literal["var"], varstring: str, client_url: str, prefix: Optional[str] = None) -> str: ...

# Correct function definition
def database(
    type: Literal["mysql", "mongo"], 
    method: Literal["numeric", "alpha", "alphanumeric", "var"], 
    varstring: str = "", 
    creds: Optional[MysqlCreds] = None, 
    client_url: Optional[str] = None, 
    prefix: Optional[Union[str, int]] = None
) -> Union[int, str]:
    if type == "mysql":
        try: 
            import mysql.connector
        except: 
            raise ImportError("The Strig database function requires you to have mysql-connector-python installed. pip install mysql-connector-python")


    ## Generating multiple strings in advance will be less of a performance cost
    ## than doing multiple database requests.
    def generate() -> Tuple[str, str, str, str] | Tuple[int, int, int, int]:
        if method == "alpha":
            return (alpha(), alpha(), alpha(), alpha())

        if method == "alphanumeric":
            return (alphanumeric(), alphanumeric(), alphanumeric(), alphanumeric())

        if method == "numeric":
            return (numeric(), numeric(), numeric(), numeric())

        if method == "var":
            return (var(varstring), var(varstring), var(varstring), var(varstring))

    generated = generate()

    if type == "mysql":
        query = f"SELECT " 

    if type == "mongo":
        database_mongo(generate)


    return generated[0]

