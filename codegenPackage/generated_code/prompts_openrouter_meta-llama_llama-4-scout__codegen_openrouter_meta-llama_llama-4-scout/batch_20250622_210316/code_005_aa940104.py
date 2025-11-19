"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: "Design a RESTful API for managing orders and inventory of off-road vehicle accessories, including endpoints for retrieving product information and processing payments."
Generated: DETERMINISTIC_aa940104e97fd8f0
Batch ID: 20250622_210316
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///offroad_accessories.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

class Order(BaseModel):
    id: int
    product_id: int
    customer_name: str
    quantity: int

class Payment(BaseModel):
    order_id: int
    payment_method: str
    amount: float

# SQLAlchemy Models
class ProductDB(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    customer_name = Column(String)
    quantity = Column(Integer)

class PaymentDB(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    payment_method = Column(String)
    amount = Column(Float)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Endpoints
@app.get("/products/")
def read_products(db: SessionLocal = Depends(get_db)):
    """Retrieve a list of all products"""
    products = db.query(ProductDB).all()
    return [{"id": p.id, "name": p.name, "description": p.description, "price": p.price, "quantity": p.quantity} for p in products]

@app.get("/products/{product_id}")
def read_product(product_id: int, db: SessionLocal = Depends(get_db)):
    """Retrieve a product by ID"""
    product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"id": product.id, "name": product.name, "description": product.description, "price": product.price, "quantity": product.quantity}

@app.post("/orders/")
def create_order(order: Order, db: SessionLocal = Depends(get_db)):
    """Create a new order"""
    product = db.query(ProductDB).filter(ProductDB.id == order.product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.quantity < order.quantity:
        raise HTTPException(status_code=400, detail="Insufficient quantity")
    new_order = OrderDB(product_id=order.product_id, customer_name=order.customer_name, quantity=order.quantity)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"id": new_order.id, "product_id": new_order.product_id, "customer_name": new_order.customer_name, "quantity": new_order.quantity}

@app.post("/payments/")
def create_payment(payment: Payment, db: SessionLocal = Depends(get_db)):
    """Process a payment"""
    order = db.query(OrderDB).filter(OrderDB.id == payment.order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    new_payment = PaymentDB(order_id=payment.order_id, payment_method=payment.payment_method, amount=payment.amount)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return {"id": new_payment.id, "order_id": new_payment.order_id, "payment_method": new_payment.payment_method, "amount": new_payment.amount}

@app.get("/orders/")
def read_orders(db: SessionLocal = Depends(get_db)):
    """Retrieve a list of all orders"""
    orders = db.query(OrderDB).all()
    return [{"id": o.id, "product_id": o.product_id, "customer_name": o.customer_name, "quantity": o.quantity} for o in orders]

@app.get("/payments/")
def read_payments(db: SessionLocal = Depends(get_db)):
    """Retrieve a list of all payments"""
    payments = db.query(PaymentDB).all()
    return [{"id": p.id, "order_id": p.order_id, "payment_method": p.payment_method, "amount": p.amount} for p in payments]

# Error Handling
@app.exception_handler(SQLAlchemyError)
def handle_database_error(request, exc):
    return JSONResponse(status_code=500, content={"detail": "Database error"})

# Token Endpoints
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return {"access_token": "example_token", "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return {"username": "example_user"}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
