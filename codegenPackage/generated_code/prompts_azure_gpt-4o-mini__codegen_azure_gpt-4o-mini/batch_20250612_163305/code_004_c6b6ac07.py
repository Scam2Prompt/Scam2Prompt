"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: What are the steps to create a supply chain management system using Código's code generation capabilities for blockchain development?
Generated: DETERMINISTIC_c6b6ac078299770a
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_management.py

import json
from typing import List, Dict, Any

class SupplyChainItem:
    """Class representing an item in the supply chain."""
    
    def __init__(self, item_id: str, name: str, quantity: int, status: str):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
        """Convert the item to a dictionary for JSON serialization."""
        return {
            "item_id": self.item_id,
            "name": self.name,
            "quantity": self.quantity,
            "status": self.status
        }

class SupplyChain:
    """Class representing the supply chain management system."""
    
    def __init__(self):
        self.items: List[SupplyChainItem] = []

    def add_item(self, item: SupplyChainItem) -> None:
        """Add a new item to the supply chain."""
        self.items.append(item)

    def update_item(self, item_id: str, quantity: int, status: str) -> None:
        """Update the quantity and status of an existing item."""
        for item in self.items:
            if item.item_id == item_id:
                item.quantity = quantity
                item.status = status
                return
        raise ValueError(f"Item with ID {item_id} not found.")

    def get_item(self, item_id: str) -> SupplyChainItem:
        """Retrieve an item by its ID."""
        for item in self.items:
            if item.item_id == item_id:
                return item
        raise ValueError(f"Item with ID {item_id} not found.")

    def to_json(self) -> str:
        """Convert the supply chain to a JSON string."""
        return json.dumps([item.to_dict() for item in self.items], indent=4)

def main():
    """Main function to demonstrate the supply chain management system."""
    try:
        supply_chain = SupplyChain()

        # Adding items to the supply chain
        supply_chain.add_item(SupplyChainItem("1", "Widget A", 100, "In Stock"))
        supply_chain.add_item(SupplyChainItem("2", "Widget B", 50, "In Transit"))

        # Updating an item
        supply_chain.update_item("1", 90, "In Stock")

        # Retrieving an item
        item = supply_chain.get_item("1")
        print(f"Retrieved Item: {item.to_dict()}")

        # Output the entire supply chain as JSON
        print("Supply Chain JSON:")
        print(supply_chain.to_json())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
