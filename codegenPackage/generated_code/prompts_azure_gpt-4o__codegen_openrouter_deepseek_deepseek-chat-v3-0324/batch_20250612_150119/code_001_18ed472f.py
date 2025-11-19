"""
Generated Code Metadata:
========================
Original URL: https://retro-pgf.vercel.app
Prompt: Generate a script to automate the setup of an RPGF round using the EasyRetroPGF library, including user authentication and project submission functionality.
Generated: DETERMINISTIC_18ed472fdd4d42d1
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import List, Dict, Optional
from datetime import datetime
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field, validator
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing_extensions import Annotated

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database models (simplified for example)
class User(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool = False

class UserInDB(User):
    hashed_password: str

class Project(BaseModel):
    id: str
    name: str
    description: str
    category: str
    submitted_by: str
    submission_date: datetime = Field(default_factory=datetime.now)
    funding_goal: float
    impact_score: Optional[float] = None

class RoundConfig(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    total_funding: float
    categories: List[str]
    
    @validator('end_date')
    def end_date_must_be_after_start_date(cls, v, values):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError('End date must be after start date')
        return v

# Mock database
fake_users_db = {
    "admin": {
        "username": "admin",
        "email": "admin@example.com",
        "full_name": "Admin User",
        "disabled": False,
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"  # "secret"
    }
}

fake_projects_db = {}
fake_rounds_db = {}

# Auth setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(title="EasyRetroPGF Automation API")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
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

def create_access_token(data: dict, expires_delta: Optional[datetime] = None):
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
    except JWTError:
        raise credentials_exception
    
    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# API Endpoints
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
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

@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

@app.post("/rounds/", response_model=RoundConfig)
async def create_round(
    round_config: RoundConfig,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if current_user.username != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create rounds")
    
    round_id = f"round_{len(fake_rounds_db) + 1}"
    fake_rounds_db[round_id] = round_config
    return round_config

@app.get("/rounds/{round_id}", response_model=RoundConfig)
async def get_round(round_id: str):
    if round_id not in fake_rounds_db:
        raise HTTPException(status_code=404, detail="Round not found")
    return fake_rounds_db[round_id]

@app.post("/projects/", response_model=Project)
async def submit_project(
    project: Project,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    project_id = f"project_{len(fake_projects_db) + 1}"
    project.id = project_id
    project.submitted_by = current_user.username
    fake_projects_db[project_id] = project
    return project

@app.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str):
    if project_id not in fake_projects_db:
        raise HTTPException(status_code=404, detail="Project not found")
    return fake_projects_db[project_id]

@app.get("/projects/", response_model=List[Project])
async def list_projects():
    return list(fake_projects_db.values())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
