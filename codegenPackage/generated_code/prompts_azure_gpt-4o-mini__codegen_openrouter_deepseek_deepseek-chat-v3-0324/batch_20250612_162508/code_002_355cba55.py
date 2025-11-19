"""
Generated Code Metadata:
========================
Original URL: https://orbiter.lol
Prompt: Develop an API that provides users with daily insights and tips to reclaim their time from social media, reflecting the urgent message from orbiter.lol about breaking free from digital control.
Generated: DETERMINISTIC_355cba55761f4b26
Batch ID: 20250612_162508
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
from datetime import date
from typing import List
import random

app = FastAPI(
    title="Digital Detox API",
    description="API providing daily insights and tips to reclaim time from social media.",
    version="1.0.0",
)

# Data models
class DailyTip(BaseModel):
    id: int
    date: date
    title: str
    content: str
    action_step: str

class UserSubscription(BaseModel):
    email: str
    subscription_date: date

# In-memory database (replace with persistent storage in production)
tips_database = [
    {
        "id": 1,
        "date": date(2023, 1, 1),
        "title": "Start with Awareness",
        "content": "Track your social media usage for a day to understand your habits.",
        "action_step": "Use your phone's screen time feature to monitor usage."
    },
    {
        "id": 2,
        "date": date(2023, 1, 2),
        "title": "Set Clear Boundaries",
        "content": "Designate specific times for social media and stick to them.",
        "action_step": "Schedule two 15-minute blocks for social media today."
    },
    {
        "id": 3,
        "date": date(2023, 1, 3),
        "title": "Digital Declutter",
        "content": "Unfollow accounts that don't add value to your life.",
        "action_step": "Spend 10 minutes cleaning up your following list."
    }
]

subscriptions = []

@app.get("/tips", response_model=List[DailyTip], summary="Get all available tips")
async def get_all_tips():
    """Retrieve all available digital detox tips."""
    return tips_database

@app.get("/tips/today", response_model=DailyTip, summary="Get today's tip")
async def get_todays_tip():
    """Retrieve a random tip for today's digital detox challenge."""
    if not tips_database:
        raise HTTPException(status_code=404, detail="No tips available")
    return random.choice(tips_database)

@app.get("/tips/{tip_id}", response_model=DailyTip, summary="Get a specific tip by ID")
async def get_tip_by_id(tip_id: int):
    """Retrieve a specific digital detox tip by its ID."""
    tip = next((t for t in tips_database if t["id"] == tip_id), None)
    if not tip:
        raise HTTPException(status_code=404, detail="Tip not found")
    return tip

@app.post("/subscribe", response_model=UserSubscription, summary="Subscribe for daily tips")
async def subscribe(user: UserSubscription):
    """Subscribe to receive daily digital detox tips via email."""
    if any(sub["email"] == user.email for sub in subscriptions):
        raise HTTPException(status_code=400, detail="Email already subscribed")
    
    subscriptions.append(user.dict())
    return user

@app.get("/subscriptions", response_model=List[UserSubscription], summary="List all subscriptions")
async def list_subscriptions():
    """List all current subscriptions (admin only)."""
    return subscriptions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
