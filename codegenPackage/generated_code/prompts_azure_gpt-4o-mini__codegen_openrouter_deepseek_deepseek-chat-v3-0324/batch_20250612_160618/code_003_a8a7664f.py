"""
Generated Code Metadata:
========================
Original URL: https://whitelist-illuminex.com
Prompt: Generate an API that facilitates networking for students and professionals in digital business, reflecting the goals of KAMISLOT.
Generated: DETERMINISTIC_a8a7664f89334c14
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
KAMISLOT Networking API
A RESTful API to facilitate networking between students and professionals in digital business.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext
import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///./kamislot.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Security configuration
SECRET_KEY = "your-secret-key-here"  # In production, use environment variables
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("full_name", sqlalchemy.String),
    sqlalchemy.Column("user_type", sqlalchemy.String),  # "student" or "professional"
    sqlalchemy.Column("bio", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("skills", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=True),
)

connections = sqlalchemy.Table(
    "connections",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("connection_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("status", sqlalchemy.String),  # "pending", "accepted", "rejected"
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.utcnow),
)

messages = sqlalchemy.Table(
    "messages",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("sender_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("receiver_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("content", sqlalchemy.String),
    sqlalchemy.Column("sent_at", sqlalchemy.DateTime, default=datetime.utcnow),
    sqlalchemy.Column("is_read", sqlalchemy.Boolean, default=False),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

# Pydantic models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    user_type: str
    bio: Optional[str] = None
    skills: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class ConnectionRequest(BaseModel):
    connection_id: int

class MessageCreate(BaseModel):
    receiver_id: int
    content: str

class Message(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    content: str
    sent_at: datetime
    is_read: bool

    class Config:
        orm_mode = True

# App initialization
app = FastAPI(
    title="KAMISLOT Networking API",
    description="API for connecting students and professionals in digital business",
    version="1.0.0",
)

# Dependency
def get_db():
    db = database
    try:
        yield db
    finally:
        pass

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(db, email: str):
    query = users.select().where(users.c.email == email)
    return await db.fetch_one(query)

async def authenticate_user(db, email: str, password: str):
    user = await get_user(db, email)
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

async def get_current_user(db = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except jwt.PyJWTError:
        raise credentials_exception
    user = await get_user(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

# Routes
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/token", response_model=Token)
async def login_for_access_token(
    db = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db = Depends(get_db)):
    existing_user = await get_user(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    query = users.insert().values(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        user_type=user.user_type,
        bio=user.bio,
        skills=user.skills
    )
    last_record_id = await db.execute(query)
    return {**user.dict(), "id": last_record_id, "is_active": True}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/users/", response_model=List[User])
async def read_users(
    skip: int = 0, 
    limit: int = 100, 
    user_type: Optional[str] = None,
    db = Depends(get_db)
):
    query = users.select().where(users.c.is_active == True)
    if user_type:
        query = query.where(users.c.user_type == user_type)
    query = query.offset(skip).limit(limit)
    return await db.fetch_all(query)

@app.post("/connections/request", status_code=status.HTTP_201_CREATED)
async def request_connection(
    connection: ConnectionRequest,
    current_user: User = Depends(get_current_user),
    db = Depends(get_db)
):
    # Check if connection exists
    query = connections.select().where(
        (connections.c.user_id == current_user.id) & 
        (connections.c.connection_id == connection.connection_id)
    )
    existing_connection = await db.fetch_one(query)
    
    if existing_connection:
        raise HTTPException(status_code=400, detail="Connection already exists")
