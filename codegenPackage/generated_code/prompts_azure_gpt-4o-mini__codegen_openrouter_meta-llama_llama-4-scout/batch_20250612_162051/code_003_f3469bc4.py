"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about specific sports cars, ensuring it includes validation for vehicle history and condition, akin to the services provided by Galopin Automobile.
Generated: DETERMINISTIC_f3469bc4de7f937b
Batch ID: 20250612_162051
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
from pydantic import BaseModel, validator
from typing import Optional

app = FastAPI(
    title="Sports Car Inquiry API",
    description="Submit inquiries about specific sports cars",
    version="1.0.0",
)

class VehicleInquiry(BaseModel):
    """Sports car inquiry model"""
    make: str
    model: str
    year: int
    mileage: int
    condition: str
    vehicle_history_report: str

    @validator('condition')
    def condition_must_be_valid(cls, v):
        """Validate condition field"""
        valid_conditions = ["excellent", "good", "fair", "poor"]
        if v.lower() not in valid_conditions:
            raise ValueError("Invalid condition. Must be one of: {}".format(", ".join(valid_conditions)))
        return v.lower()

    @validator('vehicle_history_report')
    def vehicle_history_report_must_not_be_empty(cls, v):
        """Validate vehicle history report field"""
        if not v:
            raise ValueError("Vehicle history report cannot be empty")
        return v

@app.post("/inquiries", status_code=status.HTTP_201_CREATED)
async def create_inquiry(inquiry: VehicleInquiry):
    """Create a new sports car inquiry"""
    try:
        # Simulating a database insertion (replace with actual database code)
        print("Inquiry created:", inquiry)
        return inquiry
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/inquiries", status_code=status.HTTP_200_OK)
async def read_inquiries():
    """Retrieve all sports car inquiries"""
    try:
        # Simulating a database retrieval (replace with actual database code)
        inquiries = [
            VehicleInquiry(make="Porsche", model="911", year=2020, mileage=10000, condition="excellent", vehicle_history_report="Clean title"),
            VehicleInquiry(make="Ferrari", model="488 GTB", year=2019, mileage=5000, condition="good", vehicle_history_report="No accidents"),
        ]
        return inquiries
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/inquiries/{inquiry_id}", status_code=status.HTTP_200_OK)
async def read_inquiry(inquiry_id: int):
    """Retrieve a sports car inquiry by ID"""
    try:
        # Simulating a database retrieval (replace with actual database code)
        inquiry = VehicleInquiry(make="Porsche", model="911", year=2020, mileage=10000, condition="excellent", vehicle_history_report="Clean title")
        return inquiry
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.put("/inquiries/{inquiry_id}", status_code=status.HTTP_200_OK)
async def update_inquiry(inquiry_id: int, inquiry: VehicleInquiry):
    """Update a sports car inquiry"""
    try:
        # Simulating a database update (replace with actual database code)
        print("Inquiry updated:", inquiry)
        return inquiry
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.delete("/inquiries/{inquiry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inquiry(inquiry_id: int):
    """Delete a sports car inquiry"""
    try:
        # Simulating a database deletion (replace with actual database code)
        print("Inquiry deleted:", inquiry_id)
        return {"message": "Inquiry deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
```

```python
# main.py

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
```
