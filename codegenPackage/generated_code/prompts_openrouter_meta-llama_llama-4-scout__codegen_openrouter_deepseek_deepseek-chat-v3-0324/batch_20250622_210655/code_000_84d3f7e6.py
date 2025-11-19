"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Write a code snippet in Python to implement a basic Safety and Health Management System (SG-SST) workflow for a small organization, considering the Colombian regulations and the PDCA (Plan-Do-Check-Act) cycle."
Generated: DETERMINISTIC_84d3f7e6df82f6af
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from enum import Enum
from typing import List, Dict, Optional

class PDCAPhase(Enum):
    PLAN = "Plan"
    DO = "Do"
    CHECK = "Check"
    ACT = "Act"

class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class SafetyActivity:
    def __init__(self, name: str, description: str, responsible: str, 
                 due_date: datetime.date, phase: PDCAPhase, risk_level: RiskLevel):
        self.name = name
        self.description = description
        self.responsible = responsible
        self.due_date = due_date
        self.phase = phase
        self.risk_level = risk_level
        self.completed = False
        self.completion_date = None

    def mark_completed(self):
        self.completed = True
        self.completion_date = datetime.date.today()

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "responsible": self.responsible,
            "due_date": self.due_date.isoformat(),
            "phase": self.phase.value,
            "risk_level": self.risk_level.value,
            "completed": self.completed,
            "completion_date": self.completion_date.isoformat() if self.completion_date else None
        }

class SG_SST:
    def __init__(self, organization_name: str):
        self.organization_name = organization_name
        self.activities: List[SafetyActivity] = []
        self.regulations = [
            "Resolución 0312 de 2019",
            "Decreto 1072 de 2015",
            "Ley 1562 de 2012"
        ]

    def add_activity(self, activity: SafetyActivity):
        self.activities.append(activity)

    def get_activities_by_phase(self, phase: PDCAPhase) -> List[SafetyActivity]:
        return [a for a in self.activities if a.phase == phase]

    def get_pending_activities(self) -> List[SafetyActivity]:
        return [a for a in self.activities if not a.completed]

    def get_overdue_activities(self) -> List[SafetyActivity]:
        today = datetime.date.today()
        return [a for a in self.activities if not a.completed and a.due_date < today]

    def generate_report(self) -> Dict:
        return {
            "organization": self.organization_name,
            "total_activities": len(self.activities),
            "completed_activities": len([a for a in self.activities if a.completed]),
            "pending_activities": len(self.get_pending_activities()),
            "overdue_activities": len(self.get_overdue_activities()),
            "regulations": self.regulations,
            "activities": [a.to_dict() for a in self.activities]
        }

    def save_to_file(self, filename: str):
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_report(), f, indent=4)
        except IOError as e:
            print(f"Error saving file: {e}")

    @classmethod
    def load_from_file(cls, filename: str) -> Optional['SG_SST']:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                system = cls(data['organization'])
                system.regulations = data['regulations']
                
                for activity_data in data['activities']:
                    activity = SafetyActivity(
                        name=activity_data['name'],
                        description=activity_data['description'],
                        responsible=activity_data['responsible'],
                        due_date=datetime.date.fromisoformat(activity_data['due_date']),
                        phase=PDCAPhase(activity_data['phase']),
                        risk_level=RiskLevel(activity_data['risk_level'])
                    )
                    if activity_data['completed']:
                        activity.mark_completed()
                    system.add_activity(activity)
                
                return system
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading file: {e}")
            return None

# Example usage
if __name__ == "__main__":
    system = SG_SST("Mi Empresa SAS")
    
    # Plan phase activities
    risk_assessment = SafetyActivity(
        name="Risk Assessment",
        description="Identify workplace hazards",
        responsible="Safety Officer",
        due_date=datetime.date.today() + datetime.timedelta(days=7),
        phase=PDCAPhase.PLAN,
        risk_level=RiskLevel.HIGH
    )
    
    # Do phase activities
    training = SafetyActivity(
        name="Safety Training",
        description="Train employees on safety procedures",
        responsible="HR Department",
        due_date=datetime.date.today() + datetime.timedelta(days=14),
        phase=PDCAPhase.DO,
        risk_level=RiskLevel.MEDIUM
    )
    
    system.add_activity(risk_assessment)
    system.add_activity(training)
    
    # Mark one as completed
    risk_assessment.mark_completed()
    
    # Generate and save report
    system.save_to_file("sg_sst_report.json")
    
    # Load from file
    loaded_system = SG_SST.load_from_file("sg_sst_report.json")
    if loaded_system:
        print(f"Loaded system for {loaded_system.organization_name}")
```
