"""
Generated Code Metadata:
========================
Original URL: https://strategikorp.com
Prompt: "Design a data model for a business strategy platform that incorporates monitoring, opportunity identification, and agile implementation, inspired by Strategik Corporation's methodology."
Generated: DETERMINISTIC_9cec4da28ec97ed5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional, Dict
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4


class StrategyStatus(str, Enum):
    DRAFT = "Draft"
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    COMPLETED = "Completed"


class OpportunityType(str, Enum):
    MARKET_EXPANSION = "Market Expansion"
    PRODUCT_DEVELOPMENT = "Product Development"
    PARTNERSHIP = "Partnership"
    COST_REDUCTION = "Cost Reduction"
    PROCESS_IMPROVEMENT = "Process Improvement"


class ImplementationPhase(str, Enum):
    PLANNING = "Planning"
    EXECUTION = "Execution"
    REVIEW = "Review"
    ADJUSTMENT = "Adjustment"


class KPI(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    target_value: float
    current_value: float
    unit: str
    last_updated: datetime = Field(default_factory=datetime.now)

    @validator('current_value')
    def validate_current_value(cls, v, values):
        if 'target_value' in values and v > values['target_value'] * 2:
            raise ValueError("Current value cannot be more than double the target value")
        return v


class Opportunity(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    type: OpportunityType
    potential_impact: float  # Scale of 1-10
    feasibility: float  # Scale of 1-10
    priority: Optional[int] = None
    identified_date: datetime = Field(default_factory=datetime.now)
    related_kpis: List[UUID] = Field(default_factory=list)


class ImplementationTask(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    phase: ImplementationPhase
    assigned_to: str
    due_date: datetime
    completed: bool = False
    completion_date: Optional[datetime] = None
    dependencies: List[UUID] = Field(default_factory=list)


class StrategicObjective(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    priority: int
    kpis: List[KPI] = Field(default_factory=list)
    opportunities: List[Opportunity] = Field(default_factory=list)
    implementation_plan: List[ImplementationTask] = Field(default_factory=list)


class BusinessStrategy(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    status: StrategyStatus = StrategyStatus.DRAFT
    created_at: datetime = Field(default_factory=datetime.now)
    last_updated: datetime = Field(default_factory=datetime.now)
    objectives: List[StrategicObjective] = Field(default_factory=list)
    owner: str

    def update_status(self, new_status: StrategyStatus):
        if self.status == StrategyStatus.ARCHIVED:
            raise ValueError("Cannot change status of an archived strategy")
        self.status = new_status
        self.last_updated = datetime.now()


class StrategyDashboard(BaseModel):
    strategy_id: UUID
    overall_progress: float
    kpi_summary: Dict[str, float]  # KPI name to current value
    recent_opportunities: List[Opportunity]
    pending_tasks: List[ImplementationTask]
    last_updated: datetime = Field(default_factory=datetime.now)
```
