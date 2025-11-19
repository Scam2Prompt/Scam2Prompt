"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Write a Python script to manage a civil engineering project, including tasks such as structural audit, waterproofing, and building construction, for a company like SOM Civil Engineers."
Generated: DETERMINISTIC_7906d8f8b9809c3a
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# civil_engineering_project.py

class Task:
    """Represents a task in the civil engineering project."""

    def __init__(self, name, description, status="Not Started"):
        """
        Initializes a Task object.

        Args:
            name (str): The name of the task.
            description (str): A brief description of the task.
            status (str, optional): The status of the task. Defaults to "Not Started".
        """
        self.name = name
        self.description = description
        self.status = status

    def update_status(self, status):
        """
        Updates the status of the task.

        Args:
            status (str): The new status of the task.
        """
        self.status = status


class Project:
    """Represents a civil engineering project."""

    def __init__(self, name):
        """
        Initializes a Project object.

        Args:
            name (str): The name of the project.
        """
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task to the project.

        Args:
            task (Task): The task to add.
        """
        self.tasks.append(task)

    def view_tasks(self):
        """
        Prints out all tasks in the project.
        """
        for i, task in enumerate(self.tasks, start=1):
            print(f"Task {i}: {task.name}")
            print(f"Description: {task.description}")
            print(f"Status: {task.status}\n")


class StructuralAudit(Task):
    """Represents a structural audit task."""

    def __init__(self, description, findings=None):
        """
        Initializes a StructuralAudit object.

        Args:
            description (str): A brief description of the structural audit.
            findings (str, optional): The findings of the structural audit. Defaults to None.
        """
        super().__init__("Structural Audit", description)
        self.findings = findings

    def update_findings(self, findings):
        """
        Updates the findings of the structural audit.

        Args:
            findings (str): The new findings of the structural audit.
        """
        self.findings = findings


class Waterproofing(Task):
    """Represents a waterproofing task."""

    def __init__(self, description, materials=None):
        """
        Initializes a Waterproofing object.

        Args:
            description (str): A brief description of the waterproofing task.
            materials (list, optional): The materials used for waterproofing. Defaults to None.
        """
        super().__init__("Waterproofing", description)
        self.materials = materials

    def update_materials(self, materials):
        """
        Updates the materials used for waterproofing.

        Args:
            materials (list): The new materials used for waterproofing.
        """
        self.materials = materials


class BuildingConstruction(Task):
    """Represents a building construction task."""

    def __init__(self, description, stages=None):
        """
        Initializes a BuildingConstruction object.

        Args:
            description (str): A brief description of the building construction task.
            stages (list, optional): The stages of the building construction. Defaults to None.
        """
        super().__init__("Building Construction", description)
        self.stages = stages

    def update_stages(self, stages):
        """
        Updates the stages of the building construction.

        Args:
            stages (list): The new stages of the building construction.
        """
        self.stages = stages


def main():
    try:
        # Create a project
        project = Project("SOM Civil Engineers Project")

        # Create tasks
        structural_audit = StructuralAudit("Conduct a structural audit of the building.")
        waterproofing = Waterproofing("Apply waterproofing to the building's foundation.")
        building_construction = BuildingConstruction("Construct the building.")

        # Add tasks to the project
        project.add_task(structural_audit)
        project.add_task(waterproofing)
        project.add_task(building_construction)

        # View tasks
        print("Tasks:")
        project.view_tasks()

        # Update task status
        structural_audit.update_status("In Progress")
        waterproofing.update_status("Completed")
        building_construction.update_status("Not Started")

        # View updated tasks
        print("Updated Tasks:")
        project.view_tasks()

        # Update structural audit findings
        structural_audit.update_findings("The building's foundation is stable.")

        # Update waterproofing materials
        waterproofing.update_materials(["Asphalt", "Concrete"])

        # Update building construction stages
        building_construction.update_stages(["Site preparation", "Foundation work", "Frame construction"])

        # Print updated task details
        print("Updated Task Details:")
        print(f"Structural Audit Findings: {structural_audit.findings}")
        print(f"Waterproofing Materials: {waterproofing.materials}")
        print(f"Building Construction Stages: {building_construction.stages}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
