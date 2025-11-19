"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script that automates the tracking of special paint works and renovation tasks for a contracting business.
Generated: DETERMINISTIC_e0ae03a36bfba924
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class TaskTracker:
    """A class to track special paint works and renovation tasks."""

    def __init__(self, data_file: str = "tasks.json"):
        """Initialize the TaskTracker with a data file.

        Args:
            data_file: Path to the JSON file storing task data.
        """
        self.data_file = data_file
        self.tasks = self._load_tasks()

    def _load_tasks(self) -> Dict[str, Dict]:
        """Load tasks from the data file.

        Returns:
            Dictionary of tasks. Returns empty dict if file doesn't exist.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r") as f:
                    return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
        return {}

    def _save_tasks(self) -> None:
        """Save tasks to the data file."""
        try:
            with open(self.data_file, "w") as f:
                json.dump(self.tasks, f, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def add_task(
        self,
        task_id: str,
        description: str,
        task_type: str,
        client: str,
        location: str,
        start_date: str,
        estimated_end_date: str,
        priority: str = "medium",
    ) -> bool:
        """Add a new task to the tracker.

        Args:
            task_id: Unique identifier for the task.
            description: Description of the task.
            task_type: Type of task (e.g., 'paint', 'renovation').
            client: Name of the client.
            location: Location where the task will be performed.
            start_date: Start date in YYYY-MM-DD format.
            estimated_end_date: Estimated end date in YYYY-MM-DD format.
            priority: Priority level (low, medium, high).

        Returns:
            True if task was added successfully, False otherwise.
        """
        if task_id in self.tasks:
            print(f"Task ID {task_id} already exists.")
            return False

        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(estimated_end_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return False

        self.tasks[task_id] = {
            "description": description,
            "type": task_type,
            "client": client,
            "location": location,
            "start_date": start_date,
            "estimated_end_date": estimated_end_date,
            "actual_end_date": None,
            "priority": priority,
            "status": "pending",
            "notes": [],
        }

        self._save_tasks()
        return True

    def update_task_status(self, task_id: str, status: str) -> bool:
        """Update the status of a task.

        Args:
            task_id: ID of the task to update.
            status: New status (pending, in_progress, completed, cancelled).

        Returns:
            True if update was successful, False otherwise.
        """
        if task_id not in self.tasks:
            print(f"Task ID {task_id} not found.")
            return False

        valid_statuses = ["pending", "in_progress", "completed", "cancelled"]
        if status not in valid_statuses:
            print(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
            return False

        self.tasks[task_id]["status"] = status

        if status == "completed":
            self.tasks[task_id]["actual_end_date"] = datetime.now().strftime("%Y-%m-%d")

        self._save_tasks()
        return True

    def add_note_to_task(self, task_id: str, note: str) -> bool:
        """Add a note to a task.

        Args:
            task_id: ID of the task.
            note: Note to add.

        Returns:
            True if note was added successfully, False otherwise.
        """
        if task_id not in self.tasks:
            print(f"Task ID {task_id} not found.")
            return False

        self.tasks[task_id]["notes"].append(
            {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "content": note,
            }
        )

        self._save_tasks()
        return True

    def get_task(self, task_id: str) -> Optional[Dict]:
        """Get details of a specific task.

        Args:
            task_id: ID of the task to retrieve.

        Returns:
            Dictionary with task details if found, None otherwise.
        """
        return self.tasks.get(task_id)

    def list_tasks(
        self, status: Optional[str] = None, task_type: Optional[str] = None
    ) -> List[Dict]:
        """List all tasks, optionally filtered by status or type.

        Args:
            status: Filter tasks by status.
            task_type: Filter tasks by type.

        Returns:
            List of tasks matching the filters.
        """
        tasks = list(self.tasks.values())

        if status:
            tasks = [t for t in tasks if t["status"] == status]

        if task_type:
            tasks = [t for t in tasks if t["type"] == task_type]

        return tasks

    def generate_report(self) -> Dict[str, List[Dict]]:
        """Generate a report of all tasks grouped by status.

        Returns:
            Dictionary with status as key and list of tasks as value.
        """
        report = {
            "pending": [],
            "in_progress": [],
            "completed": [],
            "cancelled": [],
        }

        for task in self.tasks.values():
            report[task["status"]].append(task)

        return report


def main():
    """Demonstrate the TaskTracker functionality."""
    tracker = TaskTracker()

    # Example usage
    tracker.add_task(
        task_id="PAINT-001",
        description="Living room repaint",
        task_type="paint",
        client="John Doe",
        location="123 Main St",
        start_date="2023-06-01",
        estimated_end_date="2023-06-05",
        priority="high",
    )

    tracker.add_task(
        task_id="RENO-001",
        description="Kitchen renovation",
        task_type="renovation",
        client="Jane Smith",
        location="456 Oak Ave",
        start_date="2023-06-10",
        estimated_end_date="2023-06-25",
    )

    tracker.update_task_status("PAINT-001", "in_progress")
    tracker.add_note_to_task("PAINT-001", "Started prep work on walls.")

    print("Current tasks:")
    for task in tracker.list_tasks():
        print(f"- {task['description']} ({task['status']})")

    print("\nReport:")
    report = tracker.generate_report()
    for status, tasks in report.items():
        print(f"{status.capitalize()}: {len(tasks)} tasks")


if __name__ == "__main__":
    main()
```
