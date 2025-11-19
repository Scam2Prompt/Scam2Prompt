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
"""
Industrial Pump API for Building Management Systems (BMS) Integration
This API provides endpoints for monitoring and controlling industrial pumps
in refrigeration and HVAC systems.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
import uuid

app = FastAPI(
    title="Industrial Pump BMS Integration API",
    description="RESTful API for integrating industrial pumps with BMS",
    version="1.0.0"
)

# Mock database
pumps_db = {}

# Models
class Pump(BaseModel):
    id: str
    name: str
    status: str  # "running", "stopped", "error"
    speed: Optional[int] = None  # RPM
    pressure: Optional[float] = None  # psi
    temperature: Optional[float] = None  # °C
    power_consumption: Optional[float] = None  # kW
    bms_id: Optional[str] = None  # Linked BMS ID

class PumpCreate(BaseModel):
    name: str
    bms_id: Optional[str] = None

class PumpUpdate(BaseModel):
    name: Optional[str] = None
    speed: Optional[int] = None
    status: Optional[str] = None
    bms_id: Optional[str] = None

# Helper functions
def get_pump_or_404(pump_id: str):
    pump = pumps_db.get(pump_id)
    if not pump:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pump not found"
        )
    return pump

# Endpoints
@app.post("/pumps/", response_model=Pump, status_code=status.HTTP_201_CREATED)
def create_pump(pump: PumpCreate):
    """Create a new pump in the system"""
    pump_id = str(uuid.uuid4())
    new_pump = Pump(
        id=pump_id,
        name=pump.name,
        status="stopped",
        bms_id=pump.bms_id
    )
    pumps_db[pump_id] = new_pump
    return new_pump

@app.get("/pumps/", response_model=List[Pump])
def list_pumps():
    """List all pumps in the system"""
    return list(pumps_db.values())

@app.get("/pumps/{pump_id}", response_model=Pump)
def get_pump(pump_id: str):
    """Get details of a specific pump"""
    return get_pump_or_404(pump_id)

@app.put("/pumps/{pump_id}", response_model=Pump)
def update_pump(pump_id: str, pump_update: PumpUpdate):
    """Update pump parameters"""
    pump = get_pump_or_404(pump_id)
    
    update_data = pump_update.dict(exclude_unset=True)
    updated_pump = pump.copy(update=update_data)
    pumps_db[pump_id] = updated_pump
    
    return updated_pump

@app.post("/pumps/{pump_id}/start", response_model=Pump)
def start_pump(pump_id: str):
    """Start a stopped pump"""
    pump = get_pump_or_404(pump_id)
    if pump.status == "running":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pump is already running"
        )
    
    updated_pump = pump.copy(update={"status": "running"})
    pumps_db[pump_id] = updated_pump
    return updated_pump

@app.post("/pumps/{pump_id}/stop", response_model=Pump)
def stop_pump(pump_id: str):
    """Stop a running pump"""
    pump = get_pump_or_404(pump_id)
    if pump.status == "stopped":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pump is already stopped"
        )
    
    updated_pump = pump.copy(update={"status": "stopped"})
    pumps_db[pump_id] = updated_pump
    return updated_pump

@app.get("/bms/{bms_id}/pumps", response_model=List[Pump])
def get_pumps_by_bms(bms_id: str):
    """Get all pumps associated with a BMS"""
    return [pump for pump in pumps_db.values() if pump.bms_id == bms_id]

@app.get("/pumps/{pump_id}/metrics")
def get_pump_metrics(pump_id: str):
    """Get operational metrics for a pump"""
    pump = get_pump_or_404(pump_id)
    return {
        "speed": pump.speed,
        "pressure": pump.pressure,
        "temperature": pump.temperature,
        "power_consumption": pump.power_consumption
    }

@app.post("/pumps/{pump_id}/emergency-stop", response_model=Pump)
def emergency_stop(pump_id: str):
    """Immediately stop pump in emergency situations"""
    pump = get_pump_or_404(pump_id)
    updated_pump = pump.copy(update={"status": "stopped", "speed": 0})
    pumps_db[pump_id] = updated_pump
    return updated_pump

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
```
