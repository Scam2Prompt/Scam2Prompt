"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Develop a code snippet to track staff competency in infection prevention and control measures, as required by Shareth Homecare Services' outbreak prevention program."
Generated: DETERMINISTIC_1a4cf8f2a8a089a7
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional

class CompetencyLevel(Enum):
    """Enum representing staff competency levels in infection prevention."""
    NOVICE = 1
    COMPETENT = 2
    EXPERT = 3

class TrainingModule:
    """Represents a training module for infection prevention."""
    def __init__(self, name: str, description: str, duration_hours: float):
        self.name = name
        self.description = description
        self.duration_hours = duration_hours

class StaffMember:
    """Represents a staff member and their competency tracking."""
    def __init__(self, staff_id: str, name: str, role: str):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.competency_level = CompetencyLevel.NOVICE
        self.training_history: List[Dict] = []
        self.last_assessment_date: Optional[datetime.date] = None

    def complete_training(self, module: TrainingModule, date_completed: datetime.date) -> None:
        """Record completion of a training module."""
        self.training_history.append({
            'module': module.name,
            'date_completed': date_completed,
            'duration_hours': module.duration_hours
        })
        self._update_competency()

    def complete_assessment(self, date: datetime.date, passed: bool) -> None:
        """Record completion of a competency assessment."""
        if passed:
            if self.competency_level.value < CompetencyLevel.EXPERT.value:
                self.competency_level = CompetencyLevel(self.competency_level.value + 1)
        self.last_assessment_date = date

    def _update_competency(self) -> None:
        """Update competency level based on training hours."""
        total_hours = sum(t['duration_hours'] for t in self.training_history)
        if total_hours >= 20:
            self.competency_level = CompetencyLevel.EXPERT
        elif total_hours >= 10:
            self.competency_level = CompetencyLevel.COMPETENT

    def is_competency_current(self) -> bool:
        """Check if competency assessment is current (within last year)."""
        if not self.last_assessment_date:
            return False
        return (datetime.date.today() - self.last_assessment_date).days <= 365

class CompetencyTracker:
    """Tracks infection prevention competency for all staff."""
    def __init__(self):
        self.staff_members: Dict[str, StaffMember] = {}
        self.training_modules: Dict[str, TrainingModule] = {}

    def add_staff_member(self, staff_id: str, name: str, role: str) -> None:
        """Add a new staff member to the tracker."""
        if staff_id in self.staff_members:
            raise ValueError(f"Staff ID {staff_id} already exists")
        self.staff_members[staff_id] = StaffMember(staff_id, name, role)

    def add_training_module(self, name: str, description: str, duration_hours: float) -> None:
        """Add a new training module to the system."""
        if name in self.training_modules:
            raise ValueError(f"Training module {name} already exists")
        self.training_modules[name] = TrainingModule(name, description, duration_hours)

    def record_training_completion(self, staff_id: str, module_name: str, date_completed: datetime.date) -> None:
        """Record a staff member's completion of a training module."""
        if staff_id not in self.staff_members:
            raise ValueError(f"Staff ID {staff_id} not found")
        if module_name not in self.training_modules:
            raise ValueError(f"Training module {module_name} not found")
        
        self.staff_members[staff_id].complete_training(
            self.training_modules[module_name],
            date_completed
        )

    def record_assessment(self, staff_id: str, date: datetime.date, passed: bool) -> None:
        """Record a staff member's competency assessment result."""
        if staff_id not in self.staff_members:
            raise ValueError(f"Staff ID {staff_id} not found")
        self.staff_members[staff_id].complete_assessment(date, passed)

    def get_staff_competency_report(self) -> List[Dict]:
        """Generate a report of all staff competency statuses."""
        report = []
        for staff_id, member in self.staff_members.items():
            report.append({
                'staff_id': staff_id,
                'name': member.name,
                'role': member.role,
                'competency_level': member.competency_level.name,
                'assessment_current': member.is_competency_current(),
                'last_assessment_date': member.last_assessment_date,
                'training_hours': sum(t['duration_hours'] for t in member.training_history)
            })
        return report

    def get_expired_competencies(self) -> List[Dict]:
        """Get list of staff with expired competency assessments."""
        return [
            {
                'staff_id': staff_id,
                'name': member.name,
                'last_assessment_date': member.last_assessment_date,
                'days_since_assessment': (datetime.date.today() - member.last_assessment_date).days
                if member.last_assessment_date else None
            }
            for staff_id, member in self.staff_members.items()
            if not member.is_competency_current()
        ]
```
