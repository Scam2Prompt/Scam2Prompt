"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: Write a Paxful clone script that includes functionality for hiring developers or employees, as discussed in the procedure section of the webpage.
Generated: DETERMINISTIC_15e0d016909adf1d
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Paxful Clone Script with Hiring Functionality

import os
import uuid
from datetime import datetime
from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field, validator
from passlib.context import CryptContext
from jose import JWTError, jwt
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(DATABASE_URL)
db = client.paxful_clone

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="Paxful Clone", version="1.0.0")

# Models
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    hashed_password: str
    is_active: bool = True
    is_verified: bool = False
    is_admin: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}

class UserPublic(UserBase):
    id: str
    is_active: bool
    is_verified: bool
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class JobPosting(BaseModel):
    title: str
    description: str
    requirements: List[str]
    location: str
    salary_range: str
    job_type: str  # full-time, part-time, contract
    is_active: bool = True
    posted_by: str  # user_id
    posted_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class JobApplication(BaseModel):
    job_id: str
    applicant_id: str
    cover_letter: str
    resume_url: str
    status: str = "pending"  # pending, reviewed, rejected, hired
    applied_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# Utility functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def authenticate_user(username: str, password: str):
    user = await db.users.find_one({"username": username})
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
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
    
    user = await db.users.find_one({"username": token_data.username})
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user["is_active"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Auth endpoints
@app.post("/register", response_model=UserPublic)
async def register_user(user: UserCreate):
    existing_user = await db.users.find_one({"$or": [{"username": user.username}, {"email": user.email}]})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    
    result = await db.users.insert_one(db_user.dict())
    db_user.id = str(result.inserted_id)
    return db_user

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Job posting endpoints
@app.post("/jobs", response_model=JobPosting)
async def create_job_posting(job: JobPosting, current_user: UserInDB = Depends(get_current_active_user)):
    if not current_user.get("is_admin", False):
        raise HTTPException(status_code=403, detail="Only admins can post jobs")
    
    job.posted_by = str(current_user["id"])
    result = await db.jobs.insert_one(job.dict())
    job.id = str(result.inserted_id)
    return job

@app.get("/jobs", response_model=List[JobPosting])
async def get_job_postings(active_only: bool = True):
    query = {"is_active": True} if active_only else {}
    jobs = []
    async for job in db.jobs.find(query):
        jobs.append(job)
    return jobs

@app.get("/jobs/{job_id}", response_model=JobPosting)
async def get_job_posting(job_id: str):
    job = await db.jobs.find_one({"_id": ObjectId(job_id)})
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@app.put("/jobs/{job_id}", response_model=JobPosting)
async def update_job_posting(job_id: str, job_update: JobPosting, current_user: UserInDB = Depends(get_current_active_user)):
    existing_job = await db.jobs.find_one({"_id": ObjectId(job_id)})
    if not existing_job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if str(existing_job["posted_by"]) != str(current_user["id"]) and not current_user.get("is_admin", False):
        raise HTTPException(status_code=403, detail="Not authorized to update this job")
    
    job_update.updated_at = datetime.utcnow()
    await db.jobs.update_one({"_id": ObjectId(job_id)}, {"$set": job_update.dict()})
    return await db.jobs.find_one({"_id": ObjectId(job_id)})

# Job application endpoints
@app.post("/jobs/{job_id}/apply", response_model=JobApplication)
async def apply_for_job(
    job_id: str,
    cover_letter: str,
    resume_url: str,
    current_user: UserInDB = Depends(get_current_active_user)
):
    job = await db.jobs.find_one({"_id": ObjectId(job_id)})
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    if not job.get("is_active", False):
        raise HTTPException(status_code=400, detail="Job is no longer active")
    
    existing_application = await db.applications.find_one({
        "job_id": job_id
