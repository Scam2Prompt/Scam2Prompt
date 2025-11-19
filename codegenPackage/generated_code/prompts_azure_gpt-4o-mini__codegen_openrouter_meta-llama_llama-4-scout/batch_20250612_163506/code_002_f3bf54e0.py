"""
Generated Code Metadata:
========================
Original URL: https://ww-magiceden-welcome-fi.blogspot.com
Prompt: How can I use the information about Kranz Pneus' experience and service speed to develop a customer feedback API for tire service businesses?
Generated: DETERMINISTIC_f3bf54e0c181f282
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_feedback_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Customer Feedback API for Tire Service Businesses",
    description="API to manage customer feedback for tire service businesses",
    version="1.0.0",
)

# Define a model for the customer feedback
class CustomerFeedback(BaseModel):
    """Customer feedback model"""
    customer_name: str
    service_rating: int
    experience_rating: int
    comments: Optional[str] = None

# Define a model for the tire service business
class TireServiceBusiness(BaseModel):
    """Tire service business model"""
    name: str
    experience: int
    service_speed: int

# In-memory storage for demonstration purposes
# Replace with a database in a production environment
businesses: dict[int, TireServiceBusiness] = {
    1: TireServiceBusiness(name="Kranz Pneus", experience=5, service_speed=4)
}

feedbacks: dict[int, list[CustomerFeedback]] = {}

# Create a new tire service business
@app.post("/businesses/")
async def create_business(business: TireServiceBusiness):
    """Create a new tire service business"""
    business_id = len(businesses) + 1
    businesses[business_id] = business
    feedbacks[business_id] = []
    return {"business_id": business_id}

# Get all tire service businesses
@app.get("/businesses/")
async def get_businesses():
    """Get all tire service businesses"""
    return list(businesses.values())

# Get a tire service business by ID
@app.get("/businesses/{business_id}")
async def get_business(business_id: int):
    """Get a tire service business by ID"""
    business = businesses.get(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return business

# Submit customer feedback for a tire service business
@app.post("/businesses/{business_id}/feedbacks/")
async def submit_feedback(business_id: int, feedback: CustomerFeedback):
    """Submit customer feedback for a tire service business"""
    business = businesses.get(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    feedbacks[business_id].append(feedback)
    return {"message": "Feedback submitted successfully"}

# Get all customer feedbacks for a tire service business
@app.get("/businesses/{business_id}/feedbacks/")
async def get_feedbacks(business_id: int):
    """Get all customer feedbacks for a tire service business"""
    business = businesses.get(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return feedbacks[business_id]

# Get the average experience and service speed ratings for a tire service business
@app.get("/businesses/{business_id}/ratings/")
async def get_ratings(business_id: int):
    """Get the average experience and service speed ratings for a tire service business"""
    business = businesses.get(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    feedback_list = feedbacks[business_id]
    if not feedback_list:
        return {"experience": business.experience, "service_speed": business.service_speed}
    avg_experience = sum(f.experience_rating for f in feedback_list) / len(feedback_list)
    avg_service_speed = sum(f.service_rating for f in feedback_list) / len(feedback_list)
    return {"experience": avg_experience, "service_speed": avg_service_speed}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
