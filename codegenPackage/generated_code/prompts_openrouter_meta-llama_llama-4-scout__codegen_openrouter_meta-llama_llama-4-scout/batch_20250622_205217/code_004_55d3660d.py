"""
Generated Code Metadata:
========================
Original URL: https://tpcontact.co.za
Prompt: Design a RESTful API for Move Up's UK visa solutions, including endpoints for client registration, visa application submission, and status updates.
Generated: DETERMINISTIC_55d3660dcf592d94
Batch ID: 20250622_205217
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
from typing import Optional
from datetime import datetime
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///move_up_visa.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Pydantic Models
class Client(BaseModel):
    """Client registration model"""
    name: str
    email: str
    phone_number: str

class VisaApplication(BaseModel):
    """Visa application model"""
    client_id: int
    visa_type: str
    application_details: str

class StatusUpdate(BaseModel):
    """Status update model"""
    application_id: int
    status: str

# SQLAlchemy Models
class ClientDB(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)

class VisaApplicationDB(Base):
    __tablename__ = "visa_applications"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    visa_type = Column(String)
    application_details = Column(String)
    status = Column(String)

# FastAPI App
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

# OAuth2 Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Client Registration Endpoint
@app.post("/clients/")
async def create_client(client: Client, db: SessionLocal = Depends(get_db)):
    """Create a new client"""
    db_client = ClientDB(name=client.name, email=client.email, phone_number=client.phone_number)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return {"id": db_client.id, "name": db_client.name, "email": db_client.email}

# Visa Application Submission Endpoint
@app.post("/visa-applications/")
async def create_visa_application(visa_application: VisaApplication, db: SessionLocal = Depends(get_db)):
    """Create a new visa application"""
    db_visa_application = VisaApplicationDB(client_id=visa_application.client_id, visa_type=visa_application.visa_type, application_details=visa_application.application_details, status="pending")
    db.add(db_visa_application)
    db.commit()
    db.refresh(db_visa_application)
    return {"id": db_visa_application.id, "client_id": db_visa_application.client_id, "visa_type": db_visa_application.visa_type}

# Status Update Endpoint
@app.put("/visa-applications/{application_id}/status")
async def update_status(application_id: int, status_update: StatusUpdate, db: SessionLocal = Depends(get_db)):
    """Update the status of a visa application"""
    db_visa_application = db.query(VisaApplicationDB).filter(VisaApplicationDB.id == application_id).first()
    if db_visa_application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    db_visa_application.status = status_update.status
    db.commit()
    db.refresh(db_visa_application)
    return {"id": db_visa_application.id, "status": db_visa_application.status}

# Get Visa Application by ID Endpoint
@app.get("/visa-applications/{application_id}")
async def get_visa_application(application_id: int, db: SessionLocal = Depends(get_db)):
    """Get a visa application by ID"""
    db_visa_application = db.query(VisaApplicationDB).filter(VisaApplicationDB.id == application_id).first()
    if db_visa_application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return {"id": db_visa_application.id, "client_id": db_visa_application.client_id, "visa_type": db_visa_application.visa_type, "status": db_visa_application.status}

# Get Client by ID Endpoint
@app.get("/clients/{client_id}")
async def get_client(client_id: int, db: SessionLocal = Depends(get_db)):
    """Get a client by ID"""
    db_client = db.query(ClientDB).filter(ClientDB.id == client_id).first()
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"id": db_client.id, "name": db_client.name, "email": db_client.email}

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
sqlalchemy
pydantic
```

To run the application:

```bash
# Create a new virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

API Endpoints:

*   **POST /clients/**: Create a new client
*   **POST /visa-applications/**: Create a new visa application
*   **PUT /visa-applications/{application_id}/status**: Update the status of a visa application
*   **GET /visa-applications/{application_id}**: Get a visa application by ID
*   **GET /clients/{client_id}**: Get a client by ID
