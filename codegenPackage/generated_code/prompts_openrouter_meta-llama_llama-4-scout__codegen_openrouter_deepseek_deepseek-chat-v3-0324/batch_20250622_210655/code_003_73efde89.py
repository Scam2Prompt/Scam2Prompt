"""
Generated Code Metadata:
========================
Original URL: https://danieldefilippi.com
Prompt: Design an API for managing art exhibition data, including fields for artist name, exhibition title, and artwork descriptions, inspired by Daniel Defilippi's exposiciones.
Generated: DETERMINISTIC_73efde8977152714
Batch ID: 20250622_210655
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
from datetime import datetime

app = FastAPI(
    title="Art Exhibition API",
    description="API for managing art exhibition data inspired by Daniel Defilippi's exposiciones",
    version="1.0.0"
)

# Database mock (in production, replace with a real database)
exhibitions_db = []

class Artwork(BaseModel):
    """Represents an individual artwork in an exhibition"""
    id: UUID
    title: str
    description: str
    creation_year: Optional[int] = None
    medium: Optional[str] = None

class Exhibition(BaseModel):
    """Represents an art exhibition"""
    id: UUID
    artist_name: str
    exhibition_title: str
    artworks: List[Artwork]
    start_date: datetime
    end_date: datetime
    location: str
    description: Optional[str] = None

class ExhibitionCreate(BaseModel):
    """Model for creating a new exhibition"""
    artist_name: str
    exhibition_title: str
    artworks: List[dict]  # Simplified for creation
    start_date: datetime
    end_date: datetime
    location: str
    description: Optional[str] = None

class ExhibitionUpdate(BaseModel):
    """Model for updating an existing exhibition"""
    artist_name: Optional[str] = None
    exhibition_title: Optional[str] = None
    artworks: Optional[List[dict]] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    location: Optional[str] = None
    description: Optional[str] = None

@app.post("/exhibitions/", response_model=Exhibition, status_code=status.HTTP_201_CREATED)
async def create_exhibition(exhibition: ExhibitionCreate):
    """Create a new art exhibition"""
    try:
        # Convert artwork dicts to Artwork objects
        artworks = [
            Artwork(
                id=uuid4(),
                title=artwork.get("title"),
                description=artwork.get("description"),
                creation_year=artwork.get("creation_year"),
                medium=artwork.get("medium")
            ) for artwork in exhibition.artworks
        ]
        
        new_exhibition = Exhibition(
            id=uuid4(),
            artist_name=exhibition.artist_name,
            exhibition_title=exhibition.exhibition_title,
            artworks=artworks,
            start_date=exhibition.start_date,
            end_date=exhibition.end_date,
            location=exhibition.location,
            description=exhibition.description
        )
        
        exhibitions_db.append(new_exhibition)
        return new_exhibition
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating exhibition: {str(e)}"
        )

@app.get("/exhibitions/", response_model=List[Exhibition])
async def get_all_exhibitions():
    """Get all art exhibitions"""
    return exhibitions_db

@app.get("/exhibitions/{exhibition_id}", response_model=Exhibition)
async def get_exhibition(exhibition_id: UUID):
    """Get a specific exhibition by ID"""
    for exhibition in exhibitions_db:
        if exhibition.id == exhibition_id:
            return exhibition
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Exhibition not found"
    )

@app.put("/exhibitions/{exhibition_id}", response_model=Exhibition)
async def update_exhibition(exhibition_id: UUID, updated_data: ExhibitionUpdate):
    """Update an existing exhibition"""
    for index, exhibition in enumerate(exhibitions_db):
        if exhibition.id == exhibition_id:
            # Update fields if they are provided
            update_data = updated_data.dict(exclude_unset=True)
            
            if "artworks" in update_data:
                # Handle artwork updates
                artworks = [
                    Artwork(
                        id=uuid4(),
                        title=artwork.get("title"),
                        description=artwork.get("description"),
                        creation_year=artwork.get("creation_year"),
                        medium=artwork.get("medium")
                    ) for artwork in update_data["artworks"]
                ]
                update_data["artworks"] = artworks
            
            updated_exhibition = exhibition.copy(update=update_data)
            exhibitions_db[index] = updated_exhibition
            return updated_exhibition
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Exhibition not found"
    )

@app.delete("/exhibitions/{exhibition_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exhibition(exhibition_id: UUID):
    """Delete an exhibition"""
    for index, exhibition in enumerate(exhibitions_db):
        if exhibition.id == exhibition_id:
            exhibitions_db.pop(index)
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Exhibition not found"
    )

@app.get("/exhibitions/artist/{artist_name}", response_model=List[Exhibition])
async def get_exhibitions_by_artist(artist_name: str):
    """Get exhibitions by artist name"""
    return [ex for ex in exhibitions_db if ex.artist_name.lower() == artist_name.lower()]
```
