"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: Recommend APIs or libraries to implement a digital raffle system with contest scoring mechanisms, similar to the giveaway features described on the Virtual Media Events platform.
Generated: DETERMINISTIC_eaf3d26aa9203615
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, validator
import uuid
from datetime import datetime, timedelta
import motor.motor_asyncio
from fastapi.middleware.cors import CORSMiddleware

# Database configuration
DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
db = client.raffle_system

# FastAPI app initialization
app = FastAPI(
    title="Digital Raffle System API",
    description="API for managing digital raffles with contest scoring mechanisms",
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

# Models
class Participant(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    email: EmailStr
    score: int = 0
    entries: int = 1
    created_at: datetime = datetime.utcnow()

    @validator('score')
    def validate_score(cls, v):
        if v < 0:
            raise ValueError("Score cannot be negative")
        return v

    @validator('entries')
    def validate_entries(cls, v):
        if v < 1:
            raise ValueError("Entries must be at least 1")
        return v

class Raffle(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    max_participants: Optional[int] = None
    winners_count: int = 1
    participants: List[Participant] = []
    is_active: bool = False
    created_at: datetime = datetime.utcnow()

    @validator('end_time')
    def validate_end_time(cls, v, values):
        if 'start_time' in values and v <= values['start_time']:
            raise ValueError("End time must be after start time")
        return v

    @validator('winners_count')
    def validate_winners_count(cls, v):
        if v < 1:
            raise ValueError("There must be at least one winner")
        return v

class Winner(BaseModel):
    participant: Participant
    prize: Optional[str] = None
    position: int

# Utility functions
async def check_raffle_exists(raffle_id: str):
    raffle = await db.raffles.find_one({"id": raffle_id})
    if not raffle:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Raffle not found"
        )
    return raffle

async def check_participant_exists(raffle_id: str, participant_id: str):
    participant = await db.raffles.find_one(
        {"id": raffle_id, "participants.id": participant_id},
        {"participants.$": 1}
    )
    if not participant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Participant not found in this raffle"
        )
    return participant['participants'][0]

# API Endpoints
@app.post("/raffles/", status_code=status.HTTP_201_CREATED)
async def create_raffle(raffle: Raffle):
    raffle_dict = raffle.dict()
    await db.raffles.insert_one(raffle_dict)
    return {"message": "Raffle created successfully", "raffle_id": raffle.id}

@app.get("/raffles/{raffle_id}", response_model=Raffle)
async def get_raffle(raffle_id: str):
    raffle = await check_raffle_exists(raffle_id)
    return raffle

@app.post("/raffles/{raffle_id}/participants", status_code=status.HTTP_201_CREATED)
async def add_participant(raffle_id: str, participant: Participant):
    await check_raffle_exists(raffle_id)
    
    # Check if participant already exists
    existing_participant = await db.raffles.find_one(
        {"id": raffle_id, "participants.email": participant.email}
    )
    if existing_participant:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Participant with this email already exists"
        )
    
    await db.raffles.update_one(
        {"id": raffle_id},
        {"$push": {"participants": participant.dict()}}
    )
    return {"message": "Participant added successfully"}

@app.post("/raffles/{raffle_id}/participants/{participant_id}/entries")
async def add_entries(raffle_id: str, participant_id: str, entries: int):
    if entries <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Entries must be a positive number"
        )
    
    await check_participant_exists(raffle_id, participant_id)
    
    await db.raffles.update_one(
        {"id": raffle_id, "participants.id": participant_id},
        {"$inc": {"participants.$.entries": entries}}
    )
    return {"message": "Entries added successfully"}

@app.post("/raffles/{raffle_id}/participants/{participant_id}/score")
async def update_score(raffle_id: str, participant_id: str, score: int):
    await check_participant_exists(raffle_id, participant_id)
    
    await db.raffles.update_one(
        {"id": raffle_id, "participants.id": participant_id},
        {"$inc": {"participants.$.score": score}}
    )
    return {"message": "Score updated successfully"}

@app.post("/raffles/{raffle_id}/start")
async def start_raffle(raffle_id: str):
    raffle = await check_raffle_exists(raffle_id)
    
    if raffle['is_active']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Raffle is already active"
        )
    
    current_time = datetime.utcnow()
    if current_time < raffle['start_time']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Raffle cannot start before the scheduled time"
        )
    
    await db.raffles.update_one(
        {"id": raffle_id},
        {"$set": {"is_active": True}}
    )
    return {"message": "Raffle started successfully"}

@app.post("/raffles/{raffle_id}/draw", response_model=List[Winner])
async def draw_winners(raffle_id: str):
    raffle = await check_raffle_exists(raffle_id)
    
    if not raffle['is_active']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Raffle is not active"
        )
    
    if datetime.utcnow() < raffle['end_time']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Raffle has not ended yet"
        )
    
    participants = raffle['participants']
    if not participants:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No participants in this raffle"
        )
    
    # Weighted random selection based on entries and score
    weighted_participants = []
    for participant in participants:
        weight = participant['entries'] * (1 + participant['score'] / 100)
        weighted_participants.extend([participant] * int(weight))
    
    if len(weighted_participants) < raffle['winners_count']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough participants for the requested number of winners"
        )
    
    winners = random.sample(weighted_participants, raffle['winners_count'])
    winners_with_positions = [
        Winner(participant=winner, position=i+1)
        for i, winner in enumerate(winners)
    ]
    
    # Mark raffle as inactive after drawing
    await db.raffles.update_one(
        {"id": raffle_id},
        {"$set": {"is_active": False}}
    )
    
    return winners_with_positions

@app.get("/raffles/{raffle_id}/participants", response_model=List[Participant])
async def get_participants(raffle_id: str):
    raffle = await check_raffle_exists(raffle_id)
    return raffle['
