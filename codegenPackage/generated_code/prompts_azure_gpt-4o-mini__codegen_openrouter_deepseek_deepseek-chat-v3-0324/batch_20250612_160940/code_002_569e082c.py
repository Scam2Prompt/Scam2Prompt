"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Create an API recommendation for a legal and accounting service platform that includes features for property law, migration law, and tax accounting, as highlighted by Carthew Chau & Co.
Generated: DETERMINISTIC_569e082cae56575e
Batch ID: 20250612_160940
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.carthewchau.com.au/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

app = FastAPI(
    title="Carthew Chau & Co Legal & Accounting API",
    description="API for legal and accounting services including property law, migration law, and tax accounting.",
    version="1.0.0",
    contact={
        "name": "Carthew Chau & Co",
        "url": "https://www.carthewchau.com.au/",
    },
    license_info={
        "name": "Proprietary",
    },
)

# Enums for service types
class ServiceType(str, Enum):
    PROPERTY_LAW = "property_law"
    MIGRATION_LAW = "migration_law"
    TAX_ACCOUNTING = "tax_accounting"

# Models
class ContactInfo(BaseModel):
    name: str
    email: str
    phone: str
    preferred_contact_method: str = "email"

class ServiceRequest(BaseModel):
    service_type: ServiceType
    description: str
    contact_info: ContactInfo
    urgency: Optional[str] = "standard"
    documents: Optional[List[str]] = None

class ServiceResponse(BaseModel):
    request_id: str
    service_type: ServiceType
    status: str
    estimated_completion_time: Optional[str]
    assigned_advisor: Optional[str]

# Mock database
service_requests_db = {}

# Helper functions
def generate_request_id():
    import uuid
    return str(uuid.uuid4())

# API Endpoints
@app.post("/services/request", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED)
async def create_service_request(request: ServiceRequest):
    """
    Submit a new service request for legal or accounting services.
    
    Supported services:
    - property_law: Property law services
    - migration_law: Migration law services
    - tax_accounting: Tax accounting services
    """
    request_id = generate_request_id()
    
    # Basic validation
    if not request.description:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Description is required"
        )
    
    # Create response
    response = ServiceResponse(
        request_id=request_id,
        service_type=request.service_type,
        status="received",
        estimated_completion_time="3 business days",
        assigned_advisor=None
    )
    
    # Store in mock DB
    service_requests_db[request_id] = {
        "request": request,
        "response": response
    }
    
    return response

@app.get("/services/status/{request_id}", response_model=ServiceResponse)
async def get_service_status(request_id: str):
    """
    Check the status of a service request.
    """
    if request_id not in service_requests_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Request not found"
        )
    
    return service_requests_db[request_id]["response"]

@app.get("/services/types", response_model=List[str])
async def get_service_types():
    """
    Get all available service types.
    """
    return [service.value for service in ServiceType]

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(500)
async def internal_server_error_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
