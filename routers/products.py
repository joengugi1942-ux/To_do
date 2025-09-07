from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

router = APIRouter()


products = [
    {"id": 1, "name": "phone", "price": 474, "quantity": 60},
    {"id": 2, "name": "laptop", "price": 1500, "quantity": 70},
    {"id": 3, "name": "ipad", "price": 474, "quantity": 30},
    {"id": 4, "name": "tablet", "price": 474, "quantity": 57}
]


@router.get('/products', response_model=List[Dict[str, Any]])
def get_products():
    return products


@router.get('/products/{product_id}', response_model=Dict[str, Any])
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.post('/products', response_model=Dict[str, Any])
def create_product(product: dict):
    # Generate new ID
    new_id = max(p["id"] for p in products) + 1 if products else 1
    new_product = {"id": new_id, **product}
    products.append(new_product)
    return new_product


@router.put('/products/{product_id}', response_model=Dict[str, Any])
def update_product(product_id: int, product_data: dict):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            # Update the product with new data, keeping the same ID
            updated_product = {"id": product_id, **product_data}
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete('/products/{product_id}')
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)
            return {"message": "Product deleted", "deleted_product": deleted_product}
    raise HTTPException(status_code=404, detail="Product not found")