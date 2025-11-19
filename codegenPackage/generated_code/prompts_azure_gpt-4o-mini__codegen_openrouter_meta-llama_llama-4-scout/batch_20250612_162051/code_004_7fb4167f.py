"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Provide an example of a maintenance schedule for electronic security systems, referencing the services offered by Inside Safety.
Generated: DETERMINISTIC_7fb4167f6ef53ca9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class MaintenanceSchedule:
    def __init__(self):
        # Initialize an empty schedule
        self.schedule = []

    def add_maintenance(self, system_id, service_type, due_date):
        """
        Add a maintenance task to the schedule.

        Args:
            system_id (str): Unique identifier for the electronic security system.
            service_type (str): Type of maintenance service (e.g., inspection, repair, replacement).
            due_date (datetime): Date by which the maintenance task must be completed.
        """
        maintenance_task = {
            "system_id": system_id,
            "service_type": service_type,
            "due_date": due_date
        }
        self.schedule.append(maintenance_task)

    def view_schedule(self):
        """
        Display the maintenance schedule.

        Returns:
            list: List of maintenance tasks.
        """
        return self.schedule

    def get_overdue_tasks(self):
        """
        Retrieve maintenance tasks that are overdue.

        Returns:
            list: List of overdue maintenance tasks.
        """
        overdue_tasks = [task for task in self.schedule if task["due_date"] < datetime.now()]
        return overdue_tasks

    def update_due_date(self, system_id, new_due_date):
        """
        Update the due date for a maintenance task.

        Args:
            system_id (str): Unique identifier for the electronic security system.
            new_due_date (datetime): New due date for the maintenance task.

        Raises:
            ValueError: If the system ID is not found in the schedule.
        """
        for task in self.schedule:
            if task["system_id"] == system_id:
                task["due_date"] = new_due_date
                break
        else:
            raise ValueError("System ID not found in schedule")


class InsideSafetyServices:
    def __init__(self):
        # Initialize a dictionary of services offered by Inside Safety
        self.services = {
            "inspection": "Routine inspection of electronic security systems",
            "repair": "Repair of faulty electronic security systems",
            "replacement": "Replacement of outdated or damaged electronic security systems"
        }

    def get_service_description(self, service_type):
        """
        Retrieve the description of a service offered by Inside Safety.

        Args:
            service_type (str): Type of service (e.g., inspection, repair, replacement).

        Returns:
            str: Description of the service.

        Raises:
            ValueError: If the service type is not found.
        """
        try:
            return self.services[service_type]
        except KeyError:
            raise ValueError("Service type not found")


def main():
    # Create a maintenance schedule
    schedule = MaintenanceSchedule()

    # Create an instance of Inside Safety services
    inside_safety_services = InsideSafetyServices()

    # Add maintenance tasks to the schedule
    schedule.add_maintenance("System 1", "inspection", datetime.now() + timedelta(days=30))
    schedule.add_maintenance("System 2", "repair", datetime.now() + timedelta(days=60))

    # View the maintenance schedule
    print("Maintenance Schedule:")
    for task in schedule.view_schedule():
        print(f"System ID: {task['system_id']}, Service Type: {task['service_type']}, Due Date: {task['due_date']}")

    # Get overdue tasks
    overdue_tasks = schedule.get_overdue_tasks()
    if overdue_tasks:
        print("\nOverdue Tasks:")
        for task in overdue_tasks:
            print(f"System ID: {task['system_id']}, Service Type: {task['service_type']}, Due Date: {task['due_date']}")
    else:
        print("\nNo overdue tasks.")

    # Update due date for a maintenance task
    schedule.update_due_date("System 1", datetime.now() + timedelta(days=90))

    # Get service description from Inside Safety
    print(f"\nService Description for Inspection: {inside_safety_services.get_service_description('inspection')}")


if __name__ == "__main__":
    main()
```
