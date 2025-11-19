"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Write a Python script that automates the scheduling of tasks related to the installation of ball protection nets and fences in construction sites.
Generated: DETERMINISTIC_4e4772e18e557169
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os


class TaskScheduler:
    """
    A class to manage and automate task scheduling for the installation of ball protection nets and fences 
    at construction sites.
    """

    def __init__(self, schedule_file="schedule.json"):
        """
        Initialize the TaskScheduler object.
        
        Args:
            schedule_file (str): Path to the schedule file. Defaults to 'schedule.json'.
        """
        self.schedule_file = schedule_file
        self.tasks = self.load_schedule()

    def load_schedule(self):
        """
        Loads the existing schedule from the JSON file.
        
        Returns:
            dict: Loaded task schedule dictionary.
        """
        if os.path.exists(self.schedule_file):
            try:
                with open(self.schedule_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error: Failed to load schedule file. Creating a new schedule.")
        return {}

    def save_schedule(self):
        """
        Saves the current schedule to the JSON file.
        """
        try:
            with open(self.schedule_file, "w") as file:
                json.dump(self.tasks, file, indent=4)
        except IOError:
            print("Error: Failed to save schedule file.")

    def add_task(self, site_name, task_type, start_date, end_date):
        """
        Adds a task to the schedule.
        
        Args:
            site_name (str): Name of the construction site.
            task_type (str): Type of task (e.g., 'Install Nets', 'Install Fences').
            start_date (str): Start date in the format 'YYYY-MM-DD'.
            end_date (str): End date in the format 'YYYY-MM-DD'.
            
        Returns:
            bool: True if the task was successfully added, False otherwise.
        """
        try:
            # Validate date formats
            start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")

            if end_date_obj < start_date_obj:
                print("Error: End date must be after start date.")
                return False

            # Create a new task entry
            task_id = len(self.tasks) + 1
            self.tasks[task_id] = {
                "site_name": site_name,
                "task_type": task_type,
                "start_date": start_date,
                "end_date": end_date,
            }

            self.save_schedule()
            print(f"Task added successfully. Task ID: {task_id}")
            return True
        except ValueError:
            print("Error: Invalid date format. Please use 'YYYY-MM-DD'.")
            return False

    def view_schedule(self):
        """
        Displays the current schedule in a readable format.
        """
        if not self.tasks:
            print("No tasks scheduled.")
            return

        print("Scheduled Tasks:")
        for task_id, task_info in self.tasks.items():
            print(f"Task ID: {task_id}")
            print(f"  Site Name: {task_info['site_name']}")
            print(f"  Task Type: {task_info['task_type']}")
            print(f"  Start Date: {task_info['start_date']}")
            print(f"  End Date: {task_info['end_date']}")
            print("-" * 40)

    def delete_task(self, task_id):
        """
        Deletes a task from the schedule.
        
        Args:
            task_id (int): ID of the task to be deleted.
            
        Returns:
            bool: True if the task was successfully deleted, False otherwise.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_schedule()
            print(f"Task ID {task_id} deleted successfully.")
            return True
        else:
            print(f"Error: Task ID {task_id} not found.")
            return False


def main():
    """
    Main function to interact with the TaskScheduler.
    """
    scheduler = TaskScheduler()

    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. View Schedule")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            site_name = input("Enter construction site name: ")
            task_type = input("Enter task type (e.g., Install Nets, Install Fences): ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            scheduler.add_task(site_name, task_type, start_date, end_date)
        elif choice == "2":
            scheduler.view_schedule()
        elif choice == "3":
            try:
                task_id = int(input("Enter Task ID to delete: "))
                scheduler.delete_task(task_id)
            except ValueError:
                print("Error: Invalid Task ID.")
        elif choice == "4":
            print("Exiting Task Scheduler...")
            break
        else:
            print("Error: Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
