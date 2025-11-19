"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Generate a code snippet for an API that schedules HVAC service appointments, incorporating features like 24/7 availability and priority service for Comfort Club members as described on RJW Mechanical's website.
Generated: DETERMINISTIC_e7a68e98573148b9
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
import logging
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, validator

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="RJW Mechanical HVAC Service API",
    description="API for scheduling HVAC service appointments with 24/7 availability and priority for Comfort Club members",
    version="1.0.0"
)


class ServiceType(str, Enum):
    MAINTENANCE = "maintenance"
    REPAIR = "repair"
    INSTALLATION = "installation"
    EMERGENCY = "emergency"


class CustomerStatus(str, Enum):
    REGULAR = "regular"
    COMFORT_CLUB = "comfort_club"


class AppointmentRequest(BaseModel):
    customer_id: str
    customer_name: str
    customer_status: CustomerStatus
    service_type: ServiceType
    preferred_date: str
    preferred_time: str
    contact_number: str
    description: Optional[str] = None

    @validator('preferred_date')
    def validate_date_format(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
            return v
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    @validator('preferred_time')
    def validate_time_format(cls, v):
        try:
            datetime.strptime(v, "%H:%M")
            return v
        except ValueError:
            raise ValueError("Incorrect time format, should be HH:MM")


class AppointmentResponse(BaseModel):
    appointment_id: str
    customer_id: str
    scheduled_time: str
    estimated_duration: str
    technician_notes: Optional[str] = None
    priority: bool


# Mock database
appointments_db: Dict[str, Dict[str, Any]] = {}


def generate_appointment_id() -> str:
    return f"RJWHVAC-{datetime.now().strftime('%Y%m%d%H%M%S')}"


def calculate_priority(customer_status: CustomerStatus, service_type: ServiceType) -> bool:
    return customer_status == CustomerStatus.COMFORT_CLUB or service_type == ServiceType.EMERGENCY


def calculate_estimated_duration(service_type: ServiceType) -> str:
    durations = {
        ServiceType.MAINTENANCE: "1 hour",
        ServiceType.REPAIR: "2 hours",
        ServiceType.INSTALLATION: "4 hours",
        ServiceType.EMERGENCY: "1.5 hours"
    }
    return durations.get(service_type, "1 hour")


@app.post("/appointments", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
async def schedule_appointment(request: AppointmentRequest):
    """
    Schedule a new HVAC service appointment.
    Comfort Club members and emergency services get priority scheduling.
    """
    try:
        # Parse datetime
        preferred_datetime = datetime.strptime(
            f"{request.preferred_date} {request.preferred_time}",
            "%Y-%m-%d %H:%M"
        )

        # Check if appointment is in the future
        if preferred_datetime < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Appointment time must be in the future"
            )

        # Generate appointment details
        appointment_id = generate_appointment_id()
        priority = calculate_priority(request.customer_status, request.service_type)
        estimated_duration = calculate_estimated_duration(request.service_type)

        # For demo purposes, we're just adding 1 hour for priority appointments
        if priority:
            scheduled_time = datetime.now() + timedelta(hours=1)
        else:
            scheduled_time = preferred_datetime

        # Create appointment record
        appointment = {
            "appointment_id": appointment_id,
            "customer_id": request.customer_id,
            "scheduled_time": scheduled_time.isoformat(),
            "estimated_duration": estimated_duration,
            "priority": priority,
            "customer_details": request.dict()
        }

        # Store in mock DB
        appointments_db[appointment_id] = appointment

        logger.info(f"Created appointment {appointment_id} for customer {request.customer_id}")

        return {
            "appointment_id": appointment_id,
            "customer_id": request.customer_id,
            "scheduled_time": scheduled_time.isoformat(),
            "estimated_duration": estimated_duration,
            "priority": priority
        }

    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )


@app.get("/appointments/{appointment_id}", response_model=AppointmentResponse)
async def get_appointment(appointment_id: str):
    """Retrieve details of a scheduled appointment"""
    if appointment_id not in appointments_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    return appointments_db[appointment_id]


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
```
