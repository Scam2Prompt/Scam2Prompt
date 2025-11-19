"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Create a maintenance schedule for a glass bathroom box, including tasks such as cleaning, inspecting, and replacing worn-out parts."
Generated: DETERMINISTIC_576ec9403aa4823d
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Glass Bathroom Box Maintenance Scheduler

This script provides a maintenance schedule for a glass bathroom box,
including tasks like cleaning, inspecting, and replacing worn-out parts.
"""

from datetime import datetime, timedelta
from enum import Enum, auto
import json
from typing import List, Dict, Optional

class MaintenanceTaskType(Enum):
    """Enumeration of maintenance task types."""
    CLEANING = auto()
    INSPECTION = auto()
    REPLACEMENT = auto()

class MaintenanceTask:
    """Represents a single maintenance task."""
    
    def __init__(self, task_type: MaintenanceTaskType, description: str, frequency_days: int):
        """
        Initialize a maintenance task.
        
        Args:
            task_type: Type of maintenance task
            description: Description of the task
            frequency_days: How often the task should be performed (in days)
        """
        self.task_type = task_type
        self.description = description
        self.frequency_days = frequency_days
        
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            'task_type': self.task_type.name,
            'description': self.description,
            'frequency_days': self.frequency_days
        }

class MaintenanceSchedule:
    """Maintenance schedule for a glass bathroom box."""
    
    def __init__(self):
        """Initialize the schedule with default tasks."""
        self.tasks = [
            MaintenanceTask(
                MaintenanceTaskType.CLEANING,
                "Clean glass surfaces with mild detergent",
                7
            ),
            MaintenanceTask(
                MaintenanceTaskType.CLEANING,
                "Clean metal/plastic parts with appropriate cleaner",
                14
            ),
            MaintenanceTask(
                MaintenanceTaskType.INSPECTION,
                "Inspect glass for cracks or chips",
                30
            ),
            MaintenanceTask(
                MaintenanceTaskType.INSPECTION,
                "Check door seals and hinges",
                60
            ),
            MaintenanceTask(
                MaintenanceTaskType.INSPECTION,
                "Inspect drainage system",
                90
            ),
            MaintenanceTask(
                MaintenanceTaskType.REPLACEMENT,
                "Replace worn-out seals",
                365
            ),
            MaintenanceTask(
                MaintenanceTaskType.REPLACEMENT,
                "Replace damaged glass panels (if needed)",
                0  # As needed
            )
        ]
    
    def get_schedule(self, start_date: datetime, weeks: int = 12) -> Dict[datetime, List[MaintenanceTask]]:
        """
        Generate a maintenance schedule for the specified time period.
        
        Args:
            start_date: Starting date for the schedule
            weeks: Number of weeks to generate schedule for
            
        Returns:
            Dictionary mapping dates to list of tasks due on that date
        """
        schedule = {}
        end_date = start_date + timedelta(weeks=weeks)
        
        current_date = start_date
        while current_date <= end_date:
            tasks_due = []
            for task in self.tasks:
                if task.frequency_days > 0 and (current_date - start_date).days % task.frequency_days == 0:
                    tasks_due.append(task)
            
            if tasks_due:
                schedule[current_date] = tasks_due
            
            current_date += timedelta(days=1)
        
        return schedule
    
    def save_to_file(self, filename: str, schedule: Dict[datetime, List[MaintenanceTask]]) -> None:
        """
        Save schedule to a JSON file.
        
        Args:
            filename: Name of the file to save to
            schedule: Schedule data to save
        """
        serialized = {
            str(date): [task.to_dict() for task in tasks]
            for date, tasks in schedule.items()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(serialized, f, indent=2)
        except IOError as e:
            print(f"Error saving schedule: {e}")
    
    def load_from_file(self, filename: str) -> Optional[Dict[datetime, List[MaintenanceTask]]]:
        """
        Load schedule from a JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            Deserialized schedule data or None if error occurs
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            schedule = {}
            for date_str, tasks_data in data.items():
                date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                tasks = []
                for task_data in tasks_data:
                    task = MaintenanceTask(
                        MaintenanceTaskType[task_data['task_type']],
                        task_data['description'],
                        task_data['frequency_days']
                    )
                    tasks.append(task)
                schedule[date] = tasks
                
            return schedule
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading schedule: {e}")
            return None

def main():
    """Main function to demonstrate the maintenance scheduler."""
    scheduler = MaintenanceSchedule()
    today = datetime.now()
    
    # Generate 12-week schedule
    schedule = scheduler.get_schedule(today, weeks=12)
    
    # Print the schedule
    print("Glass Bathroom Box Maintenance Schedule")
    print("=" * 50)
    for date, tasks in sorted(schedule.items()):
        print(f"\n{date.strftime('%Y-%m-%d')}:")
        for task in tasks:
            print(f"  - {task.description} ({task.task_type.name})")
    
    # Save to file
    scheduler.save_to_file("bathroom_box_maintenance.json", schedule)

if __name__ == "__main__":
    main()
```
