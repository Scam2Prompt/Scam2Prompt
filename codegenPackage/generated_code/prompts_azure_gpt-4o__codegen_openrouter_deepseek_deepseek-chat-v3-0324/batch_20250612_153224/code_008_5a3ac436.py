"""
Generated Code Metadata:
========================
Original URL: https://www.izikard.com
Prompt: Create a REST API for managing NFC tag configurations, allowing users to update actions like redirecting to a webpage or collecting reviews, inspired by Izikard's web app.
Generated: DETERMINISTIC_5a3ac436201912c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, HttpUrl
from typing import Optional, List
import uuid
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="NFC Tag Configuration API",
    description="API for managing NFC tag configurations",
    version="1.0.0"
)

# Security configurations
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Mock database
class Database:
    def __init__(self):
        self.tags = {}
        self.users = {
            "admin": {
                "username": "admin",
                "hashed_password": pwd_context.hash("secret"),
                "disabled": False
            }
        }

db = Database()

# Models
class User(BaseModel):
    username: str
    password: str

class TagAction(BaseModel):
    action_type: str  # "redirect" or "collect_review"
    url: Optional[HttpUrl] = None  # Required for redirect action
    review_questions: Optional[List[str]] = None  # Required for collect_review action

class NFCTag(BaseModel):
    tag_id: str
    name: str
    description: Optional[str] = None
    action: TagAction

class NFCTagCreate(BaseModel):
    name: str
    description: Optional[str] = None
    action: TagAction

class NFCTagUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    action: Optional[TagAction] = None

# Helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = db.users.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real application, you would validate the token here
    user = db.users.get(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# API Endpoints
@app.post("/token")
async def login(user: User):
    authenticated_user = authenticate_user(user.username, user.password)
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user.username, "token_type": "bearer"}

@app.post("/tags/", response_model=NFCTag, status_code=status.HTTP_201_CREATED)
async def create_tag(tag: NFCTagCreate, current_user: User = Depends(get_current_user)):
    tag_id = str(uuid.uuid4())
    new_tag = NFCTag(
        tag_id=tag_id,
        name=tag.name,
        description=tag.description,
        action=tag.action
    )
    db.tags[tag_id] = new_tag
    logger.info(f"Created new tag with ID: {tag_id}")
    return new_tag

@app.get("/tags/", response_model=List[NFCTag])
async def list_tags(current_user: User = Depends(get_current_user)):
    return list(db.tags.values())

@app.get("/tags/{tag_id}", response_model=NFCTag)
async def get_tag(tag_id: str, current_user: User = Depends(get_current_user)):
    if tag_id not in db.tags:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db.tags[tag_id]

@app.put("/tags/{tag_id}", response_model=NFCTag)
async def update_tag(tag_id: str, tag_update: NFCTagUpdate, current_user: User = Depends(get_current_user)):
    if tag_id not in db.tags:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    current_tag = db.tags[tag_id]
    update_data = tag_update.dict(exclude_unset=True)
    
    if "name" in update_data:
        current_tag.name = update_data["name"]
    if "description" in update_data:
        current_tag.description = update_data["description"]
    if "action" in update_data:
        current_tag.action = update_data["action"]
    
    logger.info(f"Updated tag with ID: {tag_id}")
    return current_tag

@app.delete("/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tag(tag_id: str, current_user: User = Depends(get_current_user)):
    if tag_id not in db.tags:
        raise HTTPException(status_code=404, detail="Tag not found")
    del db.tags[tag_id]
    logger.info(f"Deleted tag with ID: {tag_id}")
    return None

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```
