"""
Generated Code Metadata:
========================
Original URL: https://spedition-steinhuebl.de
Prompt: Develop a RESTful API endpoint that allows users to schedule package pickups with a logistics provider, inspired by the services of Spedition Steinhübl.
Generated: DETERMINISTIC_548ed6ef152457b1
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field, validator
from datetime import datetime, time
from typing import Optional
from uuid import uuid4
import logging
from fastapi.security import OAuth2PasswordBearer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Package Pickup Scheduling API",
    description="API for scheduling package pickups with logistics providers",
    version="1.0.0"
)

# Mock database
pickups_db = {}
users_db = {
    "testuser": {
        "username": "testuser",
        "password": "testpass",  # In production, use hashed passwords
        "disabled": False
    }
}

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    disabled: Optional[bool] = None

class UserInDB(User):
    password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(users_db, token)
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Models
class Address(BaseModel):
    street: str = Field(..., example="Main Street 123")
    city: str = Field(..., example="Vienna")
    postal_code: str = Field(..., example="1010")
    country: str = Field(..., example="Austria")

class ContactInfo(BaseModel):
    name: str = Field(..., example="John Doe")
    phone: str = Field(..., example="+43123456789")
    email: str = Field(..., example="john.doe@example.com")

class PackageDetails(BaseModel):
    weight_kg: float = Field(..., gt=0, example=5.0)
    dimensions_cm: tuple[float, float, float] = Field(..., example=(30, 20, 15))
    description: Optional[str] = Field(None, example="Fragile items")
    special_instructions: Optional[str] = Field(None, example="Ring bell twice")

class PickupTimeWindow(BaseModel):
    start: time
    end: time

    @validator('end')
    def end_must_be_after_start(cls, v, values):
        if 'start' in values and v <= values['start']:
            raise ValueError('End time must be after start time')
        return v

class PickupRequest(BaseModel):
    pickup_address: Address
    contact_info: ContactInfo
    package_details: PackageDetails
    pickup_time: PickupTimeWindow
    pickup_date: datetime.date
    preferred_logistics_provider: Optional[str] = Field(None, example="Steinhübl")
    reference_id: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "pickup_address": {
                    "street": "Main Street 123",
                    "city": "Vienna",
                    "postal_code": "1010",
                    "country": "Austria"
                },
                "contact_info": {
                    "name": "John Doe",
                    "phone": "+43123456789",
                    "email": "john.doe@example.com"
                },
                "package_details": {
                    "weight_kg": 5.0,
                    "dimensions_cm": [30, 20, 15],
                    "description": "Fragile items",
                    "special_instructions": "Ring bell twice"
                },
                "pickup_time": {
                    "start": "09:00:00",
                    "end": "12:00:00"
                },
                "pickup_date": "2023-12-25",
                "preferred_logistics_provider": "Steinhübl"
            }
        }

class PickupResponse(BaseModel):
    pickup_id: str
    status: str
    confirmation_number: str
    scheduled_date: datetime.date
    scheduled_time_window: PickupTimeWindow
    logistics_provider: str
    reference_id: Optional[str] = None

# Endpoints
@app.post("/pickups", response_model=PickupResponse, status_code=status.HTTP_201_CREATED)
async def schedule_pickup(
    pickup_request: PickupRequest,
    current_user: User = Depends(get_current_active_user)
):
    """
    Schedule a new package pickup with a logistics provider.
    
    Parameters:
    - pickup_request: Details about the pickup including address, contact info, package details, and time window
    
    Returns:
    - Confirmation details including pickup ID and status
    """
    try:
        # Generate unique IDs
        pickup_id = str(uuid4())
        confirmation_number = f"CONF-{datetime.now().strftime('%Y%m%d')}-{pickup_id[:8].upper()}"
        
        # Determine logistics provider
        logistics_provider = pickup_request.preferred_logistics_provider or "Default Logistics"
        
        # Create response
        pickup_response = PickupResponse(
            pickup_id=pickup_id,
            status="scheduled",
            confirmation_number=confirmation_number,
            scheduled_date=pickup_request.pickup_date,
            scheduled_time_window=pickup_request.pickup_time,
            logistics_provider=logistics_provider,
            reference_id=pickup_request.reference_id
        )
        
        # Store in database (in production, use a real database)
        pickups_db[pickup_id] = {
            "request": pickup_request.dict(),
            "response": pickup_response.dict(),
            "user": current_user.username,
            "created_at": datetime.now()
        }
        
        logger.info(f"New pickup scheduled: {pickup_id} by user {current_user.username}")
        
        return pickup_response
        
    except Exception as e:
        logger.error(f"Error scheduling pickup: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to schedule pickup"
        )

@app.get("/pickups/{pickup_id}", response_model=PickupResponse)
async def get_pickup_status(
    pickup_id: str,
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve the status of a scheduled pickup.
    
    Parameters:
    - pickup_id: The unique identifier for the pickup
    
    Returns:
    - Current status and details of the pickup
    """
    if pickup_id not in pickups_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pickup not found"
        )
    
    pickup = pickups_db[pickup_id]
    
    # Check if the current user owns this pickup
    if pickup["user"] != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this pickup"
        )
    
    return pickup["response"]

@app.delete("/pickups/{pickup_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_pickup(
    pickup_id: str,
    current_user: User = Depends(get_current_active_user)
):
    """
    Cancel a scheduled pickup.
    
    Parameters:
    - pickup_id: The unique identifier for the pickup to cancel
    """
    if pickup_id not in pickups_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pickup not found"
        )
    
    pickup = pickups_db[pickup_id]
    
    # Check if the current user owns this pickup
    if pickup["user"] != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to cancel this pickup"
        )
    
    # In production, we would also notify the logistics provider
    pickup["response"]["status"] = "cancelled"
    logger.info(f"Pickup cancelled: {pickup_id} by user {current_user.username}")
    
    return None
```
