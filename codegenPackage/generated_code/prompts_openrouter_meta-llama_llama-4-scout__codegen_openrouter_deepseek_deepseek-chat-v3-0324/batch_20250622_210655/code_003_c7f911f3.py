"""
Generated Code Metadata:
========================
Original URL: https://www.autocuyo.com.ar
Prompt: Design a RESTful API for managing car classified ads, with endpoints for creating, reading, updating, and deleting listings, using Autocuyo as a reference.
Generated: DETERMINISTIC_c7f911f3cb8a8ee1
Batch ID: 20250622_210655
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
from datetime import datetime
from uuid import uuid4
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# Security setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database mock
class Database:
    def __init__(self):
        self.listings = []
    
    def get_listing(self, listing_id: str):
        for listing in self.listings:
            if listing["id"] == listing_id:
                return listing
        return None
    
    def create_listing(self, listing_data: dict):
        listing_data["id"] = str(uuid4())
        listing_data["created_at"] = datetime.now().isoformat()
        listing_data["updated_at"] = datetime.now().isoformat()
        self.listings.append(listing_data)
        return listing_data
    
    def update_listing(self, listing_id: str, listing_data: dict):
        for listing in self.listings:
            if listing["id"] == listing_id:
                listing.update(listing_data)
                listing["updated_at"] = datetime.now().isoformat()
                return listing
        return None
    
    def delete_listing(self, listing_id: str):
        for i, listing in enumerate(self.listings):
            if listing["id"] == listing_id:
                return self.listings.pop(i)
        return None
    
    def get_all_listings(self):
        return self.listings

db = Database()

# Models
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class ListingBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    make: str = Field(..., min_length=2, max_length=50)
    model: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., gt=1900, lt=2100)
    mileage: int = Field(..., ge=0)
    color: Optional[str] = Field(None, max_length=30)
    condition: str = Field(..., regex="^(new|used|certified)$")

class ListingCreate(ListingBase):
    pass

class Listing(ListingBase):
    id: str
    created_at: str
    updated_at: str
    owner: User

    class Config:
        schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "title": "2019 Toyota Corolla",
                "description": "Excellent condition, low mileage",
                "price": 18500.00,
                "make": "Toyota",
                "model": "Corolla",
                "year": 2019,
                "mileage": 25000,
                "color": "Silver",
                "condition": "used",
                "created_at": "2023-01-01T12:00:00",
                "updated_at": "2023-01-01T12:00:00",
                "owner": {
                    "username": "johndoe",
                    "email": "john@example.com",
                    "full_name": "John Doe"
                }
            }
        }

# Auth functions (mock)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real app, you would validate the token here
    return User(username="testuser", email="user@example.com", full_name="Test User")

# API endpoints
@app.post("/listings/", response_model=Listing, status_code=status.HTTP_201_CREATED)
async def create_listing(listing: ListingCreate, current_user: User = Depends(get_current_user)):
    """
    Create a new car listing.
    """
    listing_data = listing.dict()
    listing_data["owner"] = current_user
    created_listing = db.create_listing(listing_data)
    return created_listing

@app.get("/listings/", response_model=List[Listing])
async def read_listings(skip: int = 0, limit: int = 10):
    """
    Retrieve all car listings with pagination.
    """
    return db.get_all_listings()[skip : skip + limit]

@app.get("/listings/{listing_id}", response_model=Listing)
async def read_listing(listing_id: str):
    """
    Retrieve a specific car listing by ID.
    """
    listing = db.get_listing(listing_id)
    if listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

@app.put("/listings/{listing_id}", response_model=Listing)
async def update_listing(listing_id: str, listing: ListingCreate, current_user: User = Depends(get_current_user)):
    """
    Update a car listing.
    """
    existing_listing = db.get_listing(listing_id)
    if existing_listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    if existing_listing["owner"]["username"] != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to update this listing")
    
    updated_listing = db.update_listing(listing_id, listing.dict())
    if updated_listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return updated_listing

@app.delete("/listings/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_listing(listing_id: str, current_user: User = Depends(get_current_user)):
    """
    Delete a car listing.
    """
    existing_listing = db.get_listing(listing_id)
    if existing_listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    if existing_listing["owner"]["username"] != current_user.username:
        raise HTTPException(status_code=403, detail="Not authorized to delete this listing")
    
    deleted = db.delete_listing(listing_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return None

@app.get("/listings/search/", response_model=List[Listing])
async def search_listings(
    make: Optional[str] = None,
    model: Optional[str] = None,
    min_year: Optional[int] = None,
    max_year: Optional[int] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    skip: int = 0,
    limit: int = 10
):
    """
    Search car listings with filters.
    """
    results = []
    for listing in db.get_all_listings():
        if make and listing["make"].lower() != make.lower():
            continue
        if model and listing["model"].lower() != model.lower():
            continue
        if min_year and listing["year"] < min_year:
            continue
        if max_year and listing["year"] > max_year:
            continue
        if min_price and listing["price"] < min_price:
            continue
        if max_price and listing["price"] > max_price:
            continue
        results.append(listing)
    
    return results[skip : skip + limit]
```
