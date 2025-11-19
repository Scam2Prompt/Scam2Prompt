"""
Generated Code Metadata:
========================
Original URL: https://sale-humanizedai.web.app
Prompt: "Create a data hub API for aggregating user feedback to train AI models, using a token-based economy like HMZ for incentivization."
Generated: DETERMINISTIC_dfec879a9b623a77
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Data Hub API for aggregating user feedback to train AI models.
Implements token-based economy (HMZ) for incentivization.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
HMZ_TOKEN_RATE = float(os.getenv("HMZ_TOKEN_RATE", 0.1))  # Tokens per feedback item

# MongoDB configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "feedback_hub")

# Initialize FastAPI
app = FastAPI(
    title="AI Feedback Data Hub",
    description="API for aggregating user feedback with HMZ token incentivization",
    version="1.0.0"
)

# MongoDB client
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    hmz_balance: float = Field(default=0.0, ge=0.0)

class UserInDB(User):
    hashed_password: str

class Feedback(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    content: str
    model_id: str
    rating: int = Field(..., ge=1, le=5)
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    hmz_rewarded: float = Field(default=HMZ_TOKEN_RATE, ge=0.0)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class FeedbackCreate(BaseModel):
    content: str
    model_id: str
    rating: int = Field(..., ge=1, le=5)

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(username: str):
    user = await db.users.find_one({"username": username})
    if user:
        return UserInDB(**user)

async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[datetime.timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
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
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: dict):
    user = await authenticate_user(form_data["username"], form_data["password"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/feedback", response_model=Feedback)
async def submit_feedback(
    feedback: FeedbackCreate,
    current_user: User = Depends(get_current_active_user)
):
    feedback_data = Feedback(
        user_id=current_user.username,
        content=feedback.content,
        model_id=feedback.model_id,
        rating=feedback.rating
    )
    
    # Store feedback
    await db.feedback.insert_one(feedback_data.dict())
    
    # Update user HMZ balance
    new_balance = current_user.hmz_balance + feedback_data.hmz_rewarded
    await db.users.update_one(
        {"username": current_user.username},
        {"$set": {"hmz_balance": new_balance}}
    )
    
    return feedback_data

@app.get("/feedback", response_model=List[Feedback])
async def get_all_feedback(
    model_id: Optional[str] = None,
    limit: int = 100,
    skip: int = 0,
    current_user: User = Depends(get_current_active_user)
):
    query = {}
    if model_id:
        query["model_id"] = model_id
    
    feedback_items = await db.feedback.find(query).skip(skip).limit(limit).to_list(limit)
    return feedback_items

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/users/me/hmz", response_model=float)
async def get_hmz_balance(current_user: User = Depends(get_current_active_user)):
    return current_user.hmz_balance

@app.post("/users/register")
async def register_user(username: str, password: str, email: Optional[str] = None):
    existing_user = await get_user(username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(password)
    user = UserInDB(
        username=username,
        email=email,
        hashed_password=hashed_password,
        hmz_balance=0.0
    )
    
    await db.users.insert_one(user.dict())
    return {"message": "User registered successfully"}

# Startup event
@app.on_event("startup")
async def startup_db_client():
    await db.command("ping")
    print("Connected to MongoDB!")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
    print("Disconnected from MongoDB")
```
