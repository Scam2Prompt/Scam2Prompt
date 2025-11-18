"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Write code to implement a volunteer management system for RM, including features for registration, task assignment, and tracking hours contributed.
Generated: DETERMINISTIC_e7aedb137e0b7e95
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Volunteer:
    """Class representing a volunteer with their details and hours contributed."""
    
    def __init__(self, name, email):
        """Initialize a new volunteer with name and email."""
        self.name = name
        self.email = email
        self.hours_contributed = 0

    def add_hours(self, hours):
        """Add hours contributed by the volunteer."""
        if hours < 0:
            raise ValueError("Hours cannot be negative.")
        self.hours_contributed += hours


class Task:
    """Class representing a task that can be assigned to volunteers."""
    
    def __init__(self, title, description):
        """Initialize a new task with title and description."""
        self.title = title
        self.description = description
        self.assigned_volunteers = []

    def assign_volunteer(self, volunteer):
        """Assign a volunteer to the task."""
        if volunteer in self.assigned_volunteers:
            raise ValueError(f"{volunteer.name} is already assigned to this task.")
        self.assigned_volunteers.append(volunteer)

    def complete_task(self):
        """Mark the task as complete, notifying volunteers."""
        for volunteer in self.assigned_volunteers:
            try:
                volunteer.add_hours(1)  # Assume each task contributes 1 hour
            except ValueError as e:
                print(f"Error adding hours for {volunteer.name}: {e}")
        self.assigned_volunteers.clear()  # Clear the assigned volunteers after completion


class VolunteerManagementSystem:
    """Class representing the volunteer management system."""
    
    def __init__(self):
        """Initialize the volunteer management system with empty lists."""
        self.volunteers = []
        self.tasks = []

    def register_volunteer(self, name, email):
        """Register a new volunteer and add them to the system."""
        if any(v.email == email for v in self.volunteers):
            raise ValueError("A volunteer with this email is already registered.")
        new_volunteer = Volunteer(name, email)
        self.volunteers.append(new_volunteer)

    def create_task(self, title, description):
        """Create a new task and add it to the system."""
        new_task = Task(title, description)
        self.tasks.append(new_task)
        return new_task

    def get_volunteer_hours(self, email):
        """Get total hours contributed by a volunteer identified by email."""
        for volunteer in self.volunteers:
            if volunteer.email == email:
                return volunteer.hours_contributed
        raise ValueError("Volunteer not found.")


# Example usage of the Volunteer Management System
if __name__ == "__main__":
    vms = VolunteerManagementSystem()

    # Register volunteers
    try:
        vms.register_volunteer("Alice Johnson", "alice@example.com")
        vms.register_volunteer("Bob Smith", "bob@example.com")
    except ValueError as e:
        print(e)

    # Create a task
    task1 = vms.create_task("Park Cleanup", "Clean up the local park area.")

    # Assign volunteers to the task
    try:
        task1.assign_volunteer(vms.volunteers[0])  # Assign Alice
        task1.assign_volunteer(vms.volunteers[1])  # Assign Bob
    except ValueError as e:
        print(e)

    # Complete the task
    task1.complete_task()

    # Check hours contributed
    try:
        print(f"Alice's hours: {vms.get_volunteer_hours('alice@example.com')}")
        print(f"Bob's hours: {vms.get_volunteer_hours('bob@example.com')}")
    except ValueError as e:
        print(e)
```
