"""
Generated Code Metadata:
========================
Original URL: https://todosobreguitarra.com
Prompt: Suggest an API for managing online guitar courses and integrating video tutorials, based on the offerings from Todo sobre Guitarra.
Generated: DETERMINISTIC_39afa7008679bc0c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import boto3
from botocore.exceptions import ClientError

# Initialize FastAPI app
app = FastAPI(
    title="Todo sobre Guitarra API",
    description="API for managing online guitar courses and video tutorials",
    version="1.0.0"
)

# Security configurations
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# AWS S3 configuration for video storage
S3_BUCKET = "todo-sobre-guitarra-videos"
s3_client = boto3.client('s3')

# Database models (in a real app, this would connect to a database)
fake_users_db = {}
fake_courses_db = {}
fake_videos_db = {}

# Pydantic models
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None

class Course(BaseModel):
    id: str
    title: str
    description: str
    level: str  # beginner, intermediate, advanced
    created_at: datetime
    updated_at: datetime
    instructor: str
    is_active: bool

class CourseCreate(BaseModel):
    title: str
    description: str
    level: str
    instructor: str

class VideoTutorial(BaseModel):
    id: str
    course_id: str
    title: str
    description: str
    duration: int  # in seconds
    s3_key: str
    created_at: datetime
    is_preview: bool

class VideoTutorialCreate(BaseModel):
    course_id: str
    title: str
    description: str
    duration: int
    is_preview: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Helper functions
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    # In a real app, implement proper JWT token creation
    return "fake-access-token"

def generate_s3_key(course_id: str, video_title: str):
    return f"courses/{course_id}/{video_title.replace(' ', '_')}_{uuid.uuid4().hex[:8]}"

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
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    user_in_db = UserInDB(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        disabled=False
    )
    fake_users_db[user.username] = user_in_db.dict()
    return user_in_db

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(oauth2_scheme)):
    return current_user

@app.post("/courses/", response_model=Course)
async def create_course(course: CourseCreate, current_user: User = Depends(oauth2_scheme)):
    course_id = str(uuid.uuid4())
    now = datetime.now()
    new_course = Course(
        id=course_id,
        title=course.title,
        description=course.description,
        level=course.level,
        created_at=now,
        updated_at=now,
        instructor=course.instructor,
        is_active=True
    )
    fake_courses_db[course_id] = new_course.dict()
    return new_course

@app.get("/courses/", response_model=List[Course])
async def list_courses(level: Optional[str] = None):
    courses = list(fake_courses_db.values())
    if level:
        courses = [c for c in courses if c["level"] == level]
    return courses

@app.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: str):
    if course_id not in fake_courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    return fake_courses_db[course_id]

@app.post("/courses/{course_id}/videos/", response_model=VideoTutorial)
async def create_video_tutorial(
    course_id: str,
    video: VideoTutorialCreate,
    current_user: User = Depends(oauth2_scheme)
):
    if course_id not in fake_courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    
    video_id = str(uuid.uuid4())
    s3_key = generate_s3_key(course_id, video.title)
    now = datetime.now()
    
    new_video = VideoTutorial(
        id=video_id,
        course_id=course_id,
        title=video.title,
        description=video.description,
        duration=video.duration,
        s3_key=s3_key,
        created_at=now,
        is_preview=video.is_preview
    )
    
    fake_videos_db[video_id] = new_video.dict()
    return new_video

@app.get("/courses/{course_id}/videos/", response_model=List[VideoTutorial])
async def list_video_tutorials(course_id: str):
    if course_id not in fake_courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    
    videos = [v for v in fake_videos_db.values() if v["course_id"] == course_id]
    return videos

@app.get("/videos/{video_id}/presigned-url")
async def get_video_presigned_url(video_id: str, current_user: User = Depends(oauth2_scheme)):
    if video_id not in fake_videos_db:
        raise HTTPException(status_code=404, detail="Video not found")
    
    video = fake_videos_db[video_id]
    try:
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': S3_BUCKET, 'Key': video["s3_key"]},
            ExpiresIn=3600
        )
        return {"presigned_url": presigned_url}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))
```
