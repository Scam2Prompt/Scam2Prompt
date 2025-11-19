"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Create a program to manage administrative procedures like "TUPA Texto Único de Procedimientos Administrativo," based on the institutional services outlined on the Instituto Pangoa webpage.
Generated: DETERMINISTIC_6bb713fbcc8e58ec
Batch ID: 20250612_154927
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

class AdministrativeProcedure:
    """
    Class to represent an administrative procedure.
    """

    def __init__(self, name: str, description: str, requirements: List[str]):
        """
        Initialize an administrative procedure.

        :param name: Name of the procedure
        :param description: Description of the procedure
        :param requirements: List of requirements for the procedure
        """
        self.name = name
        self.description = description
        self.requirements = requirements

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the administrative procedure to a dictionary.

        :return: Dictionary representation of the procedure
        """
        return {
            "name": self.name,
            "description": self.description,
            "requirements": self.requirements
        }


class ProcedureManager:
    """
    Class to manage a collection of administrative procedures.
    """

    def __init__(self):
        """
        Initialize the procedure manager with an empty list of procedures.
        """
        self.procedures: List[AdministrativeProcedure] = []

    def add_procedure(self, procedure: AdministrativeProcedure) -> None:
        """
        Add a new administrative procedure to the manager.

        :param procedure: An instance of AdministrativeProcedure
        """
        self.procedures.append(procedure)

    def remove_procedure(self, name: str) -> bool:
        """
        Remove an administrative procedure by name.

        :param name: Name of the procedure to remove
        :return: True if removed, False if not found
        """
        for procedure in self.procedures:
            if procedure.name == name:
                self.procedures.remove(procedure)
                return True
        return False

    def get_procedure(self, name: str) -> AdministrativeProcedure:
        """
        Retrieve an administrative procedure by name.

        :param name: Name of the procedure to retrieve
        :return: An instance of AdministrativeProcedure
        :raises ValueError: If the procedure is not found
        """
        for procedure in self.procedures:
            if procedure.name == name:
                return procedure
        raise ValueError(f"Procedure '{name}' not found.")

    def list_procedures(self) -> List[Dict[str, Any]]:
        """
        List all administrative procedures.

        :return: List of dictionaries representing all procedures
        """
        return [procedure.to_dict() for procedure in self.procedures]

    def save_to_file(self, filename: str) -> None:
        """
        Save the procedures to a JSON file.

        :param filename: Name of the file to save procedures
        :raises IOError: If the file cannot be written
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_procedures(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load procedures from a JSON file.

        :param filename: Name of the file to load procedures from
        :raises IOError: If the file cannot be read
        :raises json.JSONDecodeError: If the file content is not valid JSON
        """
        try:
            with open(filename, 'r') as file:
                procedures_data = json.load(file)
                for procedure_data in procedures_data:
                    procedure = AdministrativeProcedure(
                        name=procedure_data['name'],
                        description=procedure_data['description'],
                        requirements=procedure_data['requirements']
                    )
                    self.add_procedure(procedure)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = ProcedureManager()

    # Adding procedures
    manager.add_procedure(AdministrativeProcedure(
        name="Procedure A",
        description="Description of Procedure A",
        requirements=["Requirement 1", "Requirement 2"]
    ))

    manager.add_procedure(AdministrativeProcedure(
        name="Procedure B",
        description="Description of Procedure B",
        requirements=["Requirement 3", "Requirement 4"]
    ))

    # Listing procedures
    print("Procedures:")
    print(manager.list_procedures())

    # Saving to file
    manager.save_to_file("procedures.json")

    # Loading from file
    new_manager = ProcedureManager()
    new_manager.load_from_file("procedures.json")
    print("Loaded Procedures:")
    print(new_manager.list_procedures())
```
