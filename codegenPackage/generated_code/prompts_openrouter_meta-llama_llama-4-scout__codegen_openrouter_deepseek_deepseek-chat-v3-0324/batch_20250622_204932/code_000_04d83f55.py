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
# pump_system_api.py
# API for managing industrial pump systems with fire protection and water treatment features
# Compliant with ISO 9001 standards

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
import uuid
import datetime

app = FastAPI(
    title="Industrial Pump System API",
    description="API for managing industrial pump systems with fire protection and water treatment features",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@pumpsystems.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database simulation (in production, use a proper database)
pump_systems_db = {}

class PumpType(str, Enum):
    FIRE_PROTECTION = "fire_protection"
    WATER_TREATMENT = "water_treatment"
    GENERAL_INDUSTRIAL = "general_industrial"

class MaintenanceStatus(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    OVERDUE = "overdue"

class PumpSystem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str = Field(..., min_length=1, max_length=100)
    type: PumpType
    location: str
    installation_date: datetime.date
    last_maintenance_date: Optional[datetime.date] = None
    next_maintenance_date: Optional[datetime.date] = None
    maintenance_status: MaintenanceStatus = MaintenanceStatus.SCHEDULED
    is_active: bool = True
    flow_rate: float = Field(..., gt=0, description="Flow rate in liters per minute")
    pressure: float = Field(..., gt=0, description="Pressure in bar")
    certification: str = Field(..., min_length=1, max_length=50, description="ISO 9001 certification number")
    
    @validator('next_maintenance_date')
    def validate_next_maintenance_date(cls, v, values):
        if v and 'installation_date' in values and v < values['installation_date']:
            raise ValueError("Next maintenance date cannot be before installation date")
        return v

class PumpSystemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    location: Optional[str] = None
    last_maintenance_date: Optional[datetime.date] = None
    next_maintenance_date: Optional[datetime.date] = None
    maintenance_status: Optional[MaintenanceStatus] = None
    is_active: Optional[bool] = None
    flow_rate: Optional[float] = Field(None, gt=0)
    pressure: Optional[float] = Field(None, gt=0)

class MaintenanceLog(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    pump_system_id: str
    maintenance_date: datetime.date
    technician: str
    description: str
    parts_replaced: Optional[List[str]] = None
    certification_verified: bool = Field(..., description="ISO 9001 certification verification status")

@app.post("/pump-systems/", response_model=PumpSystem, status_code=status.HTTP_201_CREATED)
async def create_pump_system(pump_system: PumpSystem):
    """Create a new pump system with ISO 9001 certification"""
    if pump_system.id in pump_systems_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Pump system with this ID already exists"
        )
    pump_systems_db[pump_system.id] = pump_system
    return pump_system

@app.get("/pump-systems/", response_model=List[PumpSystem])
async def get_all_pump_systems(active_only: bool = True):
    """Get all pump systems, optionally filtered by active status"""
    systems = list(pump_systems_db.values())
    if active_only:
        systems = [s for s in systems if s.is_active]
    return systems

@app.get("/pump-systems/{pump_system_id}", response_model=PumpSystem)
async def get_pump_system(pump_system_id: str):
    """Get a specific pump system by ID"""
    if pump_system_id not in pump_systems_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pump system not found"
        )
    return pump_systems_db[pump_system_id]

@app.put("/pump-systems/{pump_system_id}", response_model=PumpSystem)
async def update_pump_system(pump_system_id: str, update_data: PumpSystemUpdate):
    """Update a pump system's information"""
    if pump_system_id not in pump_systems_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pump system not found"
        )
    
    pump_system = pump_systems_db[pump_system_id]
    update_dict = update_data.dict(exclude_unset=True)
    
    for field, value in update_dict.items():
        setattr(pump_system, field, value)
    
    return pump_system

@app.delete("/pump-systems/{pump_system_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pump_system(pump_system_id: str):
    """Deactivate a pump system (soft delete)"""
    if pump_system_id not in pump_systems_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pump system not found"
        )
    pump_systems_db[pump_system_id].is_active = False
    return None

@app.post("/maintenance/", response_model=MaintenanceLog, status_code=status.HTTP_201_CREATED)
async def log_maintenance(maintenance_log: MaintenanceLog):
    """Log maintenance activity for a pump system"""
    if maintenance_log.pump_system_id not in pump_systems_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pump system not found"
        )
    
    # In a real system, we would store this in a maintenance log database
    # For this example, we'll just update the pump system's maintenance dates
    pump_system = pump_systems_db[maintenance_log.pump_system_id]
    pump_system.last_maintenance_date = maintenance_log.maintenance_date
    
    return maintenance_log

@app.get("/pump-systems/type/{pump_type}", response_model=List[PumpSystem])
async def get_pump_systems_by_type(pump_type: PumpType, active_only: bool = True):
    """Get all pump systems of a specific type"""
    systems = [s for s in pump_systems_db.values() if s.type == pump_type]
    if active_only:
        systems = [s for s in systems if s.is_active]
    return systems

@app.get("/pump-systems/maintenance/overdue", response_model=List[PumpSystem])
async def get_overdue_maintenance_systems():
    """Get all pump systems with overdue maintenance"""
    today = datetime.date.today()
    systems = [
        s for s in pump_systems_db.values() 
        if s.next_maintenance_date and s.next_maintenance_date < today and s.is_active
    ]
    return systems
```
