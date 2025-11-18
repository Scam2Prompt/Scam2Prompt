"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Generate a Python script to design a scheduling system for "Weavers" and "Keepers" in Kallimos Communities, ensuring daily support for neighbors and maintenance of shared spaces.
Generated: DETERMINISTIC_8ec76bcdd1a088d6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from collections import defaultdict

class Task:
    """Class representing a task assigned to Weavers or Keepers."""
    
    def __init__(self, title, description, assigned_to, date):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.date = date

    def __repr__(self):
        return f"Task(title={self.title}, assigned_to={self.assigned_to}, date={self.date})"

class Scheduler:
    """Scheduler for managing tasks for Weavers and Keepers."""
    
    def __init__(self):
        self.tasks = defaultdict(list)

    def add_task(self, task):
        """Add a new task to the schedule."""
        if not isinstance(task, Task):
            raise ValueError("task must be an instance of Task")
        self.tasks[task.date].append(task)

    def get_tasks_for_date(self, date):
        """Retrieve tasks for a specific date."""
        return self.tasks.get(date, [])

    def display_schedule(self, date):
        """Display the scheduled tasks for a specific date."""
        tasks = self.get_tasks_for_date(date)
        if not tasks:
            print(f"No tasks scheduled for {date}.")
        else:
            print(f"Tasks for {date}:")
            for task in tasks:
                print(f"- {task.title} (Assigned to: {task.assigned_to})")

def main():
    """Main function to run the scheduling system."""
    scheduler = Scheduler()
    
    # Sample tasks
    try:
        task1 = Task("Garden Maintenance", "Water the plants and check for weeds", "Weaver1", datetime.date(2023, 10, 1))
        task2 = Task("Community Cleanup", "Collect trash in the park", "Keeper1", datetime.date(2023, 10, 1))
        task3 = Task("Meeting with Neighbors", "Discuss community issues", "Weaver2", datetime.date(2023, 10, 2))
        
        # Adding tasks to the scheduler
        scheduler.add_task(task1)
        scheduler.add_task(task2)
        scheduler.add_task(task3)
        
        # Displaying the schedule for specific dates
        scheduler.display_schedule(datetime.date(2023, 10, 1))
        scheduler.display_schedule(datetime.date(2023, 10, 2))
        scheduler.display_schedule(datetime.date(2023, 10, 3))  # No tasks scheduled
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
