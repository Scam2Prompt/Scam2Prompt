"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Create a data model for tracking patient outcomes and progress in a psychiatry and coaching setting, considering factors like mental health metrics and treatment efficacy.
Generated: DETERMINISTIC_2bb1f8ea57b71f59
Batch ID: 20250622_205139
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

class TreatmentType(str, Enum):
    PSYCHIATRY = "psychiatry"
    COACHING = "coaching"
    COMBINED = "combined"

class MoodRating(int, Enum):
    VERY_LOW = 1
    LOW = 2
    NEUTRAL = 3
    HIGH = 4
    VERY_HIGH = 5

class AnxietyLevel(int, Enum):
    NONE = 0
    MILD = 1
    MODERATE = 2
    SEVERE = 3
    EXTREME = 4

class SleepQuality(int, Enum):
    VERY_POOR = 1
    POOR = 2
    FAIR = 3
    GOOD = 4
    EXCELLENT = 5

class MedicationAdherence(int, Enum):
    NEVER = 1
    RARELY = 2
    SOMETIMES = 3
    OFTEN = 4
    ALWAYS = 5

class SessionOutcome(str, Enum):
    BREAKTHROUGH = "breakthrough"
    IMPROVED = "improved"
    NEUTRAL = "neutral"
    REGRESSED = "regressed"
    CRISIS = "crisis"

class Patient(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    date_of_birth: datetime
    email: Optional[str] = Field(None, regex=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    phone: Optional[str] = Field(None, min_length=10, max_length=15)
    treatment_type: TreatmentType
    registration_date: datetime = Field(default_factory=datetime.now)
    active: bool = True

    @validator('date_of_birth')
    def validate_date_of_birth(cls, v):
        if v > datetime.now():
            raise ValueError("Date of birth cannot be in the future")
        return v

class MentalHealthMetrics(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    patient_id: UUID
    date_recorded: datetime = Field(default_factory=datetime.now)
    mood: MoodRating
    anxiety: AnxietyLevel
    sleep_quality: SleepQuality
    medication_adherence: Optional[MedicationAdherence] = None
    notes: Optional[str] = Field(None, max_length=1000)

    @validator('date_recorded')
    def validate_date_recorded(cls, v):
        if v > datetime.now():
            raise ValueError("Record date cannot be in the future")
        return v

class TreatmentSession(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    patient_id: UUID
    date: datetime
    duration_minutes: int = Field(..., gt=0, le=240)
    treatment_type: TreatmentType
    practitioner: str = Field(..., min_length=1, max_length=100)
    outcome: SessionOutcome
    notes: Optional[str] = Field(None, max_length=2000)
    goals_met: bool
    homework_assigned: Optional[str] = Field(None, max_length=500)

    @validator('date')
    def validate_date(cls, v):
        if v > datetime.now():
            raise ValueError("Session date cannot be in the future")
        return v

class TreatmentPlan(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    patient_id: UUID
    start_date: datetime
    end_date: Optional[datetime] = None
    primary_concern: str = Field(..., min_length=1, max_length=500)
    treatment_goals: List[str] = Field(..., min_items=1)
    frequency_sessions_per_week: int = Field(..., ge=1, le=7)
    active: bool = True

    @validator('end_date')
    def validate_end_date(cls, v, values):
        if v and 'start_date' in values and v < values['start_date']:
            raise ValueError("End date must be after start date")
        return v

class ProgressReport(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    patient_id: UUID
    report_date: datetime = Field(default_factory=datetime.now)
    overall_progress: str = Field(..., min_length=1, max_length=2000)
    challenges: Optional[str] = Field(None, max_length=1000)
    next_steps: str = Field(..., min_length=1, max_length=1000)
    practitioner_comments: Optional[str] = Field(None, max_length=2000)

    @validator('report_date')
    def validate_report_date(cls, v):
        if v > datetime.now():
            raise ValueError("Report date cannot be in the future")
        return v
```
