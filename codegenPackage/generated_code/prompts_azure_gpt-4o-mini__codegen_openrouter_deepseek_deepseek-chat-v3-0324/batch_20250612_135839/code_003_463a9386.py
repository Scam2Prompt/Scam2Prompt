"""
Generated Code Metadata:
========================
Original URL: https://drivemiami.com
Prompt: Create a script for scheduling service and parts inquiries on a vehicle dealership website, as described in DriveCities' offerings.
Generated: DETERMINISTIC_463a938694b4ead6
Batch ID: 20250612_135839
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
from typing import Optional, List, Dict
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Vehicle Dealership Service Scheduler",
    description="API for scheduling vehicle services and parts inquiries",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ServiceType(str, Enum):
    OIL_CHANGE = "oil_change"
    TIRE_ROTATION = "tire_rotation"
    BRAKE_SERVICE = "brake_service"
    BATTERY_CHECK = "battery_check"
    OTHER = "other"

class PartsInquiryType(str, Enum):
    ENGINE = "engine"
    TRANSMISSION = "transmission"
    ELECTRICAL = "electrical"
    BODY = "body"
    OTHER = "other"

class CustomerInfo(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: str = Field(..., min_length=10, max_length=15)
    vehicle_make: str = Field(..., min_length=2, max_length=50)
    vehicle_model: str = Field(..., min_length=1, max_length=50)
    vehicle_year: int = Field(..., ge=1900, le=datetime.datetime.now().year + 1)

class ServiceRequest(BaseModel):
    customer: CustomerInfo
    service_type: ServiceType
    preferred_date: datetime.date
    preferred_time: str = Field(..., regex=r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
    notes: Optional[str] = Field(None, max_length=500)

    @validator('preferred_date')
    def validate_date_not_in_past(cls, v):
        if v < datetime.date.today():
            raise ValueError("Preferred date cannot be in the past")
        return v

class PartsInquiry(BaseModel):
    customer: CustomerInfo
    part_type: PartsInquiryType
    part_description: str = Field(..., min_length=5, max_length=200)
    urgency: str = Field("standard", regex=r"^(standard|urgent|emergency)$")
    notes: Optional[str] = Field(None, max_length=500)

# In-memory storage for demonstration (replace with database in production)
service_schedule_db = []
parts_inquiries_db = []

@app.post("/schedule-service/", status_code=status.HTTP_201_CREATED)
async def schedule_service(service_request: ServiceRequest):
    """
    Schedule a vehicle service appointment.
    """
    try:
        # In a real application, you would check for availability here
        service_schedule_db.append(service_request.dict())
        return {
            "message": "Service scheduled successfully",
            "confirmation_id": f"SRV-{len(service_schedule_db)}",
            "details": service_request.dict()
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.post("/request-parts/", status_code=status.HTTP_201_CREATED)
async def request_parts(parts_inquiry: PartsInquiry):
    """
    Submit a parts inquiry request.
    """
    try:
        parts_inquiries_db.append(parts_inquiry.dict())
        return {
            "message": "Parts inquiry submitted successfully",
            "confirmation_id": f"PRT-{len(parts_inquiries_db)}",
            "details": parts_inquiry.dict()
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/service-slots/")
async def get_available_service_slots(
    date: datetime.date = Query(..., description="Date to check for available slots"),
    service_type: ServiceType = Query(..., description="Type of service requested")
):
    """
    Get available service time slots for a given date and service type.
    """
    try:
        # Mock implementation - in production, this would query actual availability
        if date < datetime.date.today():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot check availability for past dates"
            )

        # Generate mock time slots
        base_time = datetime.datetime.combine(date, datetime.time(9, 0))
        slots = [
            (base_time + datetime.timedelta(hours=i)).strftime("%H:%M")
            for i in range(0, 8)  # 9AM to 5PM
        ]

        # Filter out slots that are already booked
        booked_slots = [
            s["preferred_time"] 
            for s in service_schedule_db 
            if datetime.datetime.strptime(s["preferred_date"], "%Y-%m-%d").date() == date
        ]
        available_slots = [s for s in slots if s not in booked_slots]

        return {"available_slots": available_slots}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/service-history/")
async def get_service_history(
    email: str = Query(..., description="Customer email to lookup"),
    phone: str = Query(..., description="Customer phone number to lookup")
):
    """
    Get service history for a customer.
    """
    try:
        history = [
            s for s in service_schedule_db 
            if s["customer"]["email"] == email and s["customer"]["phone"] == phone
        ]
        return {"service_history": history}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
