"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: Develop a RESTful API endpoint that allows users to submit requests for custom signage and display products, reflecting the service model of Detalj Reklam.
Generated: DETERMINISTIC_22f9b047542946ab
Batch ID: 20250612_161500
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
from typing import Optional, List
from datetime import datetime
import uuid
from enum import Enum

app = FastAPI(
    title="Detalj Reklam Signage API",
    description="API for submitting custom signage and display product requests",
    version="1.0.0"
)

# Database mock (in production, replace with actual database)
signage_requests_db = []

class ProductType(str, Enum):
    BANNER = "banner"
    POSTER = "poster"
    LIGHTBOX = "lightbox"
    VEHICLE_WRAP = "vehicle_wrap"
    WINDOW_GRAPHICS = "window_graphics"
    OTHER = "other"

class MaterialType(str, Enum):
    VINYL = "vinyl"
    FABRIC = "fabric"
    ACRYLIC = "acrylic"
    METAL = "metal"
    OTHER = "other"

class SignageRequest(BaseModel):
    request_id: str = str(uuid.uuid4())
    customer_name: str
    customer_email: EmailStr
    phone_number: str
    product_type: ProductType
    material_type: MaterialType
    dimensions: str
    quantity: int
    design_description: str
    color_scheme: str
    special_requirements: Optional[str] = None
    deadline: Optional[datetime] = None
    created_at: datetime = datetime.now()
    
    @validator('quantity')
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be at least 1')
        return v
    
    @validator('phone_number')
    def validate_phone_number(cls, v):
        if not v.replace(" ", "").replace("-", "").replace("+", "").isdigit():
            raise ValueError('Invalid phone number format')
        return v

class SignageRequestResponse(BaseModel):
    request_id: str
    status: str
    created_at: datetime

@app.post("/signage-requests/", 
          response_model=SignageRequestResponse,
          status_code=status.HTTP_201_CREATED,
          summary="Submit a new signage request",
          description="Submit a request for custom signage or display products")
async def create_signage_request(request: SignageRequest):
    try:
        signage_requests_db.append(request.dict())
        return {
            "request_id": request.request_id,
            "status": "received",
            "created_at": request.created_at
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get("/signage-requests/",
         response_model=List[SignageRequest],
         summary="List all signage requests",
         description="Retrieve all submitted signage requests (admin only)")
async def list_signage_requests():
    return signage_requests_db

@app.get("/signage-requests/{request_id}",
         response_model=SignageRequest,
         summary="Get signage request details",
         description="Retrieve details for a specific signage request")
async def get_signage_request(request_id: str):
    for request in signage_requests_db:
        if request["request_id"] == request_id:
            return request
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Request not found"
    )

@app.put("/signage-requests/{request_id}/status",
         response_model=SignageRequestResponse,
         summary="Update request status",
         description="Update the status of a signage request (admin only)")
async def update_request_status(request_id: str, status: str):
    for request in signage_requests_db:
        if request["request_id"] == request_id:
            request["status"] = status
            return {
                "request_id": request_id,
                "status": status,
                "created_at": request["created_at"]
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Request not found"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
