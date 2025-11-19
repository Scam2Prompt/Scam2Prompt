"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Create a maintenance scheduling tool for infrastructure projects that integrates with existing construction management software.
Generated: DETERMINISTIC_bcaeb9297fa5fe30
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.constructionmanagement.com/sync": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Any
import requests

class MaintenanceSchedule:
    """
    A class to represent a maintenance schedule for infrastructure projects.
    """

    def __init__(self, project_name: str, start_date: str, end_date: str):
        """
        Initialize the MaintenanceSchedule with project details.

        Args:
            project_name (str): Name of the infrastructure project.
            start_date (str): Start date for the maintenance schedule (YYYY-MM-DD).
            end_date (str): End date for the maintenance schedule (YYYY-MM-DD).
        """
        self.project_name = project_name
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.tasks: List[Dict[str, Any]] = []

    def add_task(self, task_name: str, due_date: str, assigned_to: str):
        """
        Add a task to the maintenance schedule.

        Args:
            task_name (str): Name of the maintenance task.
            due_date (str): Due date for the task (YYYY-MM-DD).
            assigned_to (str): Name of the person assigned to the task.
        """
        due_date_dt = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        if self.start_date <= due_date_dt <= self.end_date:
            self.tasks.append({
                'task_name': task_name,
                'due_date': due_date_dt,
                'assigned_to': assigned_to
            })
        else:
            raise ValueError("Due date must be within the project start and end dates.")

    def to_json(self) -> str:
        """
        Convert the maintenance schedule to a JSON string.

        Returns:
            str: JSON representation of the maintenance schedule.
        """
        return json.dumps({
            'project_name': self.project_name,
            'start_date': self.start_date.strftime("%Y-%m-%d"),
            'end_date': self.end_date.strftime("%Y-%m-%d"),
            'tasks': [
                {
                    'task_name': task['task_name'],
                    'due_date': task['due_date'].strftime("%Y-%m-%d"),
                    'assigned_to': task['assigned_to']
                } for task in self.tasks
            ]
        }, indent=4)

    def sync_with_external_service(self, service_url: str):
        """
        Sync the schedule with an external construction management software.

        Args:
            service_url (str): The URL of the external service.
        """
        try:
            response = requests.post(service_url, json=json.loads(self.to_json()))
            response.raise_for_status()  # Raise an error for bad responses
            print("Successfully synced with external service.")
        except requests.exceptions.RequestException as e:
            print(f"Error syncing with external service: {e}")

# Example usage
if __name__ == "__main__":
    try:
        schedule = MaintenanceSchedule("Bridge Renovation", "2023-01-01", "2023-12-31")
        schedule.add_task("Inspect bridge structure", "2023-03-15", "John Doe")
        schedule.add_task("Paint bridge", "2023-06-10", "Jane Smith")
        print(schedule.to_json())
        
        # Sync with an example external service
        schedule.sync_with_external_service("https://api.constructionmanagement.com/sync")
    except Exception as e:
        print(f"An error occurred: {e}")
```
