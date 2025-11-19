"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: How can I design a self-booking appointment system that filters out unqualified leads, based on the techniques shared by Client Fuel?
Generated: DETERMINISTIC_2084e75d8269e3de
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel, validator, ValidationError
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse

app = FastAPI(title="Self-Booking Appointment System")

class AppointmentRequest(BaseModel):
    """Model for appointment booking request"""
    name: str
    email: str
    phone: str
    desired_service: str
    budget: Optional[str] = None
    preferred_date: str
    preferred_time: str
    qualification_answers: Dict[str, str]

    @validator('email')
    def email_must_contain_at(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v.lower()

    @validator('preferred_date')
    def date_must_be_valid(cls, v):
        try:
            datetime.datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Invalid date format. Use YYYY-MM-DD')
        return v

    @validator('preferred_time')
    def time_must_be_valid(cls, v):
        try:
            datetime.datetime.strptime(v, '%H:%M')
        except ValueError:
            raise ValueError('Invalid time format. Use HH:MM')
        return v

class QualificationRules:
    """Business rules for lead qualification"""
    @staticmethod
    def is_qualified(appointment: AppointmentRequest) -> bool:
        """Check if lead meets qualification criteria"""
        # Example qualification rules (customize based on your business needs)
        required_answers = {
            "business_type": "B2B",  # Only accept B2B clients
            "budget": "premium",     # Only accept premium budget clients
            "timeline": "1-3 months" # Only clients ready in 1-3 months
        }
        
        for question, expected_answer in required_answers.items():
            if appointment.qualification_answers.get(question) != expected_answer:
                return False
        return True

class AppointmentSystem:
    """Core appointment booking system"""
    @staticmethod
    def book_appointment(appointment: AppointmentRequest) -> Dict:
        """Process appointment booking if qualified"""
        if not QualificationRules.is_qualified(appointment):
            raise ValueError("Lead does not meet qualification criteria")
        
        # In a real system, this would save to a database
        confirmation = {
            "confirmation_id": f"APP-{datetime.datetime.now().timestamp()}",
            "client_name": appointment.name,
            "service": appointment.desired_service,
            "date": appointment.preferred_date,
            "time": appointment.preferred_time,
            "status": "confirmed"
        }
        return confirmation

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    """Handle Pydantic validation errors"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors()},
    )

@app.post("/book-appointment/", response_model=Dict)
async def book_appointment_endpoint(appointment: AppointmentRequest):
    """Endpoint for booking appointments"""
    try:
        result = AppointmentSystem.book_appointment(appointment)
        return {"success": True, "appointment": result}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your request"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
