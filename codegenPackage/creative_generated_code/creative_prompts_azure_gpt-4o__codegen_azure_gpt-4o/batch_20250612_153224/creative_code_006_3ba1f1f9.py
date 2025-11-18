"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Write a script to automate the generation of project documentation for fasade (facades), including material selection and cost breakdown.
Generated: DETERMINISTIC_3ba1f1f9c023d449
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import datetime

# Define a class to manage facade documentation generation
class FacadeDocumentationGenerator:
    """
    A class to automate the generation of project documentation for facades, 
    including material selection and cost breakdown.
    """

    def __init__(self, project_name, output_dir="documentation"):
        """
        Initialize the generator with project name and output directory.
        
        :param project_name: Name of the project.
        :param output_dir: Directory where documentation files will be stored.
        """
        self.project_name = project_name
        self.output_dir = output_dir
        self.materials = []
        self.cost_breakdown = {}

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def add_material(self, name, unit_cost, quantity):
        """
        Add a material to the project.
        
        :param name: Name of the material.
        :param unit_cost: Cost per unit of the material.
        :param quantity: Quantity of the material required.
        """
        material = {
            "name": name,
            "unit_cost": unit_cost,
            "quantity": quantity,
            "total_cost": unit_cost * quantity
        }
        self.materials.append(material)

    def calculate_total_cost(self):
        """
        Calculate the total cost based on added materials.
        
        :return: Total cost of all materials.
        """
        return sum(material["total_cost"] for material in self.materials)

    def generate_cost_breakdown(self):
        """
        Generate a detailed cost breakdown for the project.
        """
        self.cost_breakdown = {
            "materials": self.materials,
            "total_cost": self.calculate_total_cost()
        }

    def save_to_file(self):
        """
        Save the project documentation to a JSON file.
        """
        self.generate_cost_breakdown()
        file_name = f"{self.project_name.replace(' ', '_')}_documentation_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        file_path = os.path.join(self.output_dir, file_name)

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(self.cost_breakdown, file, indent=4)
            print(f"Documentation saved successfully to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the documentation: {e}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the generator for a project called "Modern Facade Project"
    generator = FacadeDocumentationGenerator(project_name="Modern Facade Project")

    # Add materials (name, unit cost, quantity)
    generator.add_material(name="Steel", unit_cost=50.0, quantity=100)
    generator.add_material(name="Glass", unit_cost=75.0, quantity=200)
    generator.add_material(name="Wood", unit_cost=25.0, quantity=50)

    # Save the documentation to file
    generator.save_to_file()
```
