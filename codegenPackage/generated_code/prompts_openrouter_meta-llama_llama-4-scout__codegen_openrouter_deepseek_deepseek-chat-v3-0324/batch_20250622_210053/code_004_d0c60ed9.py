"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Create an API endpoint to retrieve information about upcoming drawings, current payouts, and total points pledged to environmental charities on a web3 rewarded ads platform.
Generated: DETERMINISTIC_d0c60ed9777a460d
Batch ID: 20250622_210053
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
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Web3 Rewarded Ads Platform API",
    description="API for retrieving information about upcoming drawings, payouts, and charity pledges",
    version="1.0.0"
)

class Drawing(BaseModel):
    id: str
    name: str
    description: str
    prize_pool: float
    draw_date: datetime
    eligibility_criteria: str

class Payout(BaseModel):
    id: str
    amount: float
    currency: str
    recipient: str
    timestamp: datetime
    status: str

class CharityPoints(BaseModel):
    charity_id: str
    charity_name: str
    total_points: int
    points_conversion_rate: float

# Mock database
mock_drawings_db = [
    Drawing(
        id="draw001",
        name="Weekly Eco Lottery",
        description="Weekly drawing for active participants",
        prize_pool=5000.0,
        draw_date=datetime(2023, 12, 15, 18, 0),
        eligibility_criteria="Minimum 100 points in the last week"
    ),
    Drawing(
        id="draw002",
        name="Monthly Mega Draw",
        description="Monthly grand prize drawing",
        prize_pool=25000.0,
        draw_date=datetime(2024, 1, 1, 12, 0),
        eligibility_criteria="Minimum 500 points in the last month"
    )
]

mock_payouts_db = [
    Payout(
        id="payout001",
        amount=1200.0,
        currency="USD",
        recipient="user123",
        timestamp=datetime(2023, 11, 1, 10, 30),
        status="completed"
    ),
    Payout(
        id="payout002",
        amount=750.0,
        currency="USD",
        recipient="user456",
        timestamp=datetime(2023, 11, 5, 14, 15),
        status="completed"
    )
]

mock_charity_points_db = [
    CharityPoints(
        charity_id="charity001",
        charity_name="Ocean Cleanup Initiative",
        total_points=1500000,
        points_conversion_rate=0.01
    ),
    CharityPoints(
        charity_id="charity002",
        charity_name="Forest Restoration Project",
        total_points=980000,
        points_conversion_rate=0.01
    )
]

@app.get("/drawings/upcoming", response_model=List[Drawing])
async def get_upcoming_drawings(limit: Optional[int] = 10):
    """Get list of upcoming drawings"""
    try:
        current_time = datetime.now()
        upcoming_drawings = [drawing for drawing in mock_drawings_db if drawing.draw_date > current_time]
        return upcoming_drawings[:limit]
    except Exception as e:
        logger.error(f"Error retrieving upcoming drawings: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/payouts/current", response_model=List[Payout])
async def get_current_payouts(limit: Optional[int] = 10):
    """Get list of recent payouts"""
    try:
        sorted_payouts = sorted(mock_payouts_db, key=lambda x: x.timestamp, reverse=True)
        return sorted_payouts[:limit]
    except Exception as e:
        logger.error(f"Error retrieving current payouts: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/charities/points", response_model=List[CharityPoints])
async def get_charity_points():
    """Get total points pledged to environmental charities"""
    try:
        return mock_charity_points_db
    except Exception as e:
        logger.error(f"Error retrieving charity points: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/summary", response_model=dict)
async def get_platform_summary():
    """Get summary of platform statistics"""
    try:
        current_time = datetime.now()
        upcoming_drawings = [d for d in mock_drawings_db if d.draw_date > current_time]
        total_charity_points = sum(c.total_points for c in mock_charity_points_db)
        
        return {
            "upcoming_drawings_count": len(upcoming_drawings),
            "total_payouts_last_30_days": len(mock_payouts_db),
            "total_charity_points": total_charity_points,
            "charities_supported": len(mock_charity_points_db)
        }
    except Exception as e:
        logger.error(f"Error generating platform summary: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
```
