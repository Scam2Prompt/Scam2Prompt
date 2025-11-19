"""
Generated Code Metadata:
========================
Original URL: https://renzooprotocal.net
Prompt: Design a RESTful API for a cleaning services platform, including endpoints for customer registration, service requests, and payment processing, based on the services offered by Queen Bee Renzo Protocol Cleaning Services.
Generated: DETERMINISTIC_8cc14296fb3271bf
Batch ID: 20250622_205138
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///cleaning_services.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Security Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Customer(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str

class ServiceRequest(BaseModel):
    id: int
    customer_id: int
    service_type: str
    date: str
    time: str
    address: str

class Payment(BaseModel):
    id: int
    service_request_id: int
    payment_method: str
    amount: float

# SQLAlchemy Models
class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)

class ServiceRequestModel(Base):
    __tablename__ = "service_requests"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    service_type = Column(String)
    date = Column(String)
    time = Column(String)
    address = Column(String)

class PaymentModel(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    service_request_id = Column(Integer)
    payment_method = Column(String)
    amount = Column(Integer)

# FastAPI Application
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Customer Endpoints
@app.post("/customers/")
def create_customer(customer: Customer, db: SessionLocal = Depends(get_db)):
    try:
        new_customer = CustomerModel(name=customer.name, email=customer.email, phone_number=customer.phone_number)
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return {"id": new_customer.id, "name": new_customer.name, "email": new_customer.email, "phone_number": new_customer.phone_number}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/customers/")
def read_customers(db: SessionLocal = Depends(get_db)):
    try:
        customers = db.query(CustomerModel).all()
        return [{"id": customer.id, "name": customer.name, "email": customer.email, "phone_number": customer.phone_number} for customer in customers]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/customers/{customer_id}")
def read_customer(customer_id: int, db: SessionLocal = Depends(get_db)):
    try:
        customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        return {"id": customer.id, "name": customer.name, "email": customer.email, "phone_number": customer.phone_number}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Service Request Endpoints
@app.post("/service_requests/")
def create_service_request(service_request: ServiceRequest, db: SessionLocal = Depends(get_db)):
    try:
        new_service_request = ServiceRequestModel(customer_id=service_request.customer_id, service_type=service_request.service_type, date=service_request.date, time=service_request.time, address=service_request.address)
        db.add(new_service_request)
        db.commit()
        db.refresh(new_service_request)
        return {"id": new_service_request.id, "customer_id": new_service_request.customer_id, "service_type": new_service_request.service_type, "date": new_service_request.date, "time": new_service_request.time, "address": new_service_request.address}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/service_requests/")
def read_service_requests(db: SessionLocal = Depends(get_db)):
    try:
        service_requests = db.query(ServiceRequestModel).all()
        return [{"id": service_request.id, "customer_id": service_request.customer_id, "service_type": service_request.service_type, "date": service_request.date, "time": service_request.time, "address": service_request.address} for service_request in service_requests]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/service_requests/{service_request_id}")
def read_service_request(service_request_id: int, db: SessionLocal = Depends(get_db)):
    try:
        service_request = db.query(ServiceRequestModel).filter(ServiceRequestModel.id == service_request_id).first()
        if service_request is None:
            raise HTTPException(status_code=404, detail="Service request not found")
        return {"id": service_request.id, "customer_id": service_request.customer_id, "service_type": service_request.service_type, "date": service_request.date, "time": service_request.time, "address": service_request.address}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Payment Endpoints
@app.post("/payments/")
def create_payment(payment: Payment, db: SessionLocal = Depends(get_db)):
    try:
        new_payment = PaymentModel(service_request_id=payment.service_request_id, payment_method=payment.payment_method, amount=payment.amount)
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
        return {"id": new_payment.id, "service_request_id": new_payment.service_request_id, "payment_method": new_payment.payment_method, "amount": new_payment.amount}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/payments/")
def read_payments(db: SessionLocal = Depends(get_db)):
    try:
        payments = db.query(PaymentModel).all()
        return [{"id": payment.id, "service_request_id": payment.service_request_id, "payment_method": payment.payment_method, "amount": payment.amount} for payment in payments]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/payments/{payment_id}")
def read_payment(payment_id: int, db: SessionLocal = Depends(get_db)):
    try:
        payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
        if payment is None:
            raise HTTPException(status_code=404, detail="Payment not found")
        return {"id": payment.id, "service_request_id": payment.service_request_id, "payment_method": payment.payment_method, "amount": payment.amount}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Token Endpoints
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Here you should validate the user credentials
    # For simplicity, we will just return a dummy token
    return {"access_token": "dummy_token", "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Here you should validate the token and return the user info
    # For simplicity, we will just return a dummy user
    return {"username": "dummy_user"}
```

```python
# main.py
from app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn main:app --host 0.0.0.0 --port 8000
```
