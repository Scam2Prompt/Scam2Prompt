"""
Generated Code Metadata:
========================
Original URL: https://bda.mcupr.ac.th
Prompt: Create a REST API specification for managing the collection of Buddhist art pieces, including details on the sculptures and their significance as outlined on the BDA MCU site.
Generated: DETERMINISTIC_222390521f3a1e07
Batch ID: 20250612_162051
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

app = FastAPI(
    title="Buddhist Art Collection API",
    description="REST API for managing a collection of Buddhist art pieces with their details and significance",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@bdamcu.org"
    },
    license_info={
        "name": "MIT",
    },
)

# In-memory database for demonstration
db = []

class ArtPiece(BaseModel):
    id: UUID
    title: str
    artist: Optional[str] = None
    period: str
    origin: str
    material: str
    dimensions: str
    current_location: str
    description: str
    significance: str
    image_url: Optional[str] = None

class ArtPieceCreate(BaseModel):
    title: str
    artist: Optional[str] = None
    period: str
    origin: str
    material: str
    dimensions: str
    current_location: str
    description: str
    significance: str
    image_url: Optional[str] = None

class ArtPieceUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    period: Optional[str] = None
    origin: Optional[str] = None
    material: Optional[str] = None
    dimensions: Optional[str] = None
    current_location: Optional[str] = None
    description: Optional[str] = None
    significance: Optional[str] = None
    image_url: Optional[str] = None

@app.post("/art-pieces/", response_model=ArtPiece, status_code=status.HTTP_201_CREATED)
async def create_art_piece(art_piece: ArtPieceCreate):
    """
    Create a new Buddhist art piece in the collection.
    """
    new_art_piece = ArtPiece(
        id=uuid4(),
        **art_piece.dict()
    )
    db.append(new_art_piece)
    return new_art_piece

@app.get("/art-pieces/", response_model=List[ArtPiece])
async def get_all_art_pieces():
    """
    Retrieve all Buddhist art pieces in the collection.
    """
    return db

@app.get("/art-pieces/{art_piece_id}", response_model=ArtPiece)
async def get_art_piece(art_piece_id: UUID):
    """
    Retrieve a specific Buddhist art piece by its ID.
    """
    for art_piece in db:
        if art_piece.id == art_piece_id:
            return art_piece
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Art piece not found"
    )

@app.put("/art-pieces/{art_piece_id}", response_model=ArtPiece)
async def update_art_piece(art_piece_id: UUID, art_piece_update: ArtPieceUpdate):
    """
    Update details of a specific Buddhist art piece.
    """
    for index, art_piece in enumerate(db):
        if art_piece.id == art_piece_id:
            update_data = art_piece_update.dict(exclude_unset=True)
            updated_art_piece = art_piece.copy(update=update_data)
            db[index] = updated_art_piece
            return updated_art_piece
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Art piece not found"
    )

@app.delete("/art-pieces/{art_piece_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_art_piece(art_piece_id: UUID):
    """
    Delete a Buddhist art piece from the collection.
    """
    for index, art_piece in enumerate(db):
        if art_piece.id == art_piece_id:
            db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Art piece not found"
    )

@app.get("/art-pieces/search/", response_model=List[ArtPiece])
async def search_art_pieces(
    title: Optional[str] = None,
    period: Optional[str] = None,
    origin: Optional[str] = None
):
    """
    Search for Buddhist art pieces by title, period, or origin.
    """
    results = db
    if title:
        results = [art_piece for art_piece in results if title.lower() in art_piece.title.lower()]
    if period:
        results = [art_piece for art_piece in results if period.lower() in art_piece.period.lower()]
    if origin:
        results = [art_piece for art_piece in results if origin.lower() in art_piece.origin.lower()]
    return results
```
