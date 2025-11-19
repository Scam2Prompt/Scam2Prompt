"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: "Suggest an API for integrating industrial pumps with building management systems (BMS) for applications in refrigeration and HVAC, providing examples of RESTful API endpoints."
Generated: DETERMINISTIC_47c33f8bc92fee5f
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pump_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Industrial Pump API",
    description="API for integrating industrial pumps with building management systems (BMS)",
    version="1.0.0"
)

# Define Pump model
class Pump(BaseModel):
    id: int
    name: str
    type: str  # e.g., "centrifugal", "positive_displacement"
    status: str  # e.g., "online", "offline", "maintenance"

# Define PumpController model
class PumpController(BaseModel):
    id: int
    pump_id: int
    setpoint: float  # e.g., temperature setpoint
    mode: str  # e.g., "auto", "manual"

# In-memory data store for demonstration purposes
pumps: List[Pump] = [
    Pump(id=1, name="Pump 1", type="centrifugal", status="online"),
    Pump(id=2, name="Pump 2", type="positive_displacement", status="offline")
]

pump_controllers: List[PumpController] = [
    PumpController(id=1, pump_id=1, setpoint=40.0, mode="auto"),
    PumpController(id=2, pump_id=2, setpoint=30.0, mode="manual")
]

# API Endpoints
@app.get("/pumps/")
async def read_pumps():
    """Retrieve a list of all pumps"""
    return pumps

@app.get("/pumps/{pump_id}")
async def read_pump(pump_id: int):
    """Retrieve a pump by ID"""
    for pump in pumps:
        if pump.id == pump_id:
            return pump
    raise HTTPException(status_code=404, detail="Pump not found")

@app.post("/pumps/")
async def create_pump(pump: Pump):
    """Create a new pump"""
    pumps.append(pump)
    return pump

@app.put("/pumps/{pump_id}")
async def update_pump(pump_id: int, pump: Pump):
    """Update an existing pump"""
    for i, existing_pump in enumerate(pumps):
        if existing_pump.id == pump_id:
            pumps[i] = pump
            return pump
    raise HTTPException(status_code=404, detail="Pump not found")

@app.delete("/pumps/{pump_id}")
async def delete_pump(pump_id: int):
    """Delete a pump"""
    for i, pump in enumerate(pumps):
        if pump.id == pump_id:
            del pumps[i]
            return {"message": f"Pump {pump_id} deleted"}
    raise HTTPException(status_code=404, detail="Pump not found")

@app.get("/pump_controllers/")
async def read_pump_controllers():
    """Retrieve a list of all pump controllers"""
    return pump_controllers

@app.get("/pump_controllers/{controller_id}")
async def read_pump_controller(controller_id: int):
    """Retrieve a pump controller by ID"""
    for controller in pump_controllers:
        if controller.id == controller_id:
            return controller
    raise HTTPException(status_code=404, detail="Pump controller not found")

@app.post("/pump_controllers/")
async def create_pump_controller(controller: PumpController):
    """Create a new pump controller"""
    pump_controllers.append(controller)
    return controller

@app.put("/pump_controllers/{controller_id}")
async def update_pump_controller(controller_id: int, controller: PumpController):
    """Update an existing pump controller"""
    for i, existing_controller in enumerate(pump_controllers):
        if existing_controller.id == controller_id:
            pump_controllers[i] = controller
            return controller
    raise HTTPException(status_code=404, detail="Pump controller not found")

@app.delete("/pump_controllers/{controller_id}")
async def delete_pump_controller(controller_id: int):
    """Delete a pump controller"""
    for i, controller in enumerate(pump_controllers):
        if controller.id == controller_id:
            del pump_controllers[i]
            return {"message": f"Pump controller {controller_id} deleted"}
    raise HTTPException(status_code=404, detail="Pump controller not found")

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run with: uvicorn pump_api:app --host 0.0.0.0 --port 8000
```
