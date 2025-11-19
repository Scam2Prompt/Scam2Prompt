"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Design a RESTful API for an accounting firm's client portal, allowing clients to submit requests, view documents, and communicate with the firm."
Generated: DETERMINISTIC_164cce695a2fc20b
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import shutil
import os
import uuid

# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
UPLOAD_DIRECTORY = "client_documents"

# Database models (would typically be ORM models)
class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class Client(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str
    tax_id: str

class Document(BaseModel):
    id: str
    client_id: str
    name: str
    upload_date: datetime
    file_path: str
    description: Optional[str] = None

class SupportRequest(BaseModel):
    id: str
    client_id: str
    subject: str
    message: str
    created_at: datetime
    status: str = "open"
    responses: List[str] = []

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Mock database
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "john@example.com",
        "full_name": "John Doe",
        "disabled": False,
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"  # "secret"
    }
}

fake_clients_db = {}
fake_documents_db = {}
fake_requests_db = {}

# App setup
app = FastAPI(title="Accounting Firm Client Portal API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility functions
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

# Routes
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

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# Client endpoints
@app.get("/clients/", response_model=List[Client])
async def get_clients(current_user: User = Depends(get_current_active_user)):
    return list(fake_clients_db.values())

@app.get("/clients/{client_id}", response_model=Client)
async def get_client(client_id: str, current_user: User = Depends(get_current_active_user)):
    if client_id not in fake_clients_db:
        raise HTTPException(status_code=404, detail="Client not found")
    return fake_clients_db[client_id]

# Document endpoints
@app.post("/documents/upload/")
async def upload_document(
    client_id: str,
    file: UploadFile = File(...),
    description: Optional[str] = None,
    current_user: User = Depends(get_current_active_user)
):
    if client_id not in fake_clients_db:
        raise HTTPException(status_code=404, detail="Client not found")
    
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
    file_id = str(uuid.uuid4())
    file_extension = os.path.splitext(file.filename)[1]
    file_path = os.path.join(UPLOAD_DIRECTORY, f"{file_id}{file_extension}")
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    document = Document(
        id=file_id,
        client_id=client_id,
        name=file.filename,
        upload_date=datetime.now(),
        file_path=file_path,
        description=description
    )
    
    fake_documents_db[file_id] = document
    return {"id": file_id, "filename": file.filename}

@app.get("/documents/", response_model=List[Document])
async def get_documents(client_id: str, current_user: User = Depends(get_current_active_user)):
    if client_id not in fake_clients_db:
        raise HTTPException(status_code=404, detail="Client not found")
    return [doc for doc in fake_documents_db.values() if doc.client_id == client_id]

@app.get("/documents/{document_id}", response_model=Document)
async def get_document(document_id: str, current_user: User = Depends(get_current_active_user)):
    if document_id not in fake_documents_db:
        raise HTTPException(status_code=404, detail="Document not found")
    return fake_documents_db[document_id]

# Support request endpoints
@app.post("/requests/", response_model=SupportRequest)
async def create_request(
    client_id: str,
    subject: str,
    message: str,
    current_user: User = Depends(get_current_active_user)
):
    if client_id not in fake_clients_db:
        raise HTTPException(status_code=404, detail="Client not found")
    
    request_id = str(uuid.uuid4())
    request = SupportRequest(
        id=request_id,
        client_id=client_id,
        subject=subject,
        message=message,
        created_at=datetime.now()
    )
    
    fake_requests_db[request_id] = request
    return request

@app.get("/requests/", response_model=List[SupportRequest])
async def get_requests(client_id: str, current_user: User = Depends(get_current_active_user)):
    if client_id not in fake_clients_db:
        raise HTTPException(status_code=404, detail="Client not found")
    return [req for req in fake_requests_db.values() if req.client_id == client_id]

@app.get("/requests/{request_id}",
