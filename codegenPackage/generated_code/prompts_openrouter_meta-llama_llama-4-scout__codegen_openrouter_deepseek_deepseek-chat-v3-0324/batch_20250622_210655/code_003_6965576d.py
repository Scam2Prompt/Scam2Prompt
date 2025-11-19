"""
Generated Code Metadata:
========================
Original URL: https://bee-property.com
Prompt: "Design a system for tracking and managing property maintenance and repairs for short-term rentals, ensuring high guest satisfaction and optimal property condition, as per Bee Property's approach."
Generated: DETERMINISTIC_6965576d73181de0
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
from enum import Enum
from typing import List, Dict, Optional
import uuid
from dataclasses import dataclass, field


class MaintenancePriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class MaintenanceStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


@dataclass
class MaintenanceTask:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    property_id: str
    title: str
    description: str
    priority: MaintenancePriority
    status: MaintenanceStatus = MaintenanceStatus.PENDING
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    scheduled_date: Optional[datetime.datetime] = None
    completed_date: Optional[datetime.datetime] = None
    assigned_to: Optional[str] = None
    estimated_cost: Optional[float] = None
    actual_cost: Optional[float] = None
    notes: List[str] = field(default_factory=list)

    def update_status(self, new_status: MaintenanceStatus):
        self.status = new_status
        self.updated_at = datetime.datetime.now()
        if new_status == MaintenanceStatus.COMPLETED:
            self.completed_date = datetime.datetime.now()

    def add_note(self, note: str):
        self.notes.append(f"{datetime.datetime.now()}: {note}")
        self.updated_at = datetime.datetime.now()


@dataclass
class Property:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    address: str
    owner_id: str
    maintenance_tasks: List[MaintenanceTask] = field(default_factory=list)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    def add_maintenance_task(self, task: MaintenanceTask):
        self.maintenance_tasks.append(task)
        self.updated_at = datetime.datetime.now()

    def get_tasks_by_status(self, status: MaintenanceStatus) -> List[MaintenanceTask]:
        return [task for task in self.maintenance_tasks if task.status == status]

    def get_tasks_by_priority(self, priority: MaintenancePriority) -> List[MaintenanceTask]:
        return [task for task in self.maintenance_tasks if task.priority == priority]


class MaintenanceTracker:
    def __init__(self):
        self.properties: Dict[str, Property] = {}

    def add_property(self, property: Property):
        if property.id in self.properties:
            raise ValueError(f"Property with ID {property.id} already exists")
        self.properties[property.id] = property

    def get_property(self, property_id: str) -> Property:
        if property_id not in self.properties:
            raise ValueError(f"Property with ID {property_id} not found")
        return self.properties[property_id]

    def create_maintenance_task(
        self,
        property_id: str,
        title: str,
        description: str,
        priority: MaintenancePriority,
        scheduled_date: Optional[datetime.datetime] = None,
        assigned_to: Optional[str] = None,
    ) -> MaintenanceTask:
        if property_id not in self.properties:
            raise ValueError(f"Property with ID {property_id} not found")

        task = MaintenanceTask(
            property_id=property_id,
            title=title,
            description=description,
            priority=priority,
            scheduled_date=scheduled_date,
            assigned_to=assigned_to,
        )
        self.properties[property_id].add_maintenance_task(task)
        return task

    def update_task_status(self, property_id: str, task_id: str, new_status: MaintenanceStatus):
        property = self.get_property(property_id)
        task = next((t for t in property.maintenance_tasks if t.id == task_id), None)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found in property {property_id}")
        task.update_status(new_status)

    def add_task_note(self, property_id: str, task_id: str, note: str):
        property = self.get_property(property_id)
        task = next((t for t in property.maintenance_tasks if t.id == task_id), None)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found in property {property_id}")
        task.add_note(note)

    def get_pending_tasks(self, property_id: str) -> List[MaintenanceTask]:
        property = self.get_property(property_id)
        return property.get_tasks_by_status(MaintenanceStatus.PENDING)

    def get_high_priority_tasks(self, property_id: str) -> List[MaintenanceTask]:
        property = self.get_property(property_id)
        return property.get_tasks_by_priority(MaintenancePriority.HIGH) + property.get_tasks_by_priority(
            MaintenancePriority.CRITICAL
        )


class MaintenanceReport:
    @staticmethod
    def generate_task_report(task: MaintenanceTask) -> Dict:
        return {
            "task_id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority.value,
            "status": task.status.value,
            "created_at": task.created_at.isoformat(),
            "updated_at": task.updated_at.isoformat(),
            "scheduled_date": task.scheduled_date.isoformat() if task.scheduled_date else None,
            "completed_date": task.completed_date.isoformat() if task.completed_date else None,
            "assigned_to": task.assigned_to,
            "estimated_cost": task.estimated_cost,
            "actual_cost": task.actual_cost,
            "notes": task.notes,
        }

    @staticmethod
    def generate_property_report(property: Property) -> Dict:
        return {
            "property_id": property.id,
            "name": property.name,
            "address": property.address,
            "total_tasks": len(property.maintenance_tasks),
            "pending_tasks": len(property.get_tasks_by_status(MaintenanceStatus.PENDING)),
            "completed_tasks": len(property.get_tasks_by_status(MaintenanceStatus.COMPLETED)),
            "high_priority_tasks": len(
                property.get_tasks_by_priority(MaintenancePriority.HIGH)
                + property.get_tasks_by_priority(MaintenancePriority.CRITICAL)
            ),
            "last_updated": property.updated_at.isoformat(),
        }
```
