"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: Develop an API endpoint that retrieves various entertainment options for events, inspired by the diverse services listed on Wonderplanet.ee, such as face painting and balloon modeling.
Generated: DETERMINISTIC_b8d70cb35d83b5ba
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

app = FastAPI(
    title="Entertainment Options API",
    description="API for retrieving various entertainment options for events",
    version="1.0.0"
)

class Category(str, Enum):
    face_painting = "Face Painting"
    balloon_modeling = "Balloon Modeling"
    magic_shows = "Magic Shows"
    live_music = "Live Music"
    clown_performances = "Clown Performances"
    photo_booth = "Photo Booth"
    games = "Games"
    workshops = "Workshops"

class EntertainmentOption(BaseModel):
    id: int
    name: str
    category: Category
    description: str
    price_range: str
    min_participants: Optional[int] = None
    max_participants: Optional[int] = None
    duration_minutes: int
    suitable_for_ages: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Fantasy Face Painting",
                "category": "Face Painting",
                "description": "Professional face painting for all ages with high-quality, hypoallergenic paints",
                "price_range": "50-100 EUR",
                "min_participants": 5,
                "max_participants": 30,
                "duration_minutes": 120,
                "suitable_for_ages": "3+"
            }
        }

# Mock database
entertainment_options_db = [
    {
        "id": 1,
        "name": "Fantasy Face Painting",
        "category": Category.face_painting,
        "description": "Professional face painting for all ages with high-quality, hypoallergenic paints",
        "price_range": "50-100 EUR",
        "min_participants": 5,
        "max_participants": 30,
        "duration_minutes": 120,
        "suitable_for_ages": "3+"
    },
    {
        "id": 2,
        "name": "Balloon Animal Workshop",
        "category": Category.balloon_modeling,
        "description": "Interactive workshop where participants learn to create balloon animals",
        "price_range": "80-150 EUR",
        "min_participants": 8,
        "max_participants": 20,
        "duration_minutes": 90,
        "suitable_for_ages": "6+"
    },
    {
        "id": 3,
        "name": "Magical Illusions Show",
        "category": Category.magic_shows,
        "description": "45-minute magic show with audience participation",
        "price_range": "200-300 EUR",
        "duration_minutes": 45,
        "suitable_for_ages": "All ages"
    }
]

@app.get("/options/", response_model=List[EntertainmentOption], summary="Get all entertainment options")
async def get_all_options():
    """Retrieve all available entertainment options"""
    return entertainment_options_db

@app.get("/options/{option_id}", response_model=EntertainmentOption, summary="Get a specific entertainment option")
async def get_option(option_id: int):
    """Retrieve a specific entertainment option by ID"""
    option = next((opt for opt in entertainment_options_db if opt["id"] == option_id), None)
    if not option:
        raise HTTPException(status_code=404, detail="Option not found")
    return option

@app.get("/options/category/{category}", response_model=List[EntertainmentOption], summary="Get options by category")
async def get_options_by_category(category: Category):
    """Retrieve entertainment options filtered by category"""
    options = [opt for opt in entertainment_options_db if opt["category"] == category]
    if not options:
        raise HTTPException(
            status_code=404,
            detail=f"No options found in category {category}"
        )
    return options

@app.get("/options/search/", response_model=List[EntertainmentOption], summary="Search options")
async def search_options(
    query: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    min_duration: Optional[int] = None,
    max_duration: Optional[int] = None
):
    """Search entertainment options with various filters"""
    results = entertainment_options_db
    
    if query:
        query = query.lower()
        results = [
            opt for opt in results
            if query in opt["name"].lower() or query in opt["description"].lower()
        ]
    
    if min_price or max_price:
        def parse_price(price_str):
            try:
                return int(price_str.split("-")[0].strip().split()[0])
            except:
                return 0
        
        results = [
            opt for opt in results
            if (not min_price or parse_price(opt["price_range"]) >= min_price) and
               (not max_price or parse_price(opt["price_range"]) <= max_price)
        ]
    
    if min_duration:
        results = [opt for opt in results if opt["duration_minutes"] >= min_duration]
    
    if max_duration:
        results = [opt for opt in results if opt["duration_minutes"] <= max_duration]
    
    if not results:
        raise HTTPException(
            status_code=404,
            detail="No options match the search criteria"
        )
    
    return results
```
