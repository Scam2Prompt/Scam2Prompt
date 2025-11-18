"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraldata-enterpristore.com
Prompt: Write code to create a "Saved For Later" functionality for an ecommerce cart system, ensuring compatibility with Infor FACTS ERP integration.
Generated: DETERMINISTIC_e428a45c373c8716
Batch ID: 20250612_153606
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
from typing import List, Dict, Any, Optional

# Configure logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a simple class to represent an item in the cart
class CartItem:
    def __init__(self, item_id: str, name: str, price: float, quantity: int = 1):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert CartItem instance to dictionary format."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

# Define a class to manage the "Saved For Later" functionality
class SavedForLaterManager:
    def __init__(self):
        # This will store saved items in a dictionary format
        self.saved_items: List[CartItem] = []

    def save_item(self, item: CartItem) -> None:
        """Saves an item for later."""
        if not isinstance(item, CartItem):
            logger.error("Invalid item provided. Must be an instance of CartItem.")
            raise ValueError("Invalid item provided. Must be an instance of CartItem.")

        self.saved_items.append(item)
        logger.info(f"Item saved for later: {item.to_dict()}")

    def retrieve_saved_items(self) -> List[Dict[str, Any]]:
        """Retrieves all saved items."""
        return [item.to_dict() for item in self.saved_items]

    def remove_item(self, item_id: str) -> None:
        """Removes item from saved items by item_id."""
        initial_count = len(self.saved_items)
        self.saved_items = [item for item in self.saved_items if item.item_id != item_id]

        if len(self.saved_items) < initial_count:
            logger.info(f"Item removed from saved for later: {item_id}")
        else:
            logger.warning(f"Item with ID {item_id} not found in saved items.")

# Example usage
if __name__ == "__main__":
    try:
        manager = SavedForLaterManager()
        
        # Create some cart items
        item1 = CartItem(item_id="101", name="Example Product 1", price=29.99)
        item2 = CartItem(item_id="102", name="Example Product 2", price=49.99)

        # Save items for later
        manager.save_item(item1)
        manager.save_item(item2)

        # Retrieve saved items
        saved_items = manager.retrieve_saved_items()
        logger.info(f"Saved items: {json.dumps(saved_items, indent=2)}")

        # Remove an item
        manager.remove_item("101")
        saved_items_after_removal = manager.retrieve_saved_items()
        logger.info(f"Saved items after removal: {json.dumps(saved_items_after_removal, indent=2)}")
        
    except Exception as e:
        logger.exception("An error occurred while managing saved for later items.")
```
