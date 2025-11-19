"""
Generated Code Metadata:
========================
Original URL: https://www.suezlng.com
Prompt: "Create a RESTful API for oil trading management system with endpoints for creating, reading, updating, and deleting (CRUD) customer enquiries."
Generated: DETERMINISTIC_118594ab9b4b7fd7
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# oil_trading_api.py
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
from fastapi.encoders import jsonable_encoder

app = FastAPI(
    title="Oil Trading Management System API",
    description="A RESTful API for managing customer enquiries in oil trading",
    version="1.0.0"
)

# Database simulation (in-memory storage for demonstration)
enquiries_db = {}

# Models
class EnquiryBase(BaseModel):
    customer_name: str
    email: str
    phone: str
    product_type: str
    quantity: float
    delivery_date: str
    additional_notes: Optional[str] = None

class EnquiryCreate(EnquiryBase):
    pass

class Enquiry(EnquiryBase):
    id: str
    created_at: str
    updated_at: str

    class Config:
        schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "customer_name": "John Doe",
                "email": "john@example.com",
                "phone": "+1234567890",
                "product_type": "Crude Oil",
                "quantity": 5000.0,
                "delivery_date": "2023-12-31",
                "additional_notes": "Urgent delivery required",
                "created_at": "2023-01-01T12:00:00Z",
                "updated_at": "2023-01-01T12:00:00Z"
            }
        }

# Helper functions
def get_current_timestamp():
    return datetime.utcnow().isoformat() + "Z"

def get_enquiry(enquiry_id: str):
    if enquiry_id not in enquiries_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Enquiry not found"
        )
    return enquiries_db[enquiry_id]

# API Endpoints
@app.post("/enquiries/", response_model=Enquiry, status_code=status.HTTP_201_CREATED)
async def create_enquiry(enquiry: EnquiryCreate):
    """
    Create a new customer enquiry.
    """
    enquiry_id = str(uuid.uuid4())
    timestamp = get_current_timestamp()
    new_enquiry = Enquiry(
        id=enquiry_id,
        created_at=timestamp,
        updated_at=timestamp,
        **enquiry.dict()
    )
    enquiries_db[enquiry_id] = new_enquiry
    return new_enquiry

@app.get("/enquiries/", response_model=List[Enquiry])
async def read_enquiries(skip: int = 0, limit: int = 100):
    """
    Retrieve all customer enquiries with pagination support.
    """
    return list(enquiries_db.values())[skip : skip + limit]

@app.get("/enquiries/{enquiry_id}", response_model=Enquiry)
async def read_enquiry(enquiry_id: str):
    """
    Retrieve a specific customer enquiry by ID.
    """
    return get_enquiry(enquiry_id)

@app.put("/enquiries/{enquiry_id}", response_model=Enquiry)
async def update_enquiry(enquiry_id: str, enquiry: EnquiryCreate):
    """
    Update an existing customer enquiry.
    """
    existing_enquiry = get_enquiry(enquiry_id)
    update_data = enquiry.dict(exclude_unset=True)
    updated_enquiry = existing_enquiry.copy(update=update_data)
    updated_enquiry.updated_at = get_current_timestamp()
    enquiries_db[enquiry_id] = updated_enquiry
    return updated_enquiry

@app.delete("/enquiries/{enquiry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_enquiry(enquiry_id: str):
    """
    Delete a customer enquiry.
    """
    get_enquiry(enquiry_id)  # Check if enquiry exists
    del enquiries_db[enquiry_id]
    return None

# Error handlers
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=str(exc)
    )

# Health check endpoint
@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """
    Health check endpoint to verify API is running.
    """
    return {"status": "healthy"}
```
