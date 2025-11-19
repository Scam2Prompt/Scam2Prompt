"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Develop a REST API for SKI Foundation's "Kerjasama Pendampingan Bisnis kepada Pelaku UMKM" program, allowing partners to submit business plans and track their implementation progress.
Generated: DETERMINISTIC_1f7dbdb0f82f46e9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime, date
from enum import Enum
import uuid
import databases
import sqlalchemy
from passlib.context import CryptContext

# Database configuration
DATABASE_URL = "sqlite:///./ski_foundation.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Security configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("full_name", sqlalchemy.String),
    sqlalchemy.Column("role", sqlalchemy.String),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=True),
)

business_plans = sqlalchemy.Table(
    "business_plans",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String, index=True),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("sector", sqlalchemy.String),
    sqlalchemy.Column("location", sqlalchemy.String),
    sqlalchemy.Column("owner_id", sqlalchemy.String, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("mentor_id", sqlalchemy.String, sqlalchemy.ForeignKey("users.id"), nullable=True),
    sqlalchemy.Column("submission_date", sqlalchemy.DateTime),
    sqlalchemy.Column("status", sqlalchemy.String),
)

progress_updates = sqlalchemy.Table(
    "progress_updates",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("plan_id", sqlalchemy.String, sqlalchemy.ForeignKey("business_plans.id")),
    sqlalchemy.Column("update_date", sqlalchemy.DateTime),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("milestone", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI(title="SKI Foundation UMKM Program API",
              description="API for managing business mentoring program for UMKM",
              version="1.0.0")

# Pydantic models
class UserRole(str, Enum):
    UMKM = "umkm"
    MENTOR = "mentor"
    ADMIN = "admin"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: UserRole

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class BusinessPlanStatus(str, Enum):
    SUBMITTED = "submitted"
    REVIEWED = "reviewed"
    APPROVED = "approved"
    REJECTED = "rejected"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class BusinessPlanBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: str
    sector: str
    location: str

class BusinessPlanCreate(BusinessPlanBase):
    pass

class BusinessPlan(BusinessPlanBase):
    id: str
    owner_id: str
    mentor_id: Optional[str]
    submission_date: datetime
    status: BusinessPlanStatus

    class Config:
        orm_mode = True

class ProgressUpdateBase(BaseModel):
    description: str
    milestone: str
    status: str

class ProgressUpdateCreate(ProgressUpdateBase):
    pass

class ProgressUpdate(ProgressUpdateBase):
    id: str
    plan_id: str
    update_date: datetime

    class Config:
        orm_mode = True

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(email: str):
    query = users.select().where(users.c.email == email)
    user = await database.fetch_one(query)
    if user:
        return user

async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # In a real app, you would decode the JWT token here
        # For simplicity, we're using the email as the token
        user = await get_user(token)
        if user is None:
            raise credentials_exception
        return user
    except Exception:
        raise credentials_exception

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user["is_active"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Startup and shutdown events
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Auth endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # In a real app, you would generate a JWT token here
    # For simplicity, we're returning the email as the token
    return {"access_token": user["email"], "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    existing_user = await get_user(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    user_id = str(uuid.uuid4())
    query = users.insert().values(
        id=user_id,
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        role=user.role,
        is_active=True
    )
    await database.execute(query)
    return {**user.dict(), "id": user_id, "is_active": True}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# Business Plan endpoints
@app.post("/business-plans/", response_model=BusinessPlan)
async def create_business_plan(
    plan: BusinessPlanCreate,
    current_user: User = Depends(get_current_active_user)
):
    if current_user["role"] != UserRole.UMKM:
        raise HTTPException(status_code=403, detail="Only UMKM users can submit business plans")
    
    plan_id = str(uuid.uuid4())
    query = business_plans.insert().values(
        id=plan_id,
        title=plan.title,
        description=plan.description,
        sector=plan.sector,
        location=plan.location,
        owner_id=current_user["id"],
        submission_date=datetime.now(),
        status=BusinessPlanStatus.SUBMITTED
    )
    await database.execute(query)
    
    created_plan = await database.fetch_one(
        business_plans.select().where(business_plans.c.id == plan_id)
    )
    return created_plan

@app.get("/business-plans/", response_model=List[BusinessPlan])
async def list_business_plans(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user)
):
    if current_user["role"] == UserRole.UMKM:
        query = business_plans.select().where(
            business_plans.c.owner_id == current_user["id"]
        ).offset(skip).limit(limit)
    elif current_user["
