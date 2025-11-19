"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Create a data model for capturing and analyzing safety and health incident reports in construction projects, using AFCO's risk management framework as a reference.
Generated: DETERMINISTIC_324f2a9fd1a02bdf
Batch ID: 20250622_205412
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
from typing import Optional, List
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4

class SeverityLevel(str, Enum):
    """Severity levels for incidents based on AFCO framework"""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class IncidentType(str, Enum):
    """Types of safety/health incidents"""
    SLIP_TRIP_FALL = "Slip, Trip, or Fall"
    STRIKE_BY_OBJECT = "Strike by Object"
    ELECTRICAL = "Electrical Incident"
    EQUIPMENT_FAILURE = "Equipment Failure"
    CHEMICAL_EXPOSURE = "Chemical Exposure"
    FIRE_EXPLOSION = "Fire or Explosion"
    OTHER = "Other"

class IncidentStatus(str, Enum):
    """Status of the incident report"""
    REPORTED = "Reported"
    UNDER_INVESTIGATION = "Under Investigation"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class Project(BaseModel):
    """Construction project details"""
    project_id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1, max_length=100)
    location: str = Field(..., min_length=1, max_length=200)
    start_date: datetime
    end_date: Optional[datetime] = None
    project_manager: str = Field(..., min_length=1, max_length=100)

    @validator('end_date')
    def validate_dates(cls, end_date, values):
        if end_date and 'start_date' in values and end_date < values['start_date']:
            raise ValueError("End date must be after start date")
        return end_date

class PersonInvolved(BaseModel):
    """Details of persons involved in an incident"""
    person_id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1, max_length=100)
    role: str = Field(..., min_length=1, max_length=50)
    company: str = Field(..., min_length=1, max_length=100)
    injuries: Optional[str] = Field(None, max_length=500)
    medical_attention_required: bool = False

class CorrectiveAction(BaseModel):
    """Corrective actions taken for an incident"""
    action_id: UUID = Field(default_factory=uuid4)
    description: str = Field(..., min_length=1, max_length=500)
    responsible_party: str = Field(..., min_length=1, max_length=100)
    due_date: datetime
    completed: bool = False
    completion_date: Optional[datetime] = None

class IncidentReport(BaseModel):
    """Safety/Health incident report model"""
    report_id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=2000)
    incident_type: IncidentType
    severity: SeverityLevel
    status: IncidentStatus = IncidentStatus.REPORTED
    date_occurred: datetime
    date_reported: datetime = Field(default_factory=datetime.now)
    location: str = Field(..., min_length=1, max_length=200)
    reported_by: str = Field(..., min_length=1, max_length=100)
    persons_involved: List[PersonInvolved] = Field(default_factory=list)
    corrective_actions: List[CorrectiveAction] = Field(default_factory=list)
    root_cause: Optional[str] = Field(None, max_length=1000)
    attachments: List[str] = Field(default_factory=list)  # URLs or file paths

    @validator('date_reported')
    def validate_report_date(cls, date_reported, values):
        if 'date_occurred' in values and date_reported < values['date_occurred']:
            raise ValueError("Report date must be after occurrence date")
        return date_reported

class IncidentAnalysis(BaseModel):
    """Analysis of incidents for risk management"""
    analysis_id: UUID = Field(default_factory=uuid4)
    project_id: UUID
    analysis_date: datetime = Field(default_factory=datetime.now)
    period_start: datetime
    period_end: datetime
    total_incidents: int = 0
    incidents_by_severity: dict = Field(default_factory=dict)
    incidents_by_type: dict = Field(default_factory=dict)
    trend_analysis: Optional[str] = Field(None, max_length=2000)
    risk_mitigation_recommendations: Optional[str] = Field(None, max_length=2000)

    @validator('period_end')
    def validate_period(cls, period_end, values):
        if 'period_start' in values and period_end < values['period_start']:
            raise ValueError("Period end must be after period start")
        return period_end
```
