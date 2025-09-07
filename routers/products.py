from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
router = APIRouter()


products = [
    {"id": 1, "name": "phone", "description": "model 42 2023", "price": 550},
    {"id": 2, "name": "laptop", "description": "hp i core3", "price": 1000},
    {"id": 3, "name": "television", "description": "TCL smart tv", "price": 550},
]

@router.get("/", response_model=List[Product])
def get_products():
    return products

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return product

@router.post("/", response_model=Product)
def create_product(product: Product):
    # Generate new ID
    new_id = max([p["id"] for p in products]) + 1 if products else 1
    product_dict = product.dict()
    product_dict["id"] = new_id
    products.append(product_dict)
    return product_dict


app.include_router(router, prefix="/products", tags=["Products"])


@app.get("/")
def root():
    return {"message": "Welcome to Products API"}
