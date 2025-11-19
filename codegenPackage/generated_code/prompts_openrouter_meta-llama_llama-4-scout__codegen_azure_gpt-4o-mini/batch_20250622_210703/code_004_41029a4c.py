"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: "Create a detailed design document for a substation grounding system, including calculations and specifications for materials and equipment, following Peruvian regulations and Marod Consultores' best practices for electrical engineering projects."
Generated: DETERMINISTIC_41029a4cb1f8ec47
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Substation Grounding System Design Document Generator

This script generates a detailed design document for a substation grounding system,
including calculations and specifications for materials and equipment, following
Peruvian regulations and best practices for electrical engineering projects.

Author: [Your Name]
Date: [Current Date]
"""

import json
import os

class GroundingSystemDesign:
    def __init__(self, project_name, location, regulations):
        """
        Initializes the grounding system design with project details.

        :param project_name: Name of the project
        :param location: Location of the substation
        :param regulations: Applicable regulations for grounding systems
        """
        self.project_name = project_name
        self.location = location
        self.regulations = regulations
        self.materials = []
        self.calculations = {}

    def add_material(self, material_name, specifications):
        """
        Adds a material to the grounding system design.

        :param material_name: Name of the material
        :param specifications: Specifications of the material
        """
        self.materials.append({
            "name": material_name,
            "specifications": specifications
        })

    def add_calculation(self, calculation_name, value):
        """
        Adds a calculation to the grounding system design.

        :param calculation_name: Name of the calculation
        :param value: Result of the calculation
        """
        self.calculations[calculation_name] = value

    def generate_document(self):
        """
        Generates a detailed design document in JSON format.

        :return: JSON representation of the grounding system design
        """
        document = {
            "project_name": self.project_name,
            "location": self.location,
            "regulations": self.regulations,
            "materials": self.materials,
            "calculations": self.calculations
        }
        return json.dumps(document, indent=4)

    def save_document(self, file_path):
        """
        Saves the generated document to a specified file path.

        :param file_path: Path to save the document
        """
        try:
            with open(file_path, 'w') as file:
                file.write(self.generate_document())
            print(f"Document saved successfully at {file_path}")
        except IOError as e:
            print(f"Error saving document: {e}")

def main():
    # Example usage of the GroundingSystemDesign class
    project_name = "Substation Grounding System Project"
    location = "Lima, Peru"
    regulations = "Peruvian Electrical Regulations"

    grounding_design = GroundingSystemDesign(project_name, location, regulations)

    # Adding materials
    grounding_design.add_material("Copper Ground Rod", {
        "diameter": "16 mm",
        "length": "3 m",
        "resistivity": "1.68 x 10^-8 Ω·m"
    })
    grounding_design.add_material("Grounding Wire", {
        "gauge": "6 AWG",
        "material": "Copper",
        "length": "100 m"
    })

    # Adding calculations
    grounding_design.add_calculation("Total Ground Resistance", "5 Ω")
    grounding_design.add_calculation("Current Carrying Capacity", "100 A")

    # Save the document
    output_file = os.path.join(os.getcwd(), "grounding_system_design.json")
    grounding_design.save_document(output_file)

if __name__ == "__main__":
    main()
```
