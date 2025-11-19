"""
Generated Code Metadata:
========================
Original URL: https://openweb-3ua.pages.dev
Prompt: Design an API for interacting with a digital art repository, including endpoints for submitting artworks, retrieving collection data, and querying token ownership, based on the Opepen use case.
Generated: DETERMINISTIC_5be654bf94f7ff7a
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI(
    title="Digital Art Repository API",
    description="API for interacting with a digital art repository",
    version="1.0.0"
)

# Mock database
class ArtworkDB:
    def __init__(self):
        self.artworks = []
        self.collections = []
        self.ownership_records = []

db = ArtworkDB()

# Models
class Artwork(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    artist: str
    description: Optional[str] = None
    creation_date: datetime = Field(default_factory=datetime.now)
    image_url: str
    metadata: Optional[dict] = None

class Collection(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    artworks: List[UUID] = []
    created_at: datetime = Field(default_factory=datetime.now)

class OwnershipRecord(BaseModel):
    artwork_id: UUID
    owner_address: str
    token_id: str
    acquired_at: datetime = Field(default_factory=datetime.now)

# Endpoints
@app.post("/artworks/", status_code=status.HTTP_201_CREATED)
async def submit_artwork(artwork: Artwork):
    """Submit a new artwork to the repository."""
    db.artworks.append(artwork)
    return {"message": "Artwork submitted successfully", "artwork_id": artwork.id}

@app.get("/artworks/{artwork_id}", response_model=Artwork)
async def get_artwork(artwork_id: UUID):
    """Retrieve artwork details by ID."""
    artwork = next((a for a in db.artworks if a.id == artwork_id), None)
    if not artwork:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artwork not found"
        )
    return artwork

@app.post("/collections/", status_code=status.HTTP_201_CREATED)
async def create_collection(collection: Collection):
    """Create a new collection."""
    db.collections.append(collection)
    return {"message": "Collection created successfully", "collection_id": collection.id}

@app.get("/collections/{collection_id}", response_model=Collection)
async def get_collection(collection_id: UUID):
    """Retrieve collection details by ID."""
    collection = next((c for c in db.collections if c.id == collection_id), None)
    if not collection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collection not found"
        )
    return collection

@app.post("/collections/{collection_id}/add-artwork")
async def add_artwork_to_collection(collection_id: UUID, artwork_id: UUID):
    """Add an artwork to a collection."""
    collection = next((c for c in db.collections if c.id == collection_id), None)
    if not collection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collection not found"
        )
    
    artwork = next((a for a in db.artworks if a.id == artwork_id), None)
    if not artwork:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artwork not found"
        )
    
    if artwork_id in collection.artworks:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Artwork already in collection"
        )
    
    collection.artworks.append(artwork_id)
    return {"message": "Artwork added to collection successfully"}

@app.post("/ownership/", status_code=status.HTTP_201_CREATED)
async def record_ownership(record: OwnershipRecord):
    """Record ownership of an artwork token."""
    artwork = next((a for a in db.artworks if a.id == record.artwork_id), None)
    if not artwork:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artwork not found"
        )
    
    db.ownership_records.append(record)
    return {"message": "Ownership recorded successfully"}

@app.get("/ownership/{artwork_id}", response_model=List[OwnershipRecord])
async def get_ownership_history(artwork_id: UUID):
    """Get ownership history for an artwork."""
    records = [r for r in db.ownership_records if r.artwork_id == artwork_id]
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No ownership records found for this artwork"
        )
    return records

@app.get("/ownership/current/{artwork_id}", response_model=OwnershipRecord)
async def get_current_owner(artwork_id: UUID):
    """Get current owner of an artwork."""
    records = sorted(
        [r for r in db.ownership_records if r.artwork_id == artwork_id],
        key=lambda x: x.acquired_at,
        reverse=True
    )
    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No ownership records found for this artwork"
        )
    return records[0]
```
