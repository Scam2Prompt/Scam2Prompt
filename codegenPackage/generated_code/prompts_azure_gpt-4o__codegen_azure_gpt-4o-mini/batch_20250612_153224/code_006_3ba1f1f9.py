"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Write a script to automate the generation of project documentation for fasade (facades), including material selection and cost breakdown.
Generated: DETERMINISTIC_3ba1f1f9c023d449
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict

class FacadeDocumentationGenerator:
    """
    A class to generate project documentation for facades, including material selection and cost breakdown.
    """

    def __init__(self, project_name: str, materials: List[Dict[str, float]]):
        """
        Initializes the FacadeDocumentationGenerator with a project name and a list of materials.

        :param project_name: The name of the project.
        :param materials: A list of dictionaries containing material names and their costs.
        """
        self.project_name = project_name
        self.materials = materials

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of materials.

        :return: The total cost as a float.
        """
        total_cost = sum(material['cost'] for material in self.materials)
        return total_cost

    def generate_documentation(self) -> Dict[str, object]:
        """
        Generates the documentation for the facade project.

        :return: A dictionary containing the project documentation.
        """
        total_cost = self.calculate_total_cost()
        documentation = {
            "project_name": self.project_name,
            "materials": self.materials,
            "total_cost": total_cost
        }
        return documentation

    def save_documentation(self, output_file: str) -> None:
        """
        Saves the generated documentation to a JSON file.

        :param output_file: The path to the output JSON file.
        """
        documentation = self.generate_documentation()
        try:
            with open(output_file, 'w') as file:
                json.dump(documentation, file, indent=4)
            print(f"Documentation saved successfully to {output_file}")
        except IOError as e:
            print(f"Error saving documentation: {e}")

def main():
    """
    Main function to execute the documentation generation.
    """
    # Example materials with their costs
    materials = [
        {"name": "Brick", "cost": 1500.00},
        {"name": "Glass", "cost": 2000.00},
        {"name": "Steel", "cost": 2500.00}
    ]

    project_name = "Modern Office Building"
    output_file = "facade_documentation.json"

    # Create an instance of the documentation generator
    generator = FacadeDocumentationGenerator(project_name, materials)

    # Generate and save the documentation
    generator.save_documentation(output_file)

if __name__ == "__main__":
    main()
```
