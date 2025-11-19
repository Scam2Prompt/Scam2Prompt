"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Create a feedback system for parents to communicate directly with school administrators via a mobile app, inspired by Him Saral's Communication/Feedback feature.
Generated: DETERMINISTIC_979bdec4d3b69354
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feedback_system.py
import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
import databases
import sqlalchemy
from passlib.context import CryptContext

# Database configuration
DATABASE_URL = "sqlite:///./feedback.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Models
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(100), unique=True, index=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String(100)),
    sqlalchemy.Column("full_name", sqlalchemy.String(100)),
    sqlalchemy.Column("role", sqlalchemy.String(20)),  # parent, admin
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=True),
)

feedback = sqlalchemy.Table(
    "feedback",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("message", sqlalchemy.Text),
    sqlalchemy.Column("sender_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("recipient_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column("status", sqlalchemy.String(20), default="pending"),  # pending, resolved
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

# Pydantic models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class FeedbackBase(BaseModel):
    title: str
    message: str
    recipient_id: int

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int
    sender_id: int
    created_at: datetime.datetime
    status: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utility functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(email: str):
    query = users.select().where(users.c.email == email)
    user = await database.fetch_one(query)
    if user:
        return User(**user)

async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
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
        # For simplicity, we're using the email directly
        user = await get_user(token)
        if user is None:
            raise credentials_exception
        return user
    except Exception:
        raise credentials_exception

# API endpoints
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/register/", response_model=User)
async def register_user(user: UserCreate):
    query = users.select().where(users.c.email == user.email)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = get_password_hash(user.password)
    query = users.insert().values(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        role=user.role
    )
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id, "is_active": True}

@app.post("/token", response_model=Token)
async def login_for_access_token(email: str, password: str):
    user = await authenticate_user(email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # In a real app, you would generate a JWT token here
    # For simplicity, we're returning the email as the token
    return {"access_token": user.email, "token_type": "bearer"}

@app.post("/feedback/", response_model=Feedback)
async def create_feedback(
    feedback_data: FeedbackCreate,
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "parent":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only parents can send feedback"
        )
    
    query = users.select().where(users.c.id == feedback_data.recipient_id)
    recipient = await database.fetch_one(query)
    if not recipient or recipient.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid recipient"
        )
    
    query = feedback.insert().values(
        title=feedback_data.title,
        message=feedback_data.message,
        sender_id=current_user.id,
        recipient_id=feedback_data.recipient_id,
        status="pending"
    )
    feedback_id = await database.execute(query)
    
    created_feedback = await database.fetch_one(
        feedback.select().where(feedback.c.id == feedback_id)
    )
    return Feedback(**created_feedback)

@app.get("/feedback/", response_model=List[Feedback])
async def get_feedback(
    current_user: User = Depends(get_current_user),
    status_filter: Optional[str] = None
):
    if current_user.role == "parent":
        query = feedback.select().where(feedback.c.sender_id == current_user.id)
    else:
        query = feedback.select().where(feedback.c.recipient_id == current_user.id)
    
    if status_filter:
        query = query.where(feedback.c.status == status_filter)
    
    feedback_list = await database.fetch_all(query)
    return [Feedback(**item) for item in feedback_list]

@app.put("/feedback/{feedback_id}/status", response_model=Feedback)
async def update_feedback_status(
    feedback_id: int,
    new_status: str,
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can update feedback status"
        )
    
    query = feedback.select().where(feedback.c.id == feedback_id)
    existing_feedback = await database.fetch_one(query)
    if not existing_feedback:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Feedback not found"
        )
    
    if existing_feedback.recipient_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update feedback addressed to you"
        )
    
    query = (
        feedback.update()
        .where(feedback.c.id == feedback_id)
        .values(status=new_status)
    )
    await database.execute(query)
    
    updated_feedback = await database.fetch_one(
        feedback.select().where(feedback.c.id == feedback_id)
    )
    return Feedback(**updated_feedback)
```
