"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Create a REST API endpoint that retrieves information about the "Temeljne sustavne podrške" offered by Udruga Radost Ogulin for local organizations.
Generated: DETERMINISTIC_a95f6a5eb57e662c
Batch ID: 20250612_162051
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
import uvicorn

app = FastAPI(
    title="Udruga Radost Ogulin API",
    description="API for accessing information about 'Temeljne sustavne podrške' services",
    version="1.0.0"
)

class SupportService(BaseModel):
    """Model representing a support service offered by Udruga Radost Ogulin"""
    id: int
    name: str
    description: str
    target_organizations: List[str]
    contact_email: str
    contact_phone: str
    available: bool = True

# Mock database of support services
SUPPORT_SERVICES_DB = [
    SupportService(
        id=1,
        name="Psihološka podrška",
        description="Individualne i grupne psihološke usluge za djelatnike organizacija",
        target_organizations=["NVO", "škole", "vrtići"],
        contact_email="psihologija@radost-ogulin.hr",
        contact_phone="+385 47 123 456",
        available=True
    ),
    SupportService(
        id=2,
        name="Edukacije i radionice",
        description="Organizacija edukacija i radionica po potrebama organizacija",
        target_organizations=["NVO", "škole", "vrtići", "javne ustanove"],
        contact_email="edukacije@radost-ogulin.hr",
        contact_phone="+385 47 123 457",
        available=True
    ),
    SupportService(
        id=3,
        name="Supervizije",
        description="Stručne supervizije za timove organizacija",
        target_organizations=["NVO", "socijalne ustanove"],
        contact_email="supervizije@radost-ogulin.hr",
        contact_phone="+385 47 123 458",
        available=False
    )
]

@app.get(
    "/support-services",
    response_model=List[SupportService],
    summary="Get all support services",
    description="Retrieve information about all 'Temeljne sustavne podrške' services offered by Udruga Radost Ogulin"
)
async def get_all_support_services():
    """Retrieve all support services from the database"""
    return SUPPORT_SERVICES_DB

@app.get(
    "/support-services/{service_id}",
    response_model=SupportService,
    summary="Get specific support service",
    description="Retrieve information about a specific 'Temeljne sustavne podrške' service by ID",
    responses={
        404: {"description": "Service not found"}
    }
)
async def get_support_service(service_id: int):
    """Retrieve a specific support service by ID"""
    service = next((s for s in SUPPORT_SERVICES_DB if s.id == service_id), None)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@app.get(
    "/support-services/organization-type/{org_type}",
    response_model=List[SupportService],
    summary="Get services for organization type",
    description="Retrieve support services available for a specific type of organization",
    responses={
        404: {"description": "No services found for this organization type"}
    }
)
async def get_services_for_organization(org_type: str):
    """Retrieve support services available for a specific organization type"""
    org_type_lower = org_type.lower()
    services = [s for s in SUPPORT_SERVICES_DB 
                if org_type_lower in [o.lower() for o in s.target_organizations]]
    
    if not services:
        raise HTTPException(
            status_code=404,
            detail=f"No services found for organization type: {org_type}"
        )
    return services

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
