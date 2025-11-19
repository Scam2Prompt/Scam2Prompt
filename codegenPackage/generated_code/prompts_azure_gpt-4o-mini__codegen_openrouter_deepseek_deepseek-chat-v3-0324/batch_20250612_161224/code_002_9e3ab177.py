"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Describe how to create a points system for a socialfi platform that rewards users for engaging with environmental content, inspired by Everyworld's model.
Generated: DETERMINISTIC_9e3ab1774bd226b5
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
import motor.motor_asyncio
from bson import ObjectId
from typing_extensions import Annotated
from fastapi import Depends

# Environment variables (would typically be in .env)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
MONGO_DB_URL = "mongodb://localhost:27017"
DB_NAME = "socialfi_platform"

# Initialize FastAPI
app = FastAPI()

# Security setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# MongoDB setup
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)
db = client[DB_NAME]

# Models
class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    points: int = 0
    daily_points_claimed: bool = False
    last_claim_date: Optional[datetime.date] = None

class ContentType(str, Enum):
    ARTICLE = "article"
    VIDEO = "video"
    POLL = "poll"
    COMMENT = "comment"
    SHARE = "share"

class Content(BaseModel):
    title: str
    description: str
    content_type: ContentType
    author_id: str
    created_at: datetime.datetime = datetime.datetime.now()
    environmental_score: int  # 1-10 scale of environmental impact

class Engagement(BaseModel):
    user_id: str
    content_id: str
    engagement_type: ContentType
    points_earned: int
    created_at: datetime.datetime = datetime.datetime.now()

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

async def authenticate_user(username: str, password: str):
    user = await db.users.find_one({"username": username})
    if not user or not verify_password(password, user["hashed_password"]):
        return False
    return User(**user)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
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
    
    user = await db.users.find_one({"username": token_data.username})
    if user is None:
        raise credentials_exception
    return User(**user)

# Points calculation
def calculate_points(content_type: ContentType, environmental_score: int) -> int:
    base_points = {
        ContentType.ARTICLE: 10,
        ContentType.VIDEO: 15,
        ContentType.POLL: 5,
        ContentType.COMMENT: 3,
        ContentType.SHARE: 7
    }
    
    # Environmental multiplier (1-10 scale)
    multiplier = environmental_score / 5.0
    
    return int(base_points[content_type] * multiplier)

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(username: str, password: str):
    user = await authenticate_user(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(username: str, email: str, password: str):
    hashed_password = get_password_hash(password)
    user = User(
        username=username,
        email=email,
        hashed_password=hashed_password,
        points=0
    )
    await db.users.insert_one(user.dict())
    return user

@app.post("/content/", response_model=Content)
async def create_content(
    title: str,
    description: str,
    content_type: ContentType,
    environmental_score: int,
    current_user: User = Depends(get_current_user)
):
    if environmental_score < 1 or environmental_score > 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Environmental score must be between 1 and 10"
        )
    
    content = Content(
        title=title,
        description=description,
        content_type=content_type,
        author_id=str(current_user.username),
        environmental_score=environmental_score
    )
    await db.content.insert_one(content.dict())
    return content

@app.post("/engage/{content_id}", response_model=Engagement)
async def engage_with_content(
    content_id: str,
    engagement_type: ContentType,
    current_user: User = Depends(get_current_user)
):
    content = await db.content.find_one({"_id": ObjectId(content_id)})
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    content_obj = Content(**content)
    points_earned = calculate_points(engagement_type, content_obj.environmental_score)
    
    # Update user points
    await db.users.update_one(
        {"username": current_user.username},
        {"$inc": {"points": points_earned}}
    )
    
    # Record engagement
    engagement = Engagement(
        user_id=str(current_user.username),
        content_id=content_id,
        engagement_type=engagement_type,
        points_earned=points_earned
    )
    await db.engagements.insert_one(engagement.dict())
    
    return engagement

@app.post("/claim-daily", response_model=User)
async def claim_daily_points(current_user: User = Depends(get_current_user)):
    today = datetime.date.today()
    
    if current_user.daily_points_claimed and current_user.last_claim_date == today:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Daily points already claimed today"
        )
    
    daily_points = 20  # Base daily points
    
    await db.users.update_one(
        {"username": current_user.username},
        {
            "$inc": {"points": daily_points},
            "$set": {
                "daily_points_claimed": True,
                "last_claim_date": today
            }
        }
    )
    
    updated_user = await db.users.find_one({"username": current_user.username})
    return User(**updated_user)

@app.get("/leaderboard", response_model=List[Dict[str, int]])
async def get_leaderboard(limit: int = 10):
    users = await db.users.find().sort("points", -1).limit(limit).to_list(limit)
    return [{"username": user["username"], "points": user["points"]} for user in users]

@app.get("/user/points", response_model=Dict[str, int])
async def get_user_points(current_user: User = Depends(get_current_user)):
    return {"username": current_user.username, "points": current_user.points}
```
