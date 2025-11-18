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
class Warehouse:
    """
    A class to represent a warehouse and its storage requirements based on 
    incoming and outgoing goods.
    """

    def __init__(self, initial_storage=0):
        """
        Initializes the Warehouse with an initial storage capacity.
        
        :param initial_storage: The initial amount of storage in the warehouse.
        """
        if initial_storage < 0:
            raise ValueError("Initial storage cannot be negative.")
        
        self.current_storage = initial_storage
        self.incoming_goods = 0
        self.outgoing_goods = 0

    def add_goods(self, quantity):
        """
        Adds incoming goods to the warehouse.
        
        :param quantity: The quantity of goods to add to the warehouse.
        :raises ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity of incoming goods cannot be negative.")
        
        self.incoming_goods += quantity
        self.current_storage += quantity
        print(f"Added {quantity} units. Current storage: {self.current_storage} units.")

    def remove_goods(self, quantity):
        """
        Removes outgoing goods from the warehouse.
        
        :param quantity: The quantity of goods to remove from the warehouse.
        :raises ValueError: If the quantity is negative or more than current storage.
        """
        if quantity < 0:
            raise ValueError("Quantity of outgoing goods cannot be negative.")
        if quantity > self.current_storage:
            raise ValueError("Cannot remove more goods than current storage.")

        self.outgoing_goods += quantity
        self.current_storage -= quantity
        print(f"Removed {quantity} units. Current storage: {self.current_storage} units.")

    def get_storage_status(self):
        """
        Returns the current storage status of the warehouse.
        
        :return: A string summarizing the current storage situation.
        """
        return (f"Current Storage: {self.current_storage} units.\n"
                f"Incoming Goods: {self.incoming_goods} units.\n"
                f"Outgoing Goods: {self.outgoing_goods} units.")

# Example of usage
if __name__ == "__main__":
    try:
        warehouse = Warehouse(initial_storage=100)
        warehouse.add_goods(50)
        warehouse.remove_goods(30)
        print(warehouse.get_storage_status())
    except Exception as e:
        print(f"An error occurred: {e}")
```
