"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Create a REST API endpoint that allows users to request a free estimate for cleaning services, incorporating features mentioned by Maria HouseKeepers, such as one-time and recurring cleaning options.
Generated: DETERMINISTIC_e923f63f4adaede0
Batch ID: 20250612_162051
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
import uvicorn

app = FastAPI(
    title="Maria HouseKeepers Cleaning Estimate API",
    description="API for requesting free cleaning service estimates",
    version="1.0.0"
)

class CleaningEstimateRequest(BaseModel):
    """Model for cleaning estimate request data"""
    name: str
    email: EmailStr
    phone: str
    address: str
    service_type: str  # "one-time" or "recurring"
    frequency: Optional[str] = None  # Only required for recurring (e.g., "weekly", "bi-weekly")
    bedrooms: int
    bathrooms: int
    square_footage: int
    additional_services: Optional[list[str]] = None  # e.g., ["deep_cleaning", "window_washing"]
    preferred_date: Optional[datetime] = None  # For one-time cleaning
    notes: Optional[str] = None

    @validator('service_type')
    def validate_service_type(cls, v):
        if v not in ["one-time", "recurring"]:
            raise ValueError("service_type must be either 'one-time' or 'recurring'")
        return v

    @validator('frequency')
    def validate_frequency(cls, v, values):
        if values.get('service_type') == 'recurring' and not v:
            raise ValueError("frequency is required for recurring services")
        if v and v not in ["weekly", "bi-weekly", "monthly"]:
            raise ValueError("frequency must be one of: weekly, bi-weekly, monthly")
        return v

    @validator('phone')
    def validate_phone(cls, v):
        if not v.replace('-', '').replace(' ', '').replace('(', '').replace(')', '').isdigit():
            raise ValueError("phone must contain only digits and standard formatting characters")
        return v

@app.post("/api/estimate", status_code=status.HTTP_201_CREATED)
async def request_estimate(estimate_request: CleaningEstimateRequest):
    """
    Endpoint to request a free cleaning service estimate.
    
    Parameters:
    - estimate_request: CleaningEstimateRequest object containing all necessary details
    
    Returns:
    - Confirmation message with estimate request details
    """
    try:
        # In a real application, you would:
        # 1. Validate the data further (already done by Pydantic)
        # 2. Store the request in a database
        # 3. Possibly queue for processing or send email confirmation
        
        # For demo purposes, we'll just return a confirmation
        response = {
            "message": "Estimate request received successfully",
            "details": estimate_request.dict(),
            "estimate_id": "EST-" + str(datetime.now().timestamp()).replace('.', '')[:10],
            "next_steps": "Our team will contact you within 24 hours with your estimate."
        }
        
        return response
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Maria HouseKeepers Estimate API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
