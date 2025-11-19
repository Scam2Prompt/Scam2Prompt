"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Design a data model for managing industrial maintenance requests, including scheduling and resource allocation, inspired by Tether's maintenance services."
Generated: DETERMINISTIC_ee6b7d62aa1dad68
Batch ID: 20250622_205302
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


class MaintenancePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class MaintenanceStatus(str, Enum):
    PENDING = "pending"
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Technician(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    specialization: str
    contact_number: str
    email: str
    is_available: bool = True


class Equipment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    location: str
    manufacturer: str
    model_number: str
    last_maintenance_date: Optional[datetime] = None
    maintenance_frequency_days: int = 30


class MaintenanceRequest(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    equipment_id: UUID
    description: str
    priority: MaintenancePriority = MaintenancePriority.MEDIUM
    status: MaintenanceStatus = MaintenanceStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    created_by: str
    scheduled_start: Optional[datetime] = None
    scheduled_end: Optional[datetime] = None
    assigned_technician_id: Optional[UUID] = None
    actual_start: Optional[datetime] = None
    actual_end: Optional[datetime] = None
    notes: List[str] = Field(default_factory=list)

    @validator('scheduled_end')
    def validate_scheduled_end(cls, v, values):
        if 'scheduled_start' in values and v:
            if v <= values['scheduled_start']:
                raise ValueError("Scheduled end must be after scheduled start")
        return v

    @validator('actual_end')
    def validate_actual_end(cls, v, values):
        if 'actual_start' in values and v:
            if v <= values['actual_start']:
                raise ValueError("Actual end must be after actual start")
        return v


class MaintenanceSchedule(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    request_id: UUID
    technician_id: UUID
    scheduled_start: datetime
    scheduled_end: datetime
    status: MaintenanceStatus = MaintenanceStatus.SCHEDULED


class ResourceAllocation(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    request_id: UUID
    technician_ids: List[UUID]
    tools_required: List[str]
    parts_required: List[str]
    estimated_duration_minutes: int
    allocated_at: datetime = Field(default_factory=datetime.utcnow)


class MaintenanceHistory(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    request_id: UUID
    equipment_id: UUID
    maintenance_date: datetime
    technician_id: UUID
    actions_performed: List[str]
    parts_replaced: List[str]
    duration_minutes: int
    notes: str
```
