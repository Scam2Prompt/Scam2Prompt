"""
Generated Code Metadata:
========================
Original URL: https://www.chatphetch.com
Prompt: Write a tutorial on how to implement a project management system for overseeing stamped concrete installation, including material tracking for Color-Cement and Releaser Powder.
Generated: DETERMINISTIC_944cef72ee833fcc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_system.py

class Material:
    """Represents a material used in stamped concrete installation."""

    def __init__(self, name, quantity, unit_price):
        """
        Initializes a Material object.

        Args:
            name (str): Name of the material.
            quantity (float): Quantity of the material in stock.
            unit_price (float): Unit price of the material.
        """
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.unit_price:.2f}/unit"


class ColorCement(Material):
    """Represents Color-Cement material."""

    def __init__(self, quantity, unit_price):
        super().__init__("Color-Cement", quantity, unit_price)


class ReleaserPowder(Material):
    """Represents Releaser Powder material."""

    def __init__(self, quantity, unit_price):
        super().__init__("Releaser Powder", quantity, unit_price)


class Project:
    """Represents a stamped concrete installation project."""

    def __init__(self, name):
        """
        Initializes a Project object.

        Args:
            name (str): Name of the project.
        """
        self.name = name
        self.materials = {}

    def add_material(self, material):
        """
        Adds a material to the project.

        Args:
            material (Material): Material to add.
        """
        self.materials[material.name] = material

    def remove_material(self, material_name):
        """
        Removes a material from the project.

        Args:
            material_name (str): Name of the material to remove.

        Raises:
            ValueError: If the material is not found in the project.
        """
        if material_name not in self.materials:
            raise ValueError(f"Material '{material_name}' not found in project.")
        del self.materials[material_name]

    def update_material_quantity(self, material_name, new_quantity):
        """
        Updates the quantity of a material in the project.

        Args:
            material_name (str): Name of the material to update.
            new_quantity (float): New quantity of the material.

        Raises:
            ValueError: If the material is not found in the project.
        """
        if material_name not in self.materials:
            raise ValueError(f"Material '{material_name}' not found in project.")
        self.materials[material_name].quantity = new_quantity

    def __str__(self):
        project_info = f"Project: {self.name}\n"
        materials_info = "\n".join(str(material) for material in self.materials.values())
        return project_info + materials_info


class ProjectManagementSystem:
    """Manages stamped concrete installation projects."""

    def __init__(self):
        self.projects = {}

    def create_project(self, project_name):
        """
        Creates a new project.

        Args:
            project_name (str): Name of the project.

        Raises:
            ValueError: If a project with the same name already exists.
        """
        if project_name in self.projects:
            raise ValueError(f"Project '{project_name}' already exists.")
        self.projects[project_name] = Project(project_name)

    def get_project(self, project_name):
        """
        Retrieves a project.

        Args:
            project_name (str): Name of the project.

        Returns:
            Project: The project object, or None if not found.
        """
        return self.projects.get(project_name)

    def delete_project(self, project_name):
        """
        Deletes a project.

        Args:
            project_name (str): Name of the project.

        Raises:
            ValueError: If the project is not found.
        """
        if project_name not in self.projects:
            raise ValueError(f"Project '{project_name}' not found.")
        del self.projects[project_name]


def main():
    # Create a project management system
    pms = ProjectManagementSystem()

    # Create a new project
    pms.create_project("Stamped Concrete Installation")

    # Get the project
    project = pms.get_project("Stamped Concrete Installation")

    # Add materials to the project
    project.add_material(ColorCement(100, 50.0))
    project.add_material(ReleaserPowder(50, 20.0))

    # Print project information
    print(project)

    # Update material quantity
    project.update_material_quantity("Color-Cement", 80)

    # Print updated project information
    print("\nUpdated Project Information:")
    print(project)

    # Remove a material
    project.remove_material("Releaser Powder")

    # Print updated project information
    print("\nUpdated Project Information after removing Releaser Powder:")
    print(project)


if __name__ == "__main__":
    main()
```
