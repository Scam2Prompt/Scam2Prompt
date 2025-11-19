"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Create a REST API endpoint that allows for the submission of a strategic marketing plan, incorporating the full-funnel approach mentioned on the 3rd & Taylor website.
Generated: DETERMINISTIC_9e02c9744ff948fc
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

app = FastAPI(
    title="Strategic Marketing Plan API",
    description="API for submitting strategic marketing plans",
    version="1.0.0"
)

class MarketingPlan(BaseModel):
    """Represents a strategic marketing plan"""
    id: Optional[UUID] = None
    name: str
    description: str
    awareness_goal: str
    consideration_goal: str
    conversion_goal: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        """Configuration for MarketingPlan model"""
        schema_extra = {
            "example": {
                "name": "Example Marketing Plan",
                "description": "This is an example marketing plan",
                "awareness_goal": "Increase brand awareness by 20%",
                "consideration_goal": "Increase consideration by 15%",
                "conversion_goal": "Increase conversions by 10%"
            }
        }

@app.post("/marketing-plans/", response_model=MarketingPlan, status_code=201)
async def create_marketing_plan(marketing_plan: MarketingPlan):
    """
    Create a new strategic marketing plan.

    Args:
    - marketing_plan (MarketingPlan): The marketing plan to create.

    Returns:
    - MarketingPlan: The created marketing plan.
    """
    try:
        # Save the marketing plan to a database or other storage system
        # For this example, we'll just return the plan as is
        marketing_plan.created_at = datetime.now()
        marketing_plan.updated_at = datetime.now()
        return marketing_plan
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create marketing plan") from e

@app.get("/marketing-plans/", response_model=list[MarketingPlan])
async def read_marketing_plans():
    """
    Read a list of all strategic marketing plans.

    Returns:
    - list[MarketingPlan]: A list of marketing plans.
    """
    try:
        # Retrieve the marketing plans from a database or other storage system
        # For this example, we'll just return an empty list
        return []
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to read marketing plans") from e

@app.get("/marketing-plans/{plan_id}", response_model=MarketingPlan)
async def read_marketing_plan(plan_id: UUID):
    """
    Read a strategic marketing plan by ID.

    Args:
    - plan_id (UUID): The ID of the marketing plan to read.

    Returns:
    - MarketingPlan: The marketing plan with the specified ID.
    """
    try:
        # Retrieve the marketing plan from a database or other storage system
        # For this example, we'll just return a dummy plan
        return MarketingPlan(
            id=plan_id,
            name="Example Marketing Plan",
            description="This is an example marketing plan",
            awareness_goal="Increase brand awareness by 20%",
            consideration_goal="Increase consideration by 15%",
            conversion_goal="Increase conversions by 10%",
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail="Marketing plan not found") from e

@app.put("/marketing-plans/{plan_id}", response_model=MarketingPlan)
async def update_marketing_plan(plan_id: UUID, marketing_plan: MarketingPlan):
    """
    Update a strategic marketing plan.

    Args:
    - plan_id (UUID): The ID of the marketing plan to update.
    - marketing_plan (MarketingPlan): The updated marketing plan.

    Returns:
    - MarketingPlan: The updated marketing plan.
    """
    try:
        # Update the marketing plan in a database or other storage system
        # For this example, we'll just return the updated plan as is
        marketing_plan.id = plan_id
        marketing_plan.updated_at = datetime.now()
        return marketing_plan
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update marketing plan") from e

@app.delete("/marketing-plans/{plan_id}")
async def delete_marketing_plan(plan_id: UUID):
    """
    Delete a strategic marketing plan.

    Args:
    - plan_id (UUID): The ID of the marketing plan to delete.
    """
    try:
        # Delete the marketing plan from a database or other storage system
        # For this example, we'll just do nothing
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete marketing plan") from e
```
