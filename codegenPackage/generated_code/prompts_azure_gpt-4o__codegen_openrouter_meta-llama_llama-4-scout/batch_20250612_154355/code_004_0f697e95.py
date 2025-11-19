"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Suggest APIs for tracking the performance of outdoor advertising campaigns, particularly for formats like "Vallas" and "Banderines" mentioned on WOW MEDIA.
Generated: DETERMINISTIC_0f697e95845d92f8
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# performance_tracker_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Outdoor Advertising Campaign Performance Tracker",
    description="API for tracking performance of outdoor advertising campaigns",
    version="1.0.0"
)

class AdvertisingCampaign(BaseModel):
    """Model for advertising campaign"""
    id: int
    name: str
    format: str  # e.g., "Vallas", "Banderines"
    location: str
    start_date: str
    end_date: str

class PerformanceMetric(BaseModel):
    """Model for performance metric"""
    campaign_id: int
    impressions: int
    clicks: int
    conversions: int
    date: str

# In-memory data store for demonstration purposes
# Replace with a proper database in production
campaigns: List[AdvertisingCampaign] = []
performance_metrics: List[PerformanceMetric] = []

@app.post("/campaigns/")
async def create_campaign(campaign: AdvertisingCampaign):
    """Create a new advertising campaign"""
    try:
        campaigns.append(campaign)
        logger.info(f"Campaign created: {campaign.name}")
        return {"message": "Campaign created successfully"}
    except Exception as e:
        logger.error(f"Error creating campaign: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create campaign")

@app.get("/campaigns/")
async def get_campaigns():
    """Retrieve a list of all advertising campaigns"""
    try:
        return campaigns
    except Exception as e:
        logger.error(f"Error retrieving campaigns: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve campaigns")

@app.post("/performance/metrics/")
async def create_performance_metric(metric: PerformanceMetric):
    """Create a new performance metric for a campaign"""
    try:
        performance_metrics.append(metric)
        logger.info(f"Performance metric created for campaign {metric.campaign_id}")
        return {"message": "Performance metric created successfully"}
    except Exception as e:
        logger.error(f"Error creating performance metric: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to create performance metric")

@app.get("/performance/metrics/")
async def get_performance_metrics(campaign_id: int = None):
    """Retrieve performance metrics for a campaign or all campaigns"""
    try:
        if campaign_id:
            metrics = [m for m in performance_metrics if m.campaign_id == campaign_id]
        else:
            metrics = performance_metrics
        return metrics
    except Exception as e:
        logger.error(f"Error retrieving performance metrics: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve performance metrics")

@app.get("/campaigns/{campaign_id}/performance")
async def get_campaign_performance(campaign_id: int):
    """Retrieve performance metrics for a specific campaign"""
    try:
        campaign = next((c for c in campaigns if c.id == campaign_id), None)
        if not campaign:
            raise HTTPException(status_code=404, detail="Campaign not found")
        metrics = [m for m in performance_metrics if m.campaign_id == campaign_id]
        return {"campaign": campaign, "metrics": metrics}
    except Exception as e:
        logger.error(f"Error retrieving campaign performance: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve campaign performance")
```

```python
# main.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run("performance_tracker_api:app", host="0.0.0.0", port=8000, reload=True)
```
