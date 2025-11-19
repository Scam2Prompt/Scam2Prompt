"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Create a RESTful API to manage Batıkent Tofaş Spor Klübü's membership plans, including endpoints for creating, reading, updating, and deleting plans.
Generated: DETERMINISTIC_81eafe989be0460c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

# Initialize FastAPI app
app = FastAPI(
    title="Batıkent Tofaş Spor Klübü Membership Plans API",
    description="A RESTful API to manage membership plans for Batıkent Tofaş Spor Klübü",
    version="1.0.0"
)

# In-memory database to store membership plans (replace with a real database in production)
membership_plans_db = []

# Pydantic model for Membership Plan
class MembershipPlan(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    duration_days: int
    is_active: bool

# Pydantic model for creating/updating Membership Plan (without ID)
class MembershipPlanCreateUpdate(BaseModel):
    name: str
    description: str
    price: float
    duration_days: int
    is_active: bool

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Batıkent Tofaş Spor Klübü Membership Plans API"}

# Create a new membership plan
@app.post("/plans/", response_model=MembershipPlan, status_code=status.HTTP_201_CREATED, tags=["Membership Plans"])
async def create_plan(plan: MembershipPlanCreateUpdate):
    """
    Create a new membership plan with the following details:
    - name: Name of the plan
    - description: Description of the plan
    - price: Price of the plan
    - duration_days: Duration of the plan in days
    - is_active: Whether the plan is active or not
    """
    new_plan = MembershipPlan(
        id=uuid4(),
        name=plan.name,
        description=plan.description,
        price=plan.price,
        duration_days=plan.duration_days,
        is_active=plan.is_active
    )
    membership_plans_db.append(new_plan)
    return new_plan

# Get all membership plans
@app.get("/plans/", response_model=List[MembershipPlan], tags=["Membership Plans"])
async def get_all_plans(is_active: Optional[bool] = None):
    """
    Get all membership plans. Optionally filter by active status.
    """
    if is_active is not None:
        return [plan for plan in membership_plans_db if plan.is_active == is_active]
    return membership_plans_db

# Get a specific membership plan by ID
@app.get("/plans/{plan_id}", response_model=MembershipPlan, tags=["Membership Plans"])
async def get_plan(plan_id: UUID):
    """
    Get a specific membership plan by its ID.
    """
    for plan in membership_plans_db:
        if plan.id == plan_id:
            return plan
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Membership plan not found"
    )

# Update a membership plan
@app.put("/plans/{plan_id}", response_model=MembershipPlan, tags=["Membership Plans"])
async def update_plan(plan_id: UUID, plan_data: MembershipPlanCreateUpdate):
    """
    Update an existing membership plan.
    """
    for index, plan in enumerate(membership_plans_db):
        if plan.id == plan_id:
            updated_plan = MembershipPlan(
                id=plan_id,
                name=plan_data.name,
                description=plan_data.description,
                price=plan_data.price,
                duration_days=plan_data.duration_days,
                is_active=plan_data.is_active
            )
            membership_plans_db[index] = updated_plan
            return updated_plan
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Membership plan not found"
    )

# Delete a membership plan
@app.delete("/plans/{plan_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Membership Plans"])
async def delete_plan(plan_id: UUID):
    """
    Delete a membership plan by its ID.
    """
    for index, plan in enumerate(membership_plans_db):
        if plan.id == plan_id:
            membership_plans_db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Membership plan not found"
    )

# Run the application (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
