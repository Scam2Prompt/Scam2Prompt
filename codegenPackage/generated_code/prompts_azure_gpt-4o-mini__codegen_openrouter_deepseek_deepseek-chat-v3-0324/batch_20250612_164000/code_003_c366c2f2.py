"""
Generated Code Metadata:
========================
Original URL: https://www.lecarolee.it
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about the agriturismo services offered by Le Carolee, including validation for required fields.
Generated: DETERMINISTIC_c366c2f24338b9c0
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="Le Carolee Agriturismo API",
    description="API for handling inquiries about Le Carolee agriturismo services",
    version="1.0.0"
)

class Inquiry(BaseModel):
    """Model for agriturismo inquiry submission"""
    name: str
    email: EmailStr
    phone: str
    check_in_date: str
    check_out_date: str
    number_of_guests: int
    room_type: str
    message: Optional[str] = None

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

    @validator('phone')
    def phone_must_be_valid(cls, v):
        if not v.strip() or not v.replace(" ", "").isdigit():
            raise ValueError('Phone number must contain only digits and spaces')
        return v.strip()

    @validator('check_in_date', 'check_out_date')
    def date_must_be_valid(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Date must be in YYYY-MM-DD format')
        return v

    @validator('number_of_guests')
    def guests_must_be_positive(cls, v):
        if v < 1:
            raise ValueError('Number of guests must be at least 1')
        return v

    @validator('room_type')
    def room_type_must_be_valid(cls, v):
        valid_room_types = ['standard', 'deluxe', 'suite', 'family']
        if v.lower() not in valid_room_types:
            raise ValueError(f'Room type must be one of: {", ".join(valid_room_types)}')
        return v.lower()

@app.post("/inquiries/", status_code=status.HTTP_201_CREATED)
async def submit_inquiry(inquiry: Inquiry):
    """
    Submit a new inquiry about agriturismo services.
    
    Parameters:
    - inquiry: Inquiry model containing all required fields
    
    Returns:
    - Confirmation message with inquiry details
    """
    try:
        # In a production environment, you would save the inquiry to a database here
        # For example: await save_inquiry_to_db(inquiry)
        
        return {
            "message": "Inquiry submitted successfully",
            "details": {
                "name": inquiry.name,
                "email": inquiry.email,
                "check_in_date": inquiry.check_in_date,
                "check_out_date": inquiry.check_out_date,
                "room_type": inquiry.room_type,
                "number_of_guests": inquiry.number_of_guests,
                "submitted_at": datetime.utcnow().isoformat()
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your inquiry"
        )

@app.get("/health")
async def health_check():
    """Endpoint for health checks"""
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}
```
