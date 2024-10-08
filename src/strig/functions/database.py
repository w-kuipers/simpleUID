from typing import Literal, overload, Optional, Tuple
from .alpha import alpha
from .alphanumeric import alphanumeric
from .numeric import numeric
from .var import var

types = Literal["mysql", "mongo"]
methods = Literal["alpha", "alphanumeric", "numeric", "var"]

@overload
def database(type: types, method: Literal["numeric"], prefix: Optional[int] = None) -> int: ...

@overload
def database(type: types, method: Literal["alpha", "alphanumeric"], prefix: Optional[str] = None) -> str: ...

@overload
def database(type: types, method: Literal["var"], varstring: str, prefix: Optional[str] = None) -> str: ...

def database(type: types, method: methods, varstring: str = "", prefix: Optional[str | int] = None) -> str | int:
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
         


    return generated[0]

