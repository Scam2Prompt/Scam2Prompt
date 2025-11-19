"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Outline a REST API design for managing user applications and NFT assets in the MetaLeagues platform.
Generated: DETERMINISTIC_51ff134089735bca
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="MetaLeagues API",
    description="REST API for managing user applications and NFT assets in MetaLeagues",
    version="1.0.0"
)

# Database models (in-memory for this example)
users_db = {}
nfts_db = {}
applications_db = {}

# Pydantic models for request/response validation
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

class NFTBase(BaseModel):
    name: str
    description: str
    image_url: str

class NFTCreate(NFTBase):
    owner_id: UUID

class NFT(NFTBase):
    id: UUID
    owner: User
    created_at: datetime
    token_id: str

    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    user_id: UUID
    nft_id: UUID
    message: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: UUID
    status: str = "pending"  # pending, approved, rejected
    created_at: datetime
    processed_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# Helper functions
def get_user(user_id: UUID):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

def get_nft(nft_id: UUID):
    if nft_id not in nfts_db:
        raise HTTPException(status_code=404, detail="NFT not found")
    return nfts_db[nft_id]

def get_application(application_id: UUID):
    if application_id not in applications_db:
        raise HTTPException(status_code=404, detail="Application not found")
    return applications_db[application_id]

# User endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    user_id = uuid4()
    db_user = User(
        id=user_id,
        username=user.username,
        email=user.email,
        created_at=datetime.utcnow()
    )
    users_db[user_id] = db_user
    return db_user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: UUID):
    return get_user(user_id)

# NFT endpoints
@app.post("/nfts/", response_model=NFT, status_code=status.HTTP_201_CREATED)
def create_nft(nft: NFTCreate):
    owner = get_user(nft.owner_id)
    nft_id = uuid4()
    db_nft = NFT(
        id=nft_id,
        name=nft.name,
        description=nft.description,
        image_url=nft.image_url,
        owner=owner,
        created_at=datetime.utcnow(),
        token_id=f"ML-{nft_id}"
    )
    nfts_db[nft_id] = db_nft
    return db_nft

@app.get("/nfts/{nft_id}", response_model=NFT)
def read_nft(nft_id: UUID):
    return get_nft(nft_id)

@app.get("/users/{user_id}/nfts", response_model=List[NFT])
def get_user_nfts(user_id: UUID):
    user = get_user(user_id)
    return [nft for nft in nfts_db.values() if nft.owner.id == user_id]

# Application endpoints
@app.post("/applications/", response_model=Application, status_code=status.HTTP_201_CREATED)
def create_application(application: ApplicationCreate):
    get_user(application.user_id)  # Validate user exists
    get_nft(application.nft_id)    # Validate NFT exists
    
    application_id = uuid4()
    db_application = Application(
        id=application_id,
        user_id=application.user_id,
        nft_id=application.nft_id,
        message=application.message,
        created_at=datetime.utcnow()
    )
    applications_db[application_id] = db_application
    return db_application

@app.get("/applications/{application_id}", response_model=Application)
def read_application(application_id: UUID):
    return get_application(application_id)

@app.patch("/applications/{application_id}", response_model=Application)
def update_application_status(application_id: UUID, status: str):
    if status not in ["pending", "approved", "rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    
    application = get_application(application_id)
    application.status = status
    application.processed_at = datetime.utcnow()
    return application

@app.get("/users/{user_id}/applications", response_model=List[Application])
def get_user_applications(user_id: UUID):
    get_user(user_id)  # Validate user exists
    return [app for app in applications_db.values() if app.user_id == user_id]

@app.get("/nfts/{nft_id}/applications", response_model=List[Application])
def get_nft_applications(nft_id: UUID):
    get_nft(nft_id)  # Validate NFT exists
    return [app for app in applications_db.values() if app.nft_id == nft_id]
```
