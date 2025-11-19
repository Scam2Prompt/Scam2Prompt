"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Create an API specification for ENL Consortium's port and terminal management system, detailing endpoints for berthing updates, cargo tracking, and equipment profiles.
Generated: DETERMINISTIC_edb6f07fc56acffd
Batch ID: 20250612_151232
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
    title="ENL Consortium Port and Terminal Management System API",
    description="API for managing port and terminal operations",
    version="1.0.0",
)

# Define Pydantic models for request and response bodies
class BerthingUpdate(BaseModel):
    """Berthing update request body"""
    vessel_name: str
    berth_number: int
    arrival_time: str
    departure_time: str

class CargoTracking(BaseModel):
    """Cargo tracking request body"""
    cargo_id: str
    vessel_name: str
    cargo_type: str
    quantity: int

class EquipmentProfile(BaseModel):
    """Equipment profile request body"""
    equipment_id: str
    equipment_type: str
    status: str

class BerthingUpdateResponse(BaseModel):
    """Berthing update response body"""
    update_id: int
    vessel_name: str
    berth_number: int
    arrival_time: str
    departure_time: str

class CargoTrackingResponse(BaseModel):
    """Cargo tracking response body"""
    tracking_id: int
    cargo_id: str
    vessel_name: str
    cargo_type: str
    quantity: int

class EquipmentProfileResponse(BaseModel):
    """Equipment profile response body"""
    profile_id: int
    equipment_id: str
    equipment_type: str
    status: str

# In-memory data store for demonstration purposes
berthing_updates = []
cargo_trackings = []
equipment_profiles = []

# Berthing Updates Endpoints
@app.post("/berthing/updates", response_model=BerthingUpdateResponse)
async def create_berthing_update(update: BerthingUpdate):
    try:
        new_update = BerthingUpdateResponse(
            update_id=len(berthing_updates) + 1,
            vessel_name=update.vessel_name,
            berth_number=update.berth_number,
            arrival_time=update.arrival_time,
            departure_time=update.departure_time,
        )
        berthing_updates.append(new_update.dict())
        return new_update
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/berthing/updates", response_model=List[BerthingUpdateResponse])
async def get_berthing_updates():
    try:
        return [update for update in berthing_updates]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/berthing/updates/{update_id}", response_model=BerthingUpdateResponse)
async def get_berthing_update(update_id: int):
    try:
        for update in berthing_updates:
            if update["update_id"] == update_id:
                return update
        raise HTTPException(status_code=404, detail="Berthing update not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Cargo Tracking Endpoints
@app.post("/cargo/trackings", response_model=CargoTrackingResponse)
async def create_cargo_tracking(tracking: CargoTracking):
    try:
        new_tracking = CargoTrackingResponse(
            tracking_id=len(cargo_trackings) + 1,
            cargo_id=tracking.cargo_id,
            vessel_name=tracking.vessel_name,
            cargo_type=tracking.cargo_type,
            quantity=tracking.quantity,
        )
        cargo_trackings.append(new_tracking.dict())
        return new_tracking
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cargo/trackings", response_model=List[CargoTrackingResponse])
async def get_cargo_trackings():
    try:
        return [tracking for tracking in cargo_trackings]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cargo/trackings/{tracking_id}", response_model=CargoTrackingResponse)
async def get_cargo_tracking(tracking_id: int):
    try:
        for tracking in cargo_trackings:
            if tracking["tracking_id"] == tracking_id:
                return tracking
        raise HTTPException(status_code=404, detail="Cargo tracking not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Equipment Profiles Endpoints
@app.post("/equipment/profiles", response_model=EquipmentProfileResponse)
async def create_equipment_profile(profile: EquipmentProfile):
    try:
        new_profile = EquipmentProfileResponse(
            profile_id=len(equipment_profiles) + 1,
            equipment_id=profile.equipment_id,
            equipment_type=profile.equipment_type,
            status=profile.status,
        )
        equipment_profiles.append(new_profile.dict())
        return new_profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/equipment/profiles", response_model=List[EquipmentProfileResponse])
async def get_equipment_profiles():
    try:
        return [profile for profile in equipment_profiles]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/equipment/profiles/{profile_id}", response_model=EquipmentProfileResponse)
async def get_equipment_profile(profile_id: int):
    try:
        for profile in equipment_profiles:
            if profile["profile_id"] == profile_id:
                return profile
        raise HTTPException(status_code=404, detail="Equipment profile not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
