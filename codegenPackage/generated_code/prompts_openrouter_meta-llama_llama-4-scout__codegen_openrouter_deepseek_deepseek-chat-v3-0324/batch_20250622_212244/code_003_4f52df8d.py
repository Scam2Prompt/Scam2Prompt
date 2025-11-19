"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Design a data model for storing client project information and maintenance records, considering the requirements of a company like SET Ingeniería."
Generated: DETERMINISTIC_4f52df8dc5f937a4
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, validator
from enum import Enum

class ProjectStatus(str, Enum):
    PLANNING = "Planning"
    IN_PROGRESS = "In Progress"
    ON_HOLD = "On Hold"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class MaintenanceType(str, Enum):
    PREVENTIVE = "Preventive"
    CORRECTIVE = "Corrective"
    PREDICTIVE = "Predictive"

class Client(BaseModel):
    """
    Represents a client entity.
    """
    id: str = Field(..., description="Unique identifier for the client")
    name: str = Field(..., max_length=100, description="Client's full name")
    email: EmailStr = Field(..., description="Client's email address")
    phone: str = Field(..., max_length=20, description="Client's phone number")
    address: str = Field(..., max_length=200, description="Client's physical address")
    tax_id: str = Field(..., max_length=50, description="Client's tax identification number")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")

    @validator('phone')
    def validate_phone(cls, v):
        if not v.isdigit():
            raise ValueError("Phone number must contain only digits")
        return v

class Project(BaseModel):
    """
    Represents a project entity.
    """
    id: str = Field(..., description="Unique identifier for the project")
    client_id: str = Field(..., description="Reference to the client")
    name: str = Field(..., max_length=100, description="Project name")
    description: str = Field(..., max_length=500, description="Project description")
    start_date: datetime = Field(..., description="Project start date")
    end_date: Optional[datetime] = Field(None, description="Project end date")
    status: ProjectStatus = Field(default=ProjectStatus.PLANNING, description="Current project status")
    budget: float = Field(..., ge=0, description="Project budget")
    team_lead: str = Field(..., max_length=100, description="Project team lead")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")

    @validator('end_date')
    def validate_dates(cls, v, values):
        if v and 'start_date' in values and v < values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class MaintenanceRecord(BaseModel):
    """
    Represents a maintenance record entity.
    """
    id: str = Field(..., description="Unique identifier for the maintenance record")
    project_id: str = Field(..., description="Reference to the project")
    type: MaintenanceType = Field(..., description="Type of maintenance")
    description: str = Field(..., max_length=500, description="Maintenance description")
    performed_by: str = Field(..., max_length=100, description="Person who performed the maintenance")
    performed_at: datetime = Field(..., description="When maintenance was performed")
    cost: float = Field(..., ge=0, description="Cost of maintenance")
    parts_used: Optional[List[str]] = Field(None, description="List of parts used in maintenance")
    next_maintenance_date: Optional[datetime] = Field(None, description="Next scheduled maintenance date")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")

class ProjectWithMaintenance(BaseModel):
    """
    Represents a project with its maintenance records.
    """
    project: Project
    maintenance_records: List[MaintenanceRecord] = Field(default_factory=list)
```
