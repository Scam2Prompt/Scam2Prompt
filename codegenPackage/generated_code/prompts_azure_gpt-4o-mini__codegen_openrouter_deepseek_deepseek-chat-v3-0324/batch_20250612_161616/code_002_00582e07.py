"""
Generated Code Metadata:
========================
Original URL: https://jualessandraensina.com
Prompt: Create an API endpoint that retrieves the latest makeup techniques and strategies for client attraction, inspired by the content offered in Ju Ensina's curriculum.
Generated: DETERMINISTIC_00582e07952feca6
Batch ID: 20250612_161616
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
from typing import List
import datetime

app = FastAPI(
    title="Makeup Techniques API",
    description="API for retrieving latest makeup techniques and strategies for client attraction",
    version="1.0.0"
)

class Technique(BaseModel):
    id: int
    title: str
    description: str
    category: str
    difficulty: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

# Mock database
techniques_db = [
    Technique(
        id=1,
        title="Contouring for Face Shape",
        description="Learn how to contour based on different face shapes to enhance features",
        category="Contouring",
        difficulty="Intermediate",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    ),
    Technique(
        id=2,
        title="Eyebrow Mapping",
        description="Precision technique for perfect eyebrow shaping that attracts attention",
        category="Eyebrows",
        difficulty="Beginner",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    ),
    Technique(
        id=3,
        title="Color Theory in Makeup",
        description="Using color theory to select shades that complement skin tones",
        category="Color Theory",
        difficulty="Advanced",
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )
]

@app.get("/techniques/", response_model=List[Technique])
async def get_all_techniques():
    """
    Retrieve all makeup techniques
    """
    return techniques_db

@app.get("/techniques/{technique_id}", response_model=Technique)
async def get_technique(technique_id: int):
    """
    Retrieve a specific makeup technique by ID
    """
    technique = next((t for t in techniques_db if t.id == technique_id), None)
    if technique is None:
        raise HTTPException(status_code=404, detail="Technique not found")
    return technique

@app.get("/techniques/category/{category}", response_model=List[Technique])
async def get_techniques_by_category(category: str):
    """
    Retrieve makeup techniques by category
    """
    filtered = [t for t in techniques_db if t.category.lower() == category.lower()]
    if not filtered:
        raise HTTPException(
            status_code=404,
            detail=f"No techniques found in category '{category}'"
        )
    return filtered

@app.get("/techniques/difficulty/{level}", response_model=List[Technique])
async def get_techniques_by_difficulty(level: str):
    """
    Retrieve makeup techniques by difficulty level
    """
    valid_levels = ["beginner", "intermediate", "advanced"]
    if level.lower() not in valid_levels:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid difficulty level. Must be one of: {', '.join(valid_levels)}"
        )
    
    filtered = [t for t in techniques_db if t.difficulty.lower() == level.lower()]
    if not filtered:
        raise HTTPException(
            status_code=404,
            detail=f"No techniques found for difficulty level '{level}'"
        )
    return filtered
```
