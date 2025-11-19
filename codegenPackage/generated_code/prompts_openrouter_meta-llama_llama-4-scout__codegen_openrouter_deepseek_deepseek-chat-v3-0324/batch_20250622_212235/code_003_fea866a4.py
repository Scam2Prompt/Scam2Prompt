"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: Develop an API to facilitate the submission and verification of financing and reimbursement requests for GIAC1, ensuring secure data handling and compliance with Moroccan regulations.
Generated: DETERMINISTIC_fea866a41390fd9b
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import uuid
import logging
from enum import Enum
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="GIAC1 Financing and Reimbursement API",
    description="API for handling financing and reimbursement requests in compliance with Moroccan regulations",
    version="1.0.0"
)

# Security configurations
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (simulated with in-memory storage)
class UserRole(str, Enum):
    ADMIN = "admin"
    FINANCE_OFFICER = "finance_officer"
    APPLICANT = "applicant"

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: EmailStr
    full_name: str
    hashed_password: str
    role: UserRole
    disabled: bool = False

class UserInDB(User):
    pass

class RequestStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    PROCESSED = "processed"

class DocumentType(str, Enum):
    INVOICE = "invoice"
    RECEIPT = "receipt"
    CONTRACT = "contract"
    IDENTIFICATION = "identification"

class Document(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: DocumentType
    file_path: str
    upload_date: datetime = Field(default_factory=datetime.now)

class Request(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    applicant_id: str
    request_type: str
    amount: float
    currency: str = "MAD"
    description: str
    status: RequestStatus = RequestStatus.PENDING
    submission_date: datetime = Field(default_factory=datetime.now)
    documents: List[Document] = []
    reviewer_id: Optional[str] = None
    review_date: Optional[datetime] = None
    rejection_reason: Optional[str] = None

# Simulated database
fake_users_db = {
    "admin": {
        "id": "1",
        "username": "admin",
        "email": "admin@giac1.ma",
        "full_name": "Admin User",
        "hashed_password": pwd_context.hash("adminpass"),
        "role": UserRole.ADMIN,
        "disabled": False
    },
    "finance": {
        "id": "2",
        "username": "finance",
        "email": "finance@giac1.ma",
        "full_name": "Finance Officer",
        "hashed_password": pwd_context.hash("financepass"),
        "role": UserRole.FINANCE_OFFICER,
        "disabled": False
    },
    "applicant1": {
        "id": "3",
        "username": "applicant1",
        "email": "applicant1@example.com",
        "full_name": "Applicant One",
        "hashed_password": pwd_context.hash("applicantpass"),
        "role": UserRole.APPLICANT,
        "disabled": False
    }
}

fake_requests_db = {}
fake_documents_db = {}

# Helper functions
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
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
    except JWTError:
        raise credentials_exception
    
    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def check_permission(user: User, required_role: UserRole):
    if user.role != required_role and user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions"
        )

# Models for API requests/responses
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class RequestCreate(BaseModel):
    request_type: str
    amount: float
    currency: str = "MAD"
    description: str
    documents: List[DocumentType]

class RequestUpdate(BaseModel):
    status: Optional[RequestStatus] = None
    rejection_reason: Optional[str] = None

class RequestResponse(BaseModel):
    id: str
    request_type: str
    amount: float
    currency: str
    description: str
    status: RequestStatus
    submission_date: datetime
    documents: List[Document]

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str
    role: UserRole

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    full_name: str
    role: UserRole

# Authentication endpoints
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

# User management endpoints
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, current_user: User = Depends(get_current_active_user)):
    check_permission(current_user, UserRole.ADMIN)
    
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = pwd_context.hash(user.password)
    user_dict = {
        "id": str(uuid.uuid4()),
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hashed_password,
        "role": user.role,
        "disabled": False
    }
    fake_users_db[user.username] = user_dict
    return UserResponse(**user_dict)

# Request endpoints
@app.post("/requests/", response_model=RequestResponse)
async def create_request(
    request: RequestCreate,
    current_user: User = Depends(get_current_active_user)
):
    check_permission(current_user, UserRole.APPLICANT)
    
    request_id = str(uuid.uuid4())
    documents = [Document(type=doc_type, file_path
