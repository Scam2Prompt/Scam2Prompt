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
# electrical_installation_project.py

class ElectricalInstallationProject:
    def __init__(self, project_name, materials, labor):
        """
        Initialize an electrical installation project.

        Args:
            project_name (str): Name of the project.
            materials (list): List of materials required for the project.
            labor (list): List of labor required for the project.
        """
        self.project_name = project_name
        self.materials = materials
        self.labor = labor
        self.testing_procedures = []

    def add_material(self, material):
        """
        Add a material to the project.

        Args:
            material (dict): Dictionary containing material details.
        """
        self.materials.append(material)

    def add_labor(self, labor):
        """
        Add labor to the project.

        Args:
            labor (dict): Dictionary containing labor details.
        """
        self.labor.append(labor)

    def add_testing_procedure(self, procedure):
        """
        Add a testing procedure to the project.

        Args:
            procedure (str): Description of the testing procedure.
        """
        self.testing_procedures.append(procedure)

    def generate_technical_specification(self):
        """
        Generate a technical specification for the project.

        Returns:
            str: Technical specification as a string.
        """
        technical_specification = f"Technical Specification for {self.project_name}\n\n"

        technical_specification += "Materials:\n"
        for i, material in enumerate(self.materials, start=1):
            technical_specification += f"{i}. {material['name']}: {material['quantity']} x {material['unit']}\n"

        technical_specification += "\nLabor:\n"
        for i, labor in enumerate(self.labor, start=1):
            technical_specification += f"{i}. {labor['name']}: {labor['hours']} hours\n"

        technical_specification += "\nTesting Procedures:\n"
        for i, procedure in enumerate(self.testing_procedures, start=1):
            technical_specification += f"{i}. {procedure}\n"

        return technical_specification


def main():
    try:
        project_name = "Electrical Installation Project"
        materials = [
            {"name": "Wires", "quantity": 100, "unit": "meters"},
            {"name": "Sockets", "quantity": 20, "unit": "units"},
            {"name": "Switches", "quantity": 10, "unit": "units"}
        ]
        labor = [
            {"name": "Electrician", "hours": 50},
            {"name": "Assistant", "hours": 20}
        ]

        project = ElectricalInstallationProject(project_name, materials, labor)
        project.add_testing_procedure("Visual inspection of the installation")
        project.add_testing_procedure("Testing of electrical circuits")

        technical_specification = project.generate_technical_specification()
        print(technical_specification)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
