"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: How can I implement a home maintenance scheduling system using an API that tracks services like pest control and furniture moving, as described on the website?
Generated: DETERMINISTIC_4b24e85e3d6659c1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import uuid
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI(
    title="Home Maintenance Scheduler API",
    description="API for scheduling and tracking home maintenance services",
    version="1.0.0"
)

class ServiceType(str, Enum):
    PEST_CONTROL = "pest_control"
    FURNITURE_MOVING = "furniture_moving"
    CLEANING = "cleaning"
    LANDSCAPING = "landscaping"
    PLUMBING = "plumbing"
    ELECTRICAL = "electrical"

class ServiceStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Service(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    type: ServiceType
    scheduled_date: datetime
    status: ServiceStatus = ServiceStatus.SCHEDULED
    provider: str
    notes: Optional[str] = None
    duration_hours: float = Field(..., gt=0, description="Duration of service in hours")
    recurring: bool = False
    recurrence_interval_days: Optional[int] = Field(None, ge=1)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Quarterly Pest Control",
                "type": "pest_control",
                "scheduled_date": "2023-12-15T09:00:00",
                "provider": "Acme Pest Control",
                "notes": "Focus on basement area",
                "duration_hours": 2.5,
                "recurring": True,
                "recurrence_interval_days": 90
            }
        }

# In-memory database for demonstration
services_db: Dict[str, Service] = {}

@app.post("/services/", response_model=Service, status_code=status.HTTP_201_CREATED)
def create_service(service: Service) -> Service:
    """Create a new maintenance service."""
    if service.id in services_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Service with this ID already exists"
        )
    
    services_db[service.id] = service
    return service

@app.get("/services/", response_model=List[Service])
def list_services(
    type: Optional[ServiceType] = None,
    status: Optional[ServiceStatus] = None,
    upcoming: bool = False
) -> List[Service]:
    """List all services with optional filtering."""
    result = list(services_db.values())
    
    if type:
        result = [s for s in result if s.type == type]
    
    if status:
        result = [s for s in result if s.status == status]
    
    if upcoming:
        now = datetime.now()
        result = [s for s in result if s.scheduled_date >= now]
    
    return sorted(result, key=lambda s: s.scheduled_date)

@app.get("/services/{service_id}", response_model=Service)
def get_service(service_id: str) -> Service:
    """Get a specific service by ID."""
    if service_id not in services_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    return services_db[service_id]

@app.put("/services/{service_id}", response_model=Service)
def update_service(service_id: str, updated_service: Service) -> Service:
    """Update an existing service."""
    if service_id not in services_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    
    if service_id != updated_service.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Service ID mismatch"
        )
    
    services_db[service_id] = updated_service
    return updated_service

@app.patch("/services/{service_id}/status", response_model=Service)
def update_service_status(service_id: str, new_status: ServiceStatus) -> Service:
    """Update the status of a service."""
    if service_id not in services_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    
    service = services_db[service_id]
    service.status = new_status
    return service

@app.delete("/services/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(service_id: str) -> None:
    """Delete a service."""
    if service_id not in services_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )
    
    del services_db[service_id]

@app.get("/services/upcoming/recurring", response_model=List[Service])
def get_upcoming_recurring_services(days_ahead: int = 30) -> List[Service]:
    """Get upcoming recurring services within the specified days ahead."""
    now = datetime.now()
    end_date = now + timedelta(days=days_ahead)
    
    result = []
    for service in services_db.values():
        if not service.recurring:
            continue
        
        next_date = service.scheduled_date
        while next_date <= end_date:
            if next_date >= now:
                recurring_service = service.copy()
                recurring_service.scheduled_date = next_date
                result.append(recurring_service)
            
            if not service.recurrence_interval_days:
                break
            next_date += timedelta(days=service.recurrence_interval_days)
    
    return sorted(result, key=lambda s: s.scheduled_date)
```
