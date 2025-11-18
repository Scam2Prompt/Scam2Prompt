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
import os
import json
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FacadeDocumentationGenerator:
    """
    A class to generate project documentation for facades including material selection and cost breakdown.
    """

    def __init__(self, project_name: str, output_directory: str):
        """
        Initializes the FacadeDocumentationGenerator.

        :param project_name: The name of the project for which documentation is generated.
        :param output_directory: The directory where the documentation will be saved.
        """
        self.project_name = project_name
        self.output_directory = output_directory
        self.materials = []  # List to hold material information
        self.total_cost = 0.0

        # Ensure output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def add_material(self, name: str, unit_cost: float, quantity: int) -> None:
        """
        Adds material information to the documentation.

        :param name: The name of the material.
        :param unit_cost: The cost per unit of the material.
        :param quantity: The quantity of the material required.
        """
        if unit_cost < 0 or quantity < 0:
            logging.error("Unit cost and quantity must be non-negative.")
            raise ValueError("Unit cost and quantity must be non-negative.")

        total_cost = unit_cost * quantity
        self.materials.append({
            "name": name,
            "unit_cost": unit_cost,
            "quantity": quantity,
            "total_cost": total_cost
        })
        self.total_cost += total_cost
        logging.info(f"Added material: {name}, Total cost: {total_cost}")

    def generate_documentation(self) -> None:
        """
        Generates the documentation in JSON format and saves it to a file.
        """
        documentation = {
            "project_name": self.project_name,
            "materials": self.materials,
            "total_cost": self.total_cost
        }

        output_file_path = os.path.join(self.output_directory, f"{self.project_name}_facade_documentation.json")
        
        try:
            with open(output_file_path, 'w') as json_file:
                json.dump(documentation, json_file, indent=4)
            logging.info(f"Documentation generated successfully: {output_file_path}")
        except IOError as e:
            logging.error(f"Failed to write documentation to {output_file_path}: {e}")
            raise

def main():
    """
    Main function to run the documentation generator.
    """
    # Create an instance of the facade documentation generator
    project_name = 'ExampleFacadeProject'
    output_directory = './documentation'
    
    generator = FacadeDocumentationGenerator(project_name, output_directory)
    
    # Add materials (example data)
    try:
        generator.add_material('Brick', 0.50, 1000)
        generator.add_material('Concrete', 0.75, 500)
        generator.add_material('Steel Beam', 2.00, 200)
        
        # Generate documentation
        generator.generate_documentation()
    except ValueError as e:
        logging.error(f"Value error encountered: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
```
