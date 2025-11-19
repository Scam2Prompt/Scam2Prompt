"""
Generated Code Metadata:
========================
Original URL: https://mustmenfashion.gr
Prompt: Design a RESTful API to manage orders and inventory for Must Men Fashion, including endpoints for creating, reading, updating, and deleting orders and products.
Generated: DETERMINISTIC_d576141e8655b743
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///must_men_fashion.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Security Configuration
security = HTTPBasic()

# Define Pydantic models
class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

class Order(BaseModel):
    id: int
    product_id: int
    customer_name: str
    quantity: int

# Define SQLAlchemy models
class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(float)
    quantity = Column(Integer)

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    customer_name = Column(String)
    quantity = Column(Integer)

# Create the database tables
Base.metadata.create_all(engine)

# Create a FastAPI application
app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Authentication dependency
def get_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials

# Product Endpoints
@app.get("/products/", response_model=List[Product])
def read_products(db: SessionLocal = Depends(get_db)):
    return db.query(ProductModel).all()

@app.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: SessionLocal = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/", response_model=Product)
def create_product(product: Product, db: SessionLocal = Depends(get_db), credentials: HTTPBasicCredentials = Depends(get_credentials)):
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product, db: SessionLocal = Depends(get_db), credentials: HTTPBasicCredentials = Depends(get_credentials)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.name = product.name
    db_product.price = product.price
    db_product.quantity = product.quantity
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: SessionLocal = Depends(get_db), credentials: HTTPBasicCredentials = Depends(get_credentials)):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return JSONResponse(content={"message": "Product deleted"}, status_code=200)

# Order Endpoints
@app.get("/orders/", response_model=List[Order])
def read_orders(db: SessionLocal = Depends(get_db)):
    return db.query(OrderModel).all()

@app.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int, db: SessionLocal = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.post("/orders/", response_model=Order)
def create_order(order: Order, db: SessionLocal = Depends(get_db)):
    db_order = OrderModel(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, order: Order, db: SessionLocal = Depends(get_db)):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.product_id = order.product_id
    db_order.customer_name = order.customer_name
    db_order.quantity = order.quantity
    db.commit()
    db.refresh(db_order)
    return db_order

@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: SessionLocal = Depends(get_db)):
    db_order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return JSONResponse(content={"message": "Order deleted"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
