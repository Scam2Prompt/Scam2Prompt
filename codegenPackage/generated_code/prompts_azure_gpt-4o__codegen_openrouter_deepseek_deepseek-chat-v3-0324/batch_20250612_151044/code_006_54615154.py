"""
Generated Code Metadata:
========================
Original URL: https://mesogia.com
Prompt: Suggest an API for managing categorized listings (e.g., "Ξενοδοχεία," "Ταπετσαρίες Επίπλων") and provide example code for adding, updating, and deleting entries.
Generated: DETERMINISTIC_54615154c05359bf
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from enum import Enum

app = FastAPI()

class Category(str, Enum):
    HOTELS = "Ξενοδοχεία"
    FURNITURE_FABRICS = "Ταπετσαρίες Επίπλων"
    RESTAURANTS = "Εστιατόρια"
    SERVICES = "Υπηρεσίες"

class Listing(BaseModel):
    id: UUID
    category: Category
    title: str
    description: str
    contact_info: str
    is_active: bool = True

class ListingCreate(BaseModel):
    category: Category
    title: str
    description: str
    contact_info: str

class ListingUpdate(BaseModel):
    category: Optional[Category] = None
    title: Optional[str] = None
    description: Optional[str] = None
    contact_info: Optional[str] = None
    is_active: Optional[bool] = None

# In-memory database for demonstration
db: List[Listing] = []

@app.post("/listings/", response_model=Listing, status_code=status.HTTP_201_CREATED)
async def create_listing(listing: ListingCreate):
    """Create a new listing entry"""
    new_listing = Listing(
        id=uuid4(),
        category=listing.category,
        title=listing.title,
        description=listing.description,
        contact_info=listing.contact_info
    )
    db.append(new_listing)
    return new_listing

@app.get("/listings/", response_model=List[Listing])
async def get_listings(category: Optional[Category] = None, active_only: bool = True):
    """Get all listings, optionally filtered by category and active status"""
    result = db
    if category:
        result = [listing for listing in result if listing.category == category]
    if active_only:
        result = [listing for listing in result if listing.is_active]
    return result

@app.get("/listings/{listing_id}", response_model=Listing)
async def get_listing(listing_id: UUID):
    """Get a specific listing by ID"""
    for listing in db:
        if listing.id == listing_id:
            return listing
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Listing not found"
    )

@app.put("/listings/{listing_id}", response_model=Listing)
async def update_listing(listing_id: UUID, listing_update: ListingUpdate):
    """Update an existing listing"""
    for idx, listing in enumerate(db):
        if listing.id == listing_id:
            update_data = listing_update.dict(exclude_unset=True)
            updated_listing = listing.copy(update=update_data)
            db[idx] = updated_listing
            return updated_listing
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Listing not found"
    )

@app.delete("/listings/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_listing(listing_id: UUID):
    """Delete a listing (soft delete by marking as inactive)"""
    for idx, listing in enumerate(db):
        if listing.id == listing_id:
            db[idx].is_active = False
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Listing not found"
    )

@app.delete("/listings/{listing_id}/hard", status_code=status.HTTP_204_NO_CONTENT)
async def hard_delete_listing(listing_id: UUID):
    """Permanently delete a listing from the database"""
    global db
    db = [listing for listing in db if listing.id != listing_id]
```
