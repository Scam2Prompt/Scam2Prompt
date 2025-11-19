"""
Generated Code Metadata:
========================
Original URL: https://michelledoylegoldsmith.com
Prompt: Create an API endpoint for a jewelry shop that allows customers to inquire about bespoke designs and schedule appointments with a goldsmith.
Generated: DETERMINISTIC_75e2bbaa99525dfb
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime, date
from typing import Optional
from enum import Enum
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Jewelry Shop Bespoke Design API",
    description="API for customers to inquire about bespoke jewelry designs and schedule appointments with goldsmiths",
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

# Database simulation
class DesignInquiryDB:
    def __init__(self):
        self.inquiries = {}
        self.appointments = {}

db = DesignInquiryDB()

# Enums and Models
class JewelryType(str, Enum):
    RING = "ring"
    NECKLACE = "necklace"
    BRACELET = "bracelet"
    EARRINGS = "earrings"
    OTHER = "other"

class MetalType(str, Enum):
    GOLD = "gold"
    SILVER = "silver"
    PLATINUM = "platinum"
    PALLADIUM = "palladium"
    OTHER = "other"

class DesignInquiry(BaseModel):
    customer_name: str
    email: EmailStr
    phone: str
    jewelry_type: JewelryType
    metal_type: MetalType
    budget: float
    description: str
    reference_images: Optional[list[str]] = None
    desired_completion_date: Optional[date] = None

    @validator('budget')
    def budget_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Budget must be positive')
        return v

    @validator('phone')
    def phone_validation(cls, v):
        if not v.replace(" ", "").replace("-", "").isdigit():
            raise ValueError('Phone number must contain only digits, spaces or hyphens')
        return v

class Appointment(BaseModel):
    customer_name: str
    email: EmailStr
    phone: str
    preferred_date: date
    preferred_time: str
    notes: Optional[str] = None

    @validator('preferred_time')
    def time_format(cls, v):
        try:
            datetime.strptime(v, "%H:%M")
        except ValueError:
            raise ValueError('Time must be in HH:MM format')
        return v

class InquiryResponse(BaseModel):
    inquiry_id: str
    message: str
    estimated_response_time: str

class AppointmentResponse(BaseModel):
    appointment_id: str
    message: str
    confirmation_details: str

# Endpoints
@app.post("/inquiries/", response_model=InquiryResponse, status_code=status.HTTP_201_CREATED)
async def create_design_inquiry(inquiry: DesignInquiry):
    """
    Create a new bespoke jewelry design inquiry.
    
    Parameters:
    - inquiry: DesignInquiry object containing customer details and design requirements
    
    Returns:
    - InquiryResponse with inquiry ID and confirmation message
    """
    inquiry_id = str(uuid.uuid4())
    db.inquiries[inquiry_id] = inquiry.dict()
    
    return InquiryResponse(
        inquiry_id=inquiry_id,
        message="Your design inquiry has been received. A goldsmith will contact you within 2 business days.",
        estimated_response_time="2 business days"
    )

@app.post("/appointments/", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
async def schedule_appointment(appointment: Appointment):
    """
    Schedule an appointment with a goldsmith.
    
    Parameters:
    - appointment: Appointment object containing customer details and preferred time
    
    Returns:
    - AppointmentResponse with appointment ID and confirmation message
    """
    appointment_id = str(uuid.uuid4())
    db.appointments[appointment_id] = appointment.dict()
    
    return AppointmentResponse(
        appointment_id=appointment_id,
        message="Your appointment request has been received. You will receive a confirmation email shortly.",
        confirmation_details=f"Appointment requested for {appointment.preferred_date} at {appointment.preferred_time}"
    )

@app.get("/inquiries/{inquiry_id}", response_model=DesignInquiry)
async def get_inquiry(inquiry_id: str):
    """
    Retrieve a specific design inquiry by ID.
    
    Parameters:
    - inquiry_id: UUID of the inquiry to retrieve
    
    Returns:
    - DesignInquiry object if found
    
    Raises:
    - HTTPException 404 if inquiry not found
    """
    if inquiry_id not in db.inquiries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inquiry not found"
        )
    return db.inquiries[inquiry_id]

@app.get("/appointments/{appointment_id}", response_model=Appointment)
async def get_appointment(appointment_id: str):
    """
    Retrieve a specific appointment by ID.
    
    Parameters:
    - appointment_id: UUID of the appointment to retrieve
    
    Returns:
    - Appointment object if found
    
    Raises:
    - HTTPException 404 if appointment not found
    """
    if appointment_id not in db.appointments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    return db.appointments[appointment_id]

# Health check endpoint
@app.get("/health")
async def health_check():
    """Endpoint to check API health status"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}
```
