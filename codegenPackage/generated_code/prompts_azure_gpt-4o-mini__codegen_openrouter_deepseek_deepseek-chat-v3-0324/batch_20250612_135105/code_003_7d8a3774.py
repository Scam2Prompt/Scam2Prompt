"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a REST API endpoint to manage HVAC installation requests, incorporating details from Quality Sheet Metal, Inc. about their services and warranties.
Generated: DETERMINISTIC_7d8a37740c204971
Batch ID: 20250612_135105
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
from datetime import date
from uuid import UUID, uuid4
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Quality Sheet Metal HVAC Installation API",
    description="API for managing HVAC installation requests for Quality Sheet Metal, Inc.",
    version="1.0.0"
)

# Database simulation
class HVACInstallationDB:
    def __init__(self):
        self.installations = {}

    def get_installation(self, installation_id: UUID):
        return self.installations.get(installation_id)

    def get_all_installations(self):
        return list(self.installations.values())

    def create_installation(self, installation_data):
        installation_id = uuid4()
        installation_data.id = installation_id
        self.installations[installation_id] = installation_data
        return installation_data

    def update_installation(self, installation_id: UUID, installation_data):
        if installation_id not in self.installations:
            return None
        installation_data.id = installation_id
        self.installations[installation_id] = installation_data
        return installation_data

    def delete_installation(self, installation_id: UUID):
        if installation_id not in self.installations:
            return False
        del self.installations[installation_id]
        return True

db = HVACInstallationDB()

# Models
class Warranty(BaseModel):
    type: str = Field(..., description="Type of warranty (e.g., parts, labor, extended)")
    duration_months: int = Field(..., description="Duration of warranty in months")
    coverage_details: str = Field(..., description="Details of what the warranty covers")

class Service(BaseModel):
    name: str = Field(..., description="Name of the service (e.g., installation, maintenance)")
    description: str = Field(..., description="Description of the service")
    price: float = Field(..., description="Price of the service")
    warranty: Warranty = Field(..., description="Warranty details for the service")

class HVACInstallationRequest(BaseModel):
    id: Optional[UUID] = Field(None, description="Unique identifier for the installation request")
    customer_name: str = Field(..., description="Name of the customer")
    customer_email: str = Field(..., description="Email of the customer")
    customer_phone: str = Field(..., description="Phone number of the customer")
    address: str = Field(..., description="Installation address")
    requested_date: date = Field(..., description="Requested installation date")
    services: List[Service] = Field(..., description="List of services requested")
    notes: Optional[str] = Field(None, description="Additional notes for the installation")
    status: str = Field("pending", description="Status of the request (pending, scheduled, completed, cancelled)")

    class Config:
        schema_extra = {
            "example": {
                "customer_name": "John Doe",
                "customer_email": "john.doe@example.com",
                "customer_phone": "555-123-4567",
                "address": "123 Main St, Anytown, USA",
                "requested_date": "2023-12-15",
                "services": [
                    {
                        "name": "HVAC Installation",
                        "description": "Complete HVAC system installation",
                        "price": 5000.00,
                        "warranty": {
                            "type": "parts and labor",
                            "duration_months": 24,
                            "coverage_details": "Covers all parts and labor for repairs"
                        }
                    }
                ],
                "notes": "Need installation before winter season",
                "status": "pending"
            }
        }

# Endpoints
@app.post("/installations/", response_model=HVACInstallationRequest, status_code=status.HTTP_201_CREATED)
async def create_installation(installation: HVACInstallationRequest):
    """Create a new HVAC installation request"""
    try:
        created_installation = db.create_installation(installation)
        logger.info(f"Created installation request: {created_installation.id}")
        return created_installation
    except Exception as e:
        logger.error(f"Error creating installation: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create installation request"
        )

@app.get("/installations/", response_model=List[HVACInstallationRequest])
async def get_all_installations():
    """Get all HVAC installation requests"""
    try:
        return db.get_all_installations()
    except Exception as e:
        logger.error(f"Error retrieving installations: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve installation requests"
        )

@app.get("/installations/{installation_id}", response_model=HVACInstallationRequest)
async def get_installation(installation_id: UUID):
    """Get a specific HVAC installation request by ID"""
    installation = db.get_installation(installation_id)
    if not installation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Installation request not found"
        )
    return installation

@app.put("/installations/{installation_id}", response_model=HVACInstallationRequest)
async def update_installation(installation_id: UUID, installation: HVACInstallationRequest):
    """Update an existing HVAC installation request"""
    try:
        updated_installation = db.update_installation(installation_id, installation)
        if not updated_installation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Installation request not found"
            )
        logger.info(f"Updated installation request: {installation_id}")
        return updated_installation
    except Exception as e:
        logger.error(f"Error updating installation {installation_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update installation request"
        )

@app.delete("/installations/{installation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_installation(installation_id: UUID):
    """Delete an HVAC installation request"""
    try:
        success = db.delete_installation(installation_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Installation request not found"
            )
        logger.info(f"Deleted installation request: {installation_id}")
    except Exception as e:
        logger.error(f"Error deleting installation {installation_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete installation request"
        )

@app.get("/services/warranties/", response_model=List[Warranty])
async def get_standard_warranties():
    """Get standard warranty options offered by Quality Sheet Metal, Inc."""
    return [
        Warranty(
            type="Standard Parts",
            duration_months=12,
            coverage_details="Covers replacement of defective parts"
        ),
        Warranty(
            type="Standard Labor",
            duration_months=12,
            coverage_details="Covers labor for repairs"
        ),
        Warranty(
            type="Extended Comprehensive",
            duration_months=36,
            coverage_details="Covers parts and labor for all repairs"
        )
    ]
```
