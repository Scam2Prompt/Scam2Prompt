"""
Generated Code Metadata:
========================
Original URL: https://hieroglyphics.com
Prompt: Generate a RESTful API for managing NFTs on the HIERO marketplace, including endpoints for minting, listing, and transferring unique digital assets.
Generated: DETERMINISTIC_5710b2fd01851bdc
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="HIERO NFT Marketplace API", version="0.1.0")

# Database mock (in production, replace with a real database)
class Database:
    def __init__(self):
        self.nfts = []
        self.users = []

db = Database()

# Models
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    email: str
    wallet_address: str

class NFTMetadata(BaseModel):
    name: str
    description: str
    image_url: str
    external_url: Optional[str] = None
    attributes: Optional[List[dict]] = None

class NFT(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    token_id: str
    owner_id: UUID
    creator_id: UUID
    metadata: NFTMetadata
    price: Optional[float] = None
    listed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class NFTCreate(BaseModel):
    token_id: str
    creator_id: UUID
    metadata: NFTMetadata
    price: Optional[float] = None

class NFTUpdate(BaseModel):
    price: Optional[float] = None
    listed: Optional[bool] = None

class NFTTransfer(BaseModel):
    new_owner_id: UUID

# Helper functions
def get_nft(nft_id: UUID) -> Optional[NFT]:
    for nft in db.nfts:
        if nft.id == nft_id:
            return nft
    return None

def get_user(user_id: UUID) -> Optional[User]:
    for user in db.users:
        if user.id == user_id:
            return user
    return None

# API Endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    """Create a new user."""
    db.users.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: UUID):
    """Get user details by ID."""
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/nfts/", response_model=NFT, status_code=status.HTTP_201_CREATED)
async def mint_nft(nft_data: NFTCreate):
    """Mint a new NFT."""
    creator = get_user(nft_data.creator_id)
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    
    nft = NFT(
        token_id=nft_data.token_id,
        owner_id=nft_data.creator_id,
        creator_id=nft_data.creator_id,
        metadata=nft_data.metadata,
        price=nft_data.price
    )
    
    db.nfts.append(nft)
    return nft

@app.get("/nfts/", response_model=List[NFT])
async def list_nfts(listed: Optional[bool] = None):
    """List all NFTs, optionally filtered by listing status."""
    if listed is not None:
        return [nft for nft in db.nfts if nft.listed == listed]
    return db.nfts

@app.get("/nfts/{nft_id}", response_model=NFT)
async def read_nft(nft_id: UUID):
    """Get NFT details by ID."""
    nft = get_nft(nft_id)
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found")
    return nft

@app.put("/nfts/{nft_id}", response_model=NFT)
async def update_nft(nft_id: UUID, nft_update: NFTUpdate):
    """Update NFT details (price, listing status)."""
    nft = get_nft(nft_id)
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found")
    
    if nft_update.price is not None:
        nft.price = nft_update.price
    if nft_update.listed is not None:
        nft.listed = nft_update.listed
    
    nft.updated_at = datetime.now()
    return nft

@app.post("/nfts/{nft_id}/transfer", response_model=NFT)
async def transfer_nft(nft_id: UUID, transfer_data: NFTTransfer):
    """Transfer ownership of an NFT."""
    nft = get_nft(nft_id)
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found")
    
    new_owner = get_user(transfer_data.new_owner_id)
    if not new_owner:
        raise HTTPException(status_code=404, detail="New owner not found")
    
    nft.owner_id = transfer_data.new_owner_id
    nft.updated_at = datetime.now()
    return nft

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
