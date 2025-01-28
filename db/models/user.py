from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None  # El campo id es opcional
    username:str
    email: str
   