from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    description: Optional[str] = None

class ProductResponse(ProductCreate):
    id: int

    class Config:
        orm_mode = True