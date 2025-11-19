"""
Generated Code Metadata:
========================
Original URL: https://cecd33.fr
Prompt: "Develop a data model or schema to store information about mechanical engineering projects, including project phases, client details, and product specifications, inspired by CECD 33's project management approach."
Generated: DETERMINISTIC_76555ba8ea950e65
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, validator
from enum import Enum

class ProjectPhase(str, Enum):
    CONCEPTUALIZATION = "Conceptualization"
    DESIGN = "Design"
    PROTOTYPING = "Prototyping"
    TESTING = "Testing"
    PRODUCTION = "Production"
    DELIVERY = "Delivery"
    MAINTENANCE = "Maintenance"

class Client(BaseModel):
    id: str = Field(..., description="Unique client identifier")
    name: str = Field(..., max_length=100, description="Client organization name")
    contact_person: str = Field(..., max_length=100, description="Primary contact person")
    email: EmailStr = Field(..., description="Contact email address")
    phone: str = Field(..., max_length=20, description="Contact phone number")
    address: str = Field(..., max_length=200, description="Physical address")
    tax_id: Optional[str] = Field(None, max_length=50, description="Tax identification number")

class MaterialSpecification(BaseModel):
    name: str = Field(..., max_length=100, description="Material name")
    grade: str = Field(..., max_length=50, description="Material grade/specification")
    quantity: float = Field(..., gt=0, description="Quantity required")
    unit: str = Field(..., max_length=20, description="Measurement unit")

class ProductSpecification(BaseModel):
    name: str = Field(..., max_length=100, description="Product name")
    description: str = Field(..., max_length=500, description="Detailed description")
    dimensions: str = Field(..., max_length=100, description="Product dimensions")
    weight: Optional[float] = Field(None, gt=0, description="Product weight in kg")
    materials: List[MaterialSpecification] = Field(..., description="List of materials used")

class Project(BaseModel):
    id: str = Field(..., description="Unique project identifier")
    name: str = Field(..., max_length=100, description="Project name")
    description: str = Field(..., max_length=500, description="Project description")
    start_date: datetime = Field(..., description="Project start date")
    end_date: Optional[datetime] = Field(None, description="Project end date")
    current_phase: ProjectPhase = Field(..., description="Current project phase")
    client: Client = Field(..., description="Client details")
    product_specs: ProductSpecification = Field(..., description="Product specifications")
    budget: float = Field(..., gt=0, description="Project budget in USD")
    team_members: List[str] = Field(..., description="List of team member IDs")
    documents: List[str] = Field(default_factory=list, description="List of document IDs")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if v and 'start_date' in values and v < values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100, description="Project name")
    description: Optional[str] = Field(None, max_length=500, description="Project description")
    end_date: Optional[datetime] = Field(None, description="Project end date")
    current_phase: Optional[ProjectPhase] = Field(None, description="Current project phase")
    budget: Optional[float] = Field(None, gt=0, description="Project budget in USD")
    team_members: Optional[List[str]] = Field(None, description="List of team member IDs")
    documents: Optional[List[str]] = Field(None, description="List of document IDs")

    class Config:
        extra = "forbid"
```
