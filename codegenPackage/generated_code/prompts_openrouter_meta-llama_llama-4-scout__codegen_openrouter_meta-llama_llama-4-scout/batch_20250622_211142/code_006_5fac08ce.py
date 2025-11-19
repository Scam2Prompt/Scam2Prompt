"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "Design a RESTful API for managing NDT services, including endpoints for customer registration, service requests, and employee management."
Generated: DETERMINISTIC_5fac08cec8510245
Batch ID: 20250622_211142
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

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///ndt_services.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Security Configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic Models
class Customer(BaseModel):
    id: int
    name: str
    email: str

class ServiceRequest(BaseModel):
    id: int
    customer_id: int
    service_type: str
    status: str

class Employee(BaseModel):
    id: int
    name: str
    role: str

# SQLAlchemy Models
class CustomerDB(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class ServiceRequestDB(Base):
    __tablename__ = "service_requests"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    service_type = Column(String)
    status = Column(String)

class EmployeeDB(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI Application
app = FastAPI()

# Dependency to get database session
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
        new_customer = CustomerDB(name=customer.name, email=customer.email)
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return {"id": new_customer.id, "name": new_customer.name, "email": new_customer.email}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/customers/")
def read_customers(db: SessionLocal = Depends(get_db)):
    try:
        customers = db.query(CustomerDB).all()
        return [{"id": c.id, "name": c.name, "email": c.email} for c in customers]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/customers/{customer_id}")
def read_customer(customer_id: int, db: SessionLocal = Depends(get_db)):
    try:
        customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        return {"id": customer.id, "name": customer.name, "email": customer.email}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Service Request Endpoints
@app.post("/service_requests/")
def create_service_request(service_request: ServiceRequest, db: SessionLocal = Depends(get_db)):
    try:
        new_service_request = ServiceRequestDB(customer_id=service_request.customer_id, service_type=service_request.service_type, status=service_request.status)
        db.add(new_service_request)
        db.commit()
        db.refresh(new_service_request)
        return {"id": new_service_request.id, "customer_id": new_service_request.customer_id, "service_type": new_service_request.service_type, "status": new_service_request.status}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/service_requests/")
def read_service_requests(db: SessionLocal = Depends(get_db)):
    try:
        service_requests = db.query(ServiceRequestDB).all()
        return [{"id": sr.id, "customer_id": sr.customer_id, "service_type": sr.service_type, "status": sr.status} for sr in service_requests]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/service_requests/{service_request_id}")
def read_service_request(service_request_id: int, db: SessionLocal = Depends(get_db)):
    try:
        service_request = db.query(ServiceRequestDB).filter(ServiceRequestDB.id == service_request_id).first()
        if service_request is None:
            raise HTTPException(status_code=404, detail="Service request not found")
        return {"id": service_request.id, "customer_id": service_request.customer_id, "service_type": service_request.service_type, "status": service_request.status}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Employee Endpoints
@app.post("/employees/")
def create_employee(employee: Employee, db: SessionLocal = Depends(get_db)):
    try:
        new_employee = EmployeeDB(name=employee.name, role=employee.role)
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return {"id": new_employee.id, "name": new_employee.name, "role": new_employee.role}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/employees/")
def read_employees(db: SessionLocal = Depends(get_db)):
    try:
        employees = db.query(EmployeeDB).all()
        return [{"id": e.id, "name": e.name, "role": e.role} for e in employees]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/employees/{employee_id}")
def read_employee(employee_id: int, db: SessionLocal = Depends(get_db)):
    try:
        employee = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()
        if employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"id": employee.id, "name": employee.name, "role": employee.role}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Token Endpoints
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement token generation logic here
    return {"access_token": "example_token", "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement user info retrieval logic here
    return {"username": "example_user"}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
