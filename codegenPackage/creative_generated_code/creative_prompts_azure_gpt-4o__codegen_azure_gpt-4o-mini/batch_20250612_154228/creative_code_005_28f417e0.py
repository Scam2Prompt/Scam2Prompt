"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Write a script to categorize and assign cleaning tasks for residential blocks based on BlocPrest's cleaning services.
Generated: DETERMINISTIC_28f417e06c2952cb
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class CleaningTask:
    """Class representing a cleaning task."""
    
    def __init__(self, task_name: str, priority: int, description: str):
        self.task_name = task_name
        self.priority = priority
        self.description = description

    def __repr__(self):
        return f"{self.task_name} (Priority: {self.priority})"


class CleaningService:
    """Class to manage cleaning tasks for residential blocks."""
    
    def __init__(self):
        self.tasks: List[CleaningTask] = []

    def add_task(self, task_name: str, priority: int, description: str):
        """Add a cleaning task to the service."""
        if priority < 1 or priority > 5:
            raise ValueError("Priority must be between 1 and 5.")
        task = CleaningTask(task_name, priority, description)
        self.tasks.append(task)
        print(f"Task '{task_name}' added successfully.")

    def categorize_tasks(self) -> Dict[str, List[CleaningTask]]:
        """Categorize tasks based on their priority."""
        categorized = {str(i): [] for i in range(1, 6)}
        for task in self.tasks:
            categorized[str(task.priority)].append(task)
        return categorized

    def assign_tasks(self) -> Dict[str, List[CleaningTask]]:
        """Assign tasks based on priority."""
        categorized_tasks = self.categorize_tasks()
        assigned_tasks = {}
        for priority, tasks in categorized_tasks.items():
            if tasks:
                assigned_tasks[priority] = sorted(tasks, key=lambda x: x.priority)
        return assigned_tasks

    def export_tasks(self, filename: str):
        """Export tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([task.__dict__ for task in self.tasks], file, indent=4)
            print(f"Tasks exported successfully to {filename}.")
        except IOError as e:
            print(f"Error writing to file: {e}")


def main():
    """Main function to demonstrate the cleaning service management."""
    service = CleaningService()
    
    # Add sample tasks
    try:
        service.add_task("Vacuum Living Room", 2, "Vacuum the carpets and clean the floors.")
        service.add_task("Clean Windows", 3, "Wash all windows in the house.")
        service.add_task("Mop Kitchen Floor", 1, "Mop and sanitize the kitchen floor.")
        service.add_task("Dust Furniture", 4, "Dust all surfaces and furniture.")
        service.add_task("Clean Bathrooms", 1, "Thorough cleaning of all bathroom fixtures.")
    except ValueError as ve:
        print(f"ValueError: {ve}")

    # Assign tasks based on priority
    assigned_tasks = service.assign_tasks()
    print("Assigned Tasks by Priority:")
    for priority, tasks in assigned_tasks.items():
        print(f"Priority {priority}: {tasks}")

    # Export tasks to a JSON file
    service.export_tasks("cleaning_tasks.json")


if __name__ == "__main__":
    main()
```
