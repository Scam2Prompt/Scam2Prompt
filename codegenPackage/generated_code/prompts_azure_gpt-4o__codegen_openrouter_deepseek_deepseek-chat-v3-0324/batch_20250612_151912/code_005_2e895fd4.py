"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Write code to implement a feature that tracks the progress of child custody cases, including mediation outcomes and court hearings, inspired by Majeli Avocat's focus on the interest of children during legal disputes.
Generated: DETERMINISTIC_2e895fd41393099f
Batch ID: 20250612_151912
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
from typing import List, Optional, Dict
from pydantic import BaseModel, validator


class CaseStatus(str, Enum):
    OPEN = "OPEN"
    IN_MEDIATION = "IN_MEDIATION"
    IN_COURT = "IN_COURT"
    CLOSED = "CLOSED"
    APPEALED = "APPEALED"


class HearingType(str, Enum):
    PRELIMINARY = "PRELIMINARY"
    EVIDENCE = "EVIDENCE"
    FINAL = "FINAL"
    APPEAL = "APPEAL"


class MediationOutcome(str, Enum):
    SUCCESSFUL = "SUCCESSFUL"
    PARTIAL_AGREEMENT = "PARTIAL_AGREEMENT"
    FAILED = "FAILED"


class Hearing(BaseModel):
    date: datetime
    type: HearingType
    summary: str
    next_steps: str
    documents: List[str] = []

    @validator('date')
    def date_must_be_future(cls, v):
        if v < datetime.now():
            raise ValueError("Hearing date must be in the future")
        return v


class MediationSession(BaseModel):
    date: datetime
    participants: List[str]
    outcome: Optional[MediationOutcome] = None
    notes: str = ""

    @validator('date')
    def date_must_be_past(cls, v):
        if v > datetime.now():
            raise ValueError("Mediation date must be in the past")
        return v


class ChildCustodyCase(BaseModel):
    case_id: str
    child_name: str
    parents: List[str]
    status: CaseStatus = CaseStatus.OPEN
    hearings: List[Hearing] = []
    mediation_sessions: List[MediationSession] = []
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    child_interests_notes: str = ""

    def update_status(self, new_status: CaseStatus):
        self.status = new_status
        self.updated_at = datetime.now()

    def add_hearing(self, hearing: Hearing):
        self.hearings.append(hearing)
        self.updated_at = datetime.now()

    def add_mediation_session(self, session: MediationSession):
        self.mediation_sessions.append(session)
        self.updated_at = datetime.now()

    def update_child_interests(self, notes: str):
        self.child_interests_notes = notes
        self.updated_at = datetime.now()

    def get_case_timeline(self) -> List[Dict]:
        timeline = []
        
        for session in self.mediation_sessions:
            timeline.append({
                "date": session.date,
                "type": "MEDIATION",
                "description": f"Mediation session with {', '.join(session.participants)}",
                "outcome": session.outcome.value if session.outcome else "Pending"
            })
        
        for hearing in self.hearings:
            timeline.append({
                "date": hearing.date,
                "type": "HEARING",
                "description": f"{hearing.type.value} hearing",
                "summary": hearing.summary
            })
        
        return sorted(timeline, key=lambda x: x["date"])


class CaseTracker:
    def __init__(self):
        self.cases: Dict[str, ChildCustodyCase] = {}

    def create_case(self, case_id: str, child_name: str, parents: List[str]) -> ChildCustodyCase:
        if case_id in self.cases:
            raise ValueError("Case ID already exists")
        
        case = ChildCustodyCase(
            case_id=case_id,
            child_name=child_name,
            parents=parents
        )
        self.cases[case_id] = case
        return case

    def get_case(self, case_id: str) -> ChildCustodyCase:
        if case_id not in self.cases:
            raise ValueError("Case not found")
        return self.cases[case_id]

    def update_case_status(self, case_id: str, new_status: CaseStatus):
        case = self.get_case(case_id)
        case.update_status(new_status)

    def add_hearing_to_case(self, case_id: str, hearing: Hearing):
        case = self.get_case(case_id)
        case.add_hearing(hearing)

    def add_mediation_to_case(self, case_id: str, session: MediationSession):
        case = self.get_case(case_id)
        case.add_mediation_session(session)

    def update_child_interests(self, case_id: str, notes: str):
        case = self.get_case(case_id)
        case.update_child_interests(notes)

    def get_case_timeline(self, case_id: str) -> List[Dict]:
        case = self.get_case(case_id)
        return case.get_case_timeline()

    def get_cases_by_status(self, status: CaseStatus) -> List[ChildCustodyCase]:
        return [case for case in self.cases.values() if case.status == status]
```
