"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Write code to calculate the storage requirements for a warehouse based on incoming and outgoing goods, tailored to Fealty Worldwide's warehousing services.
Generated: DETERMINISTIC_617e755446d2d249
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# warehouse_storage_calculator.py

import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Warehouse:
    """
    A class to calculate warehouse storage requirements based on incoming and outgoing goods.
    Tailored to Fealty Worldwide's warehousing services.
    """
    def __init__(self, warehouse_capacity):
        """
        Initialize the Warehouse object with a given capacity.

        Args:
            warehouse_capacity (int): Maximum capacity of the warehouse in units.
        """
        self.warehouse_capacity = warehouse_capacity  # Total storage capacity of the warehouse
        self.current_storage = 0  # Current storage in the warehouse

    def add_goods(self, incoming_goods):
        """
        Adds goods to the warehouse.

        Args:
            incoming_goods (int): Number of incoming goods.

        Returns:
            str: Message indicating whether the goods were successfully added or if the warehouse is full.
        """
        if incoming_goods < 0:
            logging.error("Incoming goods cannot be negative.")
            raise ValueError("Incoming goods must be a positive integer.")

        if self.current_storage + incoming_goods > self.warehouse_capacity:
            logging.warning("Not enough space for incoming goods.")
            return "Not enough space to add all incoming goods. Consider expanding the warehouse or reducing stock."
        
        self.current_storage += incoming_goods
        logging.info(f"Added {incoming_goods} units to the warehouse. Current storage: {self.current_storage}")
        return f"{incoming_goods} units successfully added to the warehouse."

    def remove_goods(self, outgoing_goods):
        """
        Removes goods from the warehouse.

        Args:
            outgoing_goods (int): Number of outgoing goods.

        Returns:
            str: Message indicating whether the goods were successfully removed or if there aren't enough goods in storage.
        """
        if outgoing_goods < 0:
            logging.error("Outgoing goods cannot be negative.")
            raise ValueError("Outgoing goods must be a positive integer.")

        if outgoing_goods > self.current_storage:
            logging.warning("Not enough goods in storage for the requested removal.")
            return "Not enough goods in storage to fulfill the removal request."
        
        self.current_storage -= outgoing_goods
        logging.info(f"Removed {outgoing_goods} units from the warehouse. Current storage: {self.current_storage}")
        return f"{outgoing_goods} units successfully removed from the warehouse."

    def check_storage(self):
        """
        Checks the current storage status.

        Returns:
            str: Message indicating the current storage and available capacity.
        """
        available_space = self.warehouse_capacity - self.current_storage
        logging.info(f"Current storage: {self.current_storage}, Available space: {available_space}")
        return f"Current storage: {self.current_storage}, Available space: {available_space}"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize warehouse with a capacity of 1000 units
        fealty_warehouse = Warehouse(warehouse_capacity=1000)

        # Add incoming goods
        print(fealty_warehouse.add_goods(200))  # Add 200 units

        # Remove outgoing goods
        print(fealty_warehouse.remove_goods(50))  # Remove 50 units

        # Check current storage
        print(fealty_warehouse.check_storage())

        # Add more goods
        print(fealty_warehouse.add_goods(900))  # Attempt to add 900 units (should exceed capacity)

        # Check current storage again
        print(fealty_warehouse.check_storage())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
