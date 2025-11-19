"""
Generated Code Metadata:
========================
Original URL: https://soltec-solutions.de
Prompt: Develop an API that allows users to input their energy consumption and receive tailored solar panel installation plans, as described in Soltec Solutions' individual planning services.
Generated: DETERMINISTIC_afb798eda5a50287
Batch ID: 20250612_153225
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
from typing import Dict

app = FastAPI(
    title="Solar Panel Installation Plan API",
    description="API to generate solar panel installation plans based on user energy consumption",
    version="1.0.0"
)

class EnergyConsumption(BaseModel):
    """User's energy consumption data"""
    daily_kwh: float
    monthly_kwh: float
    yearly_kwh: float

class SolarPanelInstallationPlan(BaseModel):
    """Solar panel installation plan"""
    num_panels: int
    total_watts: float
    estimated_cost: float
    payback_period: float

# Mock database for demonstration purposes
# In a real application, use a proper database
installation_plans: Dict[float, SolarPanelInstallationPlan] = {
    1000: SolarPanelInstallationPlan(num_panels=5, total_watts=2500.0, estimated_cost=15000.0, payback_period=5.0),
    2000: SolarPanelInstallationPlan(num_panels=10, total_watts=5000.0, estimated_cost=30000.0, payback_period=7.0),
    3000: SolarPanelInstallationPlan(num_panels=15, total_watts=7500.0, estimated_cost=45000.0, payback_period=10.0),
}

@app.post("/energy-consumption/")
async def create_installation_plan(energy_consumption: EnergyConsumption):
    """
    Generate a solar panel installation plan based on user's energy consumption.

    Args:
    - daily_kwh (float): User's daily energy consumption in kWh
    - monthly_kwh (float): User's monthly energy consumption in kWh
    - yearly_kwh (float): User's yearly energy consumption in kWh

    Returns:
    - SolarPanelInstallationPlan: Tailored solar panel installation plan
    """
    try:
        # Calculate the required solar panel capacity based on user's energy consumption
        required_capacity = energy_consumption.yearly_kwh * 1000 / 2000  # Assume 2000 kWh/year per kW

        # Find the closest match in the mock database
        closest_match = min(installation_plans.keys(), key=lambda x:abs(x-required_capacity))

        return installation_plans[closest_match]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/installation-plans/")
async def read_installation_plans():
    """
    Retrieve a list of available solar panel installation plans.

    Returns:
    - Dict[float, SolarPanelInstallationPlan]: Available installation plans
    """
    try:
        return installation_plans
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/installation-plans/{plan_id}")
async def read_installation_plan(plan_id: float):
    """
    Retrieve a specific solar panel installation plan.

    Args:
    - plan_id (float): ID of the installation plan

    Returns:
    - SolarPanelInstallationPlan: Installation plan with the given ID
    """
    try:
        plan = installation_plans.get(plan_id)
        if plan is None:
            raise HTTPException(status_code=404, detail="Plan not found")
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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
# Run the application
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
