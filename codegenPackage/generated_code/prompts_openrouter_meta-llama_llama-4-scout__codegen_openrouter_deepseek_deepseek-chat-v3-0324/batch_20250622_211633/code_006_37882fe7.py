"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Develop a RESTful API for managing outdoor advertising campaigns, including endpoints for creating, reading, updating, and deleting campaigns, inspired by the services provided by WOW MEDIA."
Generated: DETERMINISTIC_37882fe724c8aa4f
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import uuid4
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Outdoor Advertising Campaigns API",
    description="A RESTful API for managing outdoor advertising campaigns",
    version="1.0.0"
)

# Database simulation (in production, use a real database)
campaigns_db = []

# Pydantic models for request/response validation
class CampaignBase(BaseModel):
    name: str
    client_name: str
    start_date: datetime
    end_date: datetime
    budget: float
    locations: List[str]
    status: str = "planned"  # planned, active, completed, cancelled

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Utility functions
def get_campaign_by_id(campaign_id: str):
    for campaign in campaigns_db:
        if campaign["id"] == campaign_id:
            return campaign
    return None

# API endpoints
@app.post("/campaigns/", response_model=Campaign, status_code=status.HTTP_201_CREATED)
async def create_campaign(campaign: CampaignCreate):
    """
    Create a new advertising campaign.
    """
    try:
        campaign_id = str(uuid4())
        now = datetime.now()
        campaign_data = {
            "id": campaign_id,
            "created_at": now,
            "updated_at": now,
            **campaign.dict()
        }
        campaigns_db.append(campaign_data)
        logger.info(f"Created campaign with ID: {campaign_id}")
        return campaign_data
    except Exception as e:
        logger.error(f"Error creating campaign: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create campaign"
        )

@app.get("/campaigns/", response_model=List[Campaign])
async def get_campaigns(status_filter: Optional[str] = None):
    """
    Get all campaigns, optionally filtered by status.
    """
    try:
        if status_filter:
            filtered_campaigns = [c for c in campaigns_db if c["status"].lower() == status_filter.lower()]
            return filtered_campaigns
        return campaigns_db
    except Exception as e:
        logger.error(f"Error retrieving campaigns: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve campaigns"
        )

@app.get("/campaigns/{campaign_id}", response_model=Campaign)
async def get_campaign(campaign_id: str):
    """
    Get a specific campaign by ID.
    """
    campaign = get_campaign_by_id(campaign_id)
    if not campaign:
        logger.warning(f"Campaign not found with ID: {campaign_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Campaign not found"
        )
    return campaign

@app.put("/campaigns/{campaign_id}", response_model=Campaign)
async def update_campaign(campaign_id: str, campaign_update: CampaignCreate):
    """
    Update an existing campaign.
    """
    try:
        campaign = get_campaign_by_id(campaign_id)
        if not campaign:
            logger.warning(f"Campaign not found with ID: {campaign_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Campaign not found"
            )

        update_data = campaign_update.dict()
        update_data["updated_at"] = datetime.now()
        
        for key, value in update_data.items():
            campaign[key] = value

        logger.info(f"Updated campaign with ID: {campaign_id}")
        return campaign
    except Exception as e:
        logger.error(f"Error updating campaign: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update campaign"
        )

@app.delete("/campaigns/{campaign_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_campaign(campaign_id: str):
    """
    Delete a campaign.
    """
    try:
        global campaigns_db
        campaign = get_campaign_by_id(campaign_id)
        if not campaign:
            logger.warning(f"Campaign not found with ID: {campaign_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Campaign not found"
            )

        campaigns_db = [c for c in campaigns_db if c["id"] != campaign_id]
        logger.info(f"Deleted campaign with ID: {campaign_id}")
    except Exception as e:
        logger.error(f"Error deleting campaign: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete campaign"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring service availability.
    """
    return {"status": "healthy"}

# Main entry point (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
