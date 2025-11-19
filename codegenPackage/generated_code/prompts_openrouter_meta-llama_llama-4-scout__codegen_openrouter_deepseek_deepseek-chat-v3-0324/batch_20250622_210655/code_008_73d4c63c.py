"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Develop a RESTful API for submitting and tracking complaints about health products and services in Thailand.
Generated: DETERMINISTIC_73d4c63c5f15a522
Batch ID: 20250622_210655
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
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import Annotated

# Initialize FastAPI app
app = FastAPI(
    title="Thailand Health Products Complaints API",
    description="A RESTful API for submitting and tracking complaints about health products and services in Thailand",
    version="1.0.0"
)

# Security configurations
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in-memory for this example)
class User(BaseModel):
    id: str
    username: str
    email: str
    full_name: str
    disabled: bool = False
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str

class UserInDB(User):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Complaint(BaseModel):
    id: str
    product_name: str
    product_type: str
    manufacturer: str
    complaint_details: str
    submitter_id: str
    status: str = "Submitted"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class ComplaintCreate(BaseModel):
    product_name: str
    product_type: str
    manufacturer: str
    complaint_details: str

class ComplaintUpdate(BaseModel):
    status: Optional[str] = None
    complaint_details: Optional[str] = None

# In-memory database
fake_users_db = {}
fake_complaints_db = {}

# Utility functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[int] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
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
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
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

@app.post("/register", response_model=User)
async def register_user(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    user_id = str(uuid.uuid4())
    db_user = User(
        id=user_id,
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password
    )
    fake_users_db[user.username] = db_user.dict()
    return db_user

# Complaint endpoints
@app.post("/complaints/", response_model=Complaint)
async def create_complaint(
    complaint: ComplaintCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    complaint_id = str(uuid.uuid4())
    db_complaint = Complaint(
        id=complaint_id,
        product_name=complaint.product_name,
        product_type=complaint.product_type,
        manufacturer=complaint.manufacturer,
        complaint_details=complaint.complaint_details,
        submitter_id=current_user.id
    )
    fake_complaints_db[complaint_id] = db_complaint.dict()
    return db_complaint

@app.get("/complaints/", response_model=List[Complaint])
async def read_complaints(
    skip: int = 0,
    limit: int = 10,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    complaints = list(fake_complaints_db.values())[skip : skip + limit]
    return complaints

@app.get("/complaints/{complaint_id}", response_model=Complaint)
async def read_complaint(
    complaint_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if complaint_id not in fake_complaints_db:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return fake_complaints_db[complaint_id]

@app.put("/complaints/{complaint_id}", response_model=Complaint)
async def update_complaint(
    complaint_id: str,
    complaint_update: ComplaintUpdate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if complaint_id not in fake_complaints_db:
        raise HTTPException(status_code=404, detail="Complaint not found")
    
    complaint = Complaint(**fake_complaints_db[complaint_id])
    
    if complaint.submitter_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this complaint")
    
    update_data = complaint_update.dict(exclude_unset=True)
    updated_complaint = complaint.copy(update=update_data)
    updated_complaint.updated_at = datetime.now()
    
    fake_complaints_db[complaint_id] = updated_complaint.dict()
    return updated_complaint

@app.get("/users/me", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

@app.get("/users/me/complaints", response_model=List[Complaint])
async def read_user_complaints(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    user_complaints = [
        complaint for complaint in fake_complaints_db.values() 
        if complaint["submitter_id"] == current_user.id
    ]
    return user_complaints
```
