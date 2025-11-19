"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write a Python script that automates the scheduling of tasks related to the installation of ball protection nets and fences in construction sites.
Generated: DETERMINISTIC_4e4772e18e557169
Batch ID: 20250612_135230
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


class TaskScheduler:
    """
    A class to automate the scheduling of tasks related to the installation of ball protection nets
    and fences in construction sites.
    """

    def __init__(self, schedule_file="schedule.json"):
        """
        Initializes the TaskScheduler with a schedule file.

        :param schedule_file: Path to the JSON file where the schedule will be stored.
        """
        self.schedule_file = schedule_file
        self.tasks = self.load_schedule()

    def load_schedule(self):
        """
        Loads the schedule from the JSON file. If the file does not exist, initializes an empty schedule.

        :return: A dictionary containing the tasks.
        """
        if os.path.exists(self.schedule_file):
            try:
                with open(self.schedule_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Schedule file is corrupted. Initializing an empty schedule.")
                return {}
        return {}

    def save_schedule(self):
        """
        Saves the current schedule to the JSON file.
        """
        try:
            with open(self.schedule_file, "w") as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save schedule. {e}")

    def add_task(self, task_name, site_location, start_date, end_date):
        """
        Adds a new task to the schedule.

        :param task_name: Name of the task.
        :param site_location: Location of the construction site.
        :param start_date: Start date of the task (YYYY-MM-DD).
        :param end_date: End date of the task (YYYY-MM-DD).
        """
        try:
            # Validate date format
            start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")

            if end_date_obj < start_date_obj:
                print("Error: End date cannot be earlier than start date.")
                return

            task_id = len(self.tasks) + 1
            self.tasks[task_id] = {
                "task_name": task_name,
                "site_location": site_location,
                "start_date": start_date,
                "end_date": end_date,
            }
            self.save_schedule()
            print(f"Task '{task_name}' added successfully.")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")

    def view_tasks(self):
        """
        Displays all scheduled tasks.
        """
        if not self.tasks:
            print("No tasks scheduled.")
            return

        print("Scheduled Tasks:")
        for task_id, task_details in self.tasks.items():
            print(f"Task ID: {task_id}")
            print(f"  Name: {task_details['task_name']}")
            print(f"  Location: {task_details['site_location']}")
            print(f"  Start Date: {task_details['start_date']}")
            print(f"  End Date: {task_details['end_date']}")
            print("-" * 40)

    def delete_task(self, task_id):
        """
        Deletes a task from the schedule.

        :param task_id: ID of the task to delete.
        """
        if task_id in self.tasks:
            deleted_task = self.tasks.pop(task_id)
            self.save_schedule()
            print(f"Task '{deleted_task['task_name']}' deleted successfully.")
        else:
            print(f"Error: Task ID {task_id} not found.")

    def update_task(self, task_id, task_name=None, site_location=None, start_date=None, end_date=None):
        """
        Updates an existing task in the schedule.

        :param task_id: ID of the task to update.
        :param task_name: New name of the task (optional).
        :param site_location: New location of the construction site (optional).
        :param start_date: New start date of the task (optional, format: YYYY-MM-DD).
        :param end_date: New end date of the task (optional, format: YYYY-MM-DD).
        """
        if task_id not in self.tasks:
            print(f"Error: Task ID {task_id} not found.")
            return

        try:
            if start_date:
                datetime.datetime.strptime(start_date, "%Y-%m-%d")
            if end_date:
                datetime.datetime.strptime(end_date, "%Y-%m-%d")

            task = self.tasks[task_id]
            if task_name:
                task["task_name"] = task_name
            if site_location:
                task["site_location"] = site_location
            if start_date:
                task["start_date"] = start_date
            if end_date:
                task["end_date"] = end_date

            self.save_schedule()
            print(f"Task ID {task_id} updated successfully.")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")


# Main script
if __name__ == "__main__":
    scheduler = TaskScheduler()

    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            site_location = input("Enter site location: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            scheduler.add_task(task_name, site_location, start_date, end_date)
        elif choice == "2":
            scheduler.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            task_name = input("Enter new task name (leave blank to keep current): ")
            site_location = input("Enter new site location (leave blank to keep current): ")
            start_date = input("Enter new start date (YYYY-MM-DD, leave blank to keep current): ")
            end_date = input("Enter new end date (YYYY-MM-DD, leave blank to keep current): ")
            scheduler.update_task(task_id, task_name, site_location, start_date, end_date)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            scheduler.delete_task(task_id)
        elif choice == "5":
            print("Exiting Task Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
