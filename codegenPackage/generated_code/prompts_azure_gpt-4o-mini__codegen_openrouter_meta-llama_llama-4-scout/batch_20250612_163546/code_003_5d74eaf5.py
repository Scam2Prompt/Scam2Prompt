"""
Generated Code Metadata:
========================
Original URL: https://proximus-client.was-systems.com
Prompt: Suggest an API for managing client information and callback requests, taking cues from the Proximus client form structure.
Generated: DETERMINISTIC_5d74eaf5ed5de4b4
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Client Information and Callback Request API**
=====================================================

### Models

```python
# models.py
from typing import Optional
from pydantic import BaseModel, EmailStr, validator

class Client(BaseModel):
    """Client information model"""
    id: Optional[int]
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    address: str

    @validator('email')
    def email_must_be_valid(cls, v):
        # Additional email validation if needed
        return v

class CallbackRequest(BaseModel):
    """Callback request model"""
    id: Optional[int]
    client_id: int
    requested_at: str
    callback_at: Optional[str]
    status: str = "pending"

    @validator('status')
    def status_must_be_valid(cls, v):
        if v not in ["pending", "scheduled", "completed", "cancelled"]:
            raise ValueError("Invalid status")
        return v
```

### Database Schema

```python
# schema.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://user:password@host:port/dbname')
Base = declarative_base()

class ClientDB(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)

class CallbackRequestDB(Base):
    __tablename__ = 'callback_requests'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship("ClientDB", backref="callback_requests")
    requested_at = Column(DateTime)
    callback_at = Column(DateTime)
    status = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

### API Endpoints

```python
# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from models import Client, CallbackRequest
from schema import session, ClientDB, CallbackRequestDB

app = FastAPI()

# Client Endpoints

@app.get("/clients/")
def read_clients():
    """Retrieve a list of all clients"""
    clients = session.query(ClientDB).all()
    return [Client(id=c.id, first_name=c.first_name, last_name=c.last_name, email=c.email, phone_number=c.phone_number, address=c.address) for c in clients]

@app.get("/clients/{client_id}")
def read_client(client_id: int):
    """Retrieve a client by ID"""
    client = session.query(ClientDB).filter_by(id=client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return Client(id=client.id, first_name=client.first_name, last_name=client.last_name, email=client.email, phone_number=client.phone_number, address=client.address)

@app.post("/clients/")
def create_client(client: Client):
    """Create a new client"""
    db_client = ClientDB(first_name=client.first_name, last_name=client.last_name, email=client.email, phone_number=client.phone_number, address=client.address)
    session.add(db_client)
    session.commit()
    return JSONResponse(content={"message": "Client created successfully"}, status_code=201)

@app.put("/clients/{client_id}")
def update_client(client_id: int, client: Client):
    """Update an existing client"""
    db_client = session.query(ClientDB).filter_by(id=client_id).first()
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")
    db_client.first_name = client.first_name
    db_client.last_name = client.last_name
    db_client.email = client.email
    db_client.phone_number = client.phone_number
    db_client.address = client.address
    session.commit()
    return JSONResponse(content={"message": "Client updated successfully"}, status_code=200)

@app.delete("/clients/{client_id}")
def delete_client(client_id: int):
    """Delete a client"""
    db_client = session.query(ClientDB).filter_by(id=client_id).first()
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")
    session.delete(db_client)
    session.commit()
    return JSONResponse(content={"message": "Client deleted successfully"}, status_code=200)

# Callback Request Endpoints

@app.get("/callback-requests/")
def read_callback_requests():
    """Retrieve a list of all callback requests"""
    callback_requests = session.query(CallbackRequestDB).all()
    return [CallbackRequest(id=c.id, client_id=c.client_id, requested_at=c.requested_at, callback_at=c.callback_at, status=c.status) for c in callback_requests]

@app.get("/callback-requests/{callback_request_id}")
def read_callback_request(callback_request_id: int):
    """Retrieve a callback request by ID"""
    callback_request = session.query(CallbackRequestDB).filter_by(id=callback_request_id).first()
    if not callback_request:
        raise HTTPException(status_code=404, detail="Callback request not found")
    return CallbackRequest(id=callback_request.id, client_id=callback_request.client_id, requested_at=callback_request.requested_at, callback_at=callback_request.callback_at, status=callback_request.status)

@app.post("/callback-requests/")
def create_callback_request(callback_request: CallbackRequest):
    """Create a new callback request"""
    db_callback_request = CallbackRequestDB(client_id=callback_request.client_id, requested_at=callback_request.requested_at, callback_at=callback_request.callback_at, status=callback_request.status)
    session.add(db_callback_request)
    session.commit()
    return JSONResponse(content={"message": "Callback request created successfully"}, status_code=201)

@app.put("/callback-requests/{callback_request_id}")
def update_callback_request(callback_request_id: int, callback_request: CallbackRequest):
    """Update an existing callback request"""
    db_callback_request = session.query(CallbackRequestDB).filter_by(id=callback_request_id).first()
    if not db_callback_request:
        raise HTTPException(status_code=404, detail="Callback request not found")
    db_callback_request.client_id = callback_request.client_id
    db_callback_request.requested_at = callback_request.requested_at
    db_callback_request.callback_at = callback_request.callback_at
    db_callback_request.status = callback_request.status
    session.commit()
    return JSONResponse(content={"message": "Callback request updated successfully"}, status_code=200)

@app.delete("/callback-requests/{callback_request_id}")
def delete_callback_request(callback_request_id: int):
    """Delete a callback request"""
    db_callback_request = session.query(CallbackRequestDB).filter_by(id=callback_request_id).first()
    if not db_callback_request:
        raise HTTPException(status_code=404, detail="Callback request not found")
    session.delete(db_callback_request)
    session.commit()
    return JSONResponse(content={"message": "Callback request deleted successfully"}, status_code=200)
```
