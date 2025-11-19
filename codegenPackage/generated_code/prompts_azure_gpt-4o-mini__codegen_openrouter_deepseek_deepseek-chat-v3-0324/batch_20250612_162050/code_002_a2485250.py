"""
Generated Code Metadata:
========================
Original URL: https://lojaoficial.cloud
Prompt: Create a sample application that allows users to collaborate on architectural designs, referencing the features of the Études Architect app.
Generated: DETERMINISTIC_a24852508de2e955
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import uuid
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException, UploadFile, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
import motor.motor_asyncio
from bson import ObjectId

# Initialize FastAPI app
app = FastAPI(
    title="Études Architect Collaboration App",
    description="A platform for architects to collaborate on designs",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.etudes_architect

# Security configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class User(BaseModel):
    id: str
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    disabled: Optional[bool] = False

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class Project(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    owner_id: str
    collaborators: List[str] = []
    files: List[str] = []

class ProjectCreate(BaseModel):
    name: str
    description: str
    collaborators: List[str] = []

class Comment(BaseModel):
    id: str
    project_id: str
    user_id: str
    content: str
    created_at: datetime
    x_position: Optional[float] = None
    y_position: Optional[float] = None
    z_position: Optional[float] = None

class CommentCreate(BaseModel):
    project_id: str
    content: str
    x_position: Optional[float] = None
    y_position: Optional[float] = None
    z_position: Optional[float] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Utility functions
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

async def get_user(username: str) -> Optional[UserInDB]:
    user_data = await db.users.find_one({"username": username})
    if user_data:
        return UserInDB(**user_data)
    return None

async def authenticate_user(username: str, password: str):
    user = await get_user(username)
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
        # For simplicity, we're just using the token as username
        user = await get_user(token)
        if user is None:
            raise credentials_exception
        return user
    except Exception:
        raise credentials_exception

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # In a real app, you would generate a JWT token here
    return {"access_token": user.username, "token_type": "bearer"}

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    existing_user = await get_user(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    user_dict["id"] = str(uuid.uuid4())
    del user_dict["password"]
    
    await db.users.insert_one(user_dict)
    return User(**user_dict)

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/projects/", response_model=Project)
async def create_project(
    project: ProjectCreate,
    current_user: User = Depends(get_current_user)
):
    project_dict = project.dict()
    project_dict["id"] = str(uuid.uuid4())
    project_dict["created_at"] = datetime.utcnow()
    project_dict["updated_at"] = datetime.utcnow()
    project_dict["owner_id"] = current_user.id
    project_dict["collaborators"] = list(set(project_dict["collaborators"] + [current_user.id]))
    
    await db.projects.insert_one(project_dict)
    return Project(**project_dict)

@app.get("/projects/", response_model=List[Project])
async def list_projects(current_user: User = Depends(get_current_user)):
    projects = await db.projects.find({
        "$or": [
            {"owner_id": current_user.id},
            {"collaborators": current_user.id}
        ]
    }).to_list(100)
    return [Project(**p) for p in projects]

@app.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str, current_user: User = Depends(get_current_user)):
    project = await db.projects.find_one({"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if current_user.id not in project["collaborators"] and current_user.id != project["owner_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to access this project")
    
    return Project(**project)

@app.post("/projects/{project_id}/comments", response_model=Comment)
async def add_comment(
    project_id: str,
    comment: CommentCreate,
    current_user: User = Depends(get_current_user)
):
    project = await db.projects.find_one({"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if current_user.id not in project["collaborators"] and current_user.id != project["owner_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to comment on this project")
    
    comment_dict = comment.dict()
    comment_dict["id"] = str(uuid.uuid4())
    comment_dict["user_id"] = current_user.id
    comment_dict["created_at"] = datetime.utcnow()
    
    await db.comments.insert_one(comment_dict)
    return Comment(**comment_dict)

@app.get("/projects/{project_id}/comments", response_model=List[Comment])
async def list_comments(
    project_id: str,
    current_user: User = Depends(get_current_user)
):
    project = await db.projects.find_one({"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if current_user.id not in project["collaborators"] and current_user.id != project["owner_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to view comments for this project")
    
    comments = await db.comments.find({"project_id": project_id}).to_list(100)
    return [Comment(**c) for c in comments]

@app.post("/projects/{project_id}/files")
async def upload_file(
    project_id: str,
    file: UploadFile,
    current_user: User = Depends(get_current_user)
):
    project = await db.projects.find_one({"id": project_id})
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    if current_user.id not in project["collaborators"] and current_user.id != project["owner_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to upload files to this project")
    
    # In a real app, you would save the file to storage (S3, local
