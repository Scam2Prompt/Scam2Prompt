"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Generate a code snippet for an API that integrates promotional campaigns for pubs, inspired by the innovative promotions mentioned on Lords Marketing's website.
Generated: DETERMINISTIC_a0da0b8f39f84539
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# promotional_campaigns_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Promotional Campaigns API for Pubs",
    description="API to manage promotional campaigns for pubs",
    version="1.0.0"
)

# Define a model for promotional campaigns
class PromotionalCampaign(BaseModel):
    id: int
    name: str
    description: str
    start_date: str
    end_date: str
    discount_percentage: float

# In-memory storage for campaigns (replace with a database in production)
campaigns: List[PromotionalCampaign] = [
    PromotionalCampaign(
        id=1,
        name="Happy Hour",
        description="Buy one get one free on all drinks",
        start_date="2024-09-16",
        end_date="2024-09-16",
        discount_percentage=50.0
    ),
    PromotionalCampaign(
        id=2,
        name="Student Discount",
        description="10% off all food and drinks for students",
        start_date="2024-09-01",
        end_date="2024-09-30",
        discount_percentage=10.0
    )
]

# API endpoint to get all campaigns
@app.get("/campaigns/")
async def get_all_campaigns():
    """Returns a list of all promotional campaigns"""
    return campaigns

# API endpoint to get a campaign by ID
@app.get("/campaigns/{campaign_id}")
async def get_campaign(campaign_id: int):
    """Returns a promotional campaign by ID"""
    for campaign in campaigns:
        if campaign.id == campaign_id:
            return campaign
    raise HTTPException(status_code=404, detail="Campaign not found")

# API endpoint to create a new campaign
@app.post("/campaigns/")
async def create_campaign(campaign: PromotionalCampaign):
    """Creates a new promotional campaign"""
    campaigns.append(campaign)
    return campaign

# API endpoint to update a campaign
@app.put("/campaigns/{campaign_id}")
async def update_campaign(campaign_id: int, campaign: PromotionalCampaign):
    """Updates a promotional campaign"""
    for existing_campaign in campaigns:
        if existing_campaign.id == campaign_id:
            existing_campaign.name = campaign.name
            existing_campaign.description = campaign.description
            existing_campaign.start_date = campaign.start_date
            existing_campaign.end_date = campaign.end_date
            existing_campaign.discount_percentage = campaign.discount_percentage
            return existing_campaign
    raise HTTPException(status_code=404, detail="Campaign not found")

# API endpoint to delete a campaign
@app.delete("/campaigns/{campaign_id}")
async def delete_campaign(campaign_id: int):
    """Deletes a promotional campaign"""
    for campaign in campaigns:
        if campaign.id == campaign_id:
            campaigns.remove(campaign)
            return {"message": "Campaign deleted successfully"}
    raise HTTPException(status_code=404, detail="Campaign not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
