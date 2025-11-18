"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeg-group.com
Prompt: Create a script to automate the scheduling of outdoor environment maintenance tasks, incorporating the "nurture thriving environments with expertise and dedication" philosophy from Outdoor Environments Group.
Generated: DETERMINISTIC_fb11524426b6eb47
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for automating the scheduling of outdoor environment maintenance tasks:

```python
import datetime
import json
import os

class MaintenanceScheduler:
    """
    A class to automate the scheduling of outdoor environment maintenance tasks.
    Philosophy: Nurture thriving environments with expertise and dedication.
    """

    def __init__(self, tasks_file='tasks.json', schedule_file='schedule.json'):
        """
        Initializes the scheduler with file paths for tasks and schedule storage.
        """
        self.tasks_file = tasks_file
        self.schedule_file = schedule_file
        self.tasks = self.load_tasks()
        self.schedule = self.load_schedule()

    def load_tasks(self):
        """Loads maintenance tasks from a JSON file."""
        if not os.path.exists(self.tasks_file):
            # Return an empty list if the file does not exist
            return []
        
        try:
            with open(self.tasks_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading tasks file: {e}")
            return []

    def load_schedule(self):
        """Loads the existing schedule from a JSON file."""
        if not os.path.exists(self.schedule_file):
            # Return an empty dictionary if the file does not exist
            return {}
        
        try:
            with open(self.schedule_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading schedule file: {e}")
            return {}

    def save_schedule(self):
        """Saves the updated schedule to a JSON file."""
        try:
            with open(self.schedule_file, 'w') as file:
                json.dump(self.schedule, file, indent=4)
        except Exception as e:
            print(f"Error saving schedule: {e}")

    def schedule_task(self, task_name, frequency):
        """
        Schedules a maintenance task based on its frequency.
        :param task_name: Name of the task to be scheduled.
        :param frequency: Frequency of the task (daily, weekly, monthly).
        """
        if not task_name or not frequency:
            print("Invalid task name or frequency.")
            return

        if frequency not in ['daily', 'weekly', 'monthly']:
            print("Frequency must be one of: daily, weekly, monthly.")
            return

        next_date = self.calculate_next_date(frequency)
        self.schedule[task_name] = next_date
        print(f"Scheduled '{task_name}' for {next_date}.")
        self.save_schedule()

    @staticmethod
    def calculate_next_date(frequency):
        """
        Calculates the next date for a task based on its frequency.
        :param frequency: Frequency of the task (daily, weekly, monthly).
        :return: The next scheduled date as a string (YYYY-MM-DD).
        """
        today = datetime.date.today()
        if frequency == 'daily':
            next_date = today + datetime.timedelta(days=1)
        elif frequency == 'weekly':
            next_date = today + datetime.timedelta(weeks=1)
        elif frequency == 'monthly':
            next_date = today + datetime.timedelta(days=30)  # Rough approximation
        return next_date.strftime('%Y-%m-%d')

    def display_schedule(self):
        """Displays the current schedule in a readable format."""
        if not self.schedule:
            print("No tasks scheduled yet.")
            return

        print("Current Maintenance Schedule:")
        for task, date in self.schedule.items():
            print(f"  - {task}: {date}")

    def add_task(self, task_name):
        """
        Adds a new maintenance task to the list.
        :param task_name: Name of the task to be added.
        """
        if not task_name:
            print("Task name cannot be empty.")
            return

        self.tasks.append(task_name)
        print(f"Added task: {task_name}")
        self.save_tasks()

    def save_tasks(self):
        """Saves the updated tasks list to the JSON file."""
        try:
            with open(self.tasks_file, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except Exception as e:
            print(f"Error saving tasks: {e}")

def main():
    """
    Main function to interact with the maintenance scheduler.
    """
    scheduler = MaintenanceScheduler()

    print("Welcome to the Outdoor Environment Maintenance Scheduler!")
    print("Philosophy: Nurture thriving environments with expertise and dedication.\n")

    while True:
        print("Options:")
        print("  1. Display current schedule")
        print("  2. Schedule a task")
        print("  3. Add a new task")
        print("  4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            scheduler.display_schedule()
        elif choice == '2':
            task_name = input("Enter the task name: ")
            frequency = input("Enter the frequency (daily, weekly, monthly): ")
            scheduler.schedule_task(task_name, frequency)
        elif choice == '3':
            task_name = input("Enter the new task name: ")
            scheduler.add_task(task_name)
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```
