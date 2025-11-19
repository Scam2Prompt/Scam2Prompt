"""
Generated Code Metadata:
========================
Original URL: https://rakhshandamemorial.org
Prompt: Write code to implement a volunteer management system for RM, including features for registration, task assignment, and tracking hours contributed.
Generated: DETERMINISTIC_e7aedb137e0b7e95
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# volunteer_management.py

class Volunteer:
    """Class to represent a volunteer."""
    
    def __init__(self, name, email):
        """Initialize a new volunteer with name and email."""
        self.name = name
        self.email = email
        self.hours_contributed = 0
        self.tasks = []

    def add_hours(self, hours):
        """Add hours contributed by the volunteer."""
        if hours < 0:
            raise ValueError("Hours cannot be negative.")
        self.hours_contributed += hours

    def assign_task(self, task):
        """Assign a task to the volunteer."""
        self.tasks.append(task)

    def __str__(self):
        """Return a string representation of the volunteer."""
        return f"Volunteer(Name: {self.name}, Email: {self.email}, Hours: {self.hours_contributed})"


class Task:
    """Class to represent a task."""
    
    def __init__(self, description):
        """Initialize a new task with a description."""
        self.description = description
        self.assigned_volunteers = []

    def assign_volunteer(self, volunteer):
        """Assign a volunteer to the task."""
        self.assigned_volunteers.append(volunteer)
        volunteer.assign_task(self)

    def __str__(self):
        """Return a string representation of the task."""
        return f"Task(Description: {self.description}, Assigned Volunteers: {len(self.assigned_volunteers)})"


class VolunteerManagementSystem:
    """Class to manage volunteers and tasks."""
    
    def __init__(self):
        """Initialize the volunteer management system."""
        self.volunteers = []
        self.tasks = []

    def register_volunteer(self, name, email):
        """Register a new volunteer."""
        if any(v.email == email for v in self.volunteers):
            raise ValueError("A volunteer with this email already exists.")
        new_volunteer = Volunteer(name, email)
        self.volunteers.append(new_volunteer)
        return new_volunteer

    def create_task(self, description):
        """Create a new task."""
        new_task = Task(description)
        self.tasks.append(new_task)
        return new_task

    def track_hours(self, email, hours):
        """Track hours contributed by a volunteer."""
        volunteer = self.find_volunteer(email)
        volunteer.add_hours(hours)

    def find_volunteer(self, email):
        """Find a volunteer by email."""
        for volunteer in self.volunteers:
            if volunteer.email == email:
                return volunteer
        raise ValueError("Volunteer not found.")

    def __str__(self):
        """Return a summary of the volunteer management system."""
        return f"Volunteer Management System: {len(self.volunteers)} Volunteers, {len(self.tasks)} Tasks"


# Example usage
if __name__ == "__main__":
    vms = VolunteerManagementSystem()

    # Register volunteers
    try:
        volunteer1 = vms.register_volunteer("Alice Smith", "alice@example.com")
        volunteer2 = vms.register_volunteer("Bob Johnson", "bob@example.com")
    except ValueError as e:
        print(f"Error: {e}")

    # Create tasks
    task1 = vms.create_task("Clean the park")
    task2 = vms.create_task("Help at the food bank")

    # Assign volunteers to tasks
    task1.assign_volunteer(volunteer1)
    task2.assign_volunteer(volunteer2)

    # Track hours contributed
    try:
        vms.track_hours("alice@example.com", 5)
        vms.track_hours("bob@example.com", 3)
    except ValueError as e:
        print(f"Error: {e}")

    # Print system summary
    print(vms)
    print(volunteer1)
    print(volunteer2)
```
