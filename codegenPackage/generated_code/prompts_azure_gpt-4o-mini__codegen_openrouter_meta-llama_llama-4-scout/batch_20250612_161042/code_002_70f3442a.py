"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: Generate a code snippet for a training management system that tracks the training progress of security personnel, inspired by Mando Security's Training Academy offerings.
Generated: DETERMINISTIC_70f3442ab71f8c64
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_management_system.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class TrainingStatus(str, Enum):
    """Training status enumeration"""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"

class SecurityPersonnel:
    """Security personnel class"""
    def __init__(self, personnel_id: int, name: str):
        self.personnel_id = personnel_id
        self.name = name
        self.trainings = {}

    def add_training(self, training_id: int, training_name: str):
        """Add a training to the personnel's schedule"""
        self.trainings[training_id] = {
            "training_name": training_name,
            "status": TrainingStatus.PENDING,
            "start_date": None,
            "completion_date": None
        }

    def update_training_status(self, training_id: int, status: TrainingStatus, start_date: datetime = None, completion_date: datetime = None):
        """Update the status of a training"""
        if training_id in self.trainings:
            self.trainings[training_id]["status"] = status
            if start_date:
                self.trainings[training_id]["start_date"] = start_date
            if completion_date:
                self.trainings[training_id]["completion_date"] = completion_date
        else:
            raise ValueError("Training not found")

class TrainingManagementSystem:
    """Training management system class"""
    def __init__(self):
        self.personnel = {}

    def add_personnel(self, personnel_id: int, name: str):
        """Add security personnel to the system"""
        self.personnel[personnel_id] = SecurityPersonnel(personnel_id, name)

    def get_personnel(self, personnel_id: int) -> SecurityPersonnel:
        """Get security personnel by ID"""
        return self.personnel.get(personnel_id)

    def get_all_personnel(self) -> List[SecurityPersonnel]:
        """Get all security personnel"""
        return list(self.personnel.values())

def main():
    # Create a training management system
    tms = TrainingManagementSystem()

    # Add security personnel
    tms.add_personnel(1, "John Doe")
    tms.add_personnel(2, "Jane Smith")

    # Get a personnel
    personnel = tms.get_personnel(1)

    # Add trainings
    personnel.add_training(1, "Basic Security Training")
    personnel.add_training(2, "Advanced Security Training")

    # Update training status
    personnel.update_training_status(1, TrainingStatus.IN_PROGRESS, start_date=datetime.now())
    personnel.update_training_status(2, TrainingStatus.COMPLETED, start_date=datetime.now(), completion_date=datetime.now())

    # Print personnel trainings
    for training_id, training in personnel.trainings.items():
        print(f"Training ID: {training_id}")
        print(f"Training Name: {training['training_name']}")
        print(f"Status: {training['status']}")
        print(f"Start Date: {training['start_date']}")
        print(f"Completion Date: {training['completion_date']}")
        print("------------------------")

if __name__ == "__main__":
    main()
```
