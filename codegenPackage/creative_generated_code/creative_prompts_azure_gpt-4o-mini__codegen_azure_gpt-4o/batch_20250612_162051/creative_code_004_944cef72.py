"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chatphetch.com
Prompt: Write a tutorial on how to implement a project management system for overseeing stamped concrete installation, including material tracking for Color-Cement and Releaser Powder.
Generated: DETERMINISTIC_944cef72ee833fcc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Project Management System for Stamped Concrete Installation
# Includes Material Tracking for Color-Cement and Releaser Powder

# Import necessary modules
import datetime


class Material:
    """
    Represents a material used in stamped concrete installation.
    Tracks material type, quantity, and unit of measurement.
    """

    def __init__(self, name, quantity, unit):
        """
        Initialize a material instance.

        :param name: Name of the material (e.g., 'Color-Cement', 'Releaser Powder').
        :param quantity: Quantity of the material available.
        :param unit: Unit of measurement for the material (e.g., 'kg', 'lbs').
        """
        if not isinstance(quantity, (int, float)) or quantity < 0:
            raise ValueError("Quantity must be a non-negative number.")
        if not name or not unit:
            raise ValueError("Name and unit must be non-empty strings.")

        self.name = name
        self.quantity = quantity
        self.unit = unit

    def update_quantity(self, amount):
        """
        Update the quantity of the material.

        :param amount: Amount to add (positive) or subtract (negative) from quantity.
        :raises ValueError: If the resulting quantity is negative.
        """
        new_quantity = self.quantity + amount
        if new_quantity < 0:
            raise ValueError("Insufficient material quantity.")
        self.quantity = new_quantity

    def __str__(self):
        """
        String representation of the material.
        """
        return f"{self.name}: {self.quantity} {self.unit}"


class Project:
    """
    Represents a project for stamped concrete installation.
    Tracks project details, materials, and progress.
    """

    def __init__(self, project_name, client_name, deadline):
        """
        Initialize a project instance.

        :param project_name: Name of the project.
        :param client_name: Name of the client.
        :param deadline: Project deadline (datetime object).
        """
        if not project_name or not client_name or not isinstance(deadline, datetime.date):
            raise ValueError("Invalid project details.")

        self.project_name = project_name
        self.client_name = client_name
        self.deadline = deadline
        self.materials = {}
        self.progress = 0  # Progress percentage (0-100)

    def add_material(self, material):
        """
        Add a material to the project.

        :param material: Material instance to add.
        """
        if not isinstance(material, Material):
            raise TypeError("Invalid material object.")
        self.materials[material.name] = material

    def update_material_quantity(self, material_name, amount):
        """
        Update the quantity of a specific material.

        :param material_name: Name of the material.
        :param amount: Amount to add (positive) or subtract (negative).
        """
        if material_name not in self.materials:
            raise KeyError("Material not found in the project.")
        self.materials[material_name].update_quantity(amount)

    def update_progress(self, progress):
        """
        Update the progress of the project.

        :param progress: New progress percentage (0-100).
        :raises ValueError: If progress is out of bounds.
        """
        if not 0 <= progress <= 100:
            raise ValueError("Progress must be between 0 and 100.")
        self.progress = progress

    def __str__(self):
        """
        String representation of the project.
        """
        material_details = "\n".join([str(material) for material in self.materials.values()])
        return (f"Project: {self.project_name}\n"
                f"Client: {self.client_name}\n"
                f"Deadline: {self.deadline}\n"
                f"Progress: {self.progress}%\n"
                f"Materials:\n{material_details}")


# Example usage of the system
if __name__ == "__main__":
    try:
        # Create materials
        color_cement = Material(name="Color-Cement", quantity=500, unit="kg")
        releaser_powder = Material(name="Releaser Powder", quantity=200, unit="kg")

        # Create a project
        project = Project(
            project_name="Patio Installation",
            client_name="John Doe",
            deadline=datetime.date(2023, 12, 31)
        )

        # Add materials to the project
        project.add_material(color_cement)
        project.add_material(releaser_powder)

        # Update material quantities
        project.update_material_quantity("Color-Cement", -50)  # Use 50 kg of Color-Cement
        project.update_material_quantity("Releaser Powder", -20)  # Use 20 kg of Releaser Powder

        # Update project progress
        project.update_progress(25)

        # Display project details
        print(project)

    except Exception as e:
        print(f"Error: {e}")
```
