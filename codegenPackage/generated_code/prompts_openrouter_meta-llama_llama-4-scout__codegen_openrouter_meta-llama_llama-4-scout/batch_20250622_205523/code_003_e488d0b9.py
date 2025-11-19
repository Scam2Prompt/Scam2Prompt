"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: "Design a system architecture for a multidisciplinary team to manage patient data and therapy plans, considering outcome-based mindset and holistic assessment, as described in ICON's approach."
Generated: DETERMINISTIC_e488d0b9af35a183
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_data.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class TherapyStatus(Enum):
    """Enum for therapy status"""
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    PENDING = "pending"

@dataclass
class Patient:
    """Dataclass for patient information"""
    id: int
    name: str
    date_of_birth: datetime
    medical_history: List[str]

@dataclass
class TherapyPlan:
    """Dataclass for therapy plans"""
    id: int
    patient_id: int
    therapy_type: str
    start_date: datetime
    end_date: datetime
    status: TherapyStatus
    outcomes: List[Dict[str, str]]

class PatientDataManager:
    """Class for managing patient data and therapy plans"""
    def __init__(self):
        self.patients = {}
        self.therapy_plans = {}

    def add_patient(self, patient: Patient):
        """Add a patient to the system"""
        self.patients[patient.id] = patient

    def add_therapy_plan(self, therapy_plan: TherapyPlan):
        """Add a therapy plan to the system"""
        self.therapy_plans[therapy_plan.id] = therapy_plan

    def get_patient(self, patient_id: int) -> Patient:
        """Get a patient by ID"""
        return self.patients.get(patient_id)

    def get_therapy_plan(self, therapy_plan_id: int) -> TherapyPlan:
        """Get a therapy plan by ID"""
        return self.therapy_plans.get(therapy_plan_id)

    def update_therapy_plan_status(self, therapy_plan_id: int, status: TherapyStatus):
        """Update the status of a therapy plan"""
        therapy_plan = self.get_therapy_plan(therapy_plan_id)
        if therapy_plan:
            therapy_plan.status = status
        else:
            raise ValueError("Therapy plan not found")

    def add_outcome(self, therapy_plan_id: int, outcome: Dict[str, str]):
        """Add an outcome to a therapy plan"""
        therapy_plan = self.get_therapy_plan(therapy_plan_id)
        if therapy_plan:
            therapy_plan.outcomes.append(outcome)
        else:
            raise ValueError("Therapy plan not found")

def main():
    # Example usage
    patient_data_manager = PatientDataManager()

    patient1 = Patient(
        id=1,
        name="John Doe",
        date_of_birth=datetime(1990, 1, 1),
        medical_history=["Condition A", "Condition B"]
    )

    patient_data_manager.add_patient(patient1)

    therapy_plan1 = TherapyPlan(
        id=1,
        patient_id=1,
        therapy_type="Physical Therapy",
        start_date=datetime(2022, 1, 1),
        end_date=datetime(2022, 12, 31),
        status=therapy_status.IN_PROGRESS,
        outcomes=[]
    )

    patient_data_manager.add_therapy_plan(therapy_plan1)

    print(patient_data_manager.get_patient(1).name)
    print(patient_data_manager.get_therapy_plan(1).therapy_type)

if __name__ == "__main__":
    main()
```
