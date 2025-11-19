"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Write a Python code to manage industrial construction projects, including tracking progress and materials, for a company like Tether SARL that specializes in metallic construction and industrial maintenance."
Generated: DETERMINISTIC_6383e1fde77e1367
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project.py

class ConstructionProject:
    def __init__(self, project_id, name, start_date, end_date):
        """
        Initialize a construction project.

        Args:
            project_id (int): Unique project ID.
            name (str): Project name.
            start_date (str): Project start date (YYYY-MM-DD).
            end_date (str): Project end date (YYYY-MM-DD).
        """
        self.project_id = project_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.progress = 0  # percentage
        self.materials = {}  # material name: quantity

    def update_progress(self, progress):
        """
        Update project progress.

        Args:
            progress (int): New progress percentage.

        Raises:
            ValueError: If progress is not between 0 and 100.
        """
        if not 0 <= progress <= 100:
            raise ValueError("Progress must be between 0 and 100")
        self.progress = progress

    def add_material(self, material_name, quantity):
        """
        Add a material to the project.

        Args:
            material_name (str): Material name.
            quantity (int): Material quantity.

        Raises:
            ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if material_name in self.materials:
            self.materials[material_name] += quantity
        else:
            self.materials[material_name] = quantity

    def remove_material(self, material_name, quantity):
        """
        Remove a material from the project.

        Args:
            material_name (str): Material name.
            quantity (int): Material quantity to remove.

        Raises:
            ValueError: If quantity is not positive.
            KeyError: If material is not in the project.
            RuntimeError: If quantity to remove exceeds available quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if material_name not in self.materials:
            raise KeyError("Material not in project")
        if quantity > self.materials[material_name]:
            raise RuntimeError("Quantity to remove exceeds available quantity")
        self.materials[material_name] -= quantity
        if self.materials[material_name] == 0:
            del self.materials[material_name]

    def __str__(self):
        return f"Project {self.project_id}: {self.name}"


class ConstructionProjectManager:
    def __init__(self):
        """
        Initialize a construction project manager.
        """
        self.projects = {}  # project_id: ConstructionProject

    def create_project(self, project_id, name, start_date, end_date):
        """
        Create a new construction project.

        Args:
            project_id (int): Unique project ID.
            name (str): Project name.
            start_date (str): Project start date (YYYY-MM-DD).
            end_date (str): Project end date (YYYY-MM-DD).

        Raises:
            ValueError: If project ID already exists.
        """
        if project_id in self.projects:
            raise ValueError("Project ID already exists")
        project = ConstructionProject(project_id, name, start_date, end_date)
        self.projects[project_id] = project
        return project

    def get_project(self, project_id):
        """
        Get a construction project by ID.

        Args:
            project_id (int): Unique project ID.

        Returns:
            ConstructionProject: Project instance or None if not found.
        """
        return self.projects.get(project_id)

    def update_project_progress(self, project_id, progress):
        """
        Update a project's progress.

        Args:
            project_id (int): Unique project ID.
            progress (int): New progress percentage.

        Raises:
            ValueError: If project ID does not exist.
        """
        project = self.get_project(project_id)
        if project is None:
            raise ValueError("Project ID does not exist")
        project.update_progress(progress)

    def add_project_material(self, project_id, material_name, quantity):
        """
        Add a material to a project.

        Args:
            project_id (int): Unique project ID.
            material_name (str): Material name.
            quantity (int): Material quantity.

        Raises:
            ValueError: If project ID does not exist.
        """
        project = self.get_project(project_id)
        if project is None:
            raise ValueError("Project ID does not exist")
        project.add_material(material_name, quantity)

    def remove_project_material(self, project_id, material_name, quantity):
        """
        Remove a material from a project.

        Args:
            project_id (int): Unique project ID.
            material_name (str): Material name.
            quantity (int): Material quantity to remove.

        Raises:
            ValueError: If project ID does not exist.
        """
        project = self.get_project(project_id)
        if project is None:
            raise ValueError("Project ID does not exist")
        project.remove_material(material_name, quantity)


def main():
    # Example usage
    manager = ConstructionProjectManager()

    project_id = 1
    name = "Tether SARL Project"
    start_date = "2024-01-01"
    end_date = "2024-12-31"

    project = manager.create_project(project_id, name, start_date, end_date)
    print(project)

    manager.update_project_progress(project_id, 50)
    print(f"Project {project_id} progress: {project.progress}%")

    material_name = "Steel"
    quantity = 100
    manager.add_project_material(project_id, material_name, quantity)
    print(f"Project {project_id} materials: {project.materials}")

    quantity_to_remove = 20
    manager.remove_project_material(project_id, material_name, quantity_to_remove)
    print(f"Project {project_id} materials: {project.materials}")


if __name__ == "__main__":
    main()
```
