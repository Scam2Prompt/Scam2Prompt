"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Generate a code snippet for a preventive maintenance program that schedules regular checks for UPS systems in a data center, considering battery replacement and circuit breaker testing.
Generated: DETERMINISTIC_071e137eeeef1282
Batch ID: 20250612_162050
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
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MaintenanceType(Enum):
    """Enum for different types of maintenance tasks."""
    BATTERY_REPLACEMENT = "Battery Replacement"
    CIRCUIT_BREAKER_TEST = "Circuit Breaker Test"
    GENERAL_INSPECTION = "General Inspection"

@dataclass
class UPSSystem:
    """Data class representing a UPS system in the data center."""
    id: str
    model: str
    installation_date: datetime.date
    last_battery_replacement: Optional[datetime.date] = None
    last_circuit_test: Optional[datetime.date] = None
    last_inspection: Optional[datetime.date] = None

@dataclass
class MaintenanceTask:
    """Data class representing a maintenance task."""
    ups_id: str
    task_type: MaintenanceType
    scheduled_date: datetime.date
    completed: bool = False
    completion_date: Optional[datetime.date] = None

class PreventiveMaintenanceScheduler:
    """Class to manage preventive maintenance scheduling for UPS systems."""
    
    def __init__(self, battery_life_years: int = 3, circuit_test_interval_days: int = 180):
        """
        Initialize the scheduler with maintenance intervals.
        
        Args:
            battery_life_years: Expected battery life in years (default 3)
            circuit_test_interval_days: Interval for circuit breaker tests in days (default 180)
        """
        self.battery_life_years = battery_life_years
        self.circuit_test_interval_days = circuit_test_interval_days
        self.ups_systems: List[UPSSystem] = []
        self.maintenance_tasks: List[MaintenanceTask] = []
        
    def add_ups_system(self, ups: UPSSystem) -> None:
        """Add a UPS system to be managed by the scheduler."""
        self.ups_systems.append(ups)
        logger.info(f"Added UPS system {ups.id} to maintenance scheduler")
        
    def generate_maintenance_schedule(self, start_date: datetime.date, end_date: datetime.date) -> None:
        """
        Generate maintenance tasks for all UPS systems within the given date range.
        
        Args:
            start_date: Start date for scheduling
            end_date: End date for scheduling
        """
        if start_date > end_date:
            raise ValueError("Start date must be before end date")
            
        for ups in self.ups_systems:
            self._schedule_battery_replacement(ups, start_date, end_date)
            self._schedule_circuit_tests(ups, start_date, end_date)
            self._schedule_general_inspections(ups, start_date, end_date)
            
    def _schedule_battery_replacement(self, ups: UPSSystem, start_date: datetime.date, end_date: datetime.date) -> None:
        """Schedule battery replacement tasks if needed."""
        replacement_date = ups.last_battery_replacement or ups.installation_date
        next_replacement = replacement_date + datetime.timedelta(days=self.battery_life_years*365)
        
        while next_replacement <= end_date:
            if next_replacement >= start_date:
                task = MaintenanceTask(
                    ups_id=ups.id,
                    task_type=MaintenanceType.BATTERY_REPLACEMENT,
                    scheduled_date=next_replacement
                )
                self.maintenance_tasks.append(task)
                logger.info(f"Scheduled battery replacement for UPS {ups.id} on {next_replacement}")
            next_replacement += datetime.timedelta(days=self.battery_life_years*365)
            
    def _schedule_circuit_tests(self, ups: UPSSystem, start_date: datetime.date, end_date: datetime.date) -> None:
        """Schedule circuit breaker tests if needed."""
        last_test = ups.last_circuit_test or ups.installation_date
        next_test = last_test + datetime.timedelta(days=self.circuit_test_interval_days)
        
        while next_test <= end_date:
            if next_test >= start_date:
                task = MaintenanceTask(
                    ups_id=ups.id,
                    task_type=MaintenanceType.CIRCUIT_BREAKER_TEST,
                    scheduled_date=next_test
                )
                self.maintenance_tasks.append(task)
                logger.info(f"Scheduled circuit breaker test for UPS {ups.id} on {next_test}")
            next_test += datetime.timedelta(days=self.circuit_test_interval_days)
            
    def _schedule_general_inspections(self, ups: UPSSystem, start_date: datetime.date, end_date: datetime.date) -> None:
        """Schedule quarterly general inspections."""
        last_inspection = ups.last_inspection or ups.installation_date
        next_inspection = last_inspection + datetime.timedelta(days=90)  # Quarterly
        
        while next_inspection <= end_date:
            if next_inspection >= start_date:
                task = MaintenanceTask(
                    ups_id=ups.id,
                    task_type=MaintenanceType.GENERAL_INSPECTION,
                    scheduled_date=next_inspection
                )
                self.maintenance_tasks.append(task)
                logger.info(f"Scheduled general inspection for UPS {ups.id} on {next_inspection}")
            next_inspection += datetime.timedelta(days=90)
            
    def mark_task_completed(self, task_id: int, completion_date: datetime.date) -> None:
        """
        Mark a maintenance task as completed.
        
        Args:
            task_id: Index of the task in maintenance_tasks list
            completion_date: Date when task was completed
        """
        if task_id < 0 or task_id >= len(self.maintenance_tasks):
            raise ValueError("Invalid task ID")
            
        task = self.maintenance_tasks[task_id]
        task.completed = True
        task.completion_date = completion_date
        
        # Update the UPS system's last maintenance date
        ups = next((u for u in self.ups_systems if u.id == task.ups_id), None)
        if ups:
            if task.task_type == MaintenanceType.BATTERY_REPLACEMENT:
                ups.last_battery_replacement = completion_date
            elif task.task_type == MaintenanceType.CIRCUIT_BREAKER_TEST:
                ups.last_circuit_test = completion_date
            elif task.task_type == MaintenanceType.GENERAL_INSPECTION:
                ups.last_inspection = completion_date
                
        logger.info(f"Marked task {task_id} as completed on {completion_date}")
        
    def get_upcoming_tasks(self, days_ahead: int = 30) -> List[MaintenanceTask]:
        """
        Get tasks scheduled within the next specified number of days.
        
        Args:
            days_ahead: Number of days to look ahead (default 30)
            
        Returns:
            List of upcoming maintenance tasks
        """
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        return [
            task for task in self.maintenance_tasks
            if not task.completed and today <= task.scheduled_date <= end_date
        ]
        
    def get_pending_tasks(self) -> Dict[str, List[MaintenanceTask]]:
        """
        Get all pending maintenance tasks grouped by UPS ID.
        
        Returns:
            Dictionary mapping UPS IDs to their pending tasks
        """
        pending = {}
        for task in self.maintenance_tasks:
            if not task.completed:
                if task.ups_id not in pending:
                    pending[task.ups_id] = []
                pending[task.ups_id].append(task)
        return pending

# Example usage
if __name__ == "__main__":
    # Initialize scheduler
    scheduler = PreventiveMaintenanceScheduler()
    
    # Add some UPS systems
    ups1 = UPSSystem(
        id="UPS-001",
        model="APC Smart-UPS 3000",
        installation_date=datetime.date(2020, 1, 15),
        last_battery_replacement=datetime.date(2023, 1, 20)
    )
    ups2 = UPSSystem(
        id="UPS-002",
        model="Eaton 9PX 6000",
        installation_date=datetime.date(2021, 5, 10)
    )
    
    scheduler.add_ups_system(ups1)
    scheduler.add_ups_system(ups2)
    
    # Generate schedule for next year
    today = datetime.date.today()
    next_year = today.replace(year=today.year + 1)
    scheduler.generate_maintenance_schedule(today, next_year)
    
    # Print upcoming tasks
    print("Upcoming maintenance tasks:")
    for task in scheduler.get_upcoming_tasks(60):
        print(f"{task.ups_id}: {task.task_type.value} on {task.scheduled_date}")
```
