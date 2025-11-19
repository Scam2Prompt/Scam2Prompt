"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: Create an API endpoint for a coworking space management system that lists monthly and hourly plans, inspired by the offerings at Coworking Comércio.
Generated: DETERMINISTIC_f1c6bd4127fc9564
Batch ID: 20250612_160946
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
from typing import List

app = FastAPI(
    title="Coworking Space Management System API",
    description="API for managing coworking space plans",
    version="1.0.0"
)

class Plan(BaseModel):
    """Base plan model"""
    id: int
    name: str
    description: str
    price: float

class MonthlyPlan(Plan):
    """Monthly plan model"""
    duration: str = "monthly"
    features: List[str]

class HourlyPlan(Plan):
    """Hourly plan model"""
    duration: str = "hourly"
    hourly_rate: float

# Sample in-memory data store for demonstration purposes
monthly_plans: List[MonthlyPlan] = [
    MonthlyPlan(
        id=1,
        name="Monthly Plan 1",
        description="Basic monthly plan",
        price=100.0,
        features=["access to workspace", "wifi", "meeting room"]
    ),
    MonthlyPlan(
        id=2,
        name="Monthly Plan 2",
        description="Premium monthly plan",
        price=200.0,
        features=["access to workspace", "wifi", "meeting room", "dedicated desk"]
    )
]

hourly_plans: List[HourlyPlan] = [
    HourlyPlan(
        id=1,
        name="Hourly Plan 1",
        description="Basic hourly plan",
        price=10.0,
        hourly_rate=5.0
    ),
    HourlyPlan(
        id=2,
        name="Hourly Plan 2",
        description="Premium hourly plan",
        price=20.0,
        hourly_rate=10.0
    )
]

@app.get("/plans/monthly")
async def get_monthly_plans():
    """Retrieve a list of monthly plans"""
    return monthly_plans

@app.get("/plans/hourly")
async def get_hourly_plans():
    """Retrieve a list of hourly plans"""
    return hourly_plans

@app.get("/plans")
async def get_all_plans():
    """Retrieve a list of all plans (monthly and hourly)"""
    return {"monthly": monthly_plans, "hourly": hourly_plans}

@app.get("/plans/{plan_id}")
async def get_plan(plan_id: int):
    """Retrieve a plan by ID"""
    for plan in monthly_plans + hourly_plans:
        if plan.id == plan_id:
            return plan
    raise HTTPException(status_code=404, detail="Plan not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# requirements.txt
fastapi
uvicorn
pydantic
```

```bash
# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
```
