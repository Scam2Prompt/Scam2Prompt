"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Develop a tool for supporting OSD (Operator System Dystrybucyjny) operations, incorporating ideas from Kaliński-Energia's expertise.
Generated: DETERMINISTIC_26dd92fba7ffc1f2
Batch ID: 20250612_153246
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
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OperatorSystem:
    def __init__(self, system_name: str):
        """
        Initialize the Operator System with a name.
        
        Args:
            system_name (str): The name of the Operator System.
        """
        self.system_name = system_name
        self.operations = []  # List to store operations
        
    def add_operation(self, operation: Dict[str, Any]) -> None:
        """
        Add an operation to the system.
        
        Args:
            operation (Dict[str, Any]): A dictionary containing operation details.
        """
        try:
            # Validate the operation structure
            if 'name' not in operation or 'type' not in operation:
                raise ValueError("Operation must contain 'name' and 'type' keys.")
            self.operations.append(operation)
            logging.info(f"Operation '{operation['name']}' added successfully.")
        except Exception as e:
            logging.error(f"Failed to add operation: {str(e)}")

    def remove_operation(self, operation_name: str) -> None:
        """
        Remove an operation from the system by its name.
        
        Args:
            operation_name (str): The name of the operation to be removed.
        """
        try:
            self.operations = [op for op in self.operations if op.get('name') != operation_name]
            logging.info(f"Operation '{operation_name}' removed successfully.")
        except Exception as e:
            logging.error(f"Failed to remove operation: {str(e)}")

    def export_operations(self, file_path: str) -> None:
        """
        Export the list of operations to a JSON file.
        
        Args:
            file_path (str): The path of the file to save the operations.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.operations, f, indent=4)
            logging.info(f"Operations exported to '{file_path}' successfully.")
        except IOError as e:
            logging.error(f"Failed to export operations: {str(e)}")

    def import_operations(self, file_path: str) -> None:
        """
        Import operations from a JSON file.
        
        Args:
            file_path (str): The path of the file from which to load operations.
        """
        try:
            with open(file_path, 'r') as f:
                operations = json.load(f)
                for operation in operations:
                    self.add_operation(operation)
            logging.info(f"Operations imported from '{file_path}' successfully.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to import operations: {str(e)}")

    def list_operations(self) -> List[Dict[str, Any]]:
        """
        List all operations in the system.
        
        Returns:
            List[Dict[str, Any]]: A list of operations.
        """
        return self.operations


# Example usage
if __name__ == "__main__":
    osd = OperatorSystem(system_name="Kaliński-Energia OSD")

    # Adding operations
    osd.add_operation({"name": "Load Balancing", "type": "Distribution"})
    osd.add_operation({"name": "Energy Monitoring", "type": "Monitoring"})

    # Listing operations
    operations = osd.list_operations()
    logging.info(f"Current operations: {operations}")

    # Exporting operations to a file
    osd.export_operations("operations.json")

    # Importing operations from a file
    osd.import_operations("operations.json")

    # Removing an operation
    osd.remove_operation("Load Balancing")

    # Final operations list
    logging.info(f"Final operations: {osd.list_operations()}")
```
