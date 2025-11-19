"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Design a RESTful API for managing pipe inspection and cleaning services, considering the features and services provided by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_7323823276f7e2eb
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum
import uuid
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models
class User(BaseModel):
    id: str
    username: str
    email: str
    full_name: str
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class PipeMaterial(str, Enum):
    copper = "copper"
    pvc = "pvc"
    galvanized_steel = "galvanized_steel"
    cast_iron = "cast_iron"
    other = "other"

class PipeDiameter(str, Enum):
    small = "small"  # < 50mm
    medium = "medium"  # 50-100mm
    large = "large"  # > 100mm

class ServiceType(str, Enum):
    inspection = "inspection"
    cleaning = "cleaning"
    repair = "repair"
    maintenance = "maintenance"

class ServiceStatus(str, Enum):
    scheduled = "scheduled"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class ServiceRequest(BaseModel):
    customer_id: str
    address: str
    pipe_material: PipeMaterial
    pipe_diameter: PipeDiameter
    service_type: ServiceType
    scheduled_date: datetime
    notes: Optional[str] = None

class Service(ServiceRequest):
    id: str
    assigned_technician: Optional[str] = None
    status: ServiceStatus = ServiceStatus.scheduled
    created_at: datetime
    updated_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Mock database
fake_users_db = {
    "johndoe": {
        "id": "1",
        "username": "johndoe",
        "email": "john@example.com",
        "full_name": "John Doe",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        "disabled": False,
    }
}

fake_services_db = {}

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="Pipe Inspection and Cleaning API",
              description="API for managing pipe inspection and cleaning services",
              version="1.0.0")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Service endpoints
@app.post("/services/", response_model=Service, status_code=status.HTTP_201_CREATED)
async def create_service(service: ServiceRequest, current_user: User = Depends(get_current_active_user)):
    service_id = str(uuid.uuid4())
    now = datetime.utcnow()
    db_service = Service(
        id=service_id,
        customer_id=service.customer_id,
        address=service.address,
        pipe_material=service.pipe_material,
        pipe_diameter=service.pipe_diameter,
        service_type=service.service_type,
        scheduled_date=service.scheduled_date,
        notes=service.notes,
        created_at=now,
        updated_at=now
    )
    fake_services_db[service_id] = db_service.dict()
    return db_service

@app.get("/services/", response_model=List[Service])
async def list_services(status: Optional[ServiceStatus] = None, 
                        current_user: User = Depends(get_current_active_user)):
    if status:
        return [Service(**s) for s in fake_services_db.values() if s["status"] == status]
    return [Service(**s) for s in fake_services_db.values()]

@app.get("/services/{service_id}", response_model=Service)
async def get_service(service_id: str, current_user: User = Depends(get_current_active_user)):
    if service_id not in fake_services_db:
        raise HTTPException(status_code=404, detail="Service not found")
    return Service(**fake_services_db[service_id])

@app.put("/services/{service_id}", response_model=Service)
async def update_service(service_id: str, service_update: ServiceRequest, 
                         current_user: User = Depends(get_current_active_user)):
    if service_id not in fake_services_db:
        raise HTTPException(status_code=404, detail="Service not found")
    
    db_service = fake_services_db[service_id]
    now = datetime.utcnow()
    
    updated_service = Service(
        id=service_id,
        customer_id=service_update.customer_id,
        address=service_update.address,
        pipe_material=service_update.pipe_material,
        pipe_diameter=service_update.pipe_diameter,
        service_type=service_update.service_type,
        scheduled_date=service_update.scheduled_date,
        notes=service_update.notes,
        assigned_technician=db_service.get("assigned_technician"),
        status=db_service.get("status", ServiceStatus.scheduled),
        created_at=db_service["created_at"],
        updated_at=now
    )
    
    fake_services_db[service_id] = updated_service.dict()
    return updated_service

@app.patch("/services/{service_id}/status", response_model=Service)
async def update_service_status(service_id: str, status: ServiceStatus,
                               current_user: User = Depends(get_current_active_user)):
    if service_id not in fake_services_db:
        raise HTTPException(status_code=404, detail="Service not found")
    
    db_service = fake_services_db[service_id]
    now = datetime.utcnow()
    
    updated_service = Service(
        id=service_id,
        customer_id=db_service["customer_id"],
        address=db_service["address"],
        pipe_material=db_service["pipe_material"],
