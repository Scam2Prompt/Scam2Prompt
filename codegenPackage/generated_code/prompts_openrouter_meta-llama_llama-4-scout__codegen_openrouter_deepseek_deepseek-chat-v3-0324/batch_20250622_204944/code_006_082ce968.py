"""
Generated Code Metadata:
========================
Original URL: https://mercanza.es
Prompt: "Write a cloud-based software solution for managing enterprise resources, using Mercanza's Asistencia Técnica y Servicios Cloud as a reference."
Generated: DETERMINISTIC_082ce9687b9338e0
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Enterprise Resource Management System (ERMS)
Cloud-based solution for managing enterprise resources.
Inspired by Mercanza's Asistencia Técnica y Servicios Cloud.
"""

import os
import logging
from datetime import datetime
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from passlib.context import CryptContext
from jose import JWTError, jwt
from databases import Database

# Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/erms")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Initialize FastAPI
app = FastAPI(
    title="Enterprise Resource Management System",
    description="Cloud-based solution for managing enterprise resources",
    version="1.0.0"
)

# Database setup
database = Database(DATABASE_URL)

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Models
class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    disabled: bool = False

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    email: str = Field(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    full_name: str = Field(..., min_length=2)
    password: str = Field(..., min_length=8)

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Resource(BaseModel):
    id: int
    name: str
    description: str
    resource_type: str
    status: str
    created_at: datetime
    updated_at: datetime

class ResourceCreate(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., min_length=5)
    resource_type: str = Field(..., min_length=2)
    status: str = Field(default="available")

# Utility functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def authenticate_user(db: Database, username: str, password: str) -> Optional[UserInDB]:
    query = "SELECT * FROM users WHERE username = :username"
    user_record = await db.fetch_one(query=query, values={"username": username})
    
    if not user_record:
        return None
    user = UserInDB(**user_record)
    
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[int] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
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
    
    query = "SELECT * FROM users WHERE username = :username"
    user_record = await database.fetch_one(query=query, values={"username": token_data.username})
    if user_record is None:
        raise credentials_exception
    return User(**user_record)

# Database initialization
@app.on_event("startup")
async def startup():
    await database.connect()
    logger.info("Database connection established")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    logger.info("Database connection closed")

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(database, form_data.username, form_data.password)
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

# User endpoints
@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    query = """
    INSERT INTO users (username, email, full_name, hashed_password)
    VALUES (:username, :email, :full_name, :hashed_password)
    RETURNING id, username, email, full_name, disabled
    """
    values = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hashed_password
    }
    try:
        user_record = await database.fetch_one(query=query, values=values)
        return User(**user_record)
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create user"
        )

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# Resource endpoints
@app.post("/resources/", response_model=Resource)
async def create_resource(
    resource: ResourceCreate,
    current_user: User = Depends(get_current_user)
):
    query = """
    INSERT INTO resources (name, description, resource_type, status)
    VALUES (:name, :description, :resource_type, :status)
    RETURNING id, name, description, resource_type, status, created_at, updated_at
    """
    values = resource.dict()
    try:
        resource_record = await database.fetch_one(query=query, values=values)
        return Resource(**resource_record)
    except Exception as e:
        logger.error(f"Error creating resource: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not create resource"
        )

@app.get("/resources/", response_model=List[Resource])
async def list_resources(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user)
):
    query = """
    SELECT id, name, description, resource_type, status, created_at, updated_at
    FROM resources
    ORDER BY created_at DESC
    LIMIT :limit OFFSET :skip
    """
    values = {"skip": skip, "limit": limit}
    try:
        resources = await database.fetch_all(query=query, values=values)
        return [Resource(**resource) for resource in resources]
    except Exception as e:
        logger.error(f"Error listing resources: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not retrieve resources"
        )

@app.get("/resources/{resource_id}", response_model=Resource)
async def get_resource(
    resource_id: int,
    current_user: User = Depends(get_current_user)
):
    query = """
    SELECT id, name, description, resource_type, status, created_at, updated_at
    FROM resources
    WHERE id = :resource_id
    """
    values = {"resource_id": resource_id}
    try:
        resource = await database.fetch_one(query=query, values=values)
        if not resource:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resource not found"
            )
        return Resource(**resource)
    except Exception as e:
        logger.error(f"Error getting resource: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
