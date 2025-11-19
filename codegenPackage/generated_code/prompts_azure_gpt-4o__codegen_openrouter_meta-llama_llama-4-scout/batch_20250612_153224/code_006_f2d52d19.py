"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Develop a REST API in Python for managing architectural project data, including client details, project scope, and billing, inspired by TWM Associates' services.
Generated: DETERMINISTIC_f2d52d19f0299589
Batch ID: 20250612_153224
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
from datetime import datetime

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///project_database.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Pydantic Models
class Client(BaseModel):
    id: int
    name: str
    email: str
    phone: str

class Project(BaseModel):
    id: int
    client_id: int
    scope: str
    start_date: str
    end_date: str

class Billing(BaseModel):
    id: int
    project_id: int
    amount: float
    date: str

# SQLAlchemy Models
class ClientDB(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

class ProjectDB(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    scope = Column(String)
    start_date = Column(String)
    end_date = Column(String)

class BillingDB(Base):
    __tablename__ = "billings"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer)
    amount = Column(Float)
    date = Column(String)

# Create the database tables
Base.metadata.create_all(engine)

# FastAPI App
app = FastAPI()

# OAuth2 Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Client Endpoints
@app.get("/clients/")
def read_clients(db: SessionLocal = Depends(get_db)):
    try:
        clients = db.query(ClientDB).all()
        return [{"id": client.id, "name": client.name, "email": client.email, "phone": client.phone} for client in clients]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/clients/")
def create_client(client: Client, db: SessionLocal = Depends(get_db)):
    try:
        new_client = ClientDB(name=client.name, email=client.email, phone=client.phone)
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return {"id": new_client.id, "name": new_client.name, "email": new_client.email, "phone": new_client.phone}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Project Endpoints
@app.get("/projects/")
def read_projects(db: SessionLocal = Depends(get_db)):
    try:
        projects = db.query(ProjectDB).all()
        return [{"id": project.id, "client_id": project.client_id, "scope": project.scope, "start_date": project.start_date, "end_date": project.end_date} for project in projects]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/projects/")
def create_project(project: Project, db: SessionLocal = Depends(get_db)):
    try:
        new_project = ProjectDB(client_id=project.client_id, scope=project.scope, start_date=project.start_date, end_date=project.end_date)
        db.add(new_project)
        db.commit()
        db.refresh(new_project)
        return {"id": new_project.id, "client_id": new_project.client_id, "scope": new_project.scope, "start_date": new_project.start_date, "end_date": new_project.end_date}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Billing Endpoints
@app.get("/billings/")
def read_billings(db: SessionLocal = Depends(get_db)):
    try:
        billings = db.query(BillingDB).all()
        return [{"id": billing.id, "project_id": billing.project_id, "amount": billing.amount, "date": billing.date} for billing in billings]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/billings/")
def create_billing(billing: Billing, db: SessionLocal = Depends(get_db)):
    try:
        new_billing = BillingDB(project_id=billing.project_id, amount=billing.amount, date=billing.date)
        db.add(new_billing)
        db.commit()
        db.refresh(new_billing)
        return {"id": new_billing.id, "project_id": new_billing.project_id, "amount": new_billing.amount, "date": new_billing.date}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Token Endpoints
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Here you would authenticate the user
    return {"access_token": "your_access_token", "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    # Here you would get the current user
    return {"username": "your_username"}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
