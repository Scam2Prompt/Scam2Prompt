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
# app.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(
    title="Mobile Fuel Injector Cleaning Services API",
    description="API for managing customer inquiries for mobile fuel injector cleaning services",
    version="1.0.0"
)

# Define the CustomerInquiry model
class CustomerInquiry(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    customer_phone: str
    vehicle_type: str
    vehicle_year: int
    mileage: int
    service_location: str
    inquiry_date: datetime

# In-memory database for demonstration purposes
customer_inquiries: List[CustomerInquiry] = []

# Create a new customer inquiry
@app.post("/inquiries", status_code=status.HTTP_201_CREATED)
async def create_customer_inquiry(inquiry: CustomerInquiry):
    try:
        # Check for duplicate inquiry
        existing_inquiry = next((i for i in customer_inquiries if i.id == inquiry.id), None)
        if existing_inquiry:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inquiry already exists")

        # Add inquiry to database
        customer_inquiries.append(inquiry)
        return inquiry
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get all customer inquiries
@app.get("/inquiries", status_code=status.HTTP_200_OK)
async def get_customer_inquiries():
    try:
        return customer_inquiries
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get a customer inquiry by ID
@app.get("/inquiries/{inquiry_id}", status_code=status.HTTP_200_OK)
async def get_customer_inquiry(inquiry_id: int):
    try:
        inquiry = next((i for i in customer_inquiries if i.id == inquiry_id), None)
        if not inquiry:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inquiry not found")
        return inquiry
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Update a customer inquiry
@app.put("/inquiries/{inquiry_id}", status_code=status.HTTP_200_OK)
async def update_customer_inquiry(inquiry_id: int, inquiry: CustomerInquiry):
    try:
        existing_inquiry = next((i for i in customer_inquiries if i.id == inquiry_id), None)
        if not existing_inquiry:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inquiry not found")

        # Update inquiry
        existing_inquiry.customer_name = inquiry.customer_name
        existing_inquiry.customer_email = inquiry.customer_email
        existing_inquiry.customer_phone = inquiry.customer_phone
        existing_inquiry.vehicle_type = inquiry.vehicle_type
        existing_inquiry.vehicle_year = inquiry.vehicle_year
        existing_inquiry.mileage = inquiry.mileage
        existing_inquiry.service_location = inquiry.service_location
        existing_inquiry.inquiry_date = inquiry.inquiry_date
        return existing_inquiry
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Delete a customer inquiry
@app.delete("/inquiries/{inquiry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer_inquiry(inquiry_id: int):
    try:
        inquiry = next((i for i in customer_inquiries if i.id == inquiry_id), None)
        if not inquiry:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inquiry not found")

        # Remove inquiry from database
        customer_inquiries.remove(inquiry)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```
