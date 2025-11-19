"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: "Design a data model for storing information on community development projects, including details on vacant buildings, project goals, and outcomes, based on the Starke Orte Netzwerk's approach to gemeinwohlorientierte Bestandsentwicklung."
Generated: DETERMINISTIC_60691354f752ffd9
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

class ProjectStatus(str, Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class BuildingType(str, Enum):
    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    INDUSTRIAL = "industrial"
    MIXED_USE = "mixed_use"
    OTHER = "other"

class OwnershipType(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    COMMUNITY = "community"
    COOPERATIVE = "cooperative"

class VacantBuilding(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    address: str
    building_type: BuildingType
    square_meters: float
    ownership: OwnershipType
    vacant_since: datetime
    condition_rating: int = Field(ge=1, le=5)
    historical_significance: bool = False
    photos: List[str] = []
    description: Optional[str] = None

    @validator('condition_rating')
    def validate_condition_rating(cls, v):
        if v < 1 or v > 5:
            raise ValueError("Condition rating must be between 1 and 5")
        return v

class ProjectGoal(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    description: str
    priority: int = Field(ge=1, le=3)
    target_completion_date: Optional[datetime] = None
    metrics: List[str] = []

class ProjectOutcome(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    description: str
    impact_rating: int = Field(ge=1, le=5)
    date_recorded: datetime = Field(default_factory=datetime.now)
    supporting_documents: List[str] = []

    @validator('impact_rating')
    def validate_impact_rating(cls, v):
        if v < 1 or v > 5:
            raise ValueError("Impact rating must be between 1 and 5")
        return v

class Stakeholder(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    organization: Optional[str] = None
    role: str
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None

class CommunityDevelopmentProject(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    status: ProjectStatus = ProjectStatus.PLANNING
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    vacant_buildings: List[VacantBuilding] = []
    goals: List[ProjectGoal] = []
    outcomes: List[ProjectOutcome] = []
    stakeholders: List[Stakeholder] = []
    funding_sources: List[str] = []
    tags: List[str] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def update_timestamp(self):
        self.updated_at = datetime.now()

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
```
