"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script to manage construction projects for a company like Peace City Contracting LLC, including tasks for building construction, renovation, and MEP works.
Generated: DETERMINISTIC_72750bda4a16efd5
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_manager.py

class ConstructionProject:
    """Represents a construction project with tasks for building construction, renovation, and MEP works."""

    def __init__(self, project_name, project_manager):
        """
        Initializes a ConstructionProject instance.

        Args:
            project_name (str): The name of the construction project.
            project_manager (str): The name of the project manager.
        """
        self.project_name = project_name
        self.project_manager = project_manager
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the construction project.

        Args:
            task (Task): The task to add to the project.
        """
        self.tasks.append(task)

    def view_tasks(self):
        """Displays all tasks in the construction project."""
        for task in self.tasks:
            print(task)


class Task:
    """Represents a task in a construction project."""

    def __init__(self, task_name, task_type, status="Not Started"):
        """
        Initializes a Task instance.

        Args:
            task_name (str): The name of the task.
            task_type (str): The type of task (building construction, renovation, MEP works).
            status (str, optional): The status of the task. Defaults to "Not Started".
        """
        self.task_name = task_name
        self.task_type = task_type
        self.status = status

    def __str__(self):
        return f"Task: {self.task_name} ({self.task_type}) - Status: {self.status}"

    def update_status(self, status):
        """Updates the status of the task.

        Args:
            status (str): The new status of the task.
        """
        self.status = status


class MEPWork(Task):
    """Represents an MEP work task in a construction project."""

    def __init__(self, task_name, status="Not Started", electrical=None, plumbing=None, hvac=None):
        """
        Initializes an MEPWork instance.

        Args:
            task_name (str): The name of the MEP work task.
            status (str, optional): The status of the task. Defaults to "Not Started".
            electrical (str, optional): The electrical work details. Defaults to None.
            plumbing (str, optional): The plumbing work details. Defaults to None.
            hvac (str, optional): The HVAC work details. Defaults to None.
        """
        super().__init__(task_name, "MEP Works", status)
        self.electrical = electrical
        self.plumbing = plumbing
        self.hvac = hvac

    def __str__(self):
        return super().__str__() + f"\nElectrical: {self.electrical}\nPlumbing: {self.plumbing}\nHVAC: {self.hvac}"


class RenovationTask(Task):
    """Represents a renovation task in a construction project."""

    def __init__(self, task_name, status="Not Started", areas=None):
        """
        Initializes a RenovationTask instance.

        Args:
            task_name (str): The name of the renovation task.
            status (str, optional): The status of the task. Defaults to "Not Started".
            areas (list, optional): The areas to be renovated. Defaults to None.
        """
        super().__init__(task_name, "Renovation", status)
        self.areas = areas

    def __str__(self):
        return super().__str__() + f"\nAreas: {', '.join(self.areas)}"


class BuildingConstructionTask(Task):
    """Represents a building construction task in a construction project."""

    def __init__(self, task_name, status="Not Started", phases=None):
        """
        Initializes a BuildingConstructionTask instance.

        Args:
            task_name (str): The name of the building construction task.
            status (str, optional): The status of the task. Defaults to "Not Started".
            phases (list, optional): The construction phases. Defaults to None.
        """
        super().__init__(task_name, "Building Construction", status)
        self.phases = phases

    def __str__(self):
        return super().__str__() + f"\nPhases: {', '.join(self.phases)}"


def main():
    try:
        project = ConstructionProject("Peace City Contracting LLC Project", "John Doe")

        # Create tasks
        task1 = BuildingConstructionTask("Site Preparation", phases=["Phase 1", "Phase 2"])
        task2 = RenovationTask("Interior Renovation", areas=["Kitchen", "Bathroom"])
        task3 = MEPWork("Electrical and Plumbing", electrical="Install electrical outlets", plumbing="Install new pipes")

        # Add tasks to project
        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)

        # View tasks
        print("Construction Project Tasks:")
        project.view_tasks()

        # Update task status
        task1.update_status("In Progress")
        print("\nUpdated Task Status:")
        print(task1)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
