"""
Generated Code Metadata:
========================
Original URL: https://wonderwallmuseum.com
Prompt: Suggest an API for managing website maintenance notifications and updates, referencing the approach taken by the WonderWall Museum.
Generated: DETERMINISTIC_149578ccdac84cd6
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from enum import Enum
import uuid

app = FastAPI(
    title="Website Maintenance API",
    description="API for managing website maintenance notifications and updates",
    version="1.0.0"
)

class MaintenanceStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class MaintenanceUpdate(BaseModel):
    id: str
    title: str
    description: str
    status: MaintenanceStatus
    start_time: datetime
    end_time: datetime
    created_at: datetime
    updated_at: datetime

class CreateMaintenanceRequest(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime

class UpdateMaintenanceRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[MaintenanceStatus] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

# In-memory database simulation
maintenance_updates_db = []

@app.post("/maintenance", response_model=MaintenanceUpdate, status_code=status.HTTP_201_CREATED)
def create_maintenance_update(request: CreateMaintenanceRequest):
    """Create a new maintenance notification"""
    if request.start_time >= request.end_time:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="End time must be after start time"
        )

    maintenance_id = str(uuid.uuid4())
    now = datetime.now()
    
    maintenance_update = MaintenanceUpdate(
        id=maintenance_id,
        title=request.title,
        description=request.description,
        status=MaintenanceStatus.SCHEDULED,
        start_time=request.start_time,
        end_time=request.end_time,
        created_at=now,
        updated_at=now
    )
    
    maintenance_updates_db.append(maintenance_update)
    return maintenance_update

@app.get("/maintenance", response_model=List[MaintenanceUpdate])
def get_maintenance_updates(status: Optional[MaintenanceStatus] = None):
    """Get all maintenance updates, optionally filtered by status"""
    if status:
        return [update for update in maintenance_updates_db if update.status == status]
    return maintenance_updates_db

@app.get("/maintenance/{maintenance_id}", response_model=MaintenanceUpdate)
def get_maintenance_update(maintenance_id: str):
    """Get a specific maintenance update by ID"""
    for update in maintenance_updates_db:
        if update.id == maintenance_id:
            return update
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Maintenance update not found"
    )

@app.put("/maintenance/{maintenance_id}", response_model=MaintenanceUpdate)
def update_maintenance_update(maintenance_id: str, request: UpdateMaintenanceRequest):
    """Update an existing maintenance notification"""
    for index, update in enumerate(maintenance_updates_db):
        if update.id == maintenance_id:
            updated_data = request.dict(exclude_unset=True)
            
            if 'start_time' in updated_data and 'end_time' in updated_data:
                if updated_data['start_time'] >= updated_data['end_time']:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="End time must be after start time"
                    )
            
            for field, value in updated_data.items():
                setattr(maintenance_updates_db[index], field, value)
            
            maintenance_updates_db[index].updated_at = datetime.now()
            return maintenance_updates_db[index]
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Maintenance update not found"
    )

@app.delete("/maintenance/{maintenance_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_maintenance_update(maintenance_id: str):
    """Delete a maintenance notification"""
    for index, update in enumerate(maintenance_updates_db):
        if update.id == maintenance_id:
            maintenance_updates_db.pop(index)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Maintenance update not found"
    )

@app.get("/maintenance/current", response_model=List[MaintenanceUpdate])
def get_current_maintenance_updates():
    """Get all maintenance updates that are currently in progress"""
    now = datetime.now()
    return [
        update for update in maintenance_updates_db
        if update.status == MaintenanceStatus.IN_PROGRESS
        and update.start_time <= now <= update.end_time
    ]
```
