"""
Generated Code Metadata:
========================
Original URL: https://kraken-ec.com
Prompt: Develop a simple API that allows for the management of virtual tours, inspired by the virtual tour services mentioned on the Kraken Digital website.
Generated: DETERMINISTIC_f7e8b2a34795ba12
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Virtual Tour Management API
This API allows for creating, reading, updating, and deleting virtual tours.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI(
    title="Virtual Tour Management API",
    description="API for managing virtual tours",
    version="1.0.0"
)

# In-memory database for demonstration
virtual_tours_db = []

class VirtualTour(BaseModel):
    """Model representing a virtual tour"""
    id: Optional[UUID] = None
    title: str
    description: str
    location: str
    is_published: bool = False
    tags: List[str] = []

class VirtualTourCreate(BaseModel):
    """Model for creating a virtual tour (without ID)"""
    title: str
    description: str
    location: str
    is_published: bool = False
    tags: List[str] = []

class VirtualTourUpdate(BaseModel):
    """Model for updating a virtual tour"""
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    is_published: Optional[bool] = None
    tags: Optional[List[str]] = None

@app.get("/tours", response_model=List[VirtualTour], tags=["Tours"])
def list_tours(published: bool = None):
    """List all virtual tours, optionally filtered by published status"""
    if published is not None:
        return [tour for tour in virtual_tours_db if tour.is_published == published]
    return virtual_tours_db

@app.post("/tours", response_model=VirtualTour, status_code=status.HTTP_201_CREATED, tags=["Tours"])
def create_tour(tour: VirtualTourCreate):
    """Create a new virtual tour"""
    db_tour = VirtualTour(**tour.dict(), id=uuid4())
    virtual_tours_db.append(db_tour)
    return db_tour

@app.get("/tours/{tour_id}", response_model=VirtualTour, tags=["Tours"])
def get_tour(tour_id: UUID):
    """Get a specific virtual tour by ID"""
    for tour in virtual_tours_db:
        if tour.id == tour_id:
            return tour
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tour not found"
    )

@app.put("/tours/{tour_id}", response_model=VirtualTour, tags=["Tours"])
def update_tour(tour_id: UUID, tour_update: VirtualTourUpdate):
    """Update an existing virtual tour"""
    for index, tour in enumerate(virtual_tours_db):
        if tour.id == tour_id:
            update_data = tour_update.dict(exclude_unset=True)
            updated_tour = tour.copy(update=update_data)
            virtual_tours_db[index] = updated_tour
            return updated_tour
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tour not found"
    )

@app.delete("/tours/{tour_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tours"])
def delete_tour(tour_id: UUID):
    """Delete a virtual tour"""
    for index, tour in enumerate(virtual_tours_db):
        if tour.id == tour_id:
            virtual_tours_db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tour not found"
    )

@app.get("/tours/search/", response_model=List[VirtualTour], tags=["Search"])
def search_tours(query: str):
    """Search tours by title, description, or tags"""
    results = []
    query_lower = query.lower()
    for tour in virtual_tours_db:
        if (query_lower in tour.title.lower() or 
            query_lower in tour.description.lower() or 
            any(query_lower in tag.lower() for tag in tour.tags)):
            results.append(tour)
    return results

@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
```
