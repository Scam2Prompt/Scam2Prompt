"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: How can I implement a project management API to streamline communication and collaboration in a construction project, similar to the services offered by Bismillah Traders?
Generated: DETERMINISTIC_912da78a7ab0bc28
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
from jose import JWTError, jwt
from typing import Annotated

# Configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models (in a real app, use a proper database)
fake_users_db = {}
projects_db = {}
tasks_db = {}
comments_db = {}

# Pydantic models
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    password: str

class Project(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    budget: float
    status: str = "planned"

class Task(BaseModel):
    project_id: str
    name: str
    description: str
    assigned_to: str
    due_date: datetime
    status: str = "todo"

class Comment(BaseModel):
    task_id: str
    author: str
    content: str
    timestamp: datetime = datetime.now()

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

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

# Auth endpoints
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

@app.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_password
    user_dict["disabled"] = False
    fake_users_db[user.username] = user_dict
    return user

# Project endpoints
@app.post("/projects/", response_model=Project)
async def create_project(project: Project, current_user: Annotated[User, Depends(get_current_active_user)]):
    project_id = str(uuid.uuid4())
    project_dict = project.dict()
    project_dict["id"] = project_id
    project_dict["created_by"] = current_user.username
    projects_db[project_id] = project_dict
    return project_dict

@app.get("/projects/", response_model=List[Project])
async def list_projects(current_user: Annotated[User, Depends(get_current_active_user)]):
    return list(projects_db.values())

@app.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    if project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Project not found")
    return projects_db[project_id]

# Task endpoints
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task, current_user: Annotated[User, Depends(get_current_active_user)]):
    if task.project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Project not found")
    
    task_id = str(uuid.uuid4())
    task_dict = task.dict()
    task_dict["id"] = task_id
    task_dict["created_by"] = current_user.username
    tasks_db[task_id] = task_dict
    return task_dict

@app.get("/tasks/", response_model=List[Task])
async def list_tasks(project_id: Optional[str] = None, current_user: Annotated[User, Depends(get_current_active_user)]):
    if project_id:
        if project_id not in projects_db:
            raise HTTPException(status_code=404, detail="Project not found")
        return [task for task in tasks_db.values() if task["project_id"] == project_id]
    return list(tasks_db.values())

# Comment endpoints
@app.post("/comments/", response_model=Comment)
async def create_comment(comment: Comment, current_user: Annotated[User, Depends(get_current_active_user)]):
    if comment.task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    comment_id = str(uuid.uuid4())
    comment_dict = comment.dict()
    comment_dict["id"] = comment_id
    comments_db[comment_id] = comment_dict
    return comment_dict

@app.get("/comments/", response_model=List[Comment])
async def list_comments(task_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return [comment for comment in comments_db.values() if comment["task_id"] == task_id]

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
