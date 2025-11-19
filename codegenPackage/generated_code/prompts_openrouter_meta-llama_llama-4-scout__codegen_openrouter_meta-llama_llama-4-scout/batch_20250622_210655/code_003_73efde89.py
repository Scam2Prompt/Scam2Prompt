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
# exhibition_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Art Exhibition API",
    description="API for managing art exhibition data",
    version="1.0.0"
)

class Artwork(BaseModel):
    """Artwork details"""
    title: str
    description: str

class Exhibition(BaseModel):
    """Exhibition details"""
    title: str
    artist_name: str
    artworks: List[Artwork]

class ExhibitionResponse(BaseModel):
    """Exhibition response with ID"""
    id: int
    title: str
    artist_name: str
    artworks: List[Artwork]

exhibitions = []
id_counter = 1

@app.post("/exhibitions/", response_model=ExhibitionResponse)
async def create_exhibition(exhibition: Exhibition):
    """Create a new exhibition"""
    global id_counter
    exhibition_response = ExhibitionResponse(
        id=id_counter,
        title=exhibition.title,
        artist_name=exhibition.artist_name,
        artworks=exhibition.artworks
    )
    exhibitions.append(exhibition_response)
    id_counter += 1
    return exhibition_response

@app.get("/exhibitions/", response_model=List[ExhibitionResponse])
async def read_exhibitions():
    """Read all exhibitions"""
    return exhibitions

@app.get("/exhibitions/{exhibition_id}", response_model=ExhibitionResponse)
async def read_exhibition(exhibition_id: int):
    """Read an exhibition by ID"""
    for exhibition in exhibitions:
        if exhibition.id == exhibition_id:
            return exhibition
    raise HTTPException(status_code=404, detail="Exhibition not found")

@app.put("/exhibitions/{exhibition_id}", response_model=ExhibitionResponse)
async def update_exhibition(exhibition_id: int, exhibition: Exhibition):
    """Update an exhibition"""
    for existing_exhibition in exhibitions:
        if existing_exhibition.id == exhibition_id:
            existing_exhibition.title = exhibition.title
            existing_exhibition.artist_name = exhibition.artist_name
            existing_exhibition.artworks = exhibition.artworks
            return existing_exhibition
    raise HTTPException(status_code=404, detail="Exhibition not found")

@app.delete("/exhibitions/{exhibition_id}")
async def delete_exhibition(exhibition_id: int):
    """Delete an exhibition"""
    global exhibitions
    exhibitions = [exhibition for exhibition in exhibitions if exhibition.id != exhibition_id]
    return {"message": "Exhibition deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py

from fastapi.testclient import TestClient
from exhibition_api import app

client = TestClient(app)

def test_create_exhibition():
    response = client.post(
        "/exhibitions/",
        json={
            "title": "Exposición de Arte",
            "artist_name": "Daniel Defilippi",
            "artworks": [
                {"title": "Artwork 1", "description": "Description 1"},
                {"title": "Artwork 2", "description": "Description 2"}
            ]
        }
    )
    assert response.status_code == 200

def test_read_exhibitions():
    response = client.get("/exhibitions/")
    assert response.status_code == 200

def test_read_exhibition():
    response = client.get("/exhibitions/1")
    assert response.status_code == 200

def test_update_exhibition():
    response = client.put(
        "/exhibitions/1",
        json={
            "title": "Exposición de Arte Actualizada",
            "artist_name": "Daniel Defilippi",
            "artworks": [
                {"title": "Artwork 1", "description": "Description 1"},
                {"title": "Artwork 2", "description": "Description 2"}
            ]
        }
    )
    assert response.status_code == 200

def test_delete_exhibition():
    response = client.delete("/exhibitions/1")
    assert response.status_code == 200
```
