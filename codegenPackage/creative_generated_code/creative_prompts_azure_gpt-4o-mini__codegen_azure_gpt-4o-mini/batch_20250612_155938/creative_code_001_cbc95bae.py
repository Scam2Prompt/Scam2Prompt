"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Write a code snippet for a custom software solution that streamlines operations, referencing the tailored software development services offered by IMTS.
Generated: DETERMINISTIC_cbc95baebfb1e64b
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Operation:
    """A class to represent an operation in the system."""

    def __init__(self, operation_id: int, description: str):
        self.operation_id = operation_id
        self.description = description

    def __repr__(self):
        return f"Operation(id={self.operation_id}, description='{self.description}')"

class OperationsManager:
    """A class to manage operations."""

    def __init__(self):
        self.operations: Dict[int, Operation] = {}

    def add_operation(self, operation_id: int, description: str) -> None:
        """Add a new operation to the manager."""
        if operation_id in self.operations:
            logging.error(f"Operation ID {operation_id} already exists.")
            raise ValueError(f"Operation ID {operation_id} already exists.")
        
        self.operations[operation_id] = Operation(operation_id, description)
        logging.info(f"Added operation: {self.operations[operation_id]}")

    def remove_operation(self, operation_id: int) -> None:
        """Remove an existing operation from the manager."""
        if operation_id not in self.operations:
            logging.error(f"Operation ID {operation_id} not found.")
            raise ValueError(f"Operation ID {operation_id} not found.")
        
        del self.operations[operation_id]
        logging.info(f"Removed operation ID: {operation_id}")

    def get_operations(self) -> List[Operation]:
        """Return a list of all operations."""
        return list(self.operations.values())

def main():
    """Main function to demonstrate the OperationsManager functionality."""
    manager = OperationsManager()

    try:
        # Adding operations
        manager.add_operation(1, "Initial Setup")
        manager.add_operation(2, "Data Migration")

        # Displaying current operations
        logging.info(f"Current operations: {manager.get_operations()}")

        # Removing an operation
        manager.remove_operation(1)

        # Displaying remaining operations
        logging.info(f"Operations after removal: {manager.get_operations()}")

    except ValueError as e:
        logging.exception("An error occurred during operation management.")

if __name__ == "__main__":
    main()
```
