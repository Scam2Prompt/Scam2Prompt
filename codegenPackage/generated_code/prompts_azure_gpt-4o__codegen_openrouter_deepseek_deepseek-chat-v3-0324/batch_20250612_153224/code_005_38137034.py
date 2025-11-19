"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: Design a REST API that enables manufacturers to submit inquiries to PRGMEA about sourcing processes and receive automated responses.
Generated: DETERMINISTIC_381370342eceab6b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional
import uvicorn
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="PRGMEA Sourcing Inquiry API",
    description="API for manufacturers to submit inquiries to PRGMEA about sourcing processes",
    version="1.0.0"
)

# Database simulation (in production, use a real database)
inquiries_db = []

# Pydantic models for request/response validation
class InquiryCreate(BaseModel):
    manufacturer_name: str
    contact_person: str
    email: EmailStr
    phone: str
    inquiry_subject: str
    inquiry_details: str
    preferred_response_method: str = "email"  # email, phone, both

class InquiryResponse(BaseModel):
    inquiry_id: str
    manufacturer_name: str
    inquiry_subject: str
    status: str
    response: str
    timestamp: datetime

class InquiryStatus(BaseModel):
    inquiry_id: str
    status: str
    last_updated: datetime

# Helper function to generate unique ID
def generate_id():
    return str(len(inquiries_db) + 1).zfill(6)

# Endpoint to submit new inquiry
@app.post("/inquiries/", response_model=InquiryStatus, status_code=status.HTTP_201_CREATED)
async def submit_inquiry(inquiry: InquiryCreate):
    """
    Submit a new sourcing inquiry to PRGMEA.
    Returns inquiry ID and status.
    """
    try:
        inquiry_id = generate_id()
        timestamp = datetime.now()
        
        # Create inquiry record
        inquiry_record = {
            "inquiry_id": inquiry_id,
            **inquiry.dict(),
            "status": "received",
            "timestamp": timestamp,
            "last_updated": timestamp,
            "response": "Thank you for your inquiry. Our team will review it and respond within 2 business days."
        }
        
        inquiries_db.append(inquiry_record)
        
        return {
            "inquiry_id": inquiry_id,
            "status": "received",
            "last_updated": timestamp
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process inquiry"
        )

# Endpoint to check inquiry status
@app.get("/inquiries/{inquiry_id}/status", response_model=InquiryStatus)
async def check_inquiry_status(inquiry_id: str):
    """
    Check the status of an existing inquiry.
    """
    inquiry = next((i for i in inquiries_db if i["inquiry_id"] == inquiry_id), None)
    
    if not inquiry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inquiry not found"
        )
    
    return {
        "inquiry_id": inquiry_id,
        "status": inquiry["status"],
        "last_updated": inquiry["last_updated"]
    }

# Endpoint to get inquiry response
@app.get("/inquiries/{inquiry_id}/response", response_model=InquiryResponse)
async def get_inquiry_response(inquiry_id: str):
    """
    Get the response for an existing inquiry.
    """
    inquiry = next((i for i in inquiries_db if i["inquiry_id"] == inquiry_id), None)
    
    if not inquiry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inquiry not found"
        )
    
    return {
        "inquiry_id": inquiry_id,
        "manufacturer_name": inquiry["manufacturer_name"],
        "inquiry_subject": inquiry["inquiry_subject"],
        "status": inquiry["status"],
        "response": inquiry["response"],
        "timestamp": inquiry["timestamp"]
    }

# Endpoint to list all inquiries (for admin purposes)
@app.get("/inquiries/", response_model=list[InquiryResponse])
async def list_inquiries(limit: int = 10, offset: int = 0):
    """
    List all inquiries (paginated).
    """
    return inquiries_db[offset:offset + limit]

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {"status": "healthy", "timestamp": datetime.now()}

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
