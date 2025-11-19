"""
Generated Code Metadata:
========================
Original URL: https://monadawards.xyz
Prompt: Generate a satirical API specification for a fictional awards system that includes endpoints for submitting nominations, retrieving nominees, and filtering by categories like "Gymonad Bullies."
Generated: DETERMINISTIC_88318ea1bc1fe9a7
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://opensource.org/licenses/MIT": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional
import random

app = FastAPI(
    title="The Satirical Awards API",
    description="A fictional awards system for recognizing the most absurd achievements.",
    version="1.0.0",
    contact={
        "name": "Chief Satirist",
        "email": "satire@example.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

class Category(str, Enum):
    GYMONAD_BULLIES = "Gymonad Bullies"
    OFFICE_THERAPISTS = "Office Therapists"
    VIRTUAL_SIGNALERS = "Virtual Signalers"
    MEETING_HIJACKERS = "Meeting Hijackers"
    TPS_REPORT_CHAMPIONS = "TPS Report Champions"

class Nomination(BaseModel):
    id: str
    nominee_name: str
    category: Category
    reason: str
    satirical_score: int
    is_approved: bool = False

class NominationSubmission(BaseModel):
    nominee_name: str
    category: Category
    reason: str
    satirical_score: int

# In-memory "database"
nominations_db = []

@app.post("/nominations/", response_model=Nomination, status_code=201)
async def submit_nomination(nomination: NominationSubmission):
    """
    Submit a new nomination for a satirical award.
    
    - **nominee_name**: Name of the person/entity being nominated
    - **category**: The absurd category for this nomination
    - **reason**: Why they deserve this (un)prestigious award
    - **satirical_score**: How satirical this nomination is (1-10)
    """
    if nomination.satirical_score < 1 or nomination.satirical_score > 10:
        raise HTTPException(
            status_code=400,
            detail="Satirical score must be between 1 and 10"
        )
    
    new_nomination = Nomination(
        id=f"nom-{random.randint(1000, 9999)}",
        **nomination.dict()
    )
    nominations_db.append(new_nomination)
    return new_nomination

@app.get("/nominations/", response_model=List[Nomination])
async def get_nominations(
    category: Optional[Category] = None,
    approved_only: bool = False,
    min_score: Optional[int] = None
):
    """
    Retrieve all nominations with optional filters.
    
    - **category**: Filter by specific satirical category
    - **approved_only**: Only return approved nominations
    - **min_score**: Minimum satirical score to include
    """
    results = nominations_db
    
    if category:
        results = [n for n in results if n.category == category]
    
    if approved_only:
        results = [n for n in results if n.is_approved]
    
    if min_score:
        if min_score < 1 or min_score > 10:
            raise HTTPException(
                status_code=400,
                detail="Minimum score must be between 1 and 10"
            )
        results = [n for n in results if n.satirical_score >= min_score]
    
    return results

@app.get("/nominations/{nomination_id}", response_model=Nomination)
async def get_nomination(nomination_id: str):
    """
    Get a specific nomination by ID.
    """
    for nomination in nominations_db:
        if nomination.id == nomination_id:
            return nomination
    raise HTTPException(status_code=404, detail="Nomination not found")

@app.patch("/nominations/{nomination_id}/approve", response_model=Nomination)
async def approve_nomination(nomination_id: str):
    """
    Approve a nomination (because bureaucracy demands it).
    """
    for nomination in nominations_db:
        if nomination.id == nomination_id:
            nomination.is_approved = True
            return nomination
    raise HTTPException(status_code=404, detail="Nomination not found")

@app.get("/categories/", response_model=List[str])
async def get_categories():
    """
    Get all available satirical award categories.
    """
    return [category.value for category in Category]

@app.get("/random-winner/", response_model=Nomination)
async def get_random_winner():
    """
    Select a random winner from approved nominations (because fairness is overrated).
    """
    approved = [n for n in nominations_db if n.is_approved]
    if not approved:
        raise HTTPException(
            status_code=404,
            detail="No approved nominations available"
        )
    return random.choice(approved)
```
