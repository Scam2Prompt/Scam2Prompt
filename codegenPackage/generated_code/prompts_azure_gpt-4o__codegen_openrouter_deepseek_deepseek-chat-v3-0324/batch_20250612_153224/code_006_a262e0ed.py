"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Develop an API for monitoring agricultural activities, including field mapping, visit scheduling, and certification tracking, based on Azagros' features.
Generated: DETERMINISTIC_a262e0edb7896741
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agricultural_monitoring_api.py
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date, datetime
from uuid import UUID, uuid4
from enum import Enum
import logging
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import Annotated

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security configurations
SECRET_KEY = "your-secret-key-here"  # Should be in environment variables in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models (in-memory for this example)
class Database:
    def __init__(self):
        self.fields = []
        self.visits = []
        self.certifications = []
        self.users = []

db = Database()

# Pydantic models
class FieldSizeUnit(str, Enum):
    acres = "acres"
    hectares = "hectares"

class FieldStatus(str, Enum):
    active = "active"
    inactive = "inactive"
    fallow = "fallow"

class Field(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    location: str
    size: float
    size_unit: FieldSizeUnit
    status: FieldStatus = FieldStatus.active
    crops: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class VisitType(str, Enum):
    inspection = "inspection"
    maintenance = "maintenance"
    harvest = "harvest"
    planting = "planting"

class Visit(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    field_id: UUID
    type: VisitType
    scheduled_date: date
    completed: bool = False
    notes: Optional[str] = None
    completed_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CertificationType(str, Enum):
    organic = "organic"
    fair_trade = "fair_trade"
    gmp = "gmp"
    other = "other"

class Certification(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    field_id: UUID
    type: CertificationType
    certification_body: str
    issued_date: date
    expiry_date: date
    is_active: bool = True
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserRole(str, Enum):
    admin = "admin"
    manager = "manager"
    field_worker = "field_worker"
    inspector = "inspector"

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    role: UserRole = UserRole.field_worker

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID
    disabled: bool = False

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Security utilities
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    for user in db.users:
        if user.username == username:
            return user
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
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
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Initialize FastAPI app
app = FastAPI(
    title="Agricultural Monitoring API",
    description="API for monitoring agricultural activities including field mapping, visit scheduling, and certification tracking",
    version="1.0.0"
)

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "exp": access_token_expires}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        id=uuid4(),
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        role=user.role,
        hashed_password=hashed_password
    )
    db.users.append(db_user)
    return db_user

# Field endpoints
@app.post("/fields/", response_model=Field)
async def create_field(field: Field, current_user: Annotated[User, Depends(get_current_active_user)]):
    if current_user.role not in [UserRole.admin, UserRole.manager]:
        raise HTTPException(status_code=403, detail="Only admins and managers can create fields")
    db.fields.append(field)
    logger.info(f"Field created: {field.id}")
    return field

@app.get("/fields/", response_model=List[Field])
async def list_fields(current_user: Annotated[User, Depends(get_current_active_user)]):
    return db.fields

@app.get("/fields/{field_id}", response_model=Field)
async def get_field(field_id: UUID, current_user: Annotated[User, Depends(get_current_active_user)]):
    for field in db.fields:
        if field.id == field_id:
            return field
    raise HTTPException(status_code=404, detail="Field not found")

@app.put("/fields/{field_id}", response_model=Field)
async def update_field(field_id: UUID, updated_field: Field, current_user: Annotated[User, Depends(get_current_active_user)]):
    if current_user.role not in [UserRole.admin, UserRole.manager]:
        raise HTTPException(status_code=403, detail="Only admins and managers can update fields")
    
    for idx, field in enumerate(db.fields):
        if field.id == field_id:
            updated_field.id = field_id
            updated_field.created_at = field.created_at
            updated_field.updated_at = datetime.utcnow()
            db.fields[idx] = updated_field
            logger.info(f"Field updated: {field_id}")
            return updated_field
    raise HTTPException(status_code=404, detail="Field not found")

@app.delete("/fields/{field_id}")
async def delete_field(field_id: UUID, current_user: Annotated[User, Depends(get_current_active_user)]):
    if current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Only admins can delete fields")
    
    for idx, field in enumerate(db.fields):
        if field.id == field_id:
            db.fields.pop(idx)
            logger.info(f"Field deleted: {field_id}")
            return {"message": "Field deleted successfully"}
    raise HTTPException(status_code=404, detail="Field not found")

#
