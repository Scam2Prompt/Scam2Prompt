"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: "Design a RESTful API for an online store selling organic seeds, including endpoints for product retrieval, order creation, and payment processing, inspired by Semillas Plantae."
Generated: DETERMINISTIC_359a6df6088103c8
Batch ID: 20250622_205436
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
import stripe

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///seeds.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Stripe Payment Gateway Configuration
stripe.api_key = "YOUR_STRIPE_API_KEY"

# FastAPI App
app = FastAPI()

# OAuth2 Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Seed(BaseModel):
    id: int
    name: str
    description: str
    price: float

class Order(BaseModel):
    seed_id: int
    quantity: int

class Payment(BaseModel):
    order_id: int
    payment_method: str
    payment_token: str

# SQLAlchemy Models
class SeedModel(Base):
    __tablename__ = "seeds"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    seed_id = Column(Integer)
    quantity = Column(Integer)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# Dependency to get current user (not implemented)
def get_current_user(token: str = Depends(oauth2_scheme)):
    # TO DO: Implement user authentication
    return token

# Create database tables
Base.metadata.create_all(bind=engine)

# Endpoints
@app.get("/seeds/")
def read_seeds(db: SessionLocal = Depends(get_db)):
    """Retrieve a list of all seeds"""
    seeds = db.query(SeedModel).all()
    return [{"id": seed.id, "name": seed.name, "description": seed.description, "price": seed.price} for seed in seeds]

@app.get("/seeds/{seed_id}")
def read_seed(seed_id: int, db: SessionLocal = Depends(get_db)):
    """Retrieve a seed by ID"""
    seed = db.query(SeedModel).filter(SeedModel.id == seed_id).first()
    if seed is None:
        raise HTTPException(status_code=404, detail="Seed not found")
    return {"id": seed.id, "name": seed.name, "description": seed.description, "price": seed.price}

@app.post("/orders/")
def create_order(order: Order, db: SessionLocal = Depends(get_db)):
    """Create a new order"""
    seed = db.query(SeedModel).filter(SeedModel.id == order.seed_id).first()
    if seed is None:
        raise HTTPException(status_code=404, detail="Seed not found")
    new_order = OrderModel(seed_id=order.seed_id, quantity=order.quantity)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"id": new_order.id, "seed_id": new_order.seed_id, "quantity": new_order.quantity}

@app.post("/payments/")
def process_payment(payment: Payment, db: SessionLocal = Depends(get_db)):
    """Process a payment for an order"""
    order = db.query(OrderModel).filter(OrderModel.id == payment.order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    try:
        # Create a Stripe charge
        charge = stripe.Charge.create(
            amount=int(order.quantity * 100),  # Convert to cents
            currency="usd",
            source=payment.payment_token,
            description="Payment for seed order",
        )
        # Update order status to paid
        order.status = "paid"
        db.commit()
        return {"payment_status": "success"}
    except stripe.error.CardError as e:
        raise HTTPException(status_code=400, detail="Payment failed")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # TO DO: Implement user authentication
    return {"access_token": "dummy_token", "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(current_user: str = Depends(get_current_user)):
    # TO DO: Implement user profile retrieval
    return {"username": "dummy_user"}
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
