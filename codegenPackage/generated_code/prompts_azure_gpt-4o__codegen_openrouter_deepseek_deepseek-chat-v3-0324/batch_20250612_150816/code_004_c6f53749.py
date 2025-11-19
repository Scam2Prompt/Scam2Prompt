"""
Generated Code Metadata:
========================
Original URL: https://visa-pwr.com
Prompt: Develop an API-based solution for managing visa application workflows, tailored to the administrative services offered by visapwr.
Generated: DETERMINISTIC_c6f53749d9183e20
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Visa Application Workflow Management API for visapwr
This API provides endpoints to manage visa application workflows for administrative services.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import uuid
import logging

# Configuration
SECRET_KEY = "your-secret-key-here"  # Should be environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models (would be ORM models in a real implementation)
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    email: EmailStr
    hashed_password: str
    disabled: bool = False
    role: str  # "admin", "officer", "applicant"

class VisaApplication(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    applicant_id: str
    visa_type: str
    status: str = "submitted"  # submitted, under_review, approved, rejected
    submission_date: datetime = Field(default_factory=datetime.utcnow)
    documents: List[str] = []
    notes: Optional[str] = None
    officer_id: Optional[str] = None
    last_updated: datetime = Field(default_factory=datetime.utcnow)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class ApplicationUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None
    documents: Optional[List[str]] = None

# Mock database
fake_users_db = {
    "admin": User(
        username="admin",
        email="admin@visapwr.com",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        role="admin"
    ),
    "officer1": User(
        username="officer1",
        email="officer1@visapwr.com",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        role="officer"
    ),
    "applicant1": User(
        username="applicant1",
        email="applicant1@example.com",
        hashed_password="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        role="applicant"
    )
}

fake_applications_db = {}

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="VisaPWR Workflow API",
    description="API for managing visa application workflows",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User(**user_dict.dict())
    return None

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

def check_permission(user: User, required_role: str):
    if user.role != required_role:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Operation not permitted for {user.role} role"
        )

# API endpoints
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

@app.post("/applications/", response_model=VisaApplication)
async def create_application(
    visa_type: str,
    documents: List[str],
    current_user: User = Depends(get_current_active_user)
):
    check_permission(current_user, "applicant")
    
    application = VisaApplication(
        applicant_id=current_user.id,
        visa_type=visa_type,
        documents=documents
    )
    
    fake_applications_db[application.id] = application
    logger.info(f"Application {application.id} created by {current_user.username}")
    return application

@app.get("/applications/", response_model=List[VisaApplication])
async def get_applications(
    status: Optional[str] = None,
    current_user: User = Depends(get_current_active_user)
):
    if current_user.role == "applicant":
        apps = [app for app in fake_applications_db.values() if app.applicant_id == current_user.id]
    else:
        apps = list(fake_applications_db.values())
    
    if status:
        apps = [app for app in apps if app.status == status]
    
    return apps

@app.get("/applications/{application_id}", response_model=VisaApplication)
async def get_application(
    application_id: str,
    current_user: User = Depends(get_current_active_user)
):
    if application_id not in fake_applications_db:
        raise HTTPException(status_code=404, detail="Application not found")
    
    application = fake_applications_db[application_id]
    
    if current_user.role == "applicant" and application.applicant_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this application")
    
    return application

@app.patch("/applications/{application_id}", response_model=VisaApplication)
async def update_application(
    application_id: str,
    update: ApplicationUpdate,
    current_user: User = Depends(get_current_active_user)
):
    check_permission(current_user, "officer")
    
    if application_id not in fake_applications_db:
        raise HTTPException(status_code=404, detail="Application not found")
    
    application = fake_applications_db[application_id]
    
    if update.status:
        application.status = update.status
    if update.notes:
        application.notes = update.notes
    if update.documents:
        application
