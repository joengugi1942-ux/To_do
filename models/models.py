import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Product(BaseModel):
    name: str
    description: str
    price: float
    id: Optional[int] = None