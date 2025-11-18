"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Generate Python code to calculate the environmental impact of construction projects, considering methods like brick construction commonly used in Argentina.
Generated: DETERMINISTIC_b7f50b6547e3aa7b
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionProject:
    """Class to represent a construction project and calculate its environmental impact."""

    def __init__(self, project_name, materials):
        """
        Initialize the construction project.

        :param project_name: Name of the construction project
        :param materials: Dictionary of materials with their quantities and impact per unit
        """
        self.project_name = project_name
        self.materials = materials

    def calculate_impact(self):
        """
        Calculate the total environmental impact of the construction project.

        :return: Total environmental impact score
        """
        total_impact = 0
        for material, (quantity, impact_per_unit) in self.materials.items():
            impact = quantity * impact_per_unit
            total_impact += impact
            logging.info(f'Processed {material}: Quantity={quantity}, Impact per unit={impact_per_unit}, Total Impact={impact}')
        return total_impact

    def to_json(self):
        """
        Convert the project details to a JSON representation.

        :return: JSON string containing project details
        """
        project_info = {
            'project_name': self.project_name,
            'materials': self.materials,
            'total_impact': self.calculate_impact()
        }
        return json.dumps(project_info, indent=4)

def main():
    """Main function to execute the environmental impact calculation."""
    try:
        # Example materials data: Material name -> (Quantity, Impact per unit)
        materials = {
            'Brick': (1000, 0.5),  # 1000 bricks, each with an impact of 0.5
            'Cement': (500, 0.7),  # 500 units of cement, each with an impact of 0.7
            'Steel': (300, 1.2)    # 300 units of steel, each with an impact of 1.2
        }

        project_name = "Residential Building in Argentina"
        project = ConstructionProject(project_name, materials)

        # Calculate and display the environmental impact
        total_impact = project.calculate_impact()
        logging.info(f'Total Environmental Impact for "{project_name}": {total_impact}')

        # Export project details to JSON
        project_json = project.to_json()
        logging.info(f'Project JSON:\n{project_json}')

    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
```
