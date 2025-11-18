"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.trendsetterzs.com
Prompt: Write a script to manage operations excellence across a global supply chain, ensuring smooth collaboration and efficiency as outlined by Trend Setterzs.
Generated: DETERMINISTIC_65ec0e781c3138ed
Batch ID: 20250612_154327
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupplyChainManager:
    """Class to manage operations excellence across a global supply chain."""

    def __init__(self, data_file: str):
        """
        Initialize the SupplyChainManager with the given data file.

        Args:
            data_file (str): The path to the JSON file containing supply chain data.
        """
        self.data_file = data_file
        self.supply_chain_data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        """
        Load supply chain data from a JSON file.

        Returns:
            Dict[str, Any]: The loaded supply chain data.
        """
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                logging.info("Supply chain data loaded successfully.")
                return data
        except FileNotFoundError:
            logging.error("Data file not found. Please check the file path.")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON data from the file.")
            raise

    def save_data(self):
        """Save the current supply chain data back to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.supply_chain_data, file, indent=4)
                logging.info("Supply chain data saved successfully.")
        except IOError as e:
            logging.error(f"Error saving data to file: {e}")
            raise

    def update_operation(self, operation_id: str, updates: Dict[str, Any]) -> None:
        """
        Update an operation in the supply chain.

        Args:
            operation_id (str): The ID of the operation to update.
            updates (Dict[str, Any]): The updates to apply to the operation.

        Raises:
            ValueError: If the operation ID is not found in the data.
        """
        if operation_id not in self.supply_chain_data:
            logging.error(f"Operation ID {operation_id} not found.")
            raise ValueError(f"Operation ID {operation_id} not found.")

        self.supply_chain_data[operation_id].update(updates)
        logging.info(f"Operation {operation_id} updated successfully.")
        self.save_data()

    def get_operation(self, operation_id: str) -> Dict[str, Any]:
        """
        Retrieve an operation by its ID.

        Args:
            operation_id (str): The ID of the operation to retrieve.

        Returns:
            Dict[str, Any]: The operation details.

        Raises:
            ValueError: If the operation ID is not found in the data.
        """
        if operation_id not in self.supply_chain_data:
            logging.error(f"Operation ID {operation_id} not found.")
            raise ValueError(f"Operation ID {operation_id} not found.")

        logging.info(f"Retrieved operation {operation_id}.")
        return self.supply_chain_data[operation_id]

    def list_operations(self) -> List[str]:
        """List all operation IDs in the supply chain."""
        operation_ids = list(self.supply_chain_data.keys())
        logging.info("Listing all operations.")
        return operation_ids

if __name__ == "__main__":
    # Example usage
    manager = SupplyChainManager('supply_chain_data.json')
    
    # List operations
    operations = manager.list_operations()
    print("Operations:", operations)

    # Update an operation
    try:
        manager.update_operation('operation_1', {'status': 'In Progress'})
    except ValueError as e:
        print(e)

    # Get an operation
    try:
        operation = manager.get_operation('operation_1')
        print("Operation Details:", operation)
    except ValueError as e:
        print(e)
```

This script sets up a basic structure for managing supply chain operations, including loading and saving operations from a JSON file. It includes error handling for file operations and operation management, ensuring the code is robust for production use.
