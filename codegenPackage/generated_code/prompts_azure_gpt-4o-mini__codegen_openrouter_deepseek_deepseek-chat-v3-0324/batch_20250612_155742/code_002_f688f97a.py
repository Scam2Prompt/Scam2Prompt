"""
Generated Code Metadata:
========================
Original URL: https://suifox.online
Prompt: Generate code for a marketing campaign that includes giveaways and meme competitions, inspired by the SuiFOX roadmap.
Generated: DETERMINISTIC_f688f97aa8cd5832
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import requests
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, validator
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="SuiFOX Marketing Campaign API",
    description="API for managing SuiFOX marketing campaigns including giveaways and meme competitions",
    version="1.0.0"
)

# Database simulation (in production, use a real database)
campaigns_db = {}
participants_db = {}
submissions_db = {}

# Models
class Campaign(BaseModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime
    campaign_type: str  # "giveaway" or "meme_competition"
    prize: str
    rules: str
    max_participants: Optional[int] = None
    
    @validator('campaign_type')
    def validate_campaign_type(cls, v):
        if v not in ["giveaway", "meme_competition"]:
            raise ValueError("Campaign type must be either 'giveaway' or 'meme_competition'")
        return v
    
    @validator('end_date')
    def validate_end_date(cls, v, values):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class Participant(BaseModel):
    campaign_id: str
    name: str
    email: EmailStr
    wallet_address: str
    submission_url: Optional[str] = None  # For meme competitions

class Winner(BaseModel):
    participant_id: str
    prize: str
    awarded_at: datetime = datetime.now()

# Utility Functions
def generate_id() -> str:
    return str(random.randint(100000, 999999))

def is_campaign_active(campaign: Campaign) -> bool:
    now = datetime.now()
    return campaign.start_date <= now <= campaign.end_date

# API Endpoints
@app.post("/campaigns", status_code=status.HTTP_201_CREATED)
async def create_campaign(campaign: Campaign):
    """Create a new marketing campaign"""
    campaign_id = generate_id()
    campaigns_db[campaign_id] = campaign.dict()
    return {"campaign_id": campaign_id, "message": "Campaign created successfully"}

@app.get("/campaigns/{campaign_id}")
async def get_campaign(campaign_id: str):
    """Get campaign details"""
    if campaign_id not in campaigns_db:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaigns_db[campaign_id]

@app.post("/participate")
async def participate(participant: Participant):
    """Participate in a campaign"""
    if participant.campaign_id not in campaigns_db:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    campaign = campaigns_db[participant.campaign_id]
    
    if not is_campaign_active(campaign):
        raise HTTPException(status_code=400, detail="Campaign is not active")
    
    if campaign["max_participants"] and len(participants_db.get(participant.campaign_id, [])) >= campaign["max_participants"]:
        raise HTTPException(status_code=400, detail="Maximum participants reached")
    
    participant_id = generate_id()
    participants_db.setdefault(participant.campaign_id, {})[participant_id] = participant.dict()
    
    return {"participant_id": participant_id, "message": "Participation successful"}

@app.get("/campaigns/{campaign_id}/participants")
async def get_participants(campaign_id: str):
    """Get all participants for a campaign"""
    if campaign_id not in campaigns_db:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return participants_db.get(campaign_id, {})

@app.post("/campaigns/{campaign_id}/select-winners")
async def select_winners(campaign_id: str, num_winners: int = 1):
    """Randomly select winners for a campaign"""
    if campaign_id not in campaigns_db:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    campaign = campaigns_db[campaign_id]
    
    if datetime.now() < campaign["end_date"]:
        raise HTTPException(status_code=400, detail="Campaign has not ended yet")
    
    participants = participants_db.get(campaign_id, {})
    if not participants:
        raise HTTPException(status_code=400, detail="No participants found")
    
    if num_winners > len(participants):
        raise HTTPException(status_code=400, detail="Number of winners exceeds number of participants")
    
    winner_ids = random.sample(list(participants.keys()), num_winners)
    winners = []
    
    for winner_id in winner_ids:
        winner = Winner(
            participant_id=winner_id,
            prize=campaign["prize"]
        )
        winners.append(winner.dict())
    
    return {"winners": winners}

@app.get("/campaigns/active")
async def get_active_campaigns():
    """Get all currently active campaigns"""
    active_campaigns = []
    now = datetime.now()
    
    for campaign_id, campaign in campaigns_db.items():
        if campaign["start_date"] <= now <= campaign["end_date"]:
            active_campaigns.append({"campaign_id": campaign_id, **campaign})
    
    return {"active_campaigns": active_campaigns}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
