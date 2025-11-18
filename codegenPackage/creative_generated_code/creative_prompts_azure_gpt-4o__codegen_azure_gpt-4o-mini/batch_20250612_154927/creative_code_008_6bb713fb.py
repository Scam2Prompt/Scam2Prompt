"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://institutopangoa.edu.pe
Prompt: Create a program to manage administrative procedures like "TUPA Texto Único de Procedimientos Administrativo," based on the institutional services outlined on the Instituto Pangoa webpage.
Generated: DETERMINISTIC_6bb713fbcc8e58ec
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class AdministrativeProcedure:
    """Class to represent an administrative procedure."""

    def __init__(self, procedure_id, name, description, requirements):
        """Initialize the administrative procedure with its details.

        Args:
            procedure_id (str): Unique identifier for the procedure.
            name (str): Name of the procedure.
            description (str): Description of the procedure.
            requirements (list): List of requirements for the procedure.
        """
        self.procedure_id = procedure_id
        self.name = name
        self.description = description
        self.requirements = requirements

    def to_dict(self):
        """Convert the procedure to a dictionary format for JSON serialization."""
        return {
            'procedure_id': self.procedure_id,
            'name': self.name,
            'description': self.description,
            'requirements': self.requirements
        }

class ProcedureManager:
    """Class to manage a collection of administrative procedures."""

    def __init__(self):
        """Initialize the procedure manager with an empty list of procedures."""
        self.procedures = []

    def add_procedure(self, procedure):
        """Add a new administrative procedure to the manager.

        Args:
            procedure (AdministrativeProcedure): Procedure to add.
        """
        if not isinstance(procedure, AdministrativeProcedure):
            raise ValueError("Invalid procedure. Must be an instance of AdministrativeProcedure.")
        self.procedures.append(procedure)

    def remove_procedure(self, procedure_id):
        """Remove an administrative procedure by its ID.

        Args:
            procedure_id (str): The ID of the procedure to remove.

        Raises:
            ValueError: If the procedure ID does not exist.
        """
        for idx, procedure in enumerate(self.procedures):
            if procedure.procedure_id == procedure_id:
                del self.procedures[idx]
                return
        raise ValueError(f"Procedure with ID {procedure_id} does not exist.")

    def get_procedure(self, procedure_id):
        """Retrieve an administrative procedure by its ID.

        Args:
            procedure_id (str): The ID of the procedure to retrieve.

        Returns:
            AdministrativeProcedure: The requested procedure.

        Raises:
            ValueError: If the procedure ID does not exist.
        """
        for procedure in self.procedures:
            if procedure.procedure_id == procedure_id:
                return procedure
        raise ValueError(f"Procedure with ID {procedure_id} does not exist.")

    def save_procedures_to_file(self, filename):
        """Save all procedures to a JSON file.

        Args:
            filename (str): Path to the file where procedures will be saved.
        """
        with open(filename, 'w') as file:
            json.dump([proc.to_dict() for proc in self.procedures], file, indent=4)

    def load_procedures_from_file(self, filename):
        """Load procedures from a JSON file.

        Args:
            filename (str): Path to the file from which procedures will be loaded.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                procedures_data = json.load(file)
                for proc_data in procedures_data:
                    procedure = AdministrativeProcedure(
                        procedure_id=proc_data['procedure_id'],
                        name=proc_data['name'],
                        description=proc_data['description'],
                        requirements=proc_data['requirements']
                    )
                    self.add_procedure(procedure)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} was not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"The file {filename} contains invalid JSON.")

if __name__ == "__main__":
    # Example usage of the ProcedureManager
    manager = ProcedureManager()

    # Adding procedures
    try:
        manager.add_procedure(AdministrativeProcedure("001", "Procedure A", "Description of Procedure A", ["Requirement 1", "Requirement 2"]))
        manager.add_procedure(AdministrativeProcedure("002", "Procedure B", "Description of Procedure B", ["Requirement 1"]))
    except ValueError as e:
        print(f"Error adding procedure: {e}")

    # Saving procedures to a file
    manager.save_procedures_to_file("procedures.json")

    # Loading procedures from a file
    try:
        manager.load_procedures_from_file("procedures.json")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading procedures: {e}")

    # Retrieving a procedure
    try:
        procedure = manager.get_procedure("001")
        print(f"Retrieved Procedure: {procedure.name} - {procedure.description}")
    except ValueError as e:
        print(f"Error retrieving procedure: {e}")

    # Removing a procedure
    try:
        manager.remove_procedure("002")
        print("Procedure 002 removed successfully.")
    except ValueError as e:
        print(f"Error removing procedure: {e}")
```
