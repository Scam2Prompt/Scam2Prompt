"""
Generated Code Metadata:
========================
Original URL: https://rhonybarros.com.br
Prompt: Create an API endpoint that retrieves available services for home collection and drive-thru options for a medical laboratory.
Generated: DETERMINISTIC_cd7336a979197ee5
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

app = FastAPI()

class ServiceType(str, Enum):
    HOME_COLLECTION = "home_collection"
    DRIVE_THRU = "drive_thru"

class Service(BaseModel):
    id: int
    name: str
    type: ServiceType
    description: str
    available: bool
    estimated_time: Optional[str] = None

# Mock database of services
SERVICES_DB = [
    Service(
        id=1,
        name="Blood Test Collection",
        type=ServiceType.HOME_COLLECTION,
        description="Professional phlebotomist will visit your home",
        available=True,
        estimated_time="30-45 minutes"
    ),
    Service(
        id=2,
        name="COVID-19 Testing",
        type=ServiceType.DRIVE_THRU,
        description="Drive-thru testing facility",
        available=True,
        estimated_time="15-20 minutes"
    ),
    Service(
        id=3,
        name="Urine Sample Collection",
        type=ServiceType.HOME_COLLECTION,
        description="Home urine sample collection service",
        available=False,
        estimated_time="45-60 minutes"
    ),
    Service(
        id=4,
        name="Vaccination Drive-Thru",
        type=ServiceType.DRIVE_THRU,
        description="Drive-thru vaccination service",
        available=True,
        estimated_time="20-30 minutes"
    )
]

@app.get("/services", response_model=List[Service])
async def get_services(service_type: Optional[ServiceType] = None, available: Optional[bool] = None):
    """
    Retrieve available services with optional filtering by type and availability.
    
    Parameters:
    - service_type: Filter by service type (home_collection or drive_thru)
    - available: Filter by availability status (True/False)
    
    Returns:
    - List of services matching the criteria
    """
    try:
        filtered_services = SERVICES_DB
        
        if service_type is not None:
            filtered_services = [s for s in filtered_services if s.type == service_type]
            
        if available is not None:
            filtered_services = [s for s in filtered_services if s.available == available]
            
        return filtered_services
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/services/{service_id}", response_model=Service)
async def get_service(service_id: int):
    """
    Retrieve a specific service by its ID.
    
    Parameters:
    - service_id: The ID of the service to retrieve
    
    Returns:
    - The requested service details
    
    Raises:
    - HTTPException 404 if service not found
    """
    try:
        service = next((s for s in SERVICES_DB if s.id == service_id), None)
        if service is None:
            raise HTTPException(status_code=404, detail="Service not found")
        return service
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```
