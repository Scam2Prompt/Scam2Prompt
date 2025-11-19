"""
Generated Code Metadata:
========================
Original URL: https://mieconline.com
Prompt: Generate code to connect service providers with customers seamlessly, as described in MIEC's Service Solutions. Include features for user registration and service matching.
Generated: DETERMINISTIC_3311eecf9cbd2e4a
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Service Provider Customer Connection Platform**
=====================================================

### **Models**
```python
# models.py

from enum import Enum
from typing import List
from pydantic import BaseModel, EmailStr

class UserType(str, Enum):
    customer = "customer"
    service_provider = "service_provider"

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    user_type: UserType

class Service(BaseModel):
    id: int
    name: str
    description: str
    service_provider_id: int

class RegistrationRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    user_type: UserType

class ServiceRequest(BaseModel):
    customer_id: int
    service_id: int
```

### **Database**
```python
# database.py

from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///service_platform.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    user_type = Column(Enum(UserType))

    services = relationship("ServiceTable", back_populates="service_provider")

class ServiceTable(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    service_provider_id = Column(Integer, ForeignKey("users.id"))

    service_provider = relationship("UserTable", back_populates="services")

Base.metadata.create_all(engine)
```

### **Services**
```python
# services.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Service, RegistrationRequest, ServiceRequest

app = FastAPI()

security = HTTPBasic()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
async def register_user(registration_request: RegistrationRequest, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(UserTable).filter_by(email=registration_request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already in use")

    # Create new user
    new_user = UserTable(name=registration_request.name, email=registration_request.email, user_type=registration_request.user_type)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

@app.post("/services")
async def create_service(service: Service, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    # Authenticate service provider
    service_provider = db.query(UserTable).filter_by(email=credentials.username, user_type=UserType.service_provider).first()
    if not service_provider:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create new service
    new_service = ServiceTable(name=service.name, description=service.description, service_provider_id=service_provider.id)
    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return {"message": "Service created successfully"}

@app.post("/service-requests")
async def create_service_request(service_request: ServiceRequest, db: Session = Depends(get_db)):
    # Check if service exists
    service = db.query(ServiceTable).filter_by(id=service_request.service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    # Create new service request
    # Add logic to notify service provider and customer

    return {"message": "Service request created successfully"}
```

### **Main**
```python
# main.py

from services import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
