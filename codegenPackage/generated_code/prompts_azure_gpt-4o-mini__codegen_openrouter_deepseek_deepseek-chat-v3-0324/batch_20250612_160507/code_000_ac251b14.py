"""
Generated Code Metadata:
========================
Original URL: https://aavego.dk
Prompt: Generate a code snippet for a booking system that integrates with a holiday architecture site like House Aavego in Thy, Denmark, focusing on unique features like private courtyards.
Generated: DETERMINISTIC_ac251b14c55d8de7
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, List, Dict
from enum import Enum
from pydantic import BaseModel, validator, Field
from fastapi import FastAPI, HTTPException, status, Query
from fastapi.responses import JSONResponse

app = FastAPI(
    title="House Aavego Booking System",
    description="API for booking unique holiday homes with private courtyards in Thy, Denmark",
    version="1.0.0"
)

class PropertyType(str, Enum):
    COTTAGE = "cottage"
    VILLA = "villa"
    FARMHOUSE = "farmhouse"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class PropertyFeature(str, Enum):
    PRIVATE_COURTYARD = "private_courtyard"
    SEA_VIEW = "sea_view"
    FIREPLACE = "fireplace"

class Property(BaseModel):
    id: str
    name: str
    description: str
    property_type: PropertyType
    capacity: int
    features: List[PropertyFeature]
    courtyard_size: Optional[float] = Field(None, description="Size of private courtyard in square meters")
    base_price: float
    images: List[str]

    @validator('courtyard_size')
    def validate_courtyard_size(cls, v, values):
        if PropertyFeature.PRIVATE_COURTYARD in values.get('features', []) and v is None:
            raise ValueError("Courtyard size must be specified for properties with private courtyards")
        return v

class BookingRequest(BaseModel):
    property_id: str
    guest_name: str
    guest_email: str
    check_in: datetime.date
    check_out: datetime.date
    guests: int
    special_requests: Optional[str] = None

    @validator('check_out')
    def validate_dates(cls, v, values):
        if 'check_in' in values and v <= values['check_in']:
            raise ValueError("Check-out date must be after check-in date")
        return v

class BookingResponse(BaseModel):
    booking_id: str
    property_id: str
    status: BookingStatus
    total_price: float
    confirmation_date: datetime.datetime
    courtyard_access: bool

# Mock database
properties_db = {
    "prop1": Property(
        id="prop1",
        name="Seaside Cottage",
        description="Charming cottage with private courtyard",
        property_type=PropertyType.COTTAGE,
        capacity=4,
        features=[PropertyFeature.PRIVATE_COURTYARD, PropertyFeature.SEA_VIEW],
        courtyard_size=120.5,
        base_price=1500.0,
        images=["img1.jpg", "img2.jpg"]
    ),
    "prop2": Property(
        id="prop2",
        name="Farmhouse Retreat",
        description="Spacious farmhouse with large courtyard",
        property_type=PropertyType.FARMHOUSE,
        capacity=8,
        features=[PropertyFeature.PRIVATE_COURTYARD, PropertyFeature.FIREPLACE],
        courtyard_size=200.0,
        base_price=2500.0,
        images=["img3.jpg", "img4.jpg"]
    )
}

bookings_db = {}

@app.get("/properties", response_model=List[Property])
async def get_properties(
    courtyard: Optional[bool] = Query(None, description="Filter by private courtyard availability"),
    property_type: Optional[PropertyType] = None
):
    """Get all available properties with optional filters"""
    filtered_props = list(properties_db.values())
    
    if courtyard is not None:
        filtered_props = [
            p for p in filtered_props 
            if (PropertyFeature.PRIVATE_COURTYARD in p.features) == courtyard
        ]
    
    if property_type is not None:
        filtered_props = [p for p in filtered_props if p.property_type == property_type]
    
    return filtered_props

@app.get("/properties/{property_id}", response_model=Property)
async def get_property(property_id: str):
    """Get details of a specific property"""
    if property_id not in properties_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found"
        )
    return properties_db[property_id]

@app.post("/bookings", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(booking_request: BookingRequest):
    """Create a new booking"""
    if booking_request.property_id not in properties_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found"
        )
    
    property = properties_db[booking_request.property_id]
    
    if booking_request.guests > property.capacity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Property can only accommodate {property.capacity} guests"
        )
    
    # Check for date conflicts (simplified for demo)
    for booking in bookings_db.values():
        if (booking.property_id == booking_request.property_id and
            not (booking_request.check_out <= booking.check_in or 
                 booking_request.check_in >= booking.check_out)):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Property already booked for selected dates"
            )
    
    # Calculate price (simplified for demo)
    nights = (booking_request.check_out - booking_request.check_in).days
    total_price = nights * property.base_price
    
    # Create booking
    booking_id = f"book_{len(bookings_db) + 1}"
    courtyard_access = PropertyFeature.PRIVATE_COURTYARD in property.features
    
    booking = BookingResponse(
        booking_id=booking_id,
        property_id=booking_request.property_id,
        status=BookingStatus.CONFIRMED,
        total_price=total_price,
        confirmation_date=datetime.datetime.now(),
        courtyard_access=courtyard_access
    )
    
    bookings_db[booking_id] = booking
    
    return booking

@app.get("/bookings/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: str):
    """Get details of a specific booking"""
    if booking_id not in bookings_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return bookings_db[booking_id]

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)}
    )
```
