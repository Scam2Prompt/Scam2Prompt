"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Create a simple API to retrieve information about Jupiter Design & Manufacturing's services, including CNC cutting, punching, welding, and part repair, and their corresponding specifications.
Generated: DETERMINISTIC_cfa6385d1aea28de
Batch ID: 20250622_211652
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

app = FastAPI(
    title="Jupiter Design & Manufacturing Services API",
    description="API to retrieve information about Jupiter Design & Manufacturing's services",
    version="1.0.0"
)

class ServiceSpecs(BaseModel):
    """Model representing specifications for a manufacturing service"""
    material_thickness: str
    tolerance: str
    max_part_size: str
    finish_options: List[str]

class Service(BaseModel):
    """Model representing a manufacturing service"""
    name: str
    description: str
    capabilities: List[str]
    specifications: ServiceSpecs
    lead_time: Optional[str] = None

# Sample data - in production this would typically come from a database
SERVICES = {
    "cnc_cutting": Service(
        name="CNC Cutting",
        description="Precision CNC cutting services for various materials",
        capabilities=["Flat sheet cutting", "Contour cutting", "Bevel cutting"],
        specifications=ServiceSpecs(
            material_thickness="0.5mm to 25mm",
            tolerance="±0.1mm",
            max_part_size="3000mm x 1500mm",
            finish_options=["As-cut", "Deburred", "Powder coated"]
        ),
        lead_time="3-5 business days"
    ),
    "punching": Service(
        name="Punching",
        description="High-speed punching services for sheet metal",
        capabilities=["Hole punching", "Perforations", "Forming operations"],
        specifications=ServiceSpecs(
            material_thickness="0.5mm to 6mm",
            tolerance="±0.2mm",
            max_part_size="2500mm x 1250mm",
            finish_options=["As-punched", "Deburred"]
        )
    ),
    "welding": Service(
        name="Welding",
        description="Professional welding services for metal fabrication",
        capabilities=["MIG welding", "TIG welding", "Spot welding", "Seam welding"],
        specifications=ServiceSpecs(
            material_thickness="0.5mm to 50mm",
            tolerance="±0.5mm",
            max_part_size="Custom based on project",
            finish_options=["As-welded", "Grinded", "Painted"]
        ),
        lead_time="5-7 business days"
    ),
    "part_repair": Service(
        name="Part Repair",
        description="Expert repair and refurbishment of metal parts",
        capabilities=["Crack repair", "Wear restoration", "Geometry correction"],
        specifications=ServiceSpecs(
            material_thickness="Any",
            tolerance="Depends on part requirements",
            max_part_size="Custom based on part",
            finish_options=["As-repaired", "Refinished to match original"]
        )
    )
}

@app.get("/services", response_model=List[Service], tags=["Services"])
async def get_all_services():
    """Retrieve all available services"""
    return list(SERVICES.values())

@app.get("/services/{service_id}", response_model=Service, tags=["Services"])
async def get_service(service_id: str):
    """Retrieve details for a specific service by ID"""
    if service_id not in SERVICES:
        raise HTTPException(status_code=404, detail="Service not found")
    return SERVICES[service_id]

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Jupiter Design & Manufacturing Services API",
        "version": app.version,
        "docs": "/docs"
    }

# Error handler for validation errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Run with: uvicorn main:app --reload
```
