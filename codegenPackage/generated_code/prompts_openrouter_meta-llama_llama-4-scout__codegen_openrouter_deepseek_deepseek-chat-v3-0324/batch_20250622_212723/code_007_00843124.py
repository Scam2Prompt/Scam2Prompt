"""
Generated Code Metadata:
========================
Original URL: https://worldmobile-token.pages.dev
Prompt: "Implement an API for tracking rewards, staking, and managing nodes in the World Mobile network, ensuring secure and encrypted information storage."
Generated: DETERMINISTIC_008431245164d537
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime, timedelta
from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, APIKeyHeader
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr, validator
from passlib.context import CryptContext
from jose import JWTError, jwt
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, OperationFailure
import logging
from logging.handlers import RotatingFileHandler
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler("wm_network_api.log", maxBytes=1000000, backupCount=5),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Environment variables
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", Fernet.generate_key().decode())

# Initialize Fernet for encryption
fernet = Fernet(ENCRYPTION_KEY)

# MongoDB client
client = MongoClient(MONGO_URI)
db = client.world_mobile_network
users_collection = db.users
nodes_collection = db.nodes
rewards_collection = db.rewards
staking_collection = db.staking

# Password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

app = FastAPI(
    title="World Mobile Network API",
    description="API for tracking rewards, staking, and managing nodes in the World Mobile network",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        return v

class UserInDB(UserBase):
    hashed_password: str
    disabled: bool = False
    api_key: Optional[str] = None

class NodeBase(BaseModel):
    node_id: str = Field(..., min_length=5, max_length=50)
    location: str
    status: str = "active"
    owner: str

class NodeCreate(NodeBase):
    pass

class Node(NodeBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class Reward(BaseModel):
    reward_id: str
    node_id: str
    amount: float
    currency: str = "WMT"
    timestamp: datetime
    status: str = "pending"

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class Staking(BaseModel):
    staking_id: str
    user_id: str
    amount: float
    currency: str = "WMT"
    start_date: datetime
    end_date: datetime
    status: str = "active"

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def encrypt_data(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str) -> str:
    return fernet.decrypt(encrypted_data.encode()).decode()

def get_user(username: str) -> Optional[UserInDB]:
    user_data = users_collection.find_one({"username": username})
    if user_data:
        return UserInDB(**user_data)
    return None

def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    user = get_user(username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
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

    user = get_user(token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)) -> UserInDB:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

async def get_api_key(api_key: str = Security(api_key_header)) -> str:
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="API key required"
        )
    user = users_collection.find_one({"api_key": api_key})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )
    return api_key

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
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

@app.post("/users/", response_model=UserBase)
async def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        api_key=encrypt_data(os.urandom(16).hex())
    )
    
    try:
        users_collection.insert_one(jsonable_encoder(db_user))
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    except OperationFailure as e:
        logger.error(f"Database operation failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Error creating user")
    
    return UserBase(**user.dict())

@app.get("/users/me/", response_model=UserBase)
async def read_users_me(current_user: UserInDB = Depends(get_current_active_user)):
    return current_user

@app.post("/nodes/", response_model=Node)
async def create_node(
    node: NodeCreate,
    current_user: UserInDB = Depends(get_current_active_user)
):
    if node.owner != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to create node for this user")
