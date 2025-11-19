"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Write a script to plan and track the furniture moving process, including packing, transportation, and unpacking, inspired by شركة آل البيت's systematic approach.
Generated: DETERMINISTIC_af06796509a288a6
Batch ID: 20250612_151659
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

class FurnitureMover:
    def __init__(self, client_name):
        """
        Initialize the FurnitureMover with the client's name and an empty task list.
        """
        self.client_name = client_name
        self.tasks = []
        self.start_date = None
        self.end_date = None

    def add_task(self, task_name, due_date):
        """
        Add a task to the moving process.

        :param task_name: Name of the task to be added
        :param due_date: Due date for the task (datetime object)
        """
        if not isinstance(due_date, datetime.date):
            raise ValueError("Due date must be a datetime.date object.")
        
        task = {
            'name': task_name,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)

    def complete_task(self, task_name):
        """
        Mark a task as completed.

        :param task_name: Name of the task to be marked as completed
        """
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = True
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def set_dates(self, start_date, end_date):
        """
        Set the start and end dates for the moving process.

        :param start_date: Start date (datetime object)
        :param end_date: End date (datetime object)
        """
        if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
            raise ValueError("Start and end dates must be datetime.date objects.")
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
        
        self.start_date = start_date
        self.end_date = end_date

    def save_plan(self, filename):
        """
        Save the moving plan to a JSON file.

        :param filename: Name of the file to save the plan
        """
        plan = {
            'client_name': self.client_name,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'tasks': self.tasks
        }
        with open(filename, 'w') as file:
            json.dump(plan, file, indent=4)

    def load_plan(self, filename):
        """
        Load a moving plan from a JSON file.

        :param filename: Name of the file to load the plan from
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        
        with open(filename, 'r') as file:
            plan = json.load(file)
            self.client_name = plan['client_name']
            self.start_date = datetime.date.fromisoformat(plan['start_date']) if plan['start_date'] else None
            self.end_date = datetime.date.fromisoformat(plan['end_date']) if plan['end_date'] else None
            self.tasks = plan['tasks']

    def display_plan(self):
        """
        Display the current moving plan in a readable format.
        """
        print(f"Moving Plan for: {self.client_name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print("Tasks:")
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Pending"
            print(f" - {task['name']} (Due: {task['due_date']}, Status: {status})")

# Example usage
if __name__ == "__main__":
    mover = FurnitureMover("شركة آل البيت")
    mover.set_dates(datetime.date(2023, 10, 1), datetime.date(2023, 10, 10))
    mover.add_task("Pack furniture", datetime.date(2023, 10, 2))
    mover.add_task("Load truck", datetime.date(2023, 10, 3))
    mover.add_task("Unload truck", datetime.date(2023, 10, 4))
    mover.add_task("Unpack furniture", datetime.date(2023, 10, 5))
    
    mover.complete_task("Pack furniture")
    
    mover.display_plan()
    mover.save_plan("moving_plan.json")
```
