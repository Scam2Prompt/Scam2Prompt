"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Generate a code snippet for a construction project management tool that tracks project timelines and ensures quality delivery, similar to SSTCO's commitment to timely and quality services.
Generated: DETERMINISTIC_328a30c3623dfc0d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Management Tool
This tool helps track project timelines and ensures quality delivery.
Features include task scheduling, progress tracking, and quality checks.
"""

from datetime import datetime, timedelta
from enum import Enum, auto
import json
from typing import List, Dict, Optional


class TaskStatus(Enum):
    """Enumeration for task status"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()
    QUALITY_CHECK_PASSED = auto()
    QUALITY_CHECK_FAILED = auto()


class QualityCheck:
    """Class representing a quality check for a task"""
    
    def __init__(self, name: str, description: str, passed: bool = False):
        self.name = name
        self.description = description
        self.passed = passed
        self.check_date = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert QualityCheck to dictionary for serialization"""
        return {
            'name': self.name,
            'description': self.description,
            'passed': self.passed,
            'check_date': self.check_date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'QualityCheck':
        """Create QualityCheck from dictionary"""
        qc = cls(data['name'], data['description'], data['passed'])
        qc.check_date = datetime.fromisoformat(data['check_date'])
        return qc


class ProjectTask:
    """Class representing a task in a construction project"""
    
    def __init__(self, name: str, description: str, 
                 start_date: datetime, end_date: datetime,
                 dependencies: List[str] = None):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.dependencies = dependencies or []
        self.status = TaskStatus.NOT_STARTED
        self.quality_checks: List[QualityCheck] = []
        self.completion_date: Optional[datetime] = None
    
    def update_status(self, status: TaskStatus) -> None:
        """Update task status"""
        self.status = status
        if status == TaskStatus.COMPLETED:
            self.completion_date = datetime.now()
    
    def add_quality_check(self, quality_check: QualityCheck) -> None:
        """Add a quality check to the task"""
        self.quality_checks.append(quality_check)
        if quality_check.passed:
            self.update_status(TaskStatus.QUALITY_CHECK_PASSED)
        else:
            self.update_status(TaskStatus.QUALITY_CHECK_FAILED)
    
    def is_delayed(self) -> bool:
        """Check if task is delayed"""
        if self.status == TaskStatus.COMPLETED:
            return False
        return datetime.now() > self.end_date
    
    def to_dict(self) -> Dict:
        """Convert ProjectTask to dictionary for serialization"""
        return {
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'dependencies': self.dependencies,
            'status': self.status.name,
            'quality_checks': [qc.to_dict() for qc in self.quality_checks],
            'completion_date': self.completion_date.isoformat() if self.completion_date else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ProjectTask':
        """Create ProjectTask from dictionary"""
        task = cls(
            data['name'],
            data['description'],
            datetime.fromisoformat(data['start_date']),
            datetime.fromisoformat(data['end_date']),
            data['dependencies']
        )
        task.status = TaskStatus[data['status']]
        task.quality_checks = [QualityCheck.from_dict(qc) for qc in data['quality_checks']]
        if data['completion_date']:
            task.completion_date = datetime.fromisoformat(data['completion_date'])
        return task


class ConstructionProject:
    """Class representing a construction project"""
    
    def __init__(self, name: str, description: str, start_date: datetime, end_date: datetime):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: Dict[str, ProjectTask] = {}
    
    def add_task(self, task: ProjectTask) -> None:
        """Add a task to the project"""
        if task.name in self.tasks:
            raise ValueError(f"Task with name '{task.name}' already exists")
        self.tasks[task.name] = task
    
    def get_task(self, task_name: str) -> ProjectTask:
        """Get a task by name"""
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' not found")
        return self.tasks[task_name]
    
    def update_task_status(self, task_name: str, status: TaskStatus) -> None:
        """Update status of a task"""
        task = self.get_task(task_name)
        task.update_status(status)
    
    def add_quality_check(self, task_name: str, quality_check: QualityCheck) -> None:
        """Add quality check to a task"""
        task = self.get_task(task_name)
        task.add_quality_check(quality_check)
    
    def get_delayed_tasks(self) -> List[ProjectTask]:
        """Get all delayed tasks"""
        return [task for task in self.tasks.values() if task.is_delayed()]
    
    def get_project_progress(self) -> float:
        """Calculate project progress percentage"""
        if not self.tasks:
            return 0.0
        
        completed_tasks = sum(1 for task in self.tasks.values() 
                            if task.status == TaskStatus.COMPLETED or 
                            task.status == TaskStatus.QUALITY_CHECK_PASSED)
        return (completed_tasks / len(self.tasks)) * 100
    
    def to_dict(self) -> Dict:
        """Convert ConstructionProject to dictionary for serialization"""
        return {
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'tasks': {name: task.to_dict() for name, task in self.tasks.items()}
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ConstructionProject':
        """Create ConstructionProject from dictionary"""
        project = cls(
            data['name'],
            data['description'],
            datetime.fromisoformat(data['start_date']),
            datetime.fromisoformat(data['end_date'])
        )
        project.tasks = {
            name: ProjectTask.from_dict(task_data) 
            for name, task_data in data['tasks'].items()
        }
        return project
    
    def save_to_file(self, filename: str) -> None:
        """Save project to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'ConstructionProject':
        """Load project from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)


# Example usage
if __name__ == "__main__":
    # Create a new project
    project = ConstructionProject(
        "Office Building Construction",
        "Construction of a 10-story office building",
        datetime.now(),
        datetime.now() + timedelta(days=180)
    )
    
    # Add tasks
    foundation_task = ProjectTask(
        "Foundation Work",
        "Excavation and foundation pouring",
        datetime.now(),
        datetime.now() + timedelta(days=30)
    )
    
    framing_task = ProjectTask(
        "Framing",
        "Structural steel framing",
        datetime.now() + timedelta(days=31),
        datetime.now() + timedelta(days=60),
        ["Foundation Work"]
    )
    
    project.add_task(foundation_task)
    project.add_task(framing_task)
    
    # Update task status
    project.update_task_status("Foundation Work", TaskStatus.IN_PROGRESS)
    
    # Add quality check
    qc = QualityCheck(
        "Foundation Inspection",
        "Check foundation depth and concrete quality",
        True
    )
    project.add_quality_check("Foundation Work", qc)
    
    # Save project
    project.save_to_file("office_building_project.json")
    
    # Load project
    loaded_project = ConstructionProject.load_from_file("office_building_project.json")
    print(f"Project progress: {loaded_project.get_project_progress():.2f}%")
```
