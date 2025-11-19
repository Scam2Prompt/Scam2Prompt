"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Generate a code snippet for a simple plumbing inspection and maintenance checklist, inspired by the services provided by Certified Plumbers Graham, TX."
Generated: DETERMINISTIC_882a2ced2dfe28f9
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Plumbing Inspection and Maintenance Checklist
Inspired by Certified Plumbers Graham, TX

This script provides a simple checklist for plumbing inspection and maintenance tasks.
It allows users to track completed tasks and generate reports.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional

class PlumbingChecklist:
    """
    A class representing a plumbing inspection and maintenance checklist.
    """
    
    def __init__(self):
        """
        Initialize the checklist with default tasks and empty completion status.
        """
        self.tasks = [
            {"id": 1, "description": "Inspect water pressure", "completed": False},
            {"id": 2, "description": "Check for leaks in pipes and fixtures", "completed": False},
            {"id": 3, "description": "Test water heater performance", "completed": False},
            {"id": 4, "description": "Inspect drains for clogs or slow drainage", "completed": False},
            {"id": 5, "description": "Check toilet functionality and leaks", "completed": False},
            {"id": 6, "description": "Inspect faucets and showerheads for leaks", "completed": False},
            {"id": 7, "description": "Expose water supply valves for accessibility", "completed": False},
            {"id": 8, "description": "Check sump pump operation (if applicable)", "completed": False},
            {"id": 9, "description": "Inspect exposed pipes for corrosion", "completed": False},
            {"id": 10, "description": "Verify proper operation of garbage disposal", "completed": False}
        ]
        self.inspection_date = datetime.now().strftime("%Y-%m-%d")
        self.notes = ""
    
    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as completed by its ID.
        
        Args:
            task_id: The ID of the task to mark as complete
            
        Returns:
            bool: True if task was found and marked, False otherwise
        """
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True
        return False
    
    def add_custom_task(self, description: str) -> None:
        """
        Add a custom task to the checklist.
        
        Args:
            description: Description of the new task
        """
        new_id = max(task["id"] for task in self.tasks) + 1 if self.tasks else 1
        self.tasks.append({
            "id": new_id,
            "description": description,
            "completed": False
        })
    
    def get_completion_percentage(self) -> float:
        """
        Calculate the percentage of completed tasks.
        
        Returns:
            float: Percentage of tasks completed (0-100)
        """
        if not self.tasks:
            return 0.0
        completed = sum(1 for task in self.tasks if task["completed"])
        return (completed / len(self.tasks)) * 100
    
    def generate_report(self) -> Dict:
        """
        Generate a report of the checklist status.
        
        Returns:
            Dict: A dictionary containing the report data
        """
        return {
            "inspection_date": self.inspection_date,
            "total_tasks": len(self.tasks),
            "completed_tasks": sum(1 for task in self.tasks if task["completed"]),
            "completion_percentage": self.get_completion_percentage(),
            "notes": self.notes,
            "tasks": self.tasks
        }
    
    def save_to_file(self, filename: str) -> bool:
        """
        Save the checklist to a JSON file.
        
        Args:
            filename: Path to the output file
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_report(), f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving checklist: {e}")
            return False
    
    @classmethod
    def load_from_file(cls, filename: str) -> Optional['PlumbingChecklist']:
        """
        Load a checklist from a JSON file.
        
        Args:
            filename: Path to the input file
            
        Returns:
            Optional[PlumbingChecklist]: Loaded checklist or None if failed
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            checklist = cls()
            checklist.inspection_date = data.get("inspection_date", datetime.now().strftime("%Y-%m-%d"))
            checklist.notes = data.get("notes", "")
            
            # Preserve original tasks and update with saved data
            saved_tasks = {task["id"]: task for task in data.get("tasks", [])}
            for task in checklist.tasks:
                if task["id"] in saved_tasks:
                    task["completed"] = saved_tasks[task["id"]]["completed"]
            
            # Add any additional tasks that weren't in the default list
            default_ids = {task["id"] for task in checklist.tasks}
            for task in data.get("tasks", []):
                if task["id"] not in default_ids:
                    checklist.tasks.append(task)
            
            return checklist
        except Exception as e:
            print(f"Error loading checklist: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create a new checklist
    checklist = PlumbingChecklist()
    
    # Mark some tasks as complete
    checklist.mark_task_complete(1)
    checklist.mark_task_complete(3)
    
    # Add a custom task
    checklist.add_custom_task("Inspect outdoor faucets for winterization")
    
    # Add some notes
    checklist.notes = "Found minor leak under kitchen sink - needs repair"
    
    # Generate and print report
    report = checklist.generate_report()
    print(f"Inspection Date: {report['inspection_date']}")
    print(f"Completion: {report['completion_percentage']:.1f}%")
    print("Tasks:")
    for task in report['tasks']:
        status = "✓" if task['completed'] else " "
        print(f" [{status}] {task['id']}. {task['description']}")
    
    # Save to file
    checklist.save_to_file("plumbing_checklist.json")
    
    # Load from file (example)
    # loaded_checklist = PlumbingChecklist.load_from_file("plumbing_checklist.json")
```
