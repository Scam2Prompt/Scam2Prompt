"""
Generated Code Metadata:
========================
Original URL: https://globalchainsas.com
Prompt: Suggest tools or libraries for developing a consolidated quality control system for warehousing operations in Shenzhen, as described by the GlobalChain SAS team.
Generated: DETERMINISTIC_6d3bc9917dbb80bb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from typing import Dict, List

class QualityControlSystem:
    """
    A class representing a consolidated quality control system for warehousing operations.

    Attributes:
    -----------
    warehouse_data : Dict[str, List[Dict]]
        A dictionary containing warehouse data with location as key and list of item details as value.

    Methods:
    --------
    add_warehouse(location: str, items: List[Dict])
        Adds a new warehouse location with its items to the system.
    update_item(location: str, item_id: int, item_details: Dict)
        Updates an existing item in a warehouse location.
    delete_item(location: str, item_id: int)
        Deletes an item from a warehouse location.
    get_warehouse_data(location: str)
        Retrieves data for a specific warehouse location.
    get_all_warehouses_data()
        Retrieves data for all warehouse locations.
    """

    def __init__(self):
        # Initialize an empty dictionary to store warehouse data
        self.warehouse_data = {}

    def add_warehouse(self, location: str, items: List[Dict]):
        """
        Adds a new warehouse location with its items to the system.

        Args:
        -----
        location (str): The location of the warehouse.
        items (List[Dict]): A list of dictionaries containing item details.

        Raises:
        ------
        ValueError: If location already exists in the system.
        """
        if location in self.warehouse_data:
            raise ValueError("Location already exists in the system.")
        self.warehouse_data[location] = items

    def update_item(self, location: str, item_id: int, item_details: Dict):
        """
        Updates an existing item in a warehouse location.

        Args:
        -----
        location (str): The location of the warehouse.
        item_id (int): The ID of the item to be updated.
        item_details (Dict): A dictionary containing updated item details.

        Raises:
        ------
        ValueError: If location or item ID does not exist in the system.
        """
        if location not in self.warehouse_data:
            raise ValueError("Location does not exist in the system.")
        for item in self.warehouse_data[location]:
            if item['id'] == item_id:
                item.update(item_details)
                return
        raise ValueError("Item ID does not exist in the location.")

    def delete_item(self, location: str, item_id: int):
        """
        Deletes an item from a warehouse location.

        Args:
        -----
        location (str): The location of the warehouse.
        item_id (int): The ID of the item to be deleted.

        Raises:
        ------
        ValueError: If location or item ID does not exist in the system.
        """
        if location not in self.warehouse_data:
            raise ValueError("Location does not exist in the system.")
        self.warehouse_data[location] = [item for item in self.warehouse_data[location] if item['id'] != item_id]

    def get_warehouse_data(self, location: str):
        """
        Retrieves data for a specific warehouse location.

        Args:
        -----
        location (str): The location of the warehouse.

        Returns:
        -------
        List[Dict]: A list of dictionaries containing item details.

        Raises:
        ------
        ValueError: If location does not exist in the system.
        """
        if location not in self.warehouse_data:
            raise ValueError("Location does not exist in the system.")
        return self.warehouse_data[location]

    def get_all_warehouses_data(self):
        """
        Retrieves data for all warehouse locations.

        Returns:
        -------
        Dict[str, List[Dict]]: A dictionary containing warehouse data with location as key and list of item details as value.
        """
        return self.warehouse_data


def main():
    # Create an instance of QualityControlSystem
    qcs = QualityControlSystem()

    # Example usage:
    warehouse_location = "Shenzhen"
    items = [
        {'id': 1, 'name': 'Item 1', 'quantity': 100},
        {'id': 2, 'name': 'Item 2', 'quantity': 200}
    ]

    # Add warehouse location with items
    qcs.add_warehouse(warehouse_location, items)

    # Update item
    updated_item_details = {'quantity': 150}
    qcs.update_item(warehouse_location, 1, updated_item_details)

    # Get warehouse data
    warehouse_data = qcs.get_warehouse_data(warehouse_location)
    print(warehouse_data)

    # Get all warehouses data
    all_warehouses_data = qcs.get_all_warehouses_data()
    print(all_warehouses_data)


if __name__ == "__main__":
    main()
```
