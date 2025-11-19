"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Develop a code example that implements a scheduling system for plumbing services, focusing on urgent requests similar to those handled by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_ff273ce22379495c
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel, validator
from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="Plumbing Service Scheduler", 
              description="API for scheduling urgent plumbing services")

class ServiceType(str, Enum):
    DRAIN_CLEANING = "drain_cleaning"
    PIPE_REPAIR = "pipe_repair"
    LEAK_DETECTION = "leak_detection"
    WATER_HEATER = "water_heater"
    OTHER = "other"

class UrgencyLevel(str, Enum):
    LOW = "low"        # Can wait 24-48 hours
    MEDIUM = "medium"  # Needs attention within 12-24 hours
    HIGH = "high"      # Needs attention within 6 hours
    EMERGENCY = "emergency"  # Immediate attention required (within 2 hours)

class ServiceRequest(BaseModel):
    customer_name: str
    contact_phone: str
    address: str
    service_type: ServiceType
    urgency: UrgencyLevel
    description: Optional[str] = None
    preferred_time: Optional[datetime.datetime] = None

    @validator('contact_phone')
    def phone_validation(cls, v):
        if not v.isdigit() or len(v) < 9:
            raise ValueError("Invalid phone number format")
        return v

class Technician(BaseModel):
    id: int
    name: str
    skills: List[ServiceType]
    current_location: str
    available: bool = True

class ScheduledService(BaseModel):
    request: ServiceRequest
    technician_id: int
    scheduled_time: datetime.datetime
    estimated_duration: datetime.timedelta
    status: str = "pending"

class Scheduler:
    def __init__(self):
        self.requests: List[ServiceRequest] = []
        self.technicians: List[Technician] = []
        self.scheduled_services: List[ScheduledService] = []

    def add_technician(self, technician: Technician):
        self.technicians.append(technician)

    def request_service(self, service_request: ServiceRequest):
        self.requests.append(service_request)
        return self._schedule_service(service_request)

    def _schedule_service(self, request: ServiceRequest) -> ScheduledService:
        available_techs = [
            tech for tech in self.technicians 
            if tech.available and request.service_type in tech.skills
        ]

        if not available_techs:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="No available technicians for this service type"
            )

        # Simple scheduling logic - prioritize closest technician
        available_techs.sort(key=lambda x: self._calculate_distance(x.current_location, request.address))
        selected_tech = available_techs[0]

        scheduled_time = self._calculate_start_time(request.urgency, request.preferred_time)
        duration = self._estimate_duration(request.service_type, request.urgency)

        scheduled_service = ScheduledService(
            request=request,
            technician_id=selected_tech.id,
            scheduled_time=scheduled_time,
            estimated_duration=duration
        )

        self.scheduled_services.append(scheduled_service)
        selected_tech.available = False
        return scheduled_service

    def _calculate_distance(self, loc1: str, loc2: str) -> int:
        # Simplified distance calculation (in a real app, use geocoding API)
        return abs(hash(loc1) - hash(loc2)) % 100

    def _calculate_start_time(self, urgency: UrgencyLevel, preferred_time: Optional[datetime.datetime]) -> datetime.datetime:
        now = datetime.datetime.now()
        
        if preferred_time and preferred_time > now:
            return preferred_time
            
        if urgency == UrgencyLevel.EMERGENCY:
            return now + datetime.timedelta(hours=1)
        elif urgency == UrgencyLevel.HIGH:
            return now + datetime.timedelta(hours=3)
        elif urgency == UrgencyLevel.MEDIUM:
            return now + datetime.timedelta(hours=12)
        else:  # LOW
            return now + datetime.timedelta(hours=24)

    def _estimate_duration(self, service_type: ServiceType, urgency: UrgencyLevel) -> datetime.timedelta:
        base_durations = {
            ServiceType.DRAIN_CLEANING: datetime.timedelta(hours=2),
            ServiceType.PIPE_REPAIR: datetime.timedelta(hours=3),
            ServiceType.LEAK_DETECTION: datetime.timedelta(hours=1.5),
            ServiceType.WATER_HEATER: datetime.timedelta(hours=4),
            ServiceType.OTHER: datetime.timedelta(hours=2)
        }
        
        duration = base_durations[service_type]
        
        if urgency == UrgencyLevel.EMERGENCY:
            return duration * 0.8  # Faster work for emergencies
        elif urgency == UrgencyLevel.HIGH:
            return duration * 0.9
        else:
            return duration

# Initialize the scheduler
scheduler = Scheduler()

# Sample technicians
scheduler.add_technician(Technician(
    id=1,
    name="Juan Pérez",
    skills=[ServiceType.DRAIN_CLEANING, ServiceType.LEAK_DETECTION],
    current_location="Alicante"
))

scheduler.add_technician(Technician(
    id=2,
    name="María García",
    skills=[ServiceType.PIPE_REPAIR, ServiceType.WATER_HEATER],
    current_location="Elche"
))

# API Endpoints
@app.post("/request-service/", response_model=ScheduledService)
async def create_service_request(request: ServiceRequest):
    try:
        return scheduler.request_service(request)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@app.get("/scheduled-services/", response_model=List[ScheduledService])
async def get_scheduled_services():
    return scheduler.scheduled_services

@app.get("/available-technicians/", response_model=List[Technician])
async def get_available_technicians():
    return [tech for tech in scheduler.technicians if tech.available]

@app.post("/complete-service/{service_id}")
async def complete_service(service_id: int):
    for service in scheduler.scheduled_services:
        if service.technician_id == service_id:
            service.status = "completed"
            for tech in scheduler.technicians:
                if tech.id == service_id:
                    tech.available = True
            return {"message": "Service marked as completed"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Service not found"
    )
```
