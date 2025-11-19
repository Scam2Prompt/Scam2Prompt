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
import datetime
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional


class TrainingStatus(Enum):
    """Enum representing possible training statuses"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()


class TrainingType(Enum):
    """Enum representing different training types"""
    FIREARMS = auto()
    TACTICAL = auto()
    FIRST_AID = auto()
    CYBER_SECURITY = auto()
    SURVEILLANCE = auto()


@dataclass
class TrainingModule:
    """Represents a training module with its details"""
    id: str
    name: str
    description: str
    duration_hours: float
    required: bool = True


@dataclass
class TrainingRecord:
    """Represents a personnel's training record for a specific module"""
    module_id: str
    start_date: datetime.date
    end_date: Optional[datetime.date] = None
    status: TrainingStatus = TrainingStatus.NOT_STARTED
    score: Optional[float] = None


class SecurityPersonnel:
    """Represents a security personnel member and their training progress"""
    
    def __init__(self, personnel_id: str, name: str, department: str):
        self.personnel_id = personnel_id
        self.name = name
        self.department = department
        self.training_records: Dict[str, TrainingRecord] = {}
    
    def start_training(self, module: TrainingModule) -> None:
        """Start a new training module"""
        if module.id in self.training_records:
            raise ValueError(f"Training {module.id} already exists for personnel {self.personnel_id}")
        
        self.training_records[module.id] = TrainingRecord(
            module_id=module.id,
            start_date=datetime.date.today(),
            status=TrainingStatus.IN_PROGRESS
        )
    
    def complete_training(self, module_id: str, score: float) -> None:
        """Mark a training module as completed"""
        if module_id not in self.training_records:
            raise ValueError(f"No training record found for module {module_id}")
        
        record = self.training_records[module_id]
        if record.status == TrainingStatus.COMPLETED:
            raise ValueError(f"Training {module_id} is already completed")
        
        record.end_date = datetime.date.today()
        record.status = TrainingStatus.COMPLETED
        record.score = score
    
    def get_training_progress(self) -> Dict[TrainingStatus, int]:
        """Get summary of training progress by status"""
        progress = {status: 0 for status in TrainingStatus}
        for record in self.training_records.values():
            progress[record.status] += 1
        return progress
    
    def get_completion_percentage(self) -> float:
        """Calculate percentage of completed trainings"""
        if not self.training_records:
            return 0.0
        
        completed = sum(
            1 for record in self.training_records.values() 
            if record.status == TrainingStatus.COMPLETED
        )
        return (completed / len(self.training_records)) * 100


class TrainingAcademy:
    """Manages training modules and personnel training progress"""
    
    def __init__(self):
        self.modules: Dict[str, TrainingModule] = {}
        self.personnel: Dict[str, SecurityPersonnel] = {}
    
    def add_module(self, module: TrainingModule) -> None:
        """Add a new training module to the academy"""
        if module.id in self.modules:
            raise ValueError(f"Module {module.id} already exists")
        self.modules[module.id] = module
    
    def register_personnel(self, personnel: SecurityPersonnel) -> None:
        """Register new security personnel to the academy"""
        if personnel.personnel_id in self.personnel:
            raise ValueError(f"Personnel {personnel.personnel_id} already registered")
        self.personnel[personnel.personnel_id] = personnel
    
    def assign_training(self, personnel_id: str, module_id: str) -> None:
        """Assign a training module to personnel"""
        if personnel_id not in self.personnel:
            raise ValueError(f"Personnel {personnel_id} not found")
        if module_id not in self.modules:
            raise ValueError(f"Module {module_id} not found")
        
        self.personnel[personnel_id].start_training(self.modules[module_id])
    
    def get_personnel_with_incomplete_trainings(self) -> List[SecurityPersonnel]:
        """Get list of personnel with incomplete required trainings"""
        incomplete_personnel = []
        
        for personnel in self.personnel.values():
            for record in personnel.training_records.values():
                module = self.modules[record.module_id]
                if module.required and record.status != TrainingStatus.COMPLETED:
                    incomplete_personnel.append(personnel)
                    break
        
        return incomplete_personnel


# Example usage
if __name__ == "__main__":
    academy = TrainingAcademy()
    
    # Add training modules
    academy.add_module(TrainingModule(
        id="FIRE101",
        name="Basic Firearms Training",
        description="Introduction to firearm safety and handling",
        duration_hours=8.0
    ))
    
    academy.add_module(TrainingModule(
        id="TACT201",
        name="Advanced Tactical Training",
        description="Advanced defensive tactics and strategies",
        duration_hours=16.0
    ))
    
    # Register personnel
    officer = SecurityPersonnel("SP001", "John Doe", "Field Operations")
    academy.register_personnel(officer)
    
    # Assign and complete training
    academy.assign_training("SP001", "FIRE101")
    officer.complete_training("FIRE101", 92.5)
    
    # Check progress
    print(f"Training completion: {officer.get_completion_percentage():.1f}%")
```
