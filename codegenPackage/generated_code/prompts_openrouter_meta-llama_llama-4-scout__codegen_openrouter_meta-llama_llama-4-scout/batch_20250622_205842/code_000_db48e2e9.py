"""
Generated Code Metadata:
========================
Original URL: https://virtue.guru
Prompt: Write a Python API for tracking personal virtues and vices, including user authentication and daily reflection logging.
Generated: DETERMINISTIC_db48e2e9a1d9059c
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtues_and_vices_api.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
from typing import List
from passlib.context import CryptContext
from jose import jwt, JWTError

# Configuration
SECRET_KEY = "secret_key_here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///virtues_and_vices.db"

# Create Database Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create Session Maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base Model
Base = declarative_base()

# Password Context
pwd_context = CryptContext(schemes=["bcrypt"], default="bcrypt")

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

class Virtue(Base):
    __tablename__ = "virtues"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Vice(Base):
    __tablename__ = "vices"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Reflection(Base):
    __tablename__ = "reflections"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    date = Column(Date)
    virtues = Column(String)
    vices = Column(String)

# Pydantic Models
class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

class VirtueCreate(BaseModel):
    name: str

class ViceCreate(BaseModel):
    name: str

class ReflectionCreate(BaseModel):
    virtues: List[str]
    vices: List[str]

# Initialize App
app = FastAPI()

# Initialize Database
Base.metadata.create_all(bind=engine)

# Utility Functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def authenticate_user(db, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        expire = date.today() + expires_delta
    else:
        expire = date.today() + date.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Authentication
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/")
def create_user(user: UserCreate):
    db = SessionLocal()
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse(id=db_user.id, username=db_user.username)

# Virtues and Vices
@app.post("/virtues/")
def create_virtue(virtue: VirtueCreate, token: str = Depends(oauth2_scheme)):
    db = SessionLocal()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_virtue = Virtue(name=virtue.name)
    db.add(db_virtue)
    db.commit()
    db.refresh(db_virtue)
    return {"id": db_virtue.id, "name": db_virtue.name}

@app.post("/vices/")
def create_vice(vice: ViceCreate, token: str = Depends(oauth2_scheme)):
    db = SessionLocal()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_vice = Vice(name=vice.name)
    db.add(db_vice)
    db.commit()
    db.refresh(db_vice)
    return {"id": db_vice.id, "name": db_vice.name}

# Reflections
@app.post("/reflections/")
def create_reflection(reflection: ReflectionCreate, token: str = Depends(oauth2_scheme)):
    db = SessionLocal()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_reflection = Reflection(
        user_id=user_id,
        date=date.today(),
        virtues=",".join(reflection.virtues),
        vices=",".join(reflection.vices),
    )
    db.add(db_reflection)
    db.commit()
    db.refresh(db_reflection)
    return {"id": db_reflection.id, "date": db_reflection.date}

@app.get("/reflections/")
def get_reflections(token: str = Depends(oauth2_scheme)):
    db = SessionLocal()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    reflections = db.query(Reflection).filter(Reflection.user_id == user_id).all()
    return [{"id": reflection.id, "date": reflection.date, "virtues": reflection.virtues.split(","), "vices": reflection.vices.split(",")} for reflection in reflections]
```
