"""
Generated Code Metadata:
========================
Original URL: https://44-cm7.pages.dev
Prompt: Design a RESTful API for managing collectible items, including features like claiming and selling, using the Pudgy Penguins "GoldFeathers" as an example.
Generated: DETERMINISTIC_2cf64fb2dea61ab7
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="Collectible Items API",
    description="A RESTful API for managing collectible items like Pudgy Penguins GoldFeathers",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
db = {
    "collectibles": [],
    "users": []
}

# Models
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    wallet_address: str
    balance: float = 0.0

class Collectible(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    image_url: str
    owner_id: Optional[UUID] = None
    price: Optional[float] = None
    is_listed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class CollectibleCreate(BaseModel):
    name: str
    description: str
    image_url: str

class CollectibleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    price: Optional[float] = None
    is_listed: Optional[bool] = None

class ClaimRequest(BaseModel):
    user_id: UUID

class SellRequest(BaseModel):
    user_id: UUID
    price: float

# Helper functions
def get_user(user_id: UUID):
    for user in db["users"]:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

def get_collectible(collectible_id: UUID):
    for collectible in db["collectibles"]:
        if collectible.id == collectible_id:
            return collectible
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Collectible not found"
    )

# User endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    db["users"].append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: UUID):
    return get_user(user_id)

# Collectible endpoints
@app.post("/collectibles/", response_model=Collectible, status_code=status.HTTP_201_CREATED)
def create_collectible(collectible: CollectibleCreate):
    new_collectible = Collectible(**collectible.dict())
    db["collectibles"].append(new_collectible)
    return new_collectible

@app.get("/collectibles/", response_model=List[Collectible])
def list_collectibles():
    return db["collectibles"]

@app.get("/collectibles/{collectible_id}", response_model=Collectible)
def read_collectible(collectible_id: UUID):
    return get_collectible(collectible_id)

@app.put("/collectibles/{collectible_id}", response_model=Collectible)
def update_collectible(collectible_id: UUID, collectible_update: CollectibleUpdate):
    collectible = get_collectible(collectible_id)
    update_data = collectible_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(collectible, field, value)
    
    collectible.updated_at = datetime.now()
    return collectible

# Claim/Sell endpoints
@app.post("/collectibles/{collectible_id}/claim", response_model=Collectible)
def claim_collectible(collectible_id: UUID, claim_request: ClaimRequest):
    collectible = get_collectible(collectible_id)
    user = get_user(claim_request.user_id)
    
    if collectible.owner_id is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Collectible already claimed"
        )
    
    collectible.owner_id = user.id
    collectible.updated_at = datetime.now()
    return collectible

@app.post("/collectibles/{collectible_id}/sell", response_model=Collectible)
def sell_collectible(collectible_id: UUID, sell_request: SellRequest):
    collectible = get_collectible(collectible_id)
    user = get_user(sell_request.user_id)
    
    if collectible.owner_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only the owner can sell this collectible"
        )
    
    if sell_request.price <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Price must be greater than 0"
        )
    
    collectible.price = sell_request.price
    collectible.is_listed = True
    collectible.updated_at = datetime.now()
    return collectible

@app.post("/collectibles/{collectible_id}/buy", response_model=Collectible)
def buy_collectible(collectible_id: UUID, user_id: UUID):
    collectible = get_collectible(collectible_id)
    buyer = get_user(user_id)
    seller = get_user(collectible.owner_id) if collectible.owner_id else None
    
    if not collectible.is_listed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Collectible is not listed for sale"
        )
    
    if buyer.id == collectible.owner_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You already own this collectible"
        )
    
    if buyer.balance < collectible.price:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient balance"
        )
    
    # Transfer funds
    buyer.balance -= collectible.price
    if seller:
        seller.balance += collectible.price
    
    # Transfer ownership
    collectible.owner_id = buyer.id
    collectible.is_listed = False
    collectible.price = None
    collectible.updated_at = datetime.now()
    
    return collectible
```
