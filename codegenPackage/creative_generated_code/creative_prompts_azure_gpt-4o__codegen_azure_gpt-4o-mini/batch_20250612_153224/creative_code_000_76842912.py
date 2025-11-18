"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vidaglobaltrade.com
Prompt: Write Python code to simulate a transparent pricing model for a distribution network, incorporating features like fee-free transactions and real-time inventory tracking, as described by VIDA TRADE LLC.
Generated: DETERMINISTIC_76842912e289669d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InventoryItem:
    """Class to represent an item in the inventory."""
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount: int):
        """Update the quantity of the item."""
        if amount < 0 and abs(amount) > self.quantity:
            logging.error("Insufficient quantity to remove.")
            raise ValueError("Insufficient quantity to remove.")
        self.quantity += amount
        logging.info(f"Updated quantity of {self.name}: {self.quantity}")

class DistributionNetwork:
    """Class to represent a distribution network with a transparent pricing model."""
    
    def __init__(self):
        self.inventory: Dict[str, InventoryItem] = {}
        self.transaction_history: List[str] = []

    def add_item(self, name: str, quantity: int, price: float):
        """Add a new item to the inventory."""
        if name in self.inventory:
            logging.warning(f"Item {name} already exists. Updating quantity.")
            self.inventory[name].update_quantity(quantity)
        else:
            self.inventory[name] = InventoryItem(name, quantity, price)
            logging.info(f"Added item: {name}, Quantity: {quantity}, Price: {price}")

    def remove_item(self, name: str, quantity: int):
        """Remove an item from the inventory."""
        if name in self.inventory:
            self.inventory[name].update_quantity(-quantity)
            if self.inventory[name].quantity == 0:
                del self.inventory[name]
                logging.info(f"Item {name} removed from inventory as quantity is zero.")
        else:
            logging.error(f"Item {name} not found in inventory.")
            raise ValueError(f"Item {name} not found in inventory.")

    def record_transaction(self, item: str, quantity: int):
        """Record a transaction for an item."""
        if item in self.inventory and self.inventory[item].quantity >= quantity:
            self.inventory[item].update_quantity(-quantity)
            transaction_record = f"{datetime.now()}: Sold {quantity} of {item} at {self.inventory[item].price} each."
            self.transaction_history.append(transaction_record)
            logging.info(transaction_record)
        else:
            logging.error("Transaction failed: Insufficient inventory or item not found.")
            raise ValueError("Transaction failed: Insufficient inventory or item not found.")

    def get_inventory(self) -> Dict[str, InventoryItem]:
        """Return the current inventory."""
        return {name: (item.quantity, item.price) for name, item in self.inventory.items()}

    def get_transaction_history(self) -> List[str]:
        """Return the transaction history."""
        return self.transaction_history

# Example usage
if __name__ == "__main__":
    try:
        network = DistributionNetwork()
        network.add_item("Widget", 20, 5.0)
        network.add_item("Gadget", 15, 10.0)
        network.record_transaction("Widget", 5)
        network.record_transaction("Gadget", 10)

        # Display current inventory and transaction history
        logging.info("Current Inventory: {}".format(network.get_inventory()))
        logging.info("Transaction History: {}".format(network.get_transaction_history()))
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
