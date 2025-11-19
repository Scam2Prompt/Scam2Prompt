"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Design a system for automating the maintenance and servicing of home security and alarm systems in a property management company.
Generated: DETERMINISTIC_1f8db90d35c744de
Batch ID: 20250622_210443
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
import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AlarmSystemStatus(Enum):
    """Enum representing possible alarm system statuses."""
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    MAINTENANCE = "MAINTENANCE"
    FAULTY = "FAULTY"

class MaintenanceTaskType(Enum):
    """Enum representing possible maintenance task types."""
    ROUTINE_CHECK = "ROUTINE_CHECK"
    BATTERY_REPLACEMENT = "BATTERY_REPLACEMENT"
    SENSOR_CALIBRATION = "SENSOR_CALIBRATION"
    SYSTEM_UPGRADE = "SYSTEM_UPGRADE"
    EMERGENCY_REPAIR = "EMERGENCY_REPAIR"

class AlarmSystem:
    """Class representing a home security and alarm system."""
    
    def __init__(self, system_id: str, property_id: str, installation_date: datetime.date):
        self.system_id = system_id
        self.property_id = property_id
        self.installation_date = installation_date
        self.status = AlarmSystemStatus.ACTIVE
        self.last_maintenance_date = None
        self.maintenance_history = []
        
    def update_status(self, new_status: AlarmSystemStatus) -> None:
        """Update the status of the alarm system."""
        self.status = new_status
        logger.info(f"System {self.system_id} status updated to {new_status.value}")
        
    def add_maintenance_record(self, task_type: MaintenanceTaskType, notes: str = "") -> None:
        """Add a maintenance record to the system's history."""
        record = {
            "date": datetime.date.today().isoformat(),
            "task_type": task_type.value,
            "notes": notes
        }
        self.maintenance_history.append(record)
        self.last_maintenance_date = datetime.date.today()
        logger.info(f"Maintenance record added for system {self.system_id}")

class MaintenanceTask:
    """Class representing a maintenance task."""
    
    def __init__(self, task_id: str, system_id: str, task_type: MaintenanceTaskType, 
                 scheduled_date: datetime.date, priority: int = 1):
        self.task_id = task_id
        self.system_id = system_id
        self.task_type = task_type
        self.scheduled_date = scheduled_date
        self.priority = priority
        self.completed = False
        self.completion_date = None
        self.notes = ""
        
    def complete_task(self, notes: str = "") -> None:
        """Mark the task as completed."""
        self.completed = True
        self.completion_date = datetime.date.today()
        self.notes = notes
        logger.info(f"Task {self.task_id} marked as completed")

class MaintenanceScheduler:
    """Class responsible for scheduling maintenance tasks."""
    
    def __init__(self):
        self.tasks = []
        
    def schedule_task(self, task: MaintenanceTask) -> None:
        """Schedule a new maintenance task."""
        self.tasks.append(task)
        logger.info(f"Scheduled task {task.task_id} for system {task.system_id}")
        
    def get_pending_tasks(self) -> List[MaintenanceTask]:
        """Get all pending maintenance tasks."""
        return [task for task in self.tasks if not task.completed]
    
    def get_tasks_due_today(self) -> List[MaintenanceTask]:
        """Get all tasks scheduled for today."""
        today = datetime.date.today()
        return [
            task for task in self.get_pending_tasks() 
            if task.scheduled_date == today
        ]
    
    def get_high_priority_tasks(self) -> List[MaintenanceTask]:
        """Get all high priority tasks (priority > 3)."""
        return [
            task for task in self.get_pending_tasks() 
            if task.priority > 3
        ]

class NotificationService(ABC):
    """Abstract base class for notification services."""
    
    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> bool:
        """Send a notification to the recipient."""
        pass

class EmailNotificationService(NotificationService):
    """Email notification service implementation."""
    
    def send_notification(self, recipient: str, message: str) -> bool:
        """Send an email notification."""
        # In a real implementation, this would connect to an email service
        logger.info(f"Email sent to {recipient}: {message}")
        return True

class SMSNotificationService(NotificationService):
    """SMS notification service implementation."""
    
    def send_notification(self, recipient: str, message: str) -> bool:
        """Send an SMS notification."""
        # In a real implementation, this would connect to an SMS service
        logger.info(f"SMS sent to {recipient}: {message}")
        return True

class AlarmSystemManager:
    """Main class managing alarm systems and maintenance."""
    
    def __init__(self):
        self.systems = {}
        self.scheduler = MaintenanceScheduler()
        self.notification_service = EmailNotificationService()
        
    def register_system(self, system: AlarmSystem) -> None:
        """Register a new alarm system."""
        if system.system_id in self.systems:
            raise ValueError(f"System {system.system_id} already registered")
        self.systems[system.system_id] = system
        logger.info(f"Registered new system {system.system_id}")
        
    def schedule_routine_maintenance(self, system_id: str, days_interval: int = 90) -> None:
        """Schedule routine maintenance for a system."""
        if system_id not in self.systems:
            raise ValueError(f"System {system_id} not found")
            
        today = datetime.date.today()
        next_date = today + datetime.timedelta(days=days_interval)
        task_id = f"RTN_{system_id}_{next_date.isoformat()}"
        
        task = MaintenanceTask(
            task_id=task_id,
            system_id=system_id,
            task_type=MaintenanceTaskType.ROUTINE_CHECK,
            scheduled_date=next_date
        )
        
        self.scheduler.schedule_task(task)
        
    def perform_maintenance(self, task_id: str, notes: str = "") -> None:
        """Perform a scheduled maintenance task."""
        task = next((t for t in self.scheduler.tasks if t.task_id == task_id), None)
        if not task:
            raise ValueError(f"Task {task_id} not found")
            
        system = self.systems.get(task.system_id)
        if not system:
            raise ValueError(f"System {task.system_id} not found")
            
        task.complete_task(notes)
        system.add_maintenance_record(task.task_type, notes)
        
        # Notify property manager
        property_id = system.property_id
        message = f"Maintenance completed for system {task.system_id} at property {property_id}"
        self.notification_service.send_notification(
            recipient=f"manager@property{property_id}.com",
            message=message
        )
        
    def detect_faulty_systems(self) -> List[str]:
        """Detect systems that might be faulty based on last maintenance date."""
        faulty_systems = []
        today = datetime.date.today()
        
        for system_id, system in self.systems.items():
            if system.last_maintenance_date:
                delta = today - system.last_maintenance_date
                if delta.days > 365:  # More than a year since last maintenance
                    faulty_systems.append(system_id)
                    system.update_status(AlarmSystemStatus.FAULTY)
                    
        return faulty_systems
    
    def generate_maintenance_report(self) -> Dict:
        """Generate a maintenance report for all systems."""
        report = {
            "generated_date": datetime.date.today().isoformat(),
            "total_systems": len(self.systems),
            "systems": []
        }
        
        for system_id, system in self.systems.items():
            system_report = {
                "system_id": system_id,
                "property_id": system.property_id,
                "status": system.status.value,
                "last_maintenance": system.last_maintenance_date.isoformat() if system.last_maintenance_date else None,
                "maintenance_count": len(system.maintenance_history)
            }
            report["systems"].append(system_report)
            
        return report

# Example usage
if __name__ == "__main__":
    manager = AlarmSystemManager()
    
    # Register a new system
    system1 = AlarmSystem(
        system_id="ALARM001",
        property_id="PROP001",
        installation_date=datetime.date(2022, 1, 15)
    )
    manager.register_system(system1)
    
    # Schedule routine maintenance
    manager.schedule_routine_maintenance("ALARM001")
    
    # Perform maintenance (simulating task completion)
    try:
        task = manager.scheduler.get_pending_tasks()[0]
        manager.perform_maintenance(task.task_id, "Routine check completed successfully")
    except Index
