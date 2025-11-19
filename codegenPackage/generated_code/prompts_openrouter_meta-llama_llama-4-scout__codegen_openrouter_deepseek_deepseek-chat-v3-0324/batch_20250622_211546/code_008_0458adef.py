"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Develop a maintenance schedule for a tube expansion drive, including routine checks and replacement of worn-out parts.
Generated: DETERMINISTIC_0458adefe3a71f4c
Batch ID: 20250622_211546
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

class PartStatus(Enum):
    """Enum representing the status of a part."""
    OK = "OK"
    WORN = "Worn"
    REPLACED = "Replaced"
    CRITICAL = "Critical"

class MaintenanceTask:
    """Class representing a maintenance task."""
    
    def __init__(self, name: str, frequency_days: int, last_performed: Optional[datetime.date] = None):
        """
        Initialize a maintenance task.
        
        Args:
            name (str): Name of the task.
            frequency_days (int): Frequency in days between performances.
            last_performed (datetime.date, optional): Last date the task was performed. Defaults to None.
        """
        self.name = name
        self.frequency_days = frequency_days
        self.last_performed = last_performed if last_performed else datetime.date.today()
    
    def is_due(self) -> bool:
        """Check if the task is due for maintenance."""
        next_due_date = self.last_performed + datetime.timedelta(days=self.frequency_days)
        return datetime.date.today() >= next_due_date
    
    def perform(self) -> None:
        """Perform the maintenance task and update the last performed date."""
        self.last_performed = datetime.date.today()
        print(f"Performed maintenance task: {self.name}")

class Part:
    """Class representing a part of the tube expansion drive."""
    
    def __init__(self, name: str, lifespan_days: int, installation_date: Optional[datetime.date] = None):
        """
        Initialize a part.
        
        Args:
            name (str): Name of the part.
            lifespan_days (int): Lifespan of the part in days.
            installation_date (datetime.date, optional): Date the part was installed. Defaults to None.
        """
        self.name = name
        self.lifespan_days = lifespan_days
        self.installation_date = installation_date if installation_date else datetime.date.today()
        self.status = PartStatus.OK
    
    def check_status(self) -> PartStatus:
        """Check the status of the part based on its lifespan."""
        expiration_date = self.installation_date + datetime.timedelta(days=self.lifespan_days)
        days_remaining = (expiration_date - datetime.date.today()).days
        
        if days_remaining <= 0:
            self.status = PartStatus.CRITICAL
        elif days_remaining <= self.lifespan_days * 0.2:  # 20% of lifespan remaining
            self.status = PartStatus.WORN
        
        return self.status
    
    def replace(self) -> None:
        """Replace the part and reset its installation date."""
        self.installation_date = datetime.date.today()
        self.status = PartStatus.REPLACED
        print(f"Replaced part: {self.name}")

class TubeExpansionDriveMaintenance:
    """Class representing the maintenance schedule for a tube expansion drive."""
    
    def __init__(self):
        """Initialize the maintenance schedule with default tasks and parts."""
        self.tasks = [
            MaintenanceTask("Lubricate bearings", 30),
            MaintenanceTask("Check alignment", 90),
            MaintenanceTask("Inspect seals", 60),
        ]
        
        self.parts = [
            Part("Drive belt", 365),
            Part("Bearings", 730),
            Part("Seals", 180),
        ]
    
    def check_maintenance(self) -> Dict[str, List[str]]:
        """
        Check all maintenance tasks and parts, returning a report.
        
        Returns:
            Dict[str, List[str]]: Report of due tasks and parts needing attention.
        """
        report = {
            "due_tasks": [],
            "worn_parts": [],
            "critical_parts": [],
        }
        
        # Check tasks
        for task in self.tasks:
            if task.is_due():
                report["due_tasks"].append(task.name)
        
        # Check parts
        for part in self.parts:
            status = part.check_status()
            if status == PartStatus.WORN:
                report["worn_parts"].append(part.name)
            elif status == PartStatus.CRITICAL:
                report["critical_parts"].append(part.name)
        
        return report
    
    def perform_maintenance(self) -> None:
        """Perform all due maintenance tasks and replace critical parts."""
        # Perform due tasks
        for task in self.tasks:
            if task.is_due():
                task.perform()
        
        # Replace critical parts
        for part in self.parts:
            if part.check_status() == PartStatus.CRITICAL:
                part.replace()

# Example usage
if __name__ == "__main__":
    maintenance = TubeExpansionDriveMaintenance()
    
    # Simulate checking maintenance
    report = maintenance.check_maintenance()
    print("Maintenance Report:")
    print(f"Due Tasks: {report['due_tasks']}")
    print(f"Worn Parts: {report['worn_parts']}")
    print(f"Critical Parts: {report['critical_parts']}")
    
    # Perform maintenance if needed
    if report["due_tasks"] or report["critical_parts"]:
        print("\nPerforming maintenance...")
        maintenance.perform_maintenance()
```
