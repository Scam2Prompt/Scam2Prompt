"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Design a data model for storing information about luxury property developments, including project details, client information, and quality control metrics.
Generated: DETERMINISTIC_7851243430387304
Batch ID: 20250622_205348
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
from pydantic import BaseModel, Field, EmailStr, validator
from uuid import UUID, uuid4


class PropertyType(str, Enum):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    MIXED_USE = "mixed_use"
    HOTEL = "hotel"
    OTHER = "other"


class ProjectStatus(str, Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    CANCELLED = "cancelled"


class ClientType(str, Enum):
    INDIVIDUAL = "individual"
    CORPORATION = "corporation"
    GOVERNMENT = "government"
    OTHER = "other"


class QualityRating(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    AVERAGE = "average"
    BELOW_AVERAGE = "below_average"
    POOR = "poor"


class Address(BaseModel):
    street: str = Field(..., min_length=1, max_length=255)
    city: str = Field(..., min_length=1, max_length=100)
    state: str = Field(..., min_length=1, max_length=100)
    postal_code: str = Field(..., min_length=1, max_length=20)
    country: str = Field(..., min_length=1, max_length=100)


class Client(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1, max_length=255)
    type: ClientType
    contact_email: EmailStr
    contact_phone: str = Field(..., min_length=5, max_length=20)
    address: Address
    tax_id: Optional[str] = Field(None, min_length=1, max_length=50)
    notes: Optional[str] = None


class QualityControlMetric(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    inspection_date: datetime
    inspector_name: str = Field(..., min_length=1, max_length=255)
    overall_rating: QualityRating
    structural_rating: QualityRating
    finish_rating: QualityRating
    safety_rating: QualityRating
    notes: Optional[str] = None


class Amenity(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None


class UnitType(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    size_sqft: float = Field(..., gt=0)
    base_price: float = Field(..., gt=0)


class DevelopmentProject(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1, max_length=2000)
    property_type: PropertyType
    status: ProjectStatus
    start_date: datetime
    estimated_completion_date: Optional[datetime] = None
    actual_completion_date: Optional[datetime] = None
    address: Address
    client_id: UUID
    architect: str = Field(..., min_length=1, max_length=255)
    contractor: str = Field(..., min_length=1, max_length=255)
    total_units: int = Field(..., gt=0)
    total_area_sqft: float = Field(..., gt=0)
    amenities: List[Amenity] = Field(default_factory=list)
    unit_types: List[UnitType] = Field(default_factory=list)
    quality_metrics: List[QualityControlMetric] = Field(default_factory=list)
    
    @validator('estimated_completion_date', 'actual_completion_date')
    def validate_completion_dates(cls, v, values):
        if v and 'start_date' in values and v < values['start_date']:
            raise ValueError("Completion date must be after start date")
        return v


class ProjectUpdate(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.now)
    author: str = Field(..., min_length=1, max_length=255)
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1, max_length=5000)
    attachments: List[str] = Field(default_factory=list)


class ProjectFinancial(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    budget: float = Field(..., gt=0)
    current_spend: float = Field(..., ge=0)
    projected_final_cost: float = Field(..., gt=0)
    last_updated: datetime = Field(default_factory=datetime.now)
    
    @validator('current_spend')
    def validate_current_spend(cls, v, values):
        if 'budget' in values and v > values['budget'] * 1.2:
            raise ValueError("Current spend exceeds budget by more than 20%")
        return v
```
