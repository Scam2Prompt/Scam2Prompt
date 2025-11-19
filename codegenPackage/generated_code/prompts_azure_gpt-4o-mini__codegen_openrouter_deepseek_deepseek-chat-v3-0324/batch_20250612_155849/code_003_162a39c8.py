"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Create an API that facilitates communication between residents and property managers, reflecting the comprehensive services offered by BlocPrest for block administration.
Generated: DETERMINISTIC_162a39c82b0223b5
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from typing import Annotated

# Initialize FastAPI app
app = FastAPI(
    title="BlocPrest Resident-Manager Communication API",
    description="API for facilitating communication between residents and property managers",
    version="1.0.0"
)

# Security configurations
SECRET_KEY = "your-secret-key-here"  # In production, use environment variables
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database models (in production, use a real database)
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": pwd_context.hash("secret"),
        "disabled": False,
        "role": "resident"
    },
    "janedoe": {
        "username": "janedoe",
        "full_name": "Jane Doe",
        "email": "janedoe@example.com",
        "hashed_password": pwd_context.hash("secret"),
        "disabled": False,
        "role": "manager"
    }
}

# Pydantic models
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    role: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Message(BaseModel):
    id: str
    sender: str
    recipient: str
    content: str
    timestamp: datetime
    read: bool = False

class MessageCreate(BaseModel):
    recipient: str
    content: str

class Announcement(BaseModel):
    id: str
    title: str
    content: str
    author: str
    timestamp: datetime
    priority: str  # low, medium, high

class AnnouncementCreate(BaseModel):
    title: str
    content: str
    priority: str

class MaintenanceRequest(BaseModel):
    id: str
    resident_id: str
    title: str
    description: str
    status: str  # pending, in_progress, completed
    timestamp: datetime
    assigned_to: Optional[str] = None

class MaintenanceRequestCreate(BaseModel):
    title: str
    description: str

# In-memory storage (replace with database in production)
messages_db = []
announcements_db = []
maintenance_requests_db = []

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

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
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
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

# Message endpoints
@app.post("/messages/", response_model=Message)
async def send_message(
    message: MessageCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    # Check if recipient exists
    recipient = get_user(fake_users_db, message.recipient)
    if not recipient:
        raise HTTPException(status_code=404, detail="Recipient not found")
    
    new_message = Message(
        id=str(uuid.uuid4()),
        sender=current_user.username,
        recipient=message.recipient,
        content=message.content,
        timestamp=datetime.utcnow(),
        read=False
    )
    messages_db.append(new_message)
    return new_message

@app.get("/messages/", response_model=List[Message])
async def get_messages(
    current_user: Annotated[User, Depends(get_current_active_user)],
    unread_only: bool = False
):
    user_messages = [
        msg for msg in messages_db 
        if msg.recipient == current_user.username or msg.sender == current_user.username
    ]
    
    if unread_only:
        user_messages = [msg for msg in user_messages if not msg.read and msg.recipient == current_user.username]
    
    return user_messages

@app.put("/messages/{message_id}/read", response_model=Message)
async def mark_message_as_read(
    message_id: str,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    for msg in messages_db:
        if msg.id == message_id and msg.recipient == current_user.username:
            msg.read = True
            return msg
    raise HTTPException(status_code=404, detail="Message not found")

# Announcement endpoints
@app.post("/announcements/", response_model=Announcement)
async def create_announcement(
    announcement: AnnouncementCreate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    if current_user.role != "manager":
        raise HTTPException(status_code=403, detail="Only managers can create announcements")
    
    new_announcement = Announcement(
        id=str(uuid.uuid4()),
        title=announcement.title,
        content=announcement.content,
        author=current_user.username,
        timestamp=datetime.utcnow(),
        priority=announcement.priority
    )
    announcements_db.append(new_announcement)
    return new_announcement

@app.get("/announcements/", response_model=List[Announcement])
async def get_announcements(
    current_user: Annotated[User, Depends(get_current_active_user)],
    priority: Optional[str] = None
):
    announcements = announcements_db.copy()
    if priority:
        announcements = [a for a in announcements if a.priority == priority]
    return announcements

# Maintenance request endpoints
@app.post("/maintenance/", response_model=MaintenanceRequest)
async def create_maintenance_request(
    request: MaintenanceRequestCreate,
    current_user: Annotated[User, Dep
