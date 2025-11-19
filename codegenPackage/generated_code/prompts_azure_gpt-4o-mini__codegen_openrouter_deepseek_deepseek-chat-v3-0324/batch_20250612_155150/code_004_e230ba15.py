"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Describe an API that could be used to manage customer inquiries for mobile fuel injector cleaning services, similar to those offered in Gold Coast.
Generated: DETERMINISTIC_e230ba155f41d66c
Batch ID: 20250612_155150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from enum import Enum
import uuid

app = FastAPI(
    title="Mobile Fuel Injector Cleaning API",
    description="API for managing customer inquiries for mobile fuel injector cleaning services",
    version="1.0.0"
)

# Database mock (in production, replace with actual database)
inquiries_db = []

class ServiceType(str, Enum):
    BASIC = "basic"
    PREMIUM = "premium"
    DELUXE = "deluxe"

class InquiryStatus(str, Enum):
    NEW = "new"
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class InquiryCreate(BaseModel):
    customer_name: str
    email: EmailStr
    phone: str
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    service_type: ServiceType
    preferred_date: datetime
    notes: Optional[str] = None

class Inquiry(InquiryCreate):
    id: str
    status: InquiryStatus
    created_at: datetime
    updated_at: datetime

@app.post("/inquiries/", response_model=Inquiry, status_code=status.HTTP_201_CREATED)
async def create_inquiry(inquiry: InquiryCreate):
    """Create a new service inquiry"""
    inquiry_id = str(uuid.uuid4())
    now = datetime.now()
    db_inquiry = {
        **inquiry.dict(),
        "id": inquiry_id,
        "status": InquiryStatus.NEW,
        "created_at": now,
        "updated_at": now
    }
    inquiries_db.append(db_inquiry)
    return db_inquiry

@app.get("/inquiries/", response_model=List[Inquiry])
async def list_inquiries(status: Optional[InquiryStatus] = None):
    """List all inquiries, optionally filtered by status"""
    if status:
        return [inq for inq in inquiries_db if inq["status"] == status]
    return inquiries_db

@app.get("/inquiries/{inquiry_id}", response_model=Inquiry)
async def get_inquiry(inquiry_id: str):
    """Get details of a specific inquiry"""
    for inquiry in inquiries_db:
        if inquiry["id"] == inquiry_id:
            return inquiry
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Inquiry not found"
    )

@app.put("/inquiries/{inquiry_id}", response_model=Inquiry)
async def update_inquiry(inquiry_id: str, status: InquiryStatus):
    """Update the status of an inquiry"""
    for inquiry in inquiries_db:
        if inquiry["id"] == inquiry_id:
            inquiry["status"] = status
            inquiry["updated_at"] = datetime.now()
            return inquiry
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Inquiry not found"
    )

@app.delete("/inquiries/{inquiry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inquiry(inquiry_id: str):
    """Delete an inquiry (admin only)"""
    for i, inquiry in enumerate(inquiries_db):
        if inquiry["id"] == inquiry_id:
            inquiries_db.pop(i)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Inquiry not found"
    )

@app.get("/inquiries/customer/{email}", response_model=List[Inquiry])
async def get_customer_inquiries(email: EmailStr):
    """Get all inquiries for a specific customer"""
    customer_inquiries = [inq for inq in inquiries_db if inq["email"] == email]
    if not customer_inquiries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No inquiries found for this customer"
        )
    return customer_inquiries
```
