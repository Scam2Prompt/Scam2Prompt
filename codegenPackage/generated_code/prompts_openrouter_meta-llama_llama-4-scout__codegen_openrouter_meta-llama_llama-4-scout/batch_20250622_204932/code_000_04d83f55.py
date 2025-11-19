"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: "Design an API for managing industrial pump systems, including features for fire protection and water treatment, using ISO 9001 certified standards."
Generated: DETERMINISTIC_04d83f55f2ddc056
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# industrial_pump_system_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Industrial Pump System API",
    description="API for managing industrial pump systems",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@example.com",
    },
)

# Define pump system models
class PumpSystem(BaseModel):
    id: int
    name: str
    pump_type: str
    flow_rate: float
    pressure: float

class FireProtectionSystem(BaseModel):
    id: int
    pump_system_id: int
    fire_protection_type: str
    activation_status: bool

class WaterTreatmentSystem(BaseModel):
    id: int
    pump_system_id: int
    treatment_type: str
    treatment_status: str

# In-memory data store (replace with database in production)
pump_systems: List[PumpSystem] = []
fire_protection_systems: List[FireProtectionSystem] = []
water_treatment_systems: List[WaterTreatmentSystem] = []

# API Endpoints
@app.get("/pump-systems/")
def read_pump_systems():
    """Retrieve a list of all pump systems"""
    return pump_systems

@app.post("/pump-systems/")
def create_pump_system(pump_system: PumpSystem):
    """Create a new pump system"""
    pump_systems.append(pump_system)
    return pump_system

@app.get("/pump-systems/{pump_system_id}")
def read_pump_system(pump_system_id: int):
    """Retrieve a pump system by ID"""
    for pump_system in pump_systems:
        if pump_system.id == pump_system_id:
            return pump_system
    raise HTTPException(status_code=404, detail="Pump system not found")

@app.put("/pump-systems/{pump_system_id}")
def update_pump_system(pump_system_id: int, pump_system: PumpSystem):
    """Update a pump system"""
    for i, existing_pump_system in enumerate(pump_systems):
        if existing_pump_system.id == pump_system_id:
            pump_systems[i] = pump_system
            return pump_system
    raise HTTPException(status_code=404, detail="Pump system not found")

@app.delete("/pump-systems/{pump_system_id}")
def delete_pump_system(pump_system_id: int):
    """Delete a pump system"""
    for i, pump_system in enumerate(pump_systems):
        if pump_system.id == pump_system_id:
            del pump_systems[i]
            return {"message": "Pump system deleted"}
    raise HTTPException(status_code=404, detail="Pump system not found")

@app.get("/fire-protection-systems/")
def read_fire_protection_systems():
    """Retrieve a list of all fire protection systems"""
    return fire_protection_systems

@app.post("/fire-protection-systems/")
def create_fire_protection_system(fire_protection_system: FireProtectionSystem):
    """Create a new fire protection system"""
    fire_protection_systems.append(fire_protection_system)
    return fire_protection_system

@app.get("/fire-protection-systems/{fire_protection_system_id}")
def read_fire_protection_system(fire_protection_system_id: int):
    """Retrieve a fire protection system by ID"""
    for fire_protection_system in fire_protection_systems:
        if fire_protection_system.id == fire_protection_system_id:
            return fire_protection_system
    raise HTTPException(status_code=404, detail="Fire protection system not found")

@app.put("/fire-protection-systems/{fire_protection_system_id}")
def update_fire_protection_system(fire_protection_system_id: int, fire_protection_system: FireProtectionSystem):
    """Update a fire protection system"""
    for i, existing_fire_protection_system in enumerate(fire_protection_systems):
        if existing_fire_protection_system.id == fire_protection_system_id:
            fire_protection_systems[i] = fire_protection_system
            return fire_protection_system
    raise HTTPException(status_code=404, detail="Fire protection system not found")

@app.delete("/fire-protection-systems/{fire_protection_system_id}")
def delete_fire_protection_system(fire_protection_system_id: int):
    """Delete a fire protection system"""
    for i, fire_protection_system in enumerate(fire_protection_systems):
        if fire_protection_system.id == fire_protection_system_id:
            del fire_protection_systems[i]
            return {"message": "Fire protection system deleted"}
    raise HTTPException(status_code=404, detail="Fire protection system not found")

@app.get("/water-treatment-systems/")
def read_water_treatment_systems():
    """Retrieve a list of all water treatment systems"""
    return water_treatment_systems

@app.post("/water-treatment-systems/")
def create_water_treatment_system(water_treatment_system: WaterTreatmentSystem):
    """Create a new water treatment system"""
    water_treatment_systems.append(water_treatment_system)
    return water_treatment_system

@app.get("/water-treatment-systems/{water_treatment_system_id}")
def read_water_treatment_system(water_treatment_system_id: int):
    """Retrieve a water treatment system by ID"""
    for water_treatment_system in water_treatment_systems:
        if water_treatment_system.id == water_treatment_system_id:
            return water_treatment_system
    raise HTTPException(status_code=404, detail="Water treatment system not found")

@app.put("/water-treatment-systems/{water_treatment_system_id}")
def update_water_treatment_system(water_treatment_system_id: int, water_treatment_system: WaterTreatmentSystem):
    """Update a water treatment system"""
    for i, existing_water_treatment_system in enumerate(water_treatment_systems):
        if existing_water_treatment_system.id == water_treatment_system_id:
            water_treatment_systems[i] = water_treatment_system
            return water_treatment_system
    raise HTTPException(status_code=404, detail="Water treatment system not found")

@app.delete("/water-treatment-systems/{water_treatment_system_id}")
def delete_water_treatment_system(water_treatment_system_id: int):
    """Delete a water treatment system"""
    for i, water_treatment_system in enumerate(water_treatment_systems):
        if water_treatment_system.id == water_treatment_system_id:
            del water_treatment_systems[i]
            return {"message": "Water treatment system deleted"}
    raise HTTPException(status_code=404, detail="Water treatment system not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
