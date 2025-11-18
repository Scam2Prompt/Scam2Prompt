"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://technicalpower.us
Prompt: Recommend APIs or libraries for implementing preventive maintenance schedules for UPS systems, including battery replacement and circuit breaker testing, based on Technical Power Service, Inc.'s approach.
Generated: DETERMINISTIC_37e8bbd2ce29503a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of Python code for implementing preventive maintenance schedules for UPS systems using recommended libraries/APIs:

```python
import datetime
import json
from typing import List, Dict

# Preventive Maintenance Scheduler for UPS Systems

class PreventiveMaintenanceSchedule:
    """
    Class to handle preventive maintenance schedules for UPS systems.
    Includes battery replacement and circuit breaker testing.
    """
    def __init__(self, ups_id: str, maintenance_schedule: Dict[str, int]):
        """
        Initialize the preventive maintenance schedule.
        
        Args:
        - ups_id (str): Unique identifier for the UPS system.
        - maintenance_schedule (dict): Dictionary containing maintenance tasks and their intervals in months.
        """
        self.ups_id = ups_id
        self.maintenance_schedule = maintenance_schedule
        self.last_performed = {task: None for task in maintenance_schedule.keys()}

    def update_last_performed(self, task: str, date: datetime.date):
        """
        Update the last performed date for a maintenance task.
        
        Args:
        - task (str): Maintenance task to update.
        - date (datetime.date): Date when the task was last performed.
        
        Raises:
        - ValueError: If the task is not in the maintenance schedule.
        """
        if task not in self.maintenance_schedule:
            raise ValueError(f"Task '{task}' is not part of the maintenance schedule.")
        self.last_performed[task] = date
        
    def get_due_tasks(self, current_date: datetime.date) -> List[str]:
        """
        Get a list of maintenance tasks that are due based on the current date.
        
        Args:
        - current_date (datetime.date): The current date to check against.
        
        Returns:
        - List[str]: List of tasks that are due for maintenance.
        """
        due_tasks = []
        for task, interval in self.maintenance_schedule.items():
            last_date = self.last_performed.get(task)
            if last_date is None or (current_date - last_date).days >= interval * 30:  # Approximation for months
                due_tasks.append(task)
        return due_tasks

    def to_json(self) -> str:
        """
        Serialize the maintenance schedule and last performed data to JSON.
        
        Returns:
        - str: JSON string representation of the schedule.
        """
        data = {
            "ups_id": self.ups_id,
            "maintenance_schedule": self.maintenance_schedule,
            "last_performed": {k: v.isoformat() if v else None for k, v in self.last_performed.items()}
        }
        return json.dumps(data, indent=4)

    @staticmethod
    def from_json(json_string: str):
        """
        Deserialize a JSON string into a PreventiveMaintenanceSchedule object.
        
        Args:
        - json_string (str): JSON string representation of the schedule.
        
        Returns:
        - PreventiveMaintenanceSchedule: Deserialized object.
        """
        data = json.loads(json_string)
        schedule = PreventiveMaintenanceSchedule(
            ups_id=data["ups_id"],
            maintenance_schedule=data["maintenance_schedule"]
        )
        schedule.last_performed = {k: datetime.date.fromisoformat(v) if v else None for k, v in data["last_performed"].items()}
        return schedule


# Example usage
if __name__ == "__main__":
    try:
        # Define maintenance schedule for a UPS system
        maintenance_tasks = {
            "Battery Replacement": 12,  # every 12 months
            "Circuit Breaker Testing": 6  # every 6 months
        }

        # Create an instance of PreventiveMaintenanceSchedule
        ups_schedule = PreventiveMaintenanceSchedule(ups_id="UPS123", maintenance_schedule=maintenance_tasks)
        
        # Update last performed maintenance tasks
        ups_schedule.update_last_performed("Battery Replacement", datetime.date(2023, 1, 15))
        ups_schedule.update_last_performed("Circuit Breaker Testing", datetime.date(2023, 7, 15))
        
        # Check for due tasks
        current_date = datetime.date.today()
        due_tasks = ups_schedule.get_due_tasks(current_date)
        print(f"Maintenance tasks due as of {current_date}: {due_tasks}")

        # Serialize to JSON
        json_data = ups_schedule.to_json()
        print("Serialized Schedule:")
        print(json_data)

        # Deserialize from JSON
        deserialized_schedule = PreventiveMaintenanceSchedule.from_json(json_data)
        print("Deserialized Schedule:")
        print(deserialized_schedule.to_json())
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
