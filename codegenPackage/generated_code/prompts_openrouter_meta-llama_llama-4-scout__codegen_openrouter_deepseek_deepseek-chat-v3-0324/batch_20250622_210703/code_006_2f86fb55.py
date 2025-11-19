"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: "Design a data model for storing and managing information related to environmental impact assessments for electrical power projects, inspired by Marod Consultores' experience in EIA studies and reporting."
Generated: DETERMINISTIC_2f86fb5508bc61a8
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
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

class AssessmentStatus(str, Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    APPROVED = "approved"
    REJECTED = "rejected"

class ImpactType(str, Enum):
    AIR_QUALITY = "air_quality"
    WATER_QUALITY = "water_quality"
    SOIL_QUALITY = "soil_quality"
    NOISE = "noise"
    BIODIVERSITY = "biodiversity"
    LAND_USE = "land_use"
    SOCIAL = "social"
    ECONOMIC = "economic"

class ImpactSeverity(str, Enum):
    NEGLIGIBLE = "negligible"
    MINOR = "minor"
    MODERATE = "moderate"
    MAJOR = "major"
    SEVERE = "severe"

class MitigationMeasure(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    description: str
    implementation_status: str
    effectiveness: str
    cost_estimate: Optional[float] = None
    responsible_party: str

class EnvironmentalImpact(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    impact_type: ImpactType
    description: str
    severity: ImpactSeverity
    duration: str  # e.g., "short-term", "long-term"
    is_reversible: bool
    mitigation_measures: List[MitigationMeasure] = []

class Stakeholder(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    organization: Optional[str] = None
    contact_email: str
    role: str
    concerns: Optional[str] = None

class PowerProject(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    location: str
    project_type: str  # e.g., "wind", "solar", "hydro"
    capacity_mw: float
    start_date: datetime
    end_date: datetime
    description: Optional[str] = None

    @validator("end_date")
    def validate_dates(cls, end_date, values):
        if "start_date" in values and end_date <= values["start_date"]:
            raise ValueError("End date must be after start date")
        return end_date

class EnvironmentalAssessment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    assessment_date: datetime = Field(default_factory=datetime.now)
    status: AssessmentStatus = AssessmentStatus.PLANNED
    lead_assessor: str
    team_members: List[str] = []
    impacts: List[EnvironmentalImpact] = []
    stakeholders: List[Stakeholder] = []
    summary: Optional[str] = None
    recommendations: Optional[str] = None
    approval_date: Optional[datetime] = None
    approval_authority: Optional[str] = None

    def add_impact(self, impact: EnvironmentalImpact):
        self.impacts.append(impact)

    def add_stakeholder(self, stakeholder: Stakeholder):
        self.stakeholders.append(stakeholder)

    def add_team_member(self, member: str):
        self.team_members.append(member)

class AssessmentRepository:
    def __init__(self):
        self.assessments: List[EnvironmentalAssessment] = []
        self.projects: List[PowerProject] = []

    def create_project(self, project: PowerProject) -> PowerProject:
        self.projects.append(project)
        return project

    def get_project(self, project_id: UUID) -> Optional[PowerProject]:
        return next((p for p in self.projects if p.id == project_id), None)

    def create_assessment(self, assessment: EnvironmentalAssessment) -> EnvironmentalAssessment:
        self.assessments.append(assessment)
        return assessment

    def get_assessment(self, assessment_id: UUID) -> Optional[EnvironmentalAssessment]:
        return next((a for a in self.assessments if a.id == assessment_id), None)

    def get_assessments_by_project(self, project_id: UUID) -> List[EnvironmentalAssessment]:
        return [a for a in self.assessments if a.project_id == project_id]

    def update_assessment_status(
        self, 
        assessment_id: UUID, 
        new_status: AssessmentStatus,
        approval_date: Optional[datetime] = None,
        approval_authority: Optional[str] = None
    ) -> Optional[EnvironmentalAssessment]:
        assessment = self.get_assessment(assessment_id)
        if assessment:
            assessment.status = new_status
            if new_status == AssessmentStatus.APPROVED:
                assessment.approval_date = approval_date or datetime.now()
                assessment.approval_authority = approval_authority
        return assessment
```
