"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: Recommend an API for managing confidentiality in coworking spaces and write a sample implementation in Python, based on the "Confidentialité au coworking : enjeux et solutions clés" section of NetCoworking.
Generated: DETERMINISTIC_6eb97dd55a9b46c8
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, Optional, List
from pydantic import BaseModel, Field, validator
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext

# Configuration
SECRET_KEY = "your-secret-key-here"  # Replace with a secure secret key in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Models
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Workspace(BaseModel):
    id: str
    name: str
    description: str
    is_private: bool = Field(default=True, description="Whether the workspace is private")
    members: List[str] = Field(default_factory=list, description="List of member usernames")

class WorkspaceCreate(BaseModel):
    name: str
    description: str
    is_private: bool = True

class WorkspaceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_private: Optional[bool] = None

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock Database
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "full_name": "John Doe",
        "disabled": False,
        "hashed_password": pwd_context.hash("secret")
    }
}

fake_workspaces_db = {}

# Helper Functions
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
    except jwt.PyJWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# FastAPI App
app = FastAPI(
    title="Coworking Space Confidentiality API",
    description="API for managing confidentiality in coworking spaces",
    version="1.0.0"
)

@app.post("/token", response_model=Token)
async def login_for_access_token(username: str, password: str):
    user = authenticate_user(fake_users_db, username, password)
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

@app.post("/workspaces/", response_model=Workspace)
async def create_workspace(
    workspace: WorkspaceCreate,
    current_user: User = Depends(get_current_active_user)
):
    workspace_id = f"ws_{len(fake_workspaces_db) + 1}"
    new_workspace = Workspace(
        id=workspace_id,
        name=workspace.name,
        description=workspace.description,
        is_private=workspace.is_private,
        members=[current_user.username]
    )
    fake_workspaces_db[workspace_id] = new_workspace.dict()
    return new_workspace

@app.get("/workspaces/{workspace_id}", response_model=Workspace)
async def read_workspace(
    workspace_id: str,
    current_user: User = Depends(get_current_active_user)
):
    if workspace_id not in fake_workspaces_db:
        raise HTTPException(status_code=404, detail="Workspace not found")
    
    workspace = Workspace(**fake_workspaces_db[workspace_id])
    
    if workspace.is_private and current_user.username not in workspace.members:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to this private workspace"
        )
    
    return workspace

@app.put("/workspaces/{workspace_id}", response_model=Workspace)
async def update_workspace(
    workspace_id: str,
    workspace_update: WorkspaceUpdate,
    current_user: User = Depends(get_current_active_user)
):
    if workspace_id not in fake_workspaces_db:
        raise HTTPException(status_code=404, detail="Workspace not found")
    
    workspace = Workspace(**fake_workspaces_db[workspace_id])
    
    if current_user.username not in workspace.members:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only members can update the workspace"
        )
    
    update_data = workspace_update.dict(exclude_unset=True)
    updated_workspace = workspace.copy(update=update_data)
    fake_workspaces_db[workspace_id] = updated_workspace.dict()
    
    return updated_workspace

@app.post("/workspaces/{workspace_id}/members", response_model=Workspace)
async def add_member_to_workspace(
    workspace_id: str,
    member_username: str,
    current_user: User = Depends(get_current_active_user)
):
    if workspace_id not in fake_workspaces_db:
        raise HTTPException(status_code=404, detail="Workspace not found")
    
    workspace = Workspace(**fake_workspaces_db[workspace_id])
    
    if current_user.username not in workspace.members:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only members can add new members"
        )
    
    if member_username not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    if member_username in workspace.members:
        raise HTTPException(status_code=400, detail="User is already a member")
    
    workspace.members.append(member_username)
    fake_workspaces_db[workspace_id] = workspace.dict()
    
    return workspace

@app.get("/workspaces/", response_model=List[Workspace])
async def list_workspaces(current_user: User = Depends(get_current_active_user)):
    workspaces = []
    for workspace_id in fake_workspaces_db:
        workspace = Workspace(**fake_workspaces_db[workspace_id])
        if not workspace.is_private or current_user.username in workspace.members:
            workspaces.append(workspace)
    return workspaces

# Sample usage
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
