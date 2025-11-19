"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Design a RESTful API for managing BPL service center operations, including technician assignments, repair status updates, and customer feedback collection.
Generated: DETERMINISTIC_1a4695193aa8cc52
Batch ID: 20250622_211528
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
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///bpl_service_center.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class Technician(BaseModel):
    id: int
    name: str
    email: str

class ServiceRequest(BaseModel):
    id: int
    customer_name: str
    issue: str
    status: str

class CustomerFeedback(BaseModel):
    id: int
    service_request_id: int
    feedback: str

# SQLAlchemy Models
class TechnicianModel(Base):
    __tablename__ = "technicians"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class ServiceRequestModel(Base):
    __tablename__ = "service_requests"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    issue = Column(String)
    status = Column(String)

class CustomerFeedbackModel(Base):
    __tablename__ = "customer_feedback"

    id = Column(Integer, primary_key=True)
    service_request_id = Column(Integer)
    feedback = Column(String)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# OAuth2 Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Error Handling
class ErrorResponse(BaseModel):
    error: str

# Endpoints
@app.post("/technicians/")
def create_technician(technician: Technician, db: SessionLocal = Depends(get_db)):
    try:
        db_technician = TechnicianModel(name=technician.name, email=technician.email)
        db.add(db_technician)
        db.commit()
        db.refresh(db_technician)
        return JSONResponse(content={"id": db_technician.id, "name": db_technician.name, "email": db_technician.email}, status_code=201)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/technicians/")
def read_technicians(db: SessionLocal = Depends(get_db)):
    try:
        technicians = db.query(TechnicianModel).all()
        return JSONResponse(content=[{"id": t.id, "name": t.name, "email": t.email} for t in technicians], status_code=200)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/service_requests/")
def create_service_request(service_request: ServiceRequest, db: SessionLocal = Depends(get_db)):
    try:
        db_service_request = ServiceRequestModel(customer_name=service_request.customer_name, issue=service_request.issue, status=service_request.status)
        db.add(db_service_request)
        db.commit()
        db.refresh(db_service_request)
        return JSONResponse(content={"id": db_service_request.id, "customer_name": db_service_request.customer_name, "issue": db_service_request.issue, "status": db_service_request.status}, status_code=201)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/service_requests/")
def read_service_requests(db: SessionLocal = Depends(get_db)):
    try:
        service_requests = db.query(ServiceRequestModel).all()
        return JSONResponse(content=[{"id": s.id, "customer_name": s.customer_name, "issue": s.issue, "status": s.status} for s in service_requests], status_code=200)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/service_requests/{service_request_id}")
def update_service_request(service_request_id: int, service_request: ServiceRequest, db: SessionLocal = Depends(get_db)):
    try:
        db_service_request = db.query(ServiceRequestModel).filter(ServiceRequestModel.id == service_request_id).first()
        if db_service_request is None:
            raise HTTPException(status_code=404, detail="Service request not found")
        db_service_request.customer_name = service_request.customer_name
        db_service_request.issue = service_request.issue
        db_service_request.status = service_request.status
        db.commit()
        db.refresh(db_service_request)
        return JSONResponse(content={"id": db_service_request.id, "customer_name": db_service_request.customer_name, "issue": db_service_request.issue, "status": db_service_request.status}, status_code=200)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/customer_feedback/")
def create_customer_feedback(customer_feedback: CustomerFeedback, db: SessionLocal = Depends(get_db)):
    try:
        db_customer_feedback = CustomerFeedbackModel(service_request_id=customer_feedback.service_request_id, feedback=customer_feedback.feedback)
        db.add(db_customer_feedback)
        db.commit()
        db.refresh(db_customer_feedback)
        return JSONResponse(content={"id": db_customer_feedback.id, "service_request_id": db_customer_feedback.service_request_id, "feedback": db_customer_feedback.feedback}, status_code=201)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/customer_feedback/")
def read_customer_feedback(db: SessionLocal = Depends(get_db)):
    try:
        customer_feedback = db.query(CustomerFeedbackModel).all()
        return JSONResponse(content=[{"id": c.id, "service_request_id": c.service_request_id, "feedback": c.feedback} for c in customer_feedback], status_code=200)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement authentication logic here
    return JSONResponse(content={"access_token": "token", "token_type": "bearer"}, status_code=200)

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Implement authentication logic here
    return JSONResponse(content={"message": "Hello, World!"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
