"""
Generated Code Metadata:
========================
Original URL: https://www.cloud-telephonie.net
Prompt: How can I implement an API to handle user project selection and urgency status in a telephony service application?
Generated: DETERMINISTIC_a92f811fba23b133
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
API for handling user project selection and urgency status in a telephony service application.

Features:
- RESTful endpoints for project selection and urgency status management
- JWT-based authentication
- Input validation
- Error handling
- Database persistence
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import sqlite3
import os

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database setup
DATABASE_NAME = "telephony_service.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()

def initialize_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                hashed_password TEXT NOT NULL,
                disabled BOOLEAN DEFAULT FALSE
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                owner_id INTEGER NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES users (id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS urgency_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('low', 'medium', 'high', 'critical')),
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
        """)
        conn.commit()

initialize_db()

# Authentication setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    username: str
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Project(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class ProjectDB(Project):
    id: int
    owner_id: int

class UrgencyStatus(BaseModel):
    status: str = Field(..., regex="^(low|medium|high|critical)$")

    @validator('status')
    def validate_status(cls, v):
        if v not in ['low', 'medium', 'high', 'critical']:
            raise ValueError('Invalid urgency status')
        return v

class UrgencyStatusDB(UrgencyStatus):
    id: int
    project_id: int
    last_updated: datetime

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db: sqlite3.Connection, username: str):
    cursor = db.cursor()
    cursor.execute("SELECT id, username, hashed_password, disabled FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    if user_data:
        return UserInDB(
            username=user_data[1],
            hashed_password=user_data[2],
            disabled=user_data[3]
        )
    return None

def authenticate_user(db: sqlite3.Connection, username: str, password: str):
    user = get_user(db, username)
    if not user or not verify_password(password, user.hashed_password):
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

async def get_current_user(token: str = Depends(oauth2_scheme), db: sqlite3.Connection = Depends(get_db)):
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
    
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API setup
app = FastAPI()

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: sqlite3.Connection = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
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

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate, db: sqlite3.Connection = Depends(get_db)):
    existing_user = get_user(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (username, hashed_password) VALUES (?, ?)",
        (user.username, hashed_password)
    )
    db.commit()
    return {"username": user.username, "disabled": False}

# Project endpoints
@app.post("/projects/", response_model=ProjectDB)
async def create_project(
    project: Project,
    current_user: User = Depends(get_current_active_user),
    db: sqlite3.Connection = Depends(get_db)
):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO projects (name, description, owner_id) VALUES (?, ?, ?)",
        (project.name, project.description, current_user.id)
    )
    project_id = cursor.lastrowid
    db.commit()
    return {
        "id": project_id,
        "name": project.name,
        "description": project.description,
        "owner_id": current_user.id
    }

@app.get("/projects/", response_model=List[ProjectDB])
async def get_projects(
    current_user: User = Depends(get_current_active_user),
    db: sqlite3.Connection = Depends(get_db)
):
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name, description, owner_id FROM projects WHERE owner_id = ?",
        (current_user.id,)
    )
    projects = []
    for row in cursor.fetchall():
        projects.append({
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "owner_id": row[3]
        })
    return projects

# Urgency status endpoints
@app.post("/projects/{project_id}/urgency", response_model=UrgencyStatusDB)
async def set_urgency_status(
    project_id: int,
    status: UrgencyStatus,
    current_user: User = Depends(get_current_active_user),
    db: sqlite3.Connection = Depends(get_db)
):
    # Check if project exists and belongs to user
    cursor = db.cursor()
    cursor.execute(
        "SELECT id FROM projects WHERE id = ? AND owner_id = ?",
        (project_id, current_user.id)
    )
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="
