"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Generate an API that connects women in Igbo communities for cultural preservation activities, reflecting the offerings of Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_dad349dba7d3f035
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
API for connecting women in Igbo communities for cultural preservation activities.
Inspired by Nkata ndi Inyom Igbo's offerings.
"""

from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid
import motor.motor_asyncio
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware

# Configuration
SECRET_KEY = "your-secret-key-here"  # Should be in environment variables in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# MongoDB configuration
MONGO_DETAILS = "mongodb://localhost:27017"  # Should be in environment variables in production
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.igbo_women_db
users_collection = database.get_collection("users")
activities_collection = database.get_collection("activities")
discussions_collection = database.get_collection("discussions")

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    community: str
    disabled: Optional[bool] = False

class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    password: str

class Activity(BaseModel):
    title: str
    description: str
    location: str
    date: datetime
    organizer: str  # username of the organizer
    participants: List[str] = []  # list of usernames
    tags: List[str] = []  # e.g., ["dancing", "cooking", "language"]

class Discussion(BaseModel):
    title: str
    content: str
    author: str  # username of the author
    created_at: datetime = datetime.now()
    comments: List[dict] = []  # {author: str, content: str, created_at: datetime}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Helper functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(username: str):
    user_dict = await users_collection.find_one({"username": username})
    if user_dict:
        return UserInDB(**user_dict)

async def authenticate_user(username: str, password: str):
    user = await get_user(username)
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
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Initialize FastAPI
app = FastAPI(
    title="Nkata ndi Inyom Igbo API",
    description="API for connecting women in Igbo communities for cultural preservation activities",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
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
async def create_user(user: UserCreate):
    existing_user = await users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    existing_email = await users_collection.find_one({"email": user.email})
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    del user_dict["password"]
    
    result = await users_collection.insert_one(user_dict)
    if result.inserted_id:
        return user_dict
    raise HTTPException(status_code=500, detail="Error creating user")

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.post("/activities/", response_model=Activity)
async def create_activity(activity: Activity, current_user: User = Depends(get_current_active_user)):
    activity_dict = activity.dict()
    activity_dict["organizer"] = current_user.username
    result = await activities_collection.insert_one(activity_dict)
    if result.inserted_id:
        return activity_dict
    raise HTTPException(status_code=500, detail="Error creating activity")

@app.get("/activities/", response_model=List[Activity])
async def get_activities(skip: int = 0, limit: int = 10):
    activities = await activities_collection.find().skip(skip).limit(limit).to_list(limit)
    return activities

@app.post("/activities/{activity_id}/join")
async def join_activity(activity_id: str, current_user: User = Depends(get_current_active_user)):
    activity = await activities_collection.find_one({"_id": activity_id})
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    
    if current_user.username in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already joined this activity")
    
    result = await activities_collection.update_one(
        {"_id": activity_id},
        {"$push": {"participants": current_user.username}}
    )
    if result.modified_count == 1:
        return {"message": "Successfully joined activity"}
    raise HTTPException(status_code=500, detail="Error joining activity")

@app.post("/discussions/", response_model=Discussion)
async def create_discussion(discussion: Discussion, current_user: User = Depends(get_current_active_user)):
    discussion_dict = discussion.dict()
    discussion_dict["author"] = current_user.username
    result = await discussions_collection.insert_one(discussion_dict)
    if result.inserted_id:
        return discussion_dict
    raise HTTPException(status_code=500, detail="Error creating discussion")

@app.get("/discussions/", response_model=List[Discussion])
async def get_discussions(skip: int = 0, limit: int = 10):
    discussions = await discussions_collection.find().skip(skip).limit(limit).to_list(limit)
    return discussions

@app.post("/discussions/{discussion_id}/comments")
async def add_comment(discussion_id: str, comment: dict, current_user: User = Depends(get_current_active_user)):
    discussion = await discussions_collection.find_one({"_id": discussion_id})
    if not discussion:
