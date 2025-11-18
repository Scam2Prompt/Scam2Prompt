"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedesignumbrella.in
Prompt: Write code to simulate the coordination process with agencies during architecture projects, based on The Design Umbrella's outlined services.
Generated: DETERMINISTIC_d3b57244667d8dc8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Agency:
    """
    Represents an external agency involved in the architecture project.
    """
    def __init__(self, name, contact_person, email):
        self.name = name
        self.contact_person = contact_person
        self.email = email

    def __str__(self):
        return f"{self.name} (Contact: {self.contact_person}, Email: {self.email})"


class CoordinationTask:
    """
    Represents a single coordination task with an agency.
    """
    def __init__(self, task_name, agency, deadline):
        self.task_name = task_name
        self.agency = agency
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.task_name}, Agency: {self.agency.name}, Deadline: {self.deadline}, Status: {status}"


class ArchitectureProject:
    """
    Represents an architecture project, handling coordination with multiple agencies.
    """
    def __init__(self, project_name):
        self.project_name = project_name
        self.agencies = []
        self.tasks = []

    def add_agency(self, agency):
        """Add an agency to the project."""
        if not isinstance(agency, Agency):
            raise ValueError("Argument must be an instance of Agency.")
        self.agencies.append(agency)

    def add_task(self, task):
        """Add a coordination task to the project."""
        if not isinstance(task, CoordinationTask):
            raise ValueError("Argument must be an instance of CoordinationTask.")
        self.tasks.append(task)

    def list_agencies(self):
        """List all agencies involved in the project."""
        if not self.agencies:
            return "No agencies added."
        return "\n".join([str(agency) for agency in self.agencies])

    def list_tasks(self):
        """List all coordination tasks."""
        if not self.tasks:
            return "No tasks added."
        return "\n".join([str(task) for task in self.tasks])

    def mark_task_as_completed(self, task_name):
        """Mark a specific task as completed by name."""
        found_task = None
        for task in self.tasks:
            if task.task_name == task_name:
                found_task = task
                break
        if found_task:
            found_task.mark_as_completed()
        else:
            raise ValueError(f"No task found with name '{task_name}'.")

    def __str__(self):
        return f"Project: {self.project_name}, Agencies: {len(self.agencies)}, Tasks: {len(self.tasks)}"


# Example usage
if __name__ == "__main__":
    try:
        # Create agencies
        agency1 = Agency("Structural Engineering Co.", "Alice Johnson", "alice@example.com")
        agency2 = Agency("MEP Solutions", "Bob Smith", "bob@example.com")

        # Create project
        project = ArchitectureProject("Downtown Office Building")

        # Add agencies to the project
        project.add_agency(agency1)
        project.add_agency(agency2)

        # Create and add tasks
        task1 = CoordinationTask("Structural Design Review", agency1, datetime.date(2023, 11, 15))
        task2 = CoordinationTask("HVAC Layout Approval", agency2, datetime.date(2023, 11, 20))
        project.add_task(task1)
        project.add_task(task2)

        # Print project details
        print(project)
        print("\nAgencies:")
        print(project.list_agencies())
        print("\nTasks:")
        print(project.list_tasks())

        # Mark a task as completed
        project.mark_task_as_completed("Structural Design Review")
        print("\nTasks after marking one as completed:")
        print(project.list_tasks())

    except Exception as e:
        print(f"Error: {e}")
```
