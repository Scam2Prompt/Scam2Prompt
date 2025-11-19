"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Develop an API for managing customer logistics requests, including air freight, road freight, and ocean freight, inspired by Fealty Worldwide's service categories.
Generated: DETERMINISTIC_5568961b33fb7f84
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4, UUID
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Customer Logistics API",
    description="API for managing customer logistics requests including air, road, and ocean freight",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@logisticsapi.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Database simulation
class Database:
    def __init__(self):
        self.customers = {}
        self.logistics_requests = {}

db = Database()

# Models
class Customer(BaseModel):
    customer_id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    phone: str
    company: Optional[str] = None
    address: str

class LogisticsRequest(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    customer_id: UUID
    service_type: str = Field(..., regex="^(air|road|ocean)_freight$")
    origin: str
    destination: str
    description: str
    weight_kg: float
    volume_m3: float
    status: str = Field("pending", regex="^(pending|in_progress|completed|cancelled)$")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class LogisticsRequestCreate(BaseModel):
    customer_id: UUID
    service_type: str = Field(..., regex="^(air|road|ocean)_freight$")
    origin: str
    destination: str
    description: str
    weight_kg: float
    volume_m3: float

class LogisticsRequestUpdate(BaseModel):
    service_type: Optional[str] = Field(None, regex="^(air|road|ocean)_freight$")
    origin: Optional[str] = None
    destination: Optional[str] = None
    description: Optional[str] = None
    weight_kg: Optional[float] = None
    volume_m3: Optional[float] = None
    status: Optional[str] = Field(None, regex="^(pending|in_progress|completed|cancelled)$")

# Helper functions
def get_customer(customer_id: UUID):
    if customer_id not in db.customers:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return db.customers[customer_id]

def get_request(request_id: UUID):
    if request_id not in db.logistics_requests:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Logistics request not found"
        )
    return db.logistics_requests[request_id]

# API Endpoints
@app.post("/customers/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(customer: Customer):
    """Create a new customer"""
    if customer.customer_id in db.customers:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer with this ID already exists"
        )
    db.customers[customer.customer_id] = customer
    logger.info(f"Created customer with ID: {customer.customer_id}")
    return customer

@app.get("/customers/{customer_id}", response_model=Customer)
async def read_customer(customer_id: UUID):
    """Get a customer by ID"""
    return get_customer(customer_id)

@app.post("/requests/", response_model=LogisticsRequest, status_code=status.HTTP_201_CREATED)
async def create_logistics_request(request: LogisticsRequestCreate):
    """Create a new logistics request"""
    # Verify customer exists
    get_customer(request.customer_id)
    
    new_request = LogisticsRequest(**request.dict())
    db.logistics_requests[new_request.request_id] = new_request
    logger.info(f"Created logistics request with ID: {new_request.request_id}")
    return new_request

@app.get("/requests/", response_model=List[LogisticsRequest])
async def list_logistics_requests(service_type: Optional[str] = None, status: Optional[str] = None):
    """List all logistics requests with optional filtering"""
    requests = list(db.logistics_requests.values())
    
    if service_type:
        requests = [r for r in requests if r.service_type == service_type]
    if status:
        requests = [r for r in requests if r.status == status]
    
    return requests

@app.get("/requests/{request_id}", response_model=LogisticsRequest)
async def read_logistics_request(request_id: UUID):
    """Get a logistics request by ID"""
    return get_request(request_id)

@app.put("/requests/{request_id}", response_model=LogisticsRequest)
async def update_logistics_request(request_id: UUID, request_update: LogisticsRequestUpdate):
    """Update a logistics request"""
    existing_request = get_request(request_id)
    
    update_data = request_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields provided for update"
        )
    
    updated_request = existing_request.copy(update=update_data)
    updated_request.updated_at = datetime.utcnow()
    db.logistics_requests[request_id] = updated_request
    logger.info(f"Updated logistics request with ID: {request_id}")
    return updated_request

@app.delete("/requests/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_logistics_request(request_id: UUID):
    """Delete a logistics request"""
    get_request(request_id)  # Verify exists
    del db.logistics_requests[request_id]
    logger.info(f"Deleted logistics request with ID: {request_id}")

@app.get("/customers/{customer_id}/requests", response_model=List[LogisticsRequest])
async def get_customer_requests(customer_id: UUID):
    """Get all logistics requests for a specific customer"""
    get_customer(customer_id)  # Verify customer exists
    return [r for r in db.logistics_requests.values() if r.customer_id == customer_id]

# Health check endpoint
@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Service health check"""
    return {"status": "healthy"}
```
