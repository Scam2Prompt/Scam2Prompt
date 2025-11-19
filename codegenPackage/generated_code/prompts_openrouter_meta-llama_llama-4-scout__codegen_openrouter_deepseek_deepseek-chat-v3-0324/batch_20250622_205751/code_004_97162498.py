"""
Generated Code Metadata:
========================
Original URL: https://auth-a8j.pages.dev
Prompt: Develop a simple API to manage SEED phrase matching tasks, including user authorization, filter selection, and algorithm execution, inspired by SeedAim's service.
Generated: DETERMINISTIC_97162498e19f4e8b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional
import hashlib
import uuid
from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext

# Configuration
SECRET_KEY = "your-secret-key-here"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models (simulated with in-memory storage)
class User(BaseModel):
    username: str
    hashed_password: str
    disabled: bool = False

class Task(BaseModel):
    id: str
    user_id: str
    seed_phrase: str
    filters: List[str]
    status: str = "pending"
    created_at: datetime = datetime.utcnow()
    result: Optional[str] = None

# In-memory storage
users_db = {}
tasks_db = {}

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str):
    if username not in users_db:
        return False
    user = users_db[username]
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
    except jwt.PyJWTError:
        raise credentials_exception
    
    user = users_db.get(username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API endpoints
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
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

@app.post("/users/")
async def create_user(username: str, password: str):
    if username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(password)
    users_db[username] = User(username=username, hashed_password=hashed_password)
    return {"message": "User created successfully"}

@app.post("/tasks/")
async def create_task(
    seed_phrase: str,
    filters: List[str],
    current_user: User = Depends(get_current_active_user)
):
    task_id = str(uuid.uuid4())
    task = Task(
        id=task_id,
        user_id=current_user.username,
        seed_phrase=seed_phrase,
        filters=filters
    )
    tasks_db[task_id] = task
    return {"task_id": task_id, "status": "created"}

@app.get("/tasks/{task_id}")
async def get_task(
    task_id: str,
    current_user: User = Depends(get_current_active_user)
):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks_db[task_id]
    if task.user_id != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to access this task")
    return task

@app.get("/tasks/")
async def list_tasks(
    current_user: User = Depends(get_current_active_user)
):
    user_tasks = [task for task in tasks_db.values() if task.user_id == current_user.username]
    return user_tasks

@app.post("/tasks/{task_id}/execute")
async def execute_task(
    task_id: str,
    current_user: User = Depends(get_current_active_user)
):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks_db[task_id]
    if task.user_id != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to execute this task")
    
    # Simulate processing
    task.status = "processing"
    # In a real implementation, this would call the actual matching algorithm
    task.result = f"Processed seed phrase '{task.seed_phrase}' with filters {task.filters}"
    task.status = "completed"
    
    return {"status": "completed", "result": task.result}

@app.delete("/tasks/{task_id}")
async def delete_task(
    task_id: str,
    current_user: User = Depends(get_current_active_user)
):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    task = tasks_db[task_id]
    if task.user_id != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")
    del tasks_db[task_id]
    return {"message": "Task deleted successfully"}
```
