"""
Generated Code Metadata:
========================
Original URL: https://bayc.team
Prompt: Design a simple NFT marketplace API inspired by BAYC.
Generated: DETERMINISTIC_4056863fd585a305
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple NFT Marketplace API inspired by BAYC (Bored Ape Yacht Club)
This API provides endpoints for managing NFTs, users, and marketplace transactions.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4
from datetime import datetime

app = FastAPI(
    title="NFT Marketplace API",
    description="A simple NFT marketplace API inspired by BAYC",
    version="1.0.0"
)

# In-memory database (replace with proper database in production)
db = {
    "users": {},
    "nfts": {},
    "listings": {}
}

# Models
class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    username: str
    wallet_address: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class NFT(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    description: str
    image_url: str
    owner_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    traits: Optional[dict] = None

class Listing(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    nft_id: str
    seller_id: str
    price: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    sold_at: Optional[datetime] = None
    status: str = "active"  # active, sold, cancelled

class PurchaseRequest(BaseModel):
    buyer_id: str

# Helper functions
def get_user(user_id: str):
    user = db["users"].get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_nft(nft_id: str):
    nft = db["nfts"].get(nft_id)
    if not nft:
        raise HTTPException(status_code=404, detail="NFT not found")
    return nft

def get_listing(listing_id: str):
    listing = db["listings"].get(listing_id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

# User endpoints
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    if user.id in db["users"]:
        raise HTTPException(status_code=400, detail="User ID already exists")
    db["users"][user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: str):
    return get_user(user_id)

# NFT endpoints
@app.post("/nfts/", response_model=NFT, status_code=status.HTTP_201_CREATED)
def create_nft(nft: NFT):
    if nft.id in db["nfts"]:
        raise HTTPException(status_code=400, detail="NFT ID already exists")
    if nft.owner_id not in db["users"]:
        raise HTTPException(status_code=400, detail="Owner does not exist")
    db["nfts"][nft.id] = nft
    return nft

@app.get("/nfts/{nft_id}", response_model=NFT)
def read_nft(nft_id: str):
    return get_nft(nft_id)

@app.get("/nfts/", response_model=List[NFT])
def list_nfts(owner_id: Optional[str] = None):
    if owner_id:
        return [nft for nft in db["nfts"].values() if nft.owner_id == owner_id]
    return list(db["nfts"].values())

# Marketplace endpoints
@app.post("/listings/", response_model=Listing, status_code=status.HTTP_201_CREATED)
def create_listing(listing: Listing):
    if listing.id in db["listings"]:
        raise HTTPException(status_code=400, detail="Listing ID already exists")
    if listing.nft_id not in db["nfts"]:
        raise HTTPException(status_code=400, detail="NFT does not exist")
    if listing.seller_id not in db["users"]:
        raise HTTPException(status_code=400, detail="Seller does not exist")
    if db["nfts"][listing.nft_id].owner_id != listing.seller_id:
        raise HTTPException(status_code=400, detail="Seller does not own the NFT")
    db["listings"][listing.id] = listing
    return listing

@app.get("/listings/", response_model=List[Listing])
def list_listings(status_filter: Optional[str] = None):
    if status_filter:
        return [listing for listing in db["listings"].values() if listing.status == status_filter]
    return list(db["listings"].values())

@app.post("/listings/{listing_id}/purchase", response_model=Listing)
def purchase_nft(listing_id: str, purchase: PurchaseRequest):
    listing = get_listing(listing_id)
    if listing.status != "active":
        raise HTTPException(status_code=400, detail="Listing is not active")
    
    buyer = get_user(purchase.buyer_id)
    seller = get_user(listing.seller_id)
    nft = get_nft(listing.nft_id)
    
    # In a real implementation, you would handle the payment here
    # For simplicity, we just update the ownership
    
    nft.owner_id = buyer.id
    listing.status = "sold"
    listing.sold_at = datetime.utcnow()
    
    return listing

@app.post("/listings/{listing_id}/cancel", response_model=Listing)
def cancel_listing(listing_id: str):
    listing = get_listing(listing_id)
    if listing.status != "active":
        raise HTTPException(status_code=400, detail="Only active listings can be cancelled")
    listing.status = "cancelled"
    return listing
```
