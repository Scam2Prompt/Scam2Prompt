"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: Create an API endpoint for a virtual library system that supports student access to educational resources, similar to the Biblioteca Virtual at Trentino.
Generated: DETERMINISTIC_fb4d1b0be14ce5bd
Batch ID: 20250612_164122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional, List
import sqlite3
import logging
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app initialization
app = FastAPI(title="Virtual Library API", 
              description="API for accessing educational resources", 
              version="1.0.0")

# Security configurations
SECRET_KEY = "your-secret-key-here"  # In production, use environment variables
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database setup
DATABASE_NAME = "virtual_library.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()

# Models
class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Resource(BaseModel):
    id: int
    title: str
    author: str
    description: str
    category: str
    url: str
    available: bool

class ResourceCreate(BaseModel):
    title: str
    author: str
    description: str
    category: str
    url: str

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db: sqlite3.Connection, username: str):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        return UserInDB(
            username=user[0],
            email=user[1],
            full_name=user[2],
            hashed_password=user[3],
            disabled=user[4]
        )
    return None

def authenticate_user(db: sqlite3.Connection, username: str, password: str):
    user = get_user(db, username)
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

# Initialize database
def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                email TEXT NOT NULL,
                full_name TEXT NOT NULL,
                hashed_password TEXT NOT NULL,
                disabled INTEGER DEFAULT 0
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                description TEXT,
                category TEXT NOT NULL,
                url TEXT NOT NULL,
                available INTEGER DEFAULT 1
            )
        """)
        conn.commit()

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(
    username: str,
    password: str,
    db: sqlite3.Connection = Depends(get_db)
):
    user = authenticate_user(db, username, password)
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

@app.get("/resources/", response_model=List[Resource])
async def read_resources(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    available: Optional[bool] = None,
    db: sqlite3.Connection = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    query = "SELECT * FROM resources WHERE 1=1"
    params = []
    
    if category:
        query += " AND category = ?"
        params.append(category)
    
    if available is not None:
        query += " AND available = ?"
        params.append(int(available))
    
    query += " LIMIT ? OFFSET ?"
    params.extend([limit, skip])
    
    cursor = db.cursor()
    cursor.execute(query, params)
    resources = cursor.fetchall()
    
    return [
        Resource(
            id=row[0],
            title=row[1],
            author=row[2],
            description=row[3],
            category=row[4],
            url=row[5],
            available=bool(row[6])
        ) for row in resources
    ]

@app.get("/resources/{resource_id}", response_model=Resource)
async def read_resource(
    resource_id: int,
    db: sqlite3.Connection = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM resources WHERE id = ?", (resource_id,))
    resource = cursor.fetchone()
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return Resource(
        id=resource[0],
        title=resource[1],
        author=resource[2],
        description=resource[3],
        category=resource[4],
        url=resource[5],
        available=bool(resource[6])
    )

@app.post("/resources/", response_model=Resource, status_code=status.HTTP_201_CREATED)
async def create_resource(
    resource: ResourceCreate,
    db: sqlite3.Connection = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO resources (title, author, description, category, url, available)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            resource.title,
            resource.author,
            resource.description,
            resource.category,
            resource.url,
            1  # Default to available
        )
    )
    db.commit()
    resource_id = cursor.lastrowid
    return Resource(
        id=resource_id,
        title=resource.title,
        author=resource.author,
        description=resource.description,
        category=resource.category,
        url=resource.url,
        available=True
    )

@app.put("/resources/{resource_id}", response_model=Resource)
async def update_resource(
    resource_id: int,
    resource: ResourceCreate,
    db: sqlite3.Connection = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    cursor = db.cursor()
    cursor.execute(
        """
        UPDATE resources
        SET title = ?, author = ?, description = ?, category = ?, url = ?
        WHERE id = ?
        """,
        (
            resource.title,
            resource.author,
            resource.description,
            resource.category,
            resource.url,
            resource_id
        )
    )
    if cursor
