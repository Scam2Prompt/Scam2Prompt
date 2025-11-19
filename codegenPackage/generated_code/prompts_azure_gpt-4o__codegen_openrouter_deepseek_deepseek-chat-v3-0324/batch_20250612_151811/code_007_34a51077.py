"""
Generated Code Metadata:
========================
Original URL: https://isienvironmental.com
Prompt: Generate Python code to evaluate facility maintenance tasks such as wastewater treatment plant operation and asbestos abatement, referencing iSi Environmental’s facility support services.
Generated: DETERMINISTIC_34a5107755622718
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional, Union
from datetime import datetime

class TaskStatus(Enum):
    """Enum representing the status of a maintenance task."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    FAILED = "Failed"

class MaintenanceTask:
    """Base class representing a facility maintenance task."""
    
    def __init__(
        self,
        task_id: str,
        description: str,
        priority: int,
        due_date: datetime,
        status: TaskStatus = TaskStatus.PENDING,
        notes: Optional[str] = None
    ):
        """Initialize a maintenance task.
        
        Args:
            task_id: Unique identifier for the task.
            description: Description of the task.
            priority: Priority level (1-5, with 1 being highest).
            due_date: Due date for the task.
            status: Current status of the task.
            notes: Additional notes or comments.
        """
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status
        self.notes = notes
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_status(self, new_status: TaskStatus, notes: Optional[str] = None) -> None:
        """Update the status of the task.
        
        Args:
            new_status: New status to set.
            notes: Optional notes about the status change.
        """
        self.status = new_status
        self.updated_at = datetime.now()
        if notes:
            self.notes = notes if not self.notes else f"{self.notes}\n{notes}"
    
    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for serialization."""
        return {
            "task_id": self.task_id,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date.isoformat(),
            "status": self.status.value,
            "notes": self.notes,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class WastewaterTreatmentTask(MaintenanceTask):
    """Class representing a wastewater treatment plant operation task."""
    
    def __init__(
        self,
        task_id: str,
        description: str,
        priority: int,
        due_date: datetime,
        status: TaskStatus = TaskStatus.PENDING,
        notes: Optional[str] = None,
        compliance_standard: Optional[str] = None,
        equipment_involved: Optional[List[str]] = None
    ):
        """Initialize a wastewater treatment task.
        
        Args:
            compliance_standard: Regulatory compliance standard (e.g., 'EPA').
            equipment_involved: List of equipment involved in the task.
        """
        super().__init__(task_id, description, priority, due_date, status, notes)
        self.compliance_standard = compliance_standard
        self.equipment_involved = equipment_involved or []
    
    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for serialization."""
        base_dict = super().to_dict()
        base_dict.update({
            "type": "wastewater_treatment",
            "compliance_standard": self.compliance_standard,
            "equipment_involved": self.equipment_involved
        })
        return base_dict

class AsbestosAbatementTask(MaintenanceTask):
    """Class representing an asbestos abatement task."""
    
    def __init__(
        self,
        task_id: str,
        description: str,
        priority: int,
        due_date: datetime,
        status: TaskStatus = TaskStatus.PENDING,
        notes: Optional[str] = None,
        containment_required: bool = False,
        air_monitoring_required: bool = True
    ):
        """Initialize an asbestos abatement task.
        
        Args:
            containment_required: Whether containment is required.
            air_monitoring_required: Whether air monitoring is required.
        """
        super().__init__(task_id, description, priority, due_date, status, notes)
        self.containment_required = containment_required
        self.air_monitoring_required = air_monitoring_required
    
    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for serialization."""
        base_dict = super().to_dict()
        base_dict.update({
            "type": "asbestos_abatement",
            "containment_required": self.containment_required,
            "air_monitoring_required": self.air_monitoring_required
        })
        return base_dict

class FacilityMaintenanceEvaluator:
    """Class to evaluate and manage facility maintenance tasks."""
    
    def __init__(self):
        """Initialize the evaluator with an empty task list."""
        self.tasks: Dict[str, Union[WastewaterTreatmentTask, AsbestosAbatementTask]] = {}
    
    def add_task(self, task: Union[WastewaterTreatmentTask, AsbestosAbatementTask]) -> None:
        """Add a new maintenance task.
        
        Args:
            task: Task to add.
        
        Raises:
            ValueError: If task ID already exists.
        """
        if task.task_id in self.tasks:
            raise ValueError(f"Task ID {task.task_id} already exists.")
        self.tasks[task.task_id] = task
    
    def get_task(self, task_id: str) -> Union[WastewaterTreatmentTask, AsbestosAbatementTask]:
        """Retrieve a task by its ID.
        
        Args:
            task_id: ID of the task to retrieve.
        
        Returns:
            The requested task.
        
        Raises:
            KeyError: If task ID does not exist.
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task ID {task_id} not found.")
        return self.tasks[task_id]
    
    def update_task_status(
        self,
        task_id: str,
        new_status: TaskStatus,
        notes: Optional[str] = None
    ) -> None:
        """Update the status of a task.
        
        Args:
            task_id: ID of the task to update.
            new_status: New status to set.
            notes: Optional notes about the status change.
        
        Raises:
            KeyError: If task ID does not exist.
        """
        task = self.get_task(task_id)
        task.update_status(new_status, notes)
    
    def get_tasks_by_status(self, status: TaskStatus) -> List[Dict]:
        """Get all tasks with a specific status.
        
        Args:
            status: Status to filter by.
        
        Returns:
            List of tasks with the specified status, serialized as dictionaries.
        """
        return [task.to_dict() for task in self.tasks.values() if task.status == status]
    
    def get_high_priority_tasks(self, threshold: int = 2) -> List[Dict]:
        """Get all tasks with priority at or above a threshold.
        
        Args:
            threshold: Priority threshold (1-5, lower is higher priority).
        
        Returns:
            List of high priority tasks, serialized as dictionaries.
        """
        return [
            task.to_dict()
            for task in self.tasks.values()
            if task.priority <= threshold
        ]
    
    def save_tasks_to_file(self, file_path: str) -> None:
        """Save all tasks to a JSON file.
        
        Args:
            file_path: Path to the output file.
        
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(
                    {task_id: task.to_dict() for task_id, task in self.tasks.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            raise IOError(f"Failed to save tasks to file: {e}")
    
    def load_tasks_from_file(self, file_path: str) -> None:
        """Load tasks from a JSON file.
        
        Args:
            file_path: Path to the input file.
        
        Raises:
            IOError: If file cannot be read.
            ValueError: If file contains invalid data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            self.tasks = {}
            for task_id, task_data in data.items():
                task_type = task_data.get("type")
                due_date = datetime.fromisoformat(task_data["due_date"])
                
                if task_type == "wastewater_treatment":
                    task = WastewaterTreatmentTask(
                        task_id=task_id,
                        description=task_data["description"],
                        priority=task_data["priority"],
                        due_date=due_date,
                        status=TaskStatus(task_data["status"]),
                        notes=task_data.get("notes"),
                        compliance_standard=task_data.get("compliance_standard"),
                        equipment_involved=task_data.get("equipment_involved", [])
                    )
                elif task_type == "asbestos_abatement":
                    task = AsbestosAbatementTask(
                        task_id=task_id,
                        description=task_data["description"],
                        priority=task_data["priority"],
                        due_date=due_date,
