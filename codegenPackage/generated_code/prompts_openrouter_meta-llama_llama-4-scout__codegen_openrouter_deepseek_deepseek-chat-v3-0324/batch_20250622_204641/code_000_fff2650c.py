"""
Generated Code Metadata:
========================
Original URL: https://mixpelinfobrazz.blogspot.com
Prompt: Write a Python code snippet to manage an e-commerce inventory system for computer hardware products like SSDs, Pen Drives, and USB mice.
Generated: DETERMINISTIC_fff2650c98988f6c
Batch ID: 20250622_204641
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional, Union

class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, category: str, price: float, quantity: int):
        """Initialize a product with given attributes.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            category: Category of the product (e.g., SSD, Pen Drive)
            price: Price of the product
            quantity: Available quantity in stock
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
    
    def to_dict(self) -> Dict[str, Union[str, float, int]]:
        """Convert product to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, float, int]]) -> 'Product':
        """Create a Product instance from a dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            category=data['category'],
            price=data['price'],
            quantity=data['quantity']
        )

class InventoryManager:
    """Manages the inventory of computer hardware products."""
    
    def __init__(self, file_path: str = 'inventory.json'):
        """Initialize the inventory manager.
        
        Args:
            file_path: Path to the JSON file storing inventory data
        """
        self.file_path = file_path
        self.products: Dict[str, Product] = {}
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load inventory data from the JSON file."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    for product_data in data.values():
                        product = Product.from_dict(product_data)
                        self.products[product.product_id] = product
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading inventory: {e}")
    
    def _save_inventory(self) -> None:
        """Save inventory data to the JSON file."""
        try:
            data = {pid: product.to_dict() for pid, product in self.products.items()}
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")
    
    def add_product(self, product_id: str, name: str, category: str, price: float, quantity: int) -> bool:
        """Add a new product to the inventory.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            category: Category of the product
            price: Price of the product
            quantity: Initial quantity in stock
            
        Returns:
            True if product was added successfully, False otherwise
        """
        if product_id in self.products:
            print(f"Product with ID {product_id} already exists.")
            return False
        
        if price <= 0 or quantity < 0:
            print("Price must be positive and quantity must be non-negative.")
            return False
        
        self.products[product_id] = Product(product_id, name, category, price, quantity)
        self._save_inventory()
        return True
    
    def update_product_quantity(self, product_id: str, quantity: int) -> bool:
        """Update the quantity of a product.
        
        Args:
            product_id: ID of the product to update
            quantity: New quantity (positive for addition, negative for removal)
            
        Returns:
            True if update was successful, False otherwise
        """
        if product_id not in self.products:
            print(f"Product with ID {product_id} not found.")
            return False
        
        new_quantity = self.products[product_id].quantity + quantity
        if new_quantity < 0:
            print("Cannot have negative quantity.")
            return False
        
        self.products[product_id].quantity = new_quantity
        self._save_inventory()
        return True
    
    def remove_product(self, product_id: str) -> bool:
        """Remove a product from the inventory.
        
        Args:
            product_id: ID of the product to remove
            
        Returns:
            True if product was removed successfully, False otherwise
        """
        if product_id not in self.products:
            print(f"Product with ID {product_id} not found.")
            return False
        
        del self.products[product_id]
        self._save_inventory()
        return True
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by its ID.
        
        Args:
            product_id: ID of the product to retrieve
            
        Returns:
            The Product object if found, None otherwise
        """
        return self.products.get(product_id)
    
    def list_products(self, category: Optional[str] = None) -> List[Product]:
        """List all products or filter by category.
        
        Args:
            category: Optional category filter
            
        Returns:
            List of Product objects matching the filter
        """
        if category:
            return [p for p in self.products.values() if p.category.lower() == category.lower()]
        return list(self.products.values())
    
    def check_stock(self, product_id: str, requested_quantity: int) -> bool:
        """Check if sufficient stock is available for a product.
        
        Args:
            product_id: ID of the product to check
            requested_quantity: Quantity needed
            
        Returns:
            True if sufficient stock is available, False otherwise
        """
        product = self.get_product(product_id)
        if not product:
            print(f"Product with ID {product_id} not found.")
            return False
        return product.quantity >= requested_quantity

# Example usage
if __name__ == "__main__":
    inventory = InventoryManager()
    
    # Add some sample products
    inventory.add_product("SSD001", "Samsung 1TB SSD", "SSD", 129.99, 50)
    inventory.add_product("PEN001", "SanDisk 64GB Pen Drive", "Pen Drive", 19.99, 100)
    inventory.add_product("USB001", "Logitech USB Mouse", "USB Mouse", 24.99, 30)
    
    # List all products
    print("All Products:")
    for product in inventory.list_products():
        print(f"{product.name} - ${product.price} - Qty: {product.quantity}")
    
    # List products in a specific category
    print("\nSSD Products:")
    for product in inventory.list_products("SSD"):
        print(f"{product.name} - ${product.price} - Qty: {product.quantity}")
    
    # Update product quantity
    inventory.update_product_quantity("SSD001", -10)  # Remove 10 units
    updated_product = inventory.get_product("SSD001")
    print(f"\nUpdated SSD quantity: {updated_product.quantity}")
    
    # Check stock
    print(f"\nStock check (SSD001, 50): {inventory.check_stock('SSD001', 50)}")
    print(f"Stock check (SSD001, 30): {inventory.check_stock('SSD001', 30)}")
```
