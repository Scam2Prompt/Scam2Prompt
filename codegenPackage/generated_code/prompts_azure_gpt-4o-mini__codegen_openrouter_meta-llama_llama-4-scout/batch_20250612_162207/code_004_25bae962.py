"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Generate a code example that simulates a disaster response system for a local volunteer group, inspired by the operations of the Protezione Civile di Torre d'Isola.
Generated: DETERMINISTIC_25bae9628f8f1514
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# disaster_response_system.py

import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Volunteer:
    """Represents a volunteer in the disaster response system."""

    def __init__(self, name, contact_info):
        """
        Initializes a Volunteer object.

        Args:
            name (str): The volunteer's name.
            contact_info (str): The volunteer's contact information.
        """
        self.name = name
        self.contact_info = contact_info
        self.assigned_tasks = []

    def assign_task(self, task):
        """
        Assigns a task to the volunteer.

        Args:
            task (str): The task to be assigned.
        """
        self.assigned_tasks.append(task)

    def __str__(self):
        return f"{self.name} - {self.contact_info}"


class Task:
    """Represents a task in the disaster response system."""

    def __init__(self, description, location):
        """
        Initializes a Task object.

        Args:
            description (str): The task's description.
            location (str): The task's location.
        """
        self.description = description
        self.location = location
        self.assigned_volunteer = None

    def assign_volunteer(self, volunteer):
        """
        Assigns a volunteer to the task.

        Args:
            volunteer (Volunteer): The volunteer to be assigned.
        """
        self.assigned_volunteer = volunteer
        volunteer.assign_task(self.description)

    def __str__(self):
        return f"{self.description} at {self.location}"


class DisasterResponseSystem:
    """Simulates a disaster response system for a local volunteer group."""

    def __init__(self):
        self.volunteers = []
        self.tasks = []

    def add_volunteer(self, volunteer):
        """
        Adds a volunteer to the system.

        Args:
            volunteer (Volunteer): The volunteer to be added.
        """
        self.volunteers.append(volunteer)

    def add_task(self, task):
        """
        Adds a task to the system.

        Args:
            task (Task): The task to be added.
        """
        self.tasks.append(task)

    def assign_volunteer_to_task(self, volunteer_name, task_description):
        """
        Assigns a volunteer to a task.

        Args:
            volunteer_name (str): The name of the volunteer.
            task_description (str): The description of the task.

        Returns:
            bool: True if the assignment was successful, False otherwise.
        """
        volunteer = next((v for v in self.volunteers if v.name == volunteer_name), None)
        task = next((t for t in self.tasks if t.description == task_description), None)

        if volunteer and task:
            task.assign_volunteer(volunteer)
            return True
        else:
            logging.error("Volunteer or task not found.")
            return False

    def print_status(self):
        """Prints the current status of the system."""
        logging.info("Volunteers:")
        for volunteer in self.volunteers:
            logging.info(f"  {volunteer} - Assigned tasks: {volunteer.assigned_tasks}")

        logging.info("\nTasks:")
        for task in self.tasks:
            if task.assigned_volunteer:
                logging.info(f"  {task} - Assigned to: {task.assigned_volunteer.name}")
            else:
                logging.info(f"  {task} - Not assigned")


def main():
    # Create a disaster response system
    drs = DisasterResponseSystem()

    # Create volunteers
    volunteer1 = Volunteer("John Doe", "john.doe@example.com")
    volunteer2 = Volunteer("Jane Smith", "jane.smith@example.com")

    # Add volunteers to the system
    drs.add_volunteer(volunteer1)
    drs.add_volunteer(volunteer2)

    # Create tasks
    task1 = Task("Search and rescue", "Torre d'Isola")
    task2 = Task("Provide medical aid", "Torre d'Isola")

    # Add tasks to the system
    drs.add_task(task1)
    drs.add_task(task2)

    # Assign volunteers to tasks
    drs.assign_volunteer_to_task("John Doe", "Search and rescue")
    drs.assign_volunteer_to_task("Jane Smith", "Provide medical aid")

    # Print the current status of the system
    drs.print_status()


if __name__ == "__main__":
    main()
```
