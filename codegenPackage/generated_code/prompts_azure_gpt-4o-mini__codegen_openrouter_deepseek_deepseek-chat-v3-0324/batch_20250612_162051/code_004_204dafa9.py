"""
Generated Code Metadata:
========================
Original URL: https://consultorialicitare.com.br
Prompt: Create a REST API that facilitates communication between different public sector departments, leveraging Licitare's solutions in T.I and system development.
Generated: DETERMINISTIC_204dafa95adb8881
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
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import List, Optional
import uuid
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Public Sector Department Communication API",
    description="API to facilitate communication between public sector departments using Licitare's solutions",
    version="1.0.0",
    contact={
        "name": "Licitare Solutions",
        "email": "support@licitare.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Mock database
db = {
    "departments": {},
    "messages": {},
    "users": {
        "admin": {
            "username": "admin",
            "password": "secret",
            "department": "central",
            "disabled": False
        }
    }
}

# Models
class Department(BaseModel):
    id: str
    name: str
    description: str
    contact_email: str
    created_at: datetime

class Message(BaseModel):
    id: str
    sender_department: str
    receiver_department: str
    subject: str
    content: str
    created_at: datetime
    is_read: bool = False

class User(BaseModel):
    username: str
    password: str
    department: str
    disabled: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class MessageCreate(BaseModel):
    receiver_department: str
    subject: str
    content: str

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Helper functions
def get_department(department_id: str):
    if department_id not in db["departments"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department not found"
        )
    return db["departments"][department_id]

def get_user(username: str):
    if username not in db["users"]:
        return None
    user_dict = db["users"][username]
    return User(**user_dict)

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or user.password != password:
        return False
    return user

def create_access_token(data: dict):
    # In a real application, use proper JWT token generation
    return {"access_token": str(uuid.uuid4()), "token_type": "bearer"}

# API Endpoints
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordBearer = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/departments/", response_model=Department, status_code=status.HTTP_201_CREATED)
async def create_department(name: str, description: str, contact_email: str):
    department_id = str(uuid.uuid4())
    new_department = Department(
        id=department_id,
        name=name,
        description=description,
        contact_email=contact_email,
        created_at=datetime.now()
    )
    db["departments"][department_id] = new_department.dict()
    logger.info(f"Created new department: {department_id}")
    return new_department

@app.get("/departments/", response_model=List[Department])
async def list_departments():
    return list(db["departments"].values())

@app.get("/departments/{department_id}", response_model=Department)
async def get_department_by_id(department_id: str):
    return get_department(department_id)

@app.post("/messages/", response_model=Message, status_code=status.HTTP_201_CREATED)
async def send_message(
    message: MessageCreate,
    current_user: User = Depends(get_user)
):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled"
        )
    
    sender_department = current_user.department
    receiver_department = message.receiver_department
    
    if receiver_department not in db["departments"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receiver department not found"
        )
    
    message_id = str(uuid.uuid4())
    new_message = Message(
        id=message_id,
        sender_department=sender_department,
        receiver_department=receiver_department,
        subject=message.subject,
        content=message.content,
        created_at=datetime.now()
    )
    
    db["messages"][message_id] = new_message.dict()
    logger.info(f"New message sent from {sender_department} to {receiver_department}")
    return new_message

@app.get("/messages/inbox", response_model=List[Message])
async def get_inbox(current_user: User = Depends(get_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled"
        )
    
    department = current_user.department
    inbox = [
        Message(**msg) for msg in db["messages"].values() 
        if msg["receiver_department"] == department
    ]
    return inbox

@app.get("/messages/sent", response_model=List[Message])
async def get_sent_messages(current_user: User = Depends(get_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled"
        )
    
    department = current_user.department
    sent = [
        Message(**msg) for msg in db["messages"].values() 
        if msg["sender_department"] == department
    ]
    return sent

@app.patch("/messages/{message_id}/read", response_model=Message)
async def mark_message_as_read(message_id: str, current_user: User = Depends(get_user)):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled"
        )
    
    if message_id not in db["messages"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Message not found"
        )
    
    message = db["messages"][message_id]
    if message["receiver_department"] != current_user.department:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to mark this message as read"
        )
    
    message["is_read"] = True
    db["messages"][message_id] = message
    return Message(**message)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}
```
