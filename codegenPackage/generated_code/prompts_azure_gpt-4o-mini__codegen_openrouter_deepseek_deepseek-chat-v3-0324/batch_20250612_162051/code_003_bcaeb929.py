"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Create a maintenance scheduling tool for infrastructure projects that integrates with existing construction management software.
Generated: DETERMINISTIC_bcaeb9297fa5fe30
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.construction-management.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional
import requests
from requests.exceptions import RequestException

# Constants
API_BASE_URL = "https://api.construction-management.com/v1"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

class MaintenanceTask:
    """Class representing a maintenance task."""
    
    def __init__(self, task_id: str, name: str, description: str, 
                 due_date: datetime.date, priority: str, 
                 assigned_team: str, status: str = "Pending"):
        """
        Initialize a maintenance task.
        
        Args:
            task_id: Unique identifier for the task
            name: Name of the task
            description: Detailed description
            due_date: When the task needs to be completed
            priority: Priority level (Low, Medium, High)
            assigned_team: Team responsible for the task
            status: Current status (default: Pending)
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.assigned_team = assigned_team
        self.status = status

    def to_dict(self) -> Dict:
        """Convert task to dictionary for API calls."""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date.isoformat(),
            "priority": self.priority,
            "assigned_team": self.assigned_team,
            "status": self.status
        }

class MaintenanceScheduler:
    """Main class for maintenance scheduling operations."""
    
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []
    
    def add_task(self, task: MaintenanceTask) -> bool:
        """
        Add a new maintenance task.
        
        Args:
            task: MaintenanceTask object to add
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.tasks.append(task)
            return True
        except Exception as e:
            print(f"Error adding task: {e}")
            return False
    
    def get_tasks(self) -> List[MaintenanceTask]:
        """Get all maintenance tasks."""
        return self.tasks
    
    def get_task_by_id(self, task_id: str) -> Optional[MaintenanceTask]:
        """
        Get a task by its ID.
        
        Args:
            task_id: ID of the task to retrieve
            
        Returns:
            MaintenanceTask if found, None otherwise
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def update_task_status(self, task_id: str, new_status: str) -> bool:
        """
        Update a task's status.
        
        Args:
            task_id: ID of the task to update
            new_status: New status to set
            
        Returns:
            bool: True if successful, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.status = new_status
            return True
        return False
    
    def sync_with_cm_software(self) -> bool:
        """
        Sync tasks with construction management software via API.
        
        Returns:
            bool: True if sync successful, False otherwise
        """
        try:
            tasks_data = [task.to_dict() for task in self.tasks]
            response = requests.post(
                f"{API_BASE_URL}/maintenance/tasks/bulk",
                headers=HEADERS,
                data=json.dumps({"tasks": tasks_data})
            )
            response.raise_for_status()
            return True
        except RequestException as e:
            print(f"API request failed: {e}")
            return False
        except Exception as e:
            print(f"Error during sync: {e}")
            return False
    
    def get_upcoming_tasks(self, days: int = 7) -> List[MaintenanceTask]:
        """
        Get tasks due within a specified number of days.
        
        Args:
            days: Number of days to look ahead (default: 7)
            
        Returns:
            List of upcoming tasks
        """
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days)
        return [
            task for task in self.tasks
            if today <= task.due_date <= end_date
        ]

def validate_task_data(task_data: Dict) -> bool:
    """
    Validate maintenance task data before creation.
    
    Args:
        task_data: Dictionary containing task data
        
    Returns:
        bool: True if valid, False otherwise
    """
    required_fields = ["task_id", "name", "description", "due_date", "priority", "assigned_team"]
    for field in required_fields:
        if field not in task_data:
            print(f"Missing required field: {field}")
            return False
    
    try:
        datetime.date.fromisoformat(task_data["due_date"])
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return False
    
    if task_data["priority"] not in ["Low", "Medium", "High"]:
        print("Priority must be Low, Medium, or High")
        return False
    
    return True

def create_task_from_data(task_data: Dict) -> Optional[MaintenanceTask]:
    """
    Create a MaintenanceTask from dictionary data.
    
    Args:
        task_data: Dictionary containing task data
        
    Returns:
        MaintenanceTask if valid, None otherwise
    """
    if not validate_task_data(task_data):
        return None
    
    try:
        return MaintenanceTask(
            task_id=task_data["task_id"],
            name=task_data["name"],
            description=task_data["description"],
            due_date=datetime.date.fromisoformat(task_data["due_date"]),
            priority=task_data["priority"],
            assigned_team=task_data["assigned_team"],
            status=task_data.get("status", "Pending")
        )
    except Exception as e:
        print(f"Error creating task: {e}")
        return None

# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()
    
    # Create a sample task
    sample_task = MaintenanceTask(
        task_id="MT-001",
        name="Bridge Inspection",
        description="Annual structural inspection of main bridge",
        due_date=datetime.date.today() + datetime.timedelta(days=14),
        priority="High",
        assigned_team="Structural Engineering"
    )
    
    # Add task to scheduler
    if scheduler.add_task(sample_task):
        print("Task added successfully")
    
    # Sync with construction management software
    if scheduler.sync_with_cm_software():
        print("Sync completed successfully")
    else:
        print("Sync failed")
    
    # Get upcoming tasks
    upcoming = scheduler.get_upcoming_tasks(30)
    print(f"Upcoming tasks: {len(upcoming)}")
```
