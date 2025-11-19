"""
Generated Code Metadata:
========================
Original URL: https://treehousesessions.co.uk
Prompt: Suggest an API for managing artist profiles and performances similar to those described on the "Tree House Sessions" webpage, and demonstrate its usage with example code.
Generated: DETERMINISTIC_d9364d5416eb6b29
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Artist Profile and Performance Management API
Inspired by "Tree House Sessions" style artist profiles and performances.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
from datetime import datetime

app = FastAPI(
    title="Artist Performance API",
    description="API for managing artist profiles and performances",
    version="1.0.0"
)

# In-memory database for demonstration
artists_db = {}
performances_db = {}

class Artist(BaseModel):
    id: UUID
    name: str
    bio: str
    genre: str
    image_url: Optional[str] = None
    social_links: Optional[dict] = None

class Performance(BaseModel):
    id: UUID
    artist_id: UUID
    title: str
    description: str
    date: datetime
    video_url: str
    duration_seconds: int
    is_featured: bool = False

class ArtistCreate(BaseModel):
    name: str
    bio: str
    genre: str
    image_url: Optional[str] = None
    social_links: Optional[dict] = None

class PerformanceCreate(BaseModel):
    artist_id: UUID
    title: str
    description: str
    date: datetime
    video_url: str
    duration_seconds: int
    is_featured: bool = False

@app.post("/artists/", response_model=Artist, status_code=status.HTTP_201_CREATED)
def create_artist(artist: ArtistCreate):
    """Create a new artist profile"""
    artist_id = uuid4()
    new_artist = Artist(
        id=artist_id,
        **artist.dict()
    )
    artists_db[artist_id] = new_artist
    return new_artist

@app.get("/artists/", response_model=List[Artist])
def list_artists():
    """List all artists"""
    return list(artists_db.values())

@app.get("/artists/{artist_id}", response_model=Artist)
def get_artist(artist_id: UUID):
    """Get artist by ID"""
    if artist_id not in artists_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artist not found"
        )
    return artists_db[artist_id]

@app.post("/performances/", response_model=Performance, status_code=status.HTTP_201_CREATED)
def create_performance(performance: PerformanceCreate):
    """Create a new performance"""
    if performance.artist_id not in artists_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Artist does not exist"
        )
    
    performance_id = uuid4()
    new_performance = Performance(
        id=performance_id,
        **performance.dict()
    )
    performances_db[performance_id] = new_performance
    return new_performance

@app.get("/performances/", response_model=List[Performance])
def list_performances(featured: bool = None):
    """List all performances, optionally filtered by featured status"""
    performances = list(performances_db.values())
    if featured is not None:
        performances = [p for p in performances if p.is_featured == featured]
    return performances

@app.get("/performances/{performance_id}", response_model=Performance)
def get_performance(performance_id: UUID):
    """Get performance by ID"""
    if performance_id not in performances_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Performance not found"
        )
    return performances_db[performance_id]

@app.get("/artists/{artist_id}/performances", response_model=List[Performance])
def get_artist_performances(artist_id: UUID):
    """Get all performances by a specific artist"""
    if artist_id not in artists_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Artist not found"
        )
    return [p for p in performances_db.values() if p.artist_id == artist_id]

@app.put("/performances/{performance_id}/feature", response_model=Performance)
def toggle_featured_status(performance_id: UUID):
    """Toggle the featured status of a performance"""
    if performance_id not in performances_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Performance not found"
        )
    
    performance = performances_db[performance_id]
    performance.is_featured = not performance.is_featured
    return performance

# Example usage
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
