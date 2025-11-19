"""
Generated Code Metadata:
========================
Original URL: https://bepretty.hamburg
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries for makeup and styling services, similar to the contact form on bePretty Hamburg.
Generated: DETERMINISTIC_cfd52757f3bce26c
Batch ID: 20250612_162051
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
from typing import Optional
from datetime import datetime
import uvicorn

app = FastAPI(
    title="BePretty API",
    description="API for makeup and styling service inquiries",
    version="1.0.0"
)

# Database mock (in production, use a real database)
inquiries_db = []

class InquiryRequest(BaseModel):
    name: str
    email: EmailStr
    phone: str
    service_type: str
    event_date: str
    message: Optional[str] = None
    preferred_contact_method: str = "email"

    @validator('phone')
    def phone_validation(cls, v):
        if not v.replace(' ', '').replace('-', '').replace('+', '').isdigit():
            raise ValueError('Phone number must contain only digits and valid separators')
        return v

    @validator('event_date')
    def date_validation(cls, v):
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Date must be in YYYY-MM-DD format')
        return v

    @validator('preferred_contact_method')
    def contact_method_validation(cls, v):
        if v not in ["email", "phone"]:
            raise ValueError('Preferred contact method must be either "email" or "phone"')
        return v

class InquiryResponse(BaseModel):
    id: int
    name: str
    email: str
    service_type: str
    event_date: str
    submitted_at: str
    status: str = "received"

@app.post("/inquiries/", response_model=InquiryResponse, status_code=status.HTTP_201_CREATED)
async def submit_inquiry(inquiry: InquiryRequest):
    """
    Submit a new makeup and styling service inquiry.
    
    Parameters:
    - name: Full name of the client
    - email: Valid email address
    - phone: Phone number (digits only with optional separators)
    - service_type: Type of service requested (e.g., "bridal", "event", "photoshoot")
    - event_date: Date of the event in YYYY-MM-DD format
    - message: Optional additional message
    - preferred_contact_method: Either "email" or "phone"
    
    Returns:
    - Inquiry details with submission confirmation
    """
    try:
        # Generate a simple ID (in production, use database auto-increment)
        inquiry_id = len(inquiries_db) + 1
        submitted_at = datetime.now().isoformat()
        
        # Create the response object
        inquiry_response = {
            "id": inquiry_id,
            "name": inquiry.name,
            "email": inquiry.email,
            "service_type": inquiry.service_type,
            "event_date": inquiry.event_date,
            "submitted_at": submitted_at,
            "status": "received"
        }
        
        # Store in "database"
        inquiries_db.append(inquiry_response)
        
        return inquiry_response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/inquiries/{inquiry_id}", response_model=InquiryResponse)
async def get_inquiry(inquiry_id: int):
    """
    Retrieve a specific inquiry by its ID.
    """
    try:
        if inquiry_id < 1 or inquiry_id > len(inquiries_db):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Inquiry not found"
            )
        return inquiries_db[inquiry_id - 1]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
