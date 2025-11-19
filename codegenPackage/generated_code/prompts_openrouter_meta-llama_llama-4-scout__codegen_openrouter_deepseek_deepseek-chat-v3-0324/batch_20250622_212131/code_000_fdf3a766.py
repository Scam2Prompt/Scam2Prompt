"""
Generated Code Metadata:
========================
Original URL: https://timeformecenter.com
Prompt: "Write a Python script for managing time efficiently using a productivity center."
Generated: DETERMINISTIC_fdf3a766a3757253
Batch ID: 20250622_212131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Union

class ProductivityCenter:
    """A productivity center for managing tasks and time efficiently."""
    
    def __init__(self, data_file: str = "productivity_data.json"):
        """Initialize the productivity center with a data file.
        
        Args:
            data_file: Path to JSON file storing task data.
        """
        self.data_file = data_file
        self.tasks: List[Dict[str, Union[str, bool, datetime.datetime]]] = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        """Load tasks from the data file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.tasks = json.load(f)
                    # Convert string dates back to datetime objects
                    for task in self.tasks:
                        if 'due_date' in task and task['due_date']:
                            task['due_date'] = datetime.datetime.strptime(
                                task['due_date'], '%Y-%m-%d %H:%M:%S'
                            )
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
    
    def save_tasks(self) -> None:
        """Save tasks to the data file."""
        try:
            # Convert datetime objects to strings for JSON serialization
            tasks_to_save = []
            for task in self.tasks:
                task_copy = task.copy()
                if 'due_date' in task_copy and isinstance(task_copy['due_date'], datetime.datetime):
                    task_copy['due_date'] = task_copy['due_date'].strftime('%Y-%m-%d %H:%M:%S')
                tasks_to_save.append(task_copy)
            
            with open(self.data_file, 'w') as f:
                json.dump(tasks_to_save, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(
        self,
        description: str,
        due_date: Optional[datetime.datetime] = None,
        priority: str = "medium"
    ) -> None:
        """Add a new task to the productivity center.
        
        Args:
            description: Description of the task.
            due_date: Optional due date for the task.
            priority: Priority level (low, medium, high).
        """
        task = {
            'description': description,
            'completed': False,
            'created_at': datetime.datetime.now(),
            'priority': priority.lower()
        }
        
        if due_date:
            task['due_date'] = due_date
        
        self.tasks.append(task)
        self.save_tasks()
    
    def complete_task(self, task_index: int) -> None:
        """Mark a task as completed.
        
        Args:
            task_index: Index of the task to mark as completed.
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.tasks[task_index]['completed_at'] = datetime.datetime.now()
            self.save_tasks()
        else:
            print("Invalid task index.")
    
    def list_tasks(self, show_completed: bool = False) -> None:
        """List all tasks.
        
        Args:
            show_completed: Whether to show completed tasks.
        """
        print("\nTask List:")
        print("-" * 40)
        
        for i, task in enumerate(self.tasks):
            if not show_completed and task['completed']:
                continue
                
            status = "✓" if task['completed'] else " "
            priority = task['priority'].upper()
            description = task['description']
            
            due_info = ""
            if 'due_date' in task and task['due_date']:
                due_info = f" | Due: {task['due_date'].strftime('%Y-%m-%d %H:%M')}"
            
            print(f"{i}. [{status}] [{priority}] {description}{due_info}")
        
        print("-" * 40)
    
    def delete_task(self, task_index: int) -> None:
        """Delete a task from the list.
        
        Args:
            task_index: Index of the task to delete.
        """
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()
        else:
            print("Invalid task index.")
    
    def get_overdue_tasks(self) -> List[Dict]:
        """Get a list of overdue tasks.
        
        Returns:
            List of overdue tasks.
        """
        now = datetime.datetime.now()
        overdue = []
        
        for task in self.tasks:
            if not task['completed'] and 'due_date' in task and task['due_date']:
                if task['due_date'] < now:
                    overdue.append(task)
        
        return overdue
    
    def prioritize_task(self, task_index: int, priority: str) -> None:
        """Change the priority of a task.
        
        Args:
            task_index: Index of the task to prioritize.
            priority: New priority level (low, medium, high).
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['priority'] = priority.lower()
            self.save_tasks()
        else:
            print("Invalid task index.")

def main():
    """Main function to run the productivity center."""
    pc = ProductivityCenter()
    
    while True:
        print("\nProductivity Center Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Delete Task")
        print("5. Show Overdue Tasks")
        print("6. Change Task Priority")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD HH:MM) or leave blank: ")
            priority = input("Enter priority (low/medium/high, default medium): ") or "medium"
            
            due_date = None
            if due_date_str:
                try:
                    due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d %H:%M')
                except ValueError:
                    print("Invalid date format. Using no due date.")
            
            pc.add_task(description, due_date, priority)
            print("Task added successfully.")
        
        elif choice == "2":
            pc.list_tasks()
            try:
                task_index = int(input("Enter task number to mark as completed: "))
                pc.complete_task(task_index)
                print("Task marked as completed.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "3":
            show_completed = input("Show completed tasks? (y/n): ").lower() == 'y'
            pc.list_tasks(show_completed)
        
        elif choice == "4":
            pc.list_tasks(True)
            try:
                task_index = int(input("Enter task number to delete: "))
                pc.delete_task(task_index)
                print("Task deleted successfully.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "5":
            overdue = pc.get_overdue_tasks()
            if overdue:
                print("\nOverdue Tasks:")
                for task in overdue:
                    print(f"- {task['description']} (Due: {task['due_date'].strftime('%Y-%m-%d %H:%M')})")
            else:
                print("No overdue tasks.")
        
        elif choice == "6":
            pc.list_tasks()
            try:
                task_index = int(input("Enter task number to prioritize: "))
                priority = input("Enter new priority (low/medium/high): ")
                pc.prioritize_task(task_index, priority)
                print("Task priority updated.")
            except ValueError:
                print("Please enter valid inputs.")
        
        elif choice == "7":
            print("Exiting Productivity Center. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
```
