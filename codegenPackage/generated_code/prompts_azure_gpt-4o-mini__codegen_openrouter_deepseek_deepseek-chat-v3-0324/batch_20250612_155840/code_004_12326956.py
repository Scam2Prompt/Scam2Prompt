"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: Create a RESTful API specification for a service that provides consulting on sanitary infrastructure, based on the services offered by AJP Ingenieros.
Generated: DETERMINISTIC_1232695619dbe3de
Batch ID: 20250612_155840
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.ajpingenieros.com": {
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
    title="AJP Ingenieros Sanitary Infrastructure Consulting API",
    description="REST API for consulting services on sanitary infrastructure projects",
    version="1.0.0",
    contact={
        "name": "AJP Ingenieros",
        "url": "https://www.ajpingenieros.com",
        "email": "contacto@ajpingenieros.com",
    },
    license_info={
        "name": "Proprietary",
    },
)

class ServiceType(str, Enum):
    water_supply = "water_supply"
    sewerage = "sewerage"
    drainage = "drainage"
    wastewater_treatment = "wastewater_treatment"
    stormwater_management = "stormwater_management"
    hydraulic_modeling = "hydraulic_modeling"

class ProjectStage(str, Enum):
    feasibility = "feasibility"
    design = "design"
    construction = "construction"
    operation = "operation"
    maintenance = "maintenance"

class Consultant(BaseModel):
    id: str
    name: str
    specialization: ServiceType
    experience_years: int
    available: bool

class ProjectRequest(BaseModel):
    client_name: str
    client_email: str
    project_description: str
    service_type: ServiceType
    project_stage: ProjectStage
    estimated_budget: Optional[float] = None
    deadline: Optional[str] = None

class ProjectResponse(BaseModel):
    project_id: str
    assigned_consultant: Consultant
    estimated_timeline: str
    cost_estimate: float
    next_steps: List[str]

# In-memory database for demonstration
db_consultants = [
    Consultant(
        id="c1",
        name="Juan Perez",
        specialization=ServiceType.water_supply,
        experience_years=10,
        available=True
    ),
    Consultant(
        id="c2",
        name="Maria Gomez",
        specialization=ServiceType.wastewater_treatment,
        experience_years=8,
        available=True
    ),
    Consultant(
        id="c3",
        name="Carlos Ruiz",
        specialization=ServiceType.hydraulic_modeling,
        experience_years=12,
        available=False
    )
]

@app.get("/consultants", response_model=List[Consultant], tags=["Consultants"])
async def list_consultants(available: Optional[bool] = None, specialization: Optional[ServiceType] = None):
    """
    Retrieve list of available consultants with optional filters.
    """
    result = db_consultants
    if available is not None:
        result = [c for c in result if c.available == available]
    if specialization is not None:
        result = [c for c in result if c.specialization == specialization]
    return result

@app.get("/consultants/{consultant_id}", response_model=Consultant, tags=["Consultants"])
async def get_consultant(consultant_id: str):
    """
    Get details about a specific consultant by ID.
    """
    consultant = next((c for c in db_consultants if c.id == consultant_id), None)
    if not consultant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Consultant not found"
        )
    return consultant

@app.post("/projects/request", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED, tags=["Projects"])
async def request_project(project: ProjectRequest):
    """
    Submit a new project request for consulting services.
    """
    # Find available consultant with matching specialization
    available_consultants = [
        c for c in db_consultants 
        if c.available and c.specialization == project.service_type
    ]
    
    if not available_consultants:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No available consultants for the requested service"
        )
    
    # Simple assignment logic - pick first available consultant
    assigned_consultant = available_consultants[0]
    
    # Generate response (in a real system, this would involve more complex calculations)
    response = ProjectResponse(
        project_id=f"proj-{len(db_consultants)}",
        assigned_consultant=assigned_consultant,
        estimated_timeline="4-6 weeks",
        cost_estimate=project.estimated_budget * 0.15 if project.estimated_budget else 5000.00,
        next_steps=[
            "Initial consultation meeting",
            "Project scope definition",
            "Contract signing"
        ]
    )
    
    return response

@app.get("/services", response_model=List[str], tags=["Services"])
async def list_services():
    """
    List all available service types.
    """
    return [service.value for service in ServiceType]

@app.get("/project-stages", response_model=List[str], tags=["Projects"])
async def list_project_stages():
    """
    List all available project stages.
    """
    return [stage.value for stage in ProjectStage]
```
