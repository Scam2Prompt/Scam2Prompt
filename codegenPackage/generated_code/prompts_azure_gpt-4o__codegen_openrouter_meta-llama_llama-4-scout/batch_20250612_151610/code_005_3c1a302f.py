"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: Provide a Python example for managing project logistics and procurement in industrial engineering, inspired by Puma Ipce's technical-administrative support services.
Generated: DETERMINISTIC_3c1a302f7d5e600e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_logistics.py

class Project:
    def __init__(self, project_id, name, description):
        """
        Initialize a Project object.

        Args:
            project_id (int): Unique project identifier.
            name (str): Project name.
            description (str): Project description.
        """
        self.project_id = project_id
        self.name = name
        self.description = description
        self.tasks = []
        self.materials = []
        self.suppliers = []

    def add_task(self, task):
        """
        Add a task to the project.

        Args:
            task (Task): Task object to add.
        """
        self.tasks.append(task)

    def add_material(self, material):
        """
        Add a material to the project.

        Args:
            material (Material): Material object to add.
        """
        self.materials.append(material)

    def add_supplier(self, supplier):
        """
        Add a supplier to the project.

        Args:
            supplier (Supplier): Supplier object to add.
        """
        self.suppliers.append(supplier)


class Task:
    def __init__(self, task_id, name, description, status="Not Started"):
        """
        Initialize a Task object.

        Args:
            task_id (int): Unique task identifier.
            name (str): Task name.
            description (str): Task description.
            status (str, optional): Task status. Defaults to "Not Started".
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.status = status

    def update_status(self, status):
        """
        Update the task status.

        Args:
            status (str): New task status.
        """
        self.status = status


class Material:
    def __init__(self, material_id, name, quantity, unit_price):
        """
        Initialize a Material object.

        Args:
            material_id (int): Unique material identifier.
            name (str): Material name.
            quantity (int): Material quantity.
            unit_price (float): Material unit price.
        """
        self.material_id = material_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def calculate_total_cost(self):
        """
        Calculate the total cost of the material.

        Returns:
            float: Total cost.
        """
        return self.quantity * self.unit_price


class Supplier:
    def __init__(self, supplier_id, name, contact_info):
        """
        Initialize a Supplier object.

        Args:
            supplier_id (int): Unique supplier identifier.
            name (str): Supplier name.
            contact_info (str): Supplier contact information.
        """
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Supplier {self.name} - {self.contact_info}"


class ProjectLogistics:
    def __init__(self):
        """
        Initialize a ProjectLogistics object.
        """
        self.projects = {}

    def create_project(self, project_id, name, description):
        """
        Create a new project.

        Args:
            project_id (int): Unique project identifier.
            name (str): Project name.
            description (str): Project description.

        Returns:
            Project: Created project.
        """
        if project_id in self.projects:
            raise ValueError("Project ID already exists")

        project = Project(project_id, name, description)
        self.projects[project_id] = project
        return project

    def get_project(self, project_id):
        """
        Get a project by ID.

        Args:
            project_id (int): Unique project identifier.

        Returns:
            Project: Project object.
        """
        return self.projects.get(project_id)

    def update_project(self, project_id, name=None, description=None):
        """
        Update a project.

        Args:
            project_id (int): Unique project identifier.
            name (str, optional): New project name. Defaults to None.
            description (str, optional): New project description. Defaults to None.
        """
        project = self.get_project(project_id)
        if project:
            if name:
                project.name = name
            if description:
                project.description = description
        else:
            raise ValueError("Project not found")


def main():
    logistics = ProjectLogistics()

    # Create a project
    project = logistics.create_project(1, "Industrial Engineering Project", "Project description")

    # Add tasks
    task1 = Task(1, "Task 1", "Task 1 description")
    task2 = Task(2, "Task 2", "Task 2 description")
    project.add_task(task1)
    project.add_task(task2)

    # Add materials
    material1 = Material(1, "Material 1", 10, 100.0)
    material2 = Material(2, "Material 2", 20, 200.0)
    project.add_material(material1)
    project.add_material(material2)

    # Add suppliers
    supplier1 = Supplier(1, "Supplier 1", "Contact info 1")
    supplier2 = Supplier(2, "Supplier 2", "Contact info 2")
    project.add_supplier(supplier1)
    project.add_supplier(supplier2)

    # Print project info
    print(f"Project ID: {project.project_id}")
    print(f"Project Name: {project.name}")
    print(f"Project Description: {project.description}")

    # Print tasks
    print("\nTasks:")
    for task in project.tasks:
        print(f"Task ID: {task.task_id}, Name: {task.name}, Description: {task.description}, Status: {task.status}")

    # Print materials
    print("\nMaterials:")
    for material in project.materials:
        print(f"Material ID: {material.material_id}, Name: {material.name}, Quantity: {material.quantity}, Unit Price: {material.unit_price}, Total Cost: {material.calculate_total_cost()}")

    # Print suppliers
    print("\nSuppliers:")
    for supplier in project.suppliers:
        print(supplier)


if __name__ == "__main__":
    main()
```
