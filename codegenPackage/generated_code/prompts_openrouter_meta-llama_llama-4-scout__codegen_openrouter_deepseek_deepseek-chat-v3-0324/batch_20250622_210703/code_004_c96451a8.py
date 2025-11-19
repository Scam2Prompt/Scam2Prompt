"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: "Design a data model for tracking project progress and performance metrics in a business intelligence system similar to what Jau Consulting provides."
Generated: DETERMINISTIC_c96451a87d9918c3
Batch ID: 20250622_210703
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
from enum import Enum
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

class ProjectStatus(str, Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    ON_HOLD = "On Hold"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class MetricType(str, Enum):
    FINANCIAL = "Financial"
    OPERATIONAL = "Operational"
    CUSTOMER = "Customer"
    EMPLOYEE = "Employee"

class MetricFrequency(str, Enum):
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    YEARLY = "Yearly"

class Metric(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    metric_type: MetricType
    target_value: float
    current_value: float
    unit: str
    frequency: MetricFrequency
    project_id: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('current_value', 'target_value')
    def validate_values(cls, v):
        if v < 0:
            raise ValueError("Value cannot be negative")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Customer Satisfaction Score",
                "description": "Average customer satisfaction rating",
                "metric_type": "Customer",
                "target_value": 90.0,
                "current_value": 85.5,
                "unit": "points",
                "frequency": "Monthly"
            }
        }

class Project(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    start_date: datetime
    end_date: Optional[datetime] = None
    status: ProjectStatus = ProjectStatus.NOT_STARTED
    client_id: UUID
    manager_id: UUID
    budget: float
    actual_cost: float = 0.0
    metrics: List[Metric] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator('budget', 'actual_cost')
    def validate_costs(cls, v):
        if v < 0:
            raise ValueError("Cost cannot be negative")
        return v

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if v and 'start_date' in values and v < values['start_date']:
            raise ValueError("End date cannot be before start date")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "name": "BI Dashboard Implementation",
                "description": "Implementation of business intelligence dashboard for client",
                "start_date": "2023-01-01T00:00:00",
                "end_date": "2023-06-30T00:00:00",
                "status": "In Progress",
                "client_id": "123e4567-e89b-12d3-a456-426614174000",
                "manager_id": "123e4567-e89b-12d3-a456-426614174001",
                "budget": 50000.0,
                "actual_cost": 35000.0
            }
        }

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None
    end_date: Optional[datetime] = None
    actual_cost: Optional[float] = None

    @validator('actual_cost')
    def validate_costs(cls, v):
        if v is not None and v < 0:
            raise ValueError("Cost cannot be negative")
        return v

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if v and 'start_date' in values and v < values['start_date']:
            raise ValueError("End date cannot be before start date")
        return v

class MetricUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    current_value: Optional[float] = None
    target_value: Optional[float] = None

    @validator('current_value', 'target_value')
    def validate_values(cls, v):
        if v is not None and v < 0:
            raise ValueError("Value cannot be negative")
        return v

class ProjectProgressReport(BaseModel):
    project_id: UUID
    report_date: datetime = Field(default_factory=datetime.utcnow)
    completion_percentage: float = Field(..., ge=0, le=100)
    status_summary: str
    financial_status: str
    risks_and_issues: List[str] = []
    next_steps: List[str] = []

    @validator('completion_percentage')
    def validate_percentage(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("Percentage must be between 0 and 100")
        return v
```
