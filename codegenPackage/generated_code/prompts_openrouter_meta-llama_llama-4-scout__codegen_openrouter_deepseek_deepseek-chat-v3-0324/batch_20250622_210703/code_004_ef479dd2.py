"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: "Create a RESTful API endpoint to retrieve information about eControl SA's electrical services, including their areas of expertise, such as electrical studies and projects, and security installations."
Generated: DETERMINISTIC_ef479dd2000c1a37
Batch ID: 20250622_210703
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
    title="eControl SA Electrical Services API",
    description="API to retrieve information about eControl SA's electrical services",
    version="1.0.0"
)

class Service(BaseModel):
    """Model representing an electrical service offered by eControl SA"""
    id: int
    name: str
    description: str
    expertise_areas: List[str]
    projects_completed: Optional[int] = None

# Mock database
services_db = [
    Service(
        id=1,
        name="Electrical Studies",
        description="Comprehensive electrical system analysis and planning",
        expertise_areas=["Load Flow Analysis", "Short Circuit Studies", "Protection Coordination"],
        projects_completed=150
    ),
    Service(
        id=2,
        name="Electrical Projects",
        description="Design and implementation of electrical systems",
        expertise_areas=["HV/LV Systems", "Substation Design", "Power Distribution"],
        projects_completed=200
    ),
    Service(
        id=3,
        name="Security Installations",
        description="Installation of security and surveillance systems",
        expertise_areas=["CCTV Systems", "Access Control", "Intrusion Detection"],
        projects_completed=75
    )
]

@app.get("/services", response_model=List[Service], tags=["Services"])
async def get_all_services():
    """Retrieve all electrical services offered by eControl SA"""
    return services_db

@app.get("/services/{service_id}", response_model=Service, tags=["Services"])
async def get_service(service_id: int):
    """Retrieve a specific electrical service by ID"""
    service = next((s for s in services_db if s.id == service_id), None)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@app.get("/services/expertise/{expertise}", response_model=List[Service], tags=["Services"])
async def get_services_by_expertise(expertise: str):
    """Retrieve services that include a specific expertise area"""
    matched_services = [s for s in services_db if expertise.lower() in [e.lower() for e in s.expertise_areas]]
    if not matched_services:
        raise HTTPException(
            status_code=404,
            detail=f"No services found with expertise: {expertise}"
        )
    return matched_services

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
