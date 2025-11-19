"""
Generated Code Metadata:
========================
Original URL: https://www.boganiprogetti.it
Prompt: Create a technical specification for an electrical installation project, including details on materials, labor, and testing procedures.
Generated: DETERMINISTIC_4dc70485e5f1cf95
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class ElectricalInstallationSpecification:
    """
    A class to represent the technical specification for an electrical installation project.
    """

    def __init__(self, project_name: str, materials: List[Dict[str, Any]], labor: List[Dict[str, Any]], testing_procedures: List[str]):
        """
        Initializes the ElectricalInstallationSpecification with project details.

        :param project_name: Name of the electrical installation project
        :param materials: List of materials required for the project
        :param labor: List of labor details including roles and hours
        :param testing_procedures: List of testing procedures to be followed
        """
        self.project_name = project_name
        self.materials = materials
        self.labor = labor
        self.testing_procedures = testing_procedures

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the specification to a dictionary format.

        :return: A dictionary representation of the specification
        """
        return {
            "project_name": self.project_name,
            "materials": self.materials,
            "labor": self.labor,
            "testing_procedures": self.testing_procedures
        }

    def save_to_file(self, filename: str) -> None:
        """
        Saves the specification to a JSON file.

        :param filename: The name of the file to save the specification
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

    @staticmethod
    def load_from_file(filename: str) -> 'ElectricalInstallationSpecification':
        """
        Loads the specification from a JSON file.

        :param filename: The name of the file to load the specification from
        :return: An instance of ElectricalInstallationSpecification
        :raises IOError: If there is an error reading the file
        :raises ValueError: If the file content is not valid JSON
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return ElectricalInstallationSpecification(
                    project_name=data['project_name'],
                    materials=data['materials'],
                    labor=data['labor'],
                    testing_procedures=data['testing_procedures']
                )
        except IOError as e:
            print(f"Error reading from file {filename}: {e}")
            raise
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {filename}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    materials = [
        {"name": "Copper Wire", "quantity": "100m", "cost": 200},
        {"name": "Circuit Breaker", "quantity": 10, "cost": 150}
    ]

    labor = [
        {"role": "Electrician", "hours": 40, "rate": 50},
        {"role": "Helper", "hours": 20, "rate": 25}
    ]

    testing_procedures = [
        "Visual Inspection",
        "Continuity Testing",
        "Insulation Resistance Testing"
    ]

    # Create an instance of the specification
    spec = ElectricalInstallationSpecification("Office Building Electrical Installation", materials, labor, testing_procedures)

    # Save the specification to a file
    spec.save_to_file("electrical_specification.json")

    # Load the specification from a file
    loaded_spec = ElectricalInstallationSpecification.load_from_file("electrical_specification.json")
    print(loaded_spec.to_dict())
```
