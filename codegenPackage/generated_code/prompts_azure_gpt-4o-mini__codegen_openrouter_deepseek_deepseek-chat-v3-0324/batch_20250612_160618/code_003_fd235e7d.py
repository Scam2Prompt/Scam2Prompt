"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Create an API that collects data on women's participation in clean energy initiatives, reflecting the outcomes of Sauti Kenya's Cohort 2 project.
Generated: DETERMINISTIC_fd235e7de072ee73
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
API for collecting and managing data on women's participation in clean energy initiatives.
Reflects outcomes of Sauti Kenya's Cohort 2 project.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Women in Clean Energy API",
    description="API for tracking women's participation in clean energy initiatives",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "clean_energy_db")

client = AsyncIOMotorClient(DATABASE_URL)
db = client[DB_NAME]
participants_collection = db["participants"]
initiatives_collection = db["initiatives"]

# Models
class Participant(BaseModel):
    name: str
    age: int
    location: str
    education_level: str
    participation_date: date
    initiative_id: str
    skills_gained: List[str]
    income_change: Optional[float] = None
    employment_status: Optional[str] = None
    testimonial: Optional[str] = None

class Initiative(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date
    location: str
    total_participants: int
    women_participants: int
    outcomes: List[str]
    challenges: Optional[List[str]] = None
    success_stories: Optional[List[str]] = None

class UpdateParticipant(BaseModel):
    income_change: Optional[float] = None
    employment_status: Optional[str] = None
    testimonial: Optional[str] = None

class UpdateInitiative(BaseModel):
    total_participants: Optional[int] = None
    women_participants: Optional[int] = None
    outcomes: Optional[List[str]] = None
    challenges: Optional[List[str]] = None
    success_stories: Optional[List[str]] = None

# Helper functions
async def get_participant_or_404(participant_id: str):
    participant = await participants_collection.find_one({"_id": participant_id})
    if not participant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Participant not found"
        )
    return participant

async def get_initiative_or_404(initiative_id: str):
    initiative = await initiatives_collection.find_one({"_id": initiative_id})
    if not initiative:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Initiative not found"
        )
    return initiative

# Routes
@app.post("/participants/", status_code=status.HTTP_201_CREATED)
async def create_participant(participant: Participant):
    """Create a new participant record"""
    participant_dict = participant.dict()
    result = await participants_collection.insert_one(participant_dict)
    return {"id": str(result.inserted_id)}

@app.get("/participants/", response_model=List[Participant])
async def list_participants(limit: int = 100):
    """List all participants with optional limit"""
    cursor = participants_collection.find().limit(limit)
    participants = await cursor.to_list(length=limit)
    return participants

@app.get("/participants/{participant_id}", response_model=Participant)
async def get_participant(participant_id: str):
    """Get a specific participant by ID"""
    participant = await get_participant_or_404(participant_id)
    return participant

@app.put("/participants/{participant_id}")
async def update_participant(participant_id: str, update_data: UpdateParticipant):
    """Update participant data"""
    await get_participant_or_404(participant_id)
    update_values = {k: v for k, v in update_data.dict().items() if v is not None}
    
    if update_values:
        await participants_collection.update_one(
            {"_id": participant_id},
            {"$set": update_values}
        )
    return {"message": "Participant updated successfully"}

@app.post("/initiatives/", status_code=status.HTTP_201_CREATED)
async def create_initiative(initiative: Initiative):
    """Create a new initiative record"""
    initiative_dict = initiative.dict()
    result = await initiatives_collection.insert_one(initiative_dict)
    return {"id": str(result.inserted_id)}

@app.get("/initiatives/", response_model=List[Initiative])
async def list_initiatives(limit: int = 100):
    """List all initiatives with optional limit"""
    cursor = initiatives_collection.find().limit(limit)
    initiatives = await cursor.to_list(length=limit)
    return initiatives

@app.get("/initiatives/{initiative_id}", response_model=Initiative)
async def get_initiative(initiative_id: str):
    """Get a specific initiative by ID"""
    initiative = await get_initiative_or_404(initiative_id)
    return initiative

@app.put("/initiatives/{initiative_id}")
async def update_initiative(initiative_id: str, update_data: UpdateInitiative):
    """Update initiative data"""
    await get_initiative_or_404(initiative_id)
    update_values = {k: v for k, v in update_data.dict().items() if v is not None}
    
    if update_values:
        await initiatives_collection.update_one(
            {"_id": initiative_id},
            {"$set": update_values}
        )
    return {"message": "Initiative updated successfully"}

@app.get("/initiatives/{initiative_id}/participants", response_model=List[Participant])
async def get_initiative_participants(initiative_id: str):
    """Get all participants for a specific initiative"""
    await get_initiative_or_404(initiative_id)
    cursor = participants_collection.find({"initiative_id": initiative_id})
    participants = await cursor.to_list(length=1000)
    return participants

@app.get("/stats/women_participation")
async def get_women_participation_stats():
    """Get statistics about women's participation across all initiatives"""
    total_initiatives = await initiatives_collection.count_documents({})
    total_women = await participants_collection.count_documents({})
    
    pipeline = [
        {"$group": {
            "_id": None,
            "avg_women_percentage": {"$avg": {"$divide": ["$women_participants", "$total_participants"]}},
            "total_women_participants": {"$sum": "$women_participants"}
        }}
    ]
    
    stats = await initiatives_collection.aggregate(pipeline).to_list(length=1)
    
    return {
        "total_initiatives": total_initiatives,
        "total_women_participants": total_women,
        "average_women_percentage": stats[0]["avg_women_percentage"] if stats else 0,
        "total_women_across_initiatives": stats[0]["total_women_participants"] if stats else 0
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
