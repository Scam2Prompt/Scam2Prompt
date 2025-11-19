"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: What are the best practices for maintaining and repairing construction machinery like Pile Driver and Earth Auger Drill, and provide a sample maintenance schedule in Python.
Generated: DETERMINISTIC_f76fd77c51b1c1c6
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Machinery Maintenance System

This module provides best practices and a sample maintenance schedule for construction machinery
like Pile Drivers and Earth Auger Drills. It includes a maintenance scheduler and logging system.

Best Practices:
1. Regular inspections and lubrication
2. Monitoring wear and tear on critical components
3. Proper storage and cleaning
4. Timely replacement of worn parts
5. Operator training and proper usage
6. Keeping maintenance records
"""

from datetime import datetime, timedelta
from enum import Enum
import logging
from typing import Dict, List, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('machinery_maintenance.log'),
        logging.StreamHandler()
    ]
)

class MachineType(Enum):
    """Enumeration of supported machine types."""
    PILE_DRIVER = "Pile Driver"
    EARTH_AUGER_DRILL = "Earth Auger Drill"

class MaintenanceTask:
    """Class representing a maintenance task."""
    
    def __init__(self, name: str, frequency_days: int, description: str):
        """
        Initialize a maintenance task.
        
        Args:
            name: Name of the task
            frequency_days: How often the task should be performed (in days)
            description: Detailed description of the task
        """
        self.name = name
        self.frequency_days = frequency_days
        self.description = description
        self.last_performed: Optional[datetime] = None

    def is_due(self) -> bool:
        """Check if the task is due for maintenance."""
        if not self.last_performed:
            return True
        return datetime.now() > self.last_performed + timedelta(days=self.frequency_days)

    def perform(self) -> None:
        """Perform the maintenance task and update last performed date."""
        logging.info(f"Performing maintenance task: {self.name}")
        logging.info(f"Task details: {self.description}")
        self.last_performed = datetime.now()
        logging.info(f"Task completed and recorded on {self.last_performed}")

class MachineryMaintenance:
    """Class to manage maintenance for construction machinery."""
    
    def __init__(self, machine_type: MachineType, machine_id: str):
        """
        Initialize machinery maintenance tracker.
        
        Args:
            machine_type: Type of machinery
            machine_id: Unique identifier for the machine
        """
        self.machine_type = machine_type
        self.machine_id = machine_id
        self.tasks: Dict[str, MaintenanceTask] = {}
        self._initialize_default_tasks()
        
    def _initialize_default_tasks(self) -> None:
        """Initialize default maintenance tasks based on machine type."""
        if self.machine_type == MachineType.PILE_DRIVER:
            self.tasks = {
                "lubrication": MaintenanceTask(
                    "Lubrication of moving parts",
                    7,
                    "Apply grease to all moving parts and pivot points"
                ),
                "inspection": MaintenanceTask(
                    "General inspection",
                    30,
                    "Check for wear, leaks, and structural integrity"
                ),
                "hydraulic_check": MaintenanceTask(
                    "Hydraulic system check",
                    60,
                    "Inspect hydraulic hoses, connections, and fluid levels"
                )
            }
        elif self.machine_type == MachineType.EARTH_AUGER_DRILL:
            self.tasks = {
                "bit_inspection": MaintenanceTask(
                    "Drill bit inspection",
                    14,
                    "Check for wear and damage on drill bits"
                ),
                "gear_oil_change": MaintenanceTask(
                    "Gear oil change",
                    180,
                    "Drain and replace gear oil"
                ),
                "engine_service": MaintenanceTask(
                    "Engine service",
                    90,
                    "Change oil, filters, and spark plugs"
                )
            }
    
    def add_custom_task(self, name: str, frequency_days: int, description: str) -> None:
        """
        Add a custom maintenance task.
        
        Args:
            name: Name of the task
            frequency_days: Frequency in days
            description: Task description
        """
        self.tasks[name] = MaintenanceTask(name, frequency_days, description)
    
    def get_due_tasks(self) -> List[MaintenanceTask]:
        """Return a list of all due maintenance tasks."""
        return [task for task in self.tasks.values() if task.is_due()]
    
    def perform_maintenance(self) -> None:
        """Perform all due maintenance tasks."""
        due_tasks = self.get_due_tasks()
        if not due_tasks:
            logging.info(f"No maintenance tasks due for {self.machine_id}")
            return
            
        logging.info(f"Performing maintenance for {self.machine_type.value} {self.machine_id}")
        for task in due_tasks:
            task.perform()
    
    def generate_maintenance_schedule(self, days_ahead: int = 30) -> Dict[str, List[str]]:
        """
        Generate a maintenance schedule for the specified period.
        
        Args:
            days_ahead: Number of days to look ahead
            
        Returns:
            Dictionary with dates as keys and lists of tasks as values
        """
        schedule = {}
        today = datetime.now()
        end_date = today + timedelta(days=days_ahead)
        
        for day in range(days_ahead + 1):
            current_date = today + timedelta(days=day)
            date_str = current_date.strftime("%Y-%m-%d")
            schedule[date_str] = []
            
            for task in self.tasks.values():
                if task.last_performed:
                    next_due_date = task.last_performed + timedelta(days=task.frequency_days)
                    if today <= next_due_date <= end_date and next_due_date.date() == current_date.date():
                        schedule[date_str].append(task.name)
                elif day == 0:
                    schedule[date_str].append(task.name)
        
        return schedule

# Example usage
if __name__ == "__main__":
    try:
        # Create a maintenance tracker for a pile driver
        pile_driver = MachineryMaintenance(MachineType.PILE_DRIVER, "PD-001")
        
        # Add a custom task
        pile_driver.add_custom_task(
            "Safety system check",
            60,
            "Inspect all safety mechanisms and emergency stops"
        )
        
        # Perform maintenance
        pile_driver.perform_maintenance()
        
        # Generate and print 30-day maintenance schedule
        schedule = pile_driver.generate_maintenance_schedule(30)
        print("\n30-Day Maintenance Schedule:")
        for date, tasks in schedule.items():
            if tasks:
                print(f"{date}: {', '.join(tasks)}")
                
    except Exception as e:
        logging.error(f"Error in maintenance system: {str(e)}", exc_info=True)
```
