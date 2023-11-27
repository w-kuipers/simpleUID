from .simpleuid import * 
from typing import Optional

def alphanumeric(length:int = 10, prefix: Optional[str] = ""):
    return simpleuid.alphanumeric(length, prefix)

def numeric(length:int = 10, prefix: Optional[str] = ""):
    return simpleuid.numeric(length, prefix)
