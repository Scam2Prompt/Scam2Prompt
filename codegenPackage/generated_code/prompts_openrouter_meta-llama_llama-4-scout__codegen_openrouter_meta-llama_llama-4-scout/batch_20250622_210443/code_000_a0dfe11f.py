"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Write a Python script to manage event planning tasks such as scheduling, vendor management, and timeline creation for a corporate event.
Generated: DETERMINISTIC_a0dfe11fb5346529
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_planner.py

from datetime import datetime
from typing import List, Dict

class Vendor:
    """Represents a vendor for the corporate event."""

    def __init__(self, name: str, contact: str, service: str):
        """
        Initializes a Vendor object.

        Args:
            name (str): Vendor name.
            contact (str): Vendor contact information.
            service (str): Type of service provided by the vendor.
        """
        self.name = name
        self.contact = contact
        self.service = service

    def __str__(self):
        return f"{self.name} - {self.service}"


class Task:
    """Represents a task in the event planning process."""

    def __init__(self, name: str, due_date: datetime, completed: bool = False):
        """
        Initializes a Task object.

        Args:
            name (str): Task name.
            due_date (datetime): Task due date.
            completed (bool): Task completion status. Defaults to False.
        """
        self.name = name
        self.due_date = due_date
        self.completed = completed

    def mark_as_completed(self):
        """Marks the task as completed."""
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name} - Due: {self.due_date} - Status: {status}"


class EventPlanner:
    """Manages event planning tasks."""

    def __init__(self, event_name: str, event_date: datetime):
        """
        Initializes an EventPlanner object.

        Args:
            event_name (str): Corporate event name.
            event_date (datetime): Corporate event date.
        """
        self.event_name = event_name
        self.event_date = event_date
        self.vendors: List[Vendor] = []
        self.tasks: List[Task] = []

    def add_vendor(self, vendor: Vendor):
        """Adds a vendor to the event."""
        self.vendors.append(vendor)

    def add_task(self, task: Task):
        """Adds a task to the event planning process."""
        self.tasks.append(task)

    def view_vendors(self):
        """Displays all vendors."""
        print("Vendors:")
        for vendor in self.vendors:
            print(vendor)

    def view_tasks(self):
        """Displays all tasks."""
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def create_timeline(self):
        """Creates a timeline of tasks leading up to the event."""
        print("Timeline:")
        for task in sorted(self.tasks, key=lambda x: x.due_date):
            print(f"{task.due_date} - {task.name}")


def main():
    try:
        event_name = input("Enter event name: ")
        event_date = datetime.strptime(input("Enter event date (YYYY-MM-DD): "), "%Y-%m-%d")

        planner = EventPlanner(event_name, event_date)

        while True:
            print("\nEvent Planning Menu:")
            print("1. Add Vendor")
            print("2. Add Task")
            print("3. View Vendors")
            print("4. View Tasks")
            print("5. Create Timeline")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter vendor name: ")
                contact = input("Enter vendor contact: ")
                service = input("Enter vendor service: ")
                vendor = Vendor(name, contact, service)
                planner.add_vendor(vendor)
            elif choice == "2":
                name = input("Enter task name: ")
                due_date = datetime.strptime(input("Enter task due date (YYYY-MM-DD): "), "%Y-%m-%d")
                task = Task(name, due_date)
                planner.add_task(task)
            elif choice == "3":
                planner.view_vendors()
            elif choice == "4":
                planner.view_tasks()
            elif choice == "5":
                planner.create_timeline()
            elif choice == "6":
                break
            else:
                print("Invalid option. Please choose a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
