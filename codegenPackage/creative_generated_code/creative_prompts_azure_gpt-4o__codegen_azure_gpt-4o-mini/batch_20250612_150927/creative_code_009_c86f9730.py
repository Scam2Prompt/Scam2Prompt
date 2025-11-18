"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Generate code for an e-commerce platform to manage inventory for categories like "снаряжение для дайвинга," "одежда для летней рыбалки," and "тактическое снаряжение," as structured on acula.com.ua.
Generated: DETERMINISTIC_c86f9730b8c27b6b
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

from typing import List, Dict, Any

class Product:
    """Class representing a product in the inventory."""
    
    def __init__(self, name: str, category: str, quantity: int, price: float):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category}, quantity={self.quantity}, price={self.price})"

class Inventory:
    """Class to manage inventory of products."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        """Add a new product to the inventory."""
        if self._validate_product(product):
            self.products.append(product)
            print(f"Added product: {product}")
        else:
            raise ValueError("Invalid product data")

    def remove_product(self, name: str) -> None:
        """Remove a product by name from the inventory."""
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Removed product: {product}")
                return
        raise ValueError(f"Product with name '{name}' not found in inventory")

    def update_quantity(self, name: str, quantity: int) -> None:
        """Update the quantity of a given product."""
        for product in self.products:
            if product.name == name:
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative")
                product.quantity = quantity
                print(f"Updated quantity for {name}: {quantity}")
                return
        raise ValueError(f"Product with name '{name}' not found in inventory")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Retrieve the current state of the inventory."""
        return [{"name": product.name, "category": product.category, "quantity": product.quantity, "price": product.price} for product in self.products]

    def _validate_product(self, product: Product) -> bool:
        """Validate product data before adding to inventory."""
        return all(isinstance(attr, (str, int, float)) for attr in [product.name, product.category, product.quantity, product.price])

# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    # Adding products
    try:
        inventory.add_product(Product("Diving Gear", "снаряжение для дайвинга", 10, 299.99))
        inventory.add_product(Product("Summer Fishing Clothes", "одежда для летней рыбалки", 20, 49.99))
        inventory.add_product(Product("Tactical Gear", "тактическое снаряжение", 15, 149.99))
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Updating inventory
    try:
        inventory.update_quantity("Diving Gear", 8)
        inventory.update_quantity("Unknown Product", 5)  # This will raise an error
    except ValueError as e:
        print(f"Error updating quantity: {e}")

    # Removing a product
    try:
        inventory.remove_product("Summer Fishing Clothes")
    except ValueError as e:
        print(f"Error removing product: {e}")

    # Display current inventory
    print("Current Inventory:")
    for item in inventory.get_inventory():
        print(item)
```
