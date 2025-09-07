from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from routers import products


app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["Products"])



@app.get("/products", response_model=List[ProductResponse])
def get_products(session: Session = Depends(get_session)):
    result = session.execute(select(Product))
    products = result.scalars().all()
    return products



@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product



@app.post("/products", response_model=ProductResponse)
def create_product(product_data: ProductCreate, session: Session = Depends(get_session)):

    new_product = Product(**product_data.dict())
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product



@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_data: ProductCreate, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product_data.dict().items():
        setattr(product, key, value)

    session.commit()
    session.refresh(product)
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    session.delete(product)
    session.commit()
    return {"message": "Product deleted successfully"}