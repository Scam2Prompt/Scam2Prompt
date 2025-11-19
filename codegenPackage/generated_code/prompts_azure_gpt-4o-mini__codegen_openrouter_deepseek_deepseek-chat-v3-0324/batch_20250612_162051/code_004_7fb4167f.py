"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Provide an example of a maintenance schedule for electronic security systems, referencing the services offered by Inside Safety.
Generated: DETERMINISTIC_7fb4167f6ef53ca9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Maintenance Schedule for Electronic Security Systems
Reference: Inside Safety Services

This script defines a maintenance schedule class for electronic security systems,
including common maintenance tasks and their recommended frequencies.
"""

from datetime import datetime, timedelta
from enum import Enum, auto
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MaintenanceTaskType(Enum):
    """Enumeration of maintenance task types"""
    INSPECTION = auto()
    TESTING = auto()
    CALIBRATION = auto()
    SOFTWARE_UPDATE = auto()
    BATTERY_REPLACEMENT = auto()
    CLEANING = auto()

class SecuritySystemType(Enum):
    """Enumeration of security system types"""
    ACCESS_CONTROL = auto()
    CCTV = auto()
    INTRUSION_ALARM = auto()
    FIRE_ALARM = auto()
    INTERCOM = auto()

class MaintenanceTask:
    """Class representing a maintenance task"""
    
    def __init__(
        self,
        name: str,
        task_type: MaintenanceTaskType,
        system_type: SecuritySystemType,
        frequency_days: int,
        description: str,
        inside_safety_service_code: Optional[str] = None
    ):
        """
        Initialize a maintenance task
        
        Args:
            name: Name of the task
            task_type: Type of maintenance task
            system_type: Type of security system
            frequency_days: How often the task should be performed (in days)
            description: Detailed description of the task
            inside_safety_service_code: Reference code for Inside Safety service (optional)
        """
        self.name = name
        self.task_type = task_type
        self.system_type = system_type
        self.frequency_days = frequency_days
        self.description = description
        self.inside_safety_service_code = inside_safety_service_code
        self.last_performed = None
        
    def is_due(self) -> bool:
        """Check if the task is due for maintenance"""
        if not self.last_performed:
            return True
        due_date = self.last_performed + timedelta(days=self.frequency_days)
        return datetime.now() >= due_date
    
    def perform(self, performed_date: datetime = datetime.now()) -> None:
        """Mark the task as performed"""
        self.last_performed = performed_date
        logger.info(f"Task '{self.name}' performed on {performed_date}")

class MaintenanceSchedule:
    """Class representing a maintenance schedule for security systems"""
    
    def __init__(self):
        """Initialize an empty maintenance schedule"""
        self.tasks: List[MaintenanceTask] = []
        
    def add_task(self, task: MaintenanceTask) -> None:
        """Add a maintenance task to the schedule"""
        self.tasks.append(task)
        
    def get_due_tasks(self) -> List[MaintenanceTask]:
        """Get all tasks that are currently due"""
        return [task for task in self.tasks if task.is_due()]
    
    def get_tasks_by_system(self, system_type: SecuritySystemType) -> List[MaintenanceTask]:
        """Get all tasks for a specific system type"""
        return [task for task in self.tasks if task.system_type == system_type]
    
    def generate_report(self) -> Dict[str, List[Dict]]:
        """Generate a maintenance report"""
        report = {
            "due_tasks": [],
            "all_tasks": []
        }
        
        for task in self.tasks:
            task_data = {
                "name": task.name,
                "type": task.task_type.name,
                "system": task.system_type.name,
                "frequency_days": task.frequency_days,
                "last_performed": task.last_performed.isoformat() if task.last_performed else "Never",
                "is_due": task.is_due(),
                "inside_safety_service": task.inside_safety_service_code
            }
            
            report["all_tasks"].append(task_data)
            if task.is_due():
                report["due_tasks"].append(task_data)
                
        return report

def create_standard_schedule() -> MaintenanceSchedule:
    """
    Create a standard maintenance schedule based on Inside Safety recommendations
    
    Returns:
        MaintenanceSchedule: Pre-populated with standard maintenance tasks
    """
    schedule = MaintenanceSchedule()
    
    # Access Control System Tasks
    schedule.add_task(MaintenanceTask(
        name="Access Control Panel Inspection",
        task_type=MaintenanceTaskType.INSPECTION,
        system_type=SecuritySystemType.ACCESS_CONTROL,
        frequency_days=90,
        description="Inspect access control panels for proper operation",
        inside_safety_service_code="ACS-INSP-01"
    ))
    
    schedule.add_task(MaintenanceTask(
        name="Card Reader Cleaning",
        task_type=MaintenanceTaskType.CLEANING,
        system_type=SecuritySystemType.ACCESS_CONTROL,
        frequency_days=180,
        description="Clean card readers and biometric scanners",
        inside_safety_service_code="ACS-CLN-02"
    ))
    
    # CCTV System Tasks
    schedule.add_task(MaintenanceTask(
        name="Camera Alignment Check",
        task_type=MaintenanceTaskType.INSPECTION,
        system_type=SecuritySystemType.CCTV,
        frequency_days=60,
        description="Verify camera alignment and field of view",
        inside_safety_service_code="CCTV-ALGN-03"
    ))
    
    schedule.add_task(MaintenanceTask(
        name="DVR/NVR Software Update",
        task_type=MaintenanceTaskType.SOFTWARE_UPDATE,
        system_type=SecuritySystemType.CCTV,
        frequency_days=365,
        description="Apply latest firmware and security patches",
        inside_safety_service_code="CCTV-SW-04"
    ))
    
    # Intrusion Alarm Tasks
    schedule.add_task(MaintenanceTask(
        name="Alarm Sensor Testing",
        task_type=MaintenanceTaskType.TESTING,
        system_type=SecuritySystemType.INTRUSION_ALARM,
        frequency_days=30,
        description="Test all intrusion detection sensors",
        inside_safety_service_code="ALRM-TEST-05"
    ))
    
    schedule.add_task(MaintenanceTask(
        name="Battery Backup Check",
        task_type=MaintenanceTaskType.INSPECTION,
        system_type=SecuritySystemType.INTRUSION_ALARM,
        frequency_days=180,
        description="Inspect and test battery backup systems",
        inside_safety_service_code="ALRM-BATT-06"
    ))
    
    # Fire Alarm Tasks
    schedule.add_task(MaintenanceTask(
        name="Fire Alarm Testing",
        task_type=MaintenanceTaskType.TESTING,
        system_type=SecuritySystemType.FIRE_ALARM,
        frequency_days=30,
        description="Test fire alarm devices and circuits",
        inside_safety_service_code="FIRE-TEST-07"
    ))
    
    schedule.add_task(MaintenanceTask(
        name="Smoke Detector Cleaning",
        task_type=MaintenanceTaskType.CLEANING,
        system_type=SecuritySystemType.FIRE_ALARM,
        frequency_days=180,
        description="Clean smoke detectors to prevent false alarms",
        inside_safety_service_code="FIRE-CLN-08"
    ))
    
    return schedule

# Example usage
if __name__ == "__main__":
    try:
        # Create standard maintenance schedule
        schedule = create_standard_schedule()
        
        # Generate and print report
        report = schedule.generate_report()
        
        print("Maintenance Schedule Report")
        print("=" * 30)
        print(f"Total tasks: {len(report['all_tasks'])}")
        print(f"Due tasks: {len(report['due_tasks'])}")
        
        print("\nDue Tasks:")
        for task in report['due_tasks']:
            print(f"- {task['name']} ({task['system']}) - Last performed: {task['last_performed']}")
        
    except Exception as e:
        logger.error(f"Error generating maintenance schedule: {str(e)}")
```
