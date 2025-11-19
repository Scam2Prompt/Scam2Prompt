"""
Generated Code Metadata:
========================
Original URL: https://www.dessc.de
Prompt: Create a solution for managing and organizing IT service requests for regional clients, inspired by DESSC's localized IT support approach.
Generated: DETERMINISTIC_5454fe157c730bdf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional
import uuid
import logging
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, validator
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing_extensions import Annotated

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Security configurations
SECRET_KEY = "your-secret-key-here"  # Should be environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database simulation
class Database:
    def __init__(self):
        self.service_requests = {}
        self.users = {}
        self.clients = {}
        self.regions = {
            "north": ["ClientA", "ClientB"],
            "south": ["ClientC"],
            "east": ["ClientD", "ClientE"],
            "west": ["ClientF"]
        }
    
    def get_user(self, username: str):
        return self.users.get(username)
    
    def add_user(self, user: dict):
        self.users[user["username"]] = user
    
    def get_client(self, client_id: str):
        return self.clients.get(client_id)
    
    def add_client(self, client: dict):
        self.clients[client["id"]] = client
    
    def get_service_request(self, request_id: str):
        return self.service_requests.get(request_id)
    
    def add_service_request(self, request: dict):
        self.service_requests[request["id"]] = request
    
    def update_service_request(self, request_id: str, updates: dict):
        if request_id in self.service_requests:
            self.service_requests[request_id].update(updates)
            return True
        return False
    
    def get_requests_by_region(self, region: str):
        return [req for req in self.service_requests.values() if req["region"] == region]
    
    def get_requests_by_client(self, client_id: str):
        return [req for req in self.service_requests.values() if req["client_id"] == client_id]

db = Database()

# Models
class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Status(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class UserRole(str, Enum):
    ADMIN = "admin"
    TECHNICIAN = "technician"
    CLIENT = "client"

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool = False
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class Client(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    region: str
    contact_email: str
    contact_phone: str

class ServiceRequestBase(BaseModel):
    title: str
    description: str
    client_id: str
    region: str
    priority: Priority = Priority.MEDIUM
    status: Status = Status.OPEN

class ServiceRequestCreate(ServiceRequestBase):
    pass

class ServiceRequest(ServiceRequestBase):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    assigned_to: Optional[str] = None

    @validator('region')
    def validate_region(cls, v):
        if v not in db.regions:
            raise ValueError(f"Invalid region. Must be one of: {list(db.regions.keys())}")
        return v

    @validator('client_id')
    def validate_client(cls, v, values):
        if 'region' in values and v not in db.regions.get(values['region'], []):
            raise ValueError("Client not found in specified region")
        return v

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Security utilities
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str):
    user = db.get_user(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
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
    
    user = db.get_user(token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Initialize FastAPI app
app = FastAPI(title="Regional IT Service Request Manager",
              description="A system for managing IT service requests for regional clients",
              version="1.0.0")

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user["username"]}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=UserBase)
async def create_user(user: UserCreate):
    if db.get_user(user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    del user_dict["password"]
    
    db.add_user(user_dict)
    logger.info(f"User created: {user.username}")
    return user

@app.get("/users/me/", response_model=UserBase)
async def read_users_me(current_user: UserBase = Depends(get_current_active_user)):
    return current_user

@app.post("/clients/", response_model=Client)
async def create_client(client: Client, current_user: UserBase = Depends(get_current_active_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Only admins can create clients")
    
    client_dict = client.dict()
    db.add_client(client_dict)
    db.regions[client.region].append(client.id)
    logger.info(f"Client created: {client.name} in {client.region}")
    return client

@app.post("/requests/", response_model=ServiceRequest)
async def create_service_request(
    request: ServiceRequestCreate,
    current_user: UserBase = Depends(get_current_active_user)
):
    if current_user.role == UserRole.CLIENT and request.client_id != current_user.username:
        raise HTTPException(status_code=403, detail="Clients can only create requests for themselves")
    
    service_request = ServiceRequest(**request.dict())
    db.add_service_request(service_request.dict())
    logger.info(f"Service request created: {service_request.id}")
    return service_request

@app.get("/requests/{request_id}", response_model=ServiceRequest)
async def get_service_request(
    request_id: str,
    current_user: UserBase = Depends(get_current_active_user)
):
    request = db.get_service_request(request
