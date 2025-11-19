"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: "Write a Python code to manage inventory of confectionery products like sugar boiled candies, toffees, and lollipops for a company like Jai Gurudev Industries."
Generated: DETERMINISTIC_711a5e31eec9c938
Batch ID: 20250622_204841
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
from typing import Dict, List, Optional

class ConfectioneryProduct:
    """Class representing a confectionery product in inventory."""
    
    def __init__(self, product_id: str, name: str, category: str, 
                 quantity: int, price_per_unit: float):
        """Initialize a confectionery product.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            category: Type of product (e.g., sugar boiled candy, toffee, lollipop)
            quantity: Current stock quantity
            price_per_unit: Price per unit in INR
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price_per_unit = price_per_unit
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity,
            'price_per_unit': self.price_per_unit
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ConfectioneryProduct':
        """Create product from dictionary."""
        return cls(
            data['product_id'],
            data['name'],
            data['category'],
            data['quantity'],
            data['price_per_unit']
        )

class InventoryManager:
    """Class to manage confectionery inventory operations."""
    
    def __init__(self, inventory_file: str = 'inventory.json'):
        """Initialize inventory manager.
        
        Args:
            inventory_file: Path to JSON file storing inventory data
        """
        self.inventory_file = inventory_file
        self.products: Dict[str, ConfectioneryProduct] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """Load inventory data from JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as file:
                    data = json.load(file)
                    self.products = {
                        pid: ConfectioneryProduct.from_dict(product_data) 
                        for pid, product_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading inventory: {e}")
    
    def save_inventory(self) -> None:
        """Save inventory data to JSON file."""
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(
                    {pid: product.to_dict() for pid, product in self.products.items()},
                    file,
                    indent=4
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_product(self, product: ConfectioneryProduct) -> None:
        """Add a new product to inventory.
        
        Args:
            product: Product to add
        """
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product
        self.save_inventory()
    
    def update_product_quantity(self, product_id: str, quantity_change: int) -> None:
        """Update product quantity in inventory.
        
        Args:
            product_id: ID of product to update
            quantity_change: Amount to add/subtract from current quantity
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        new_quantity = self.products[product_id].quantity + quantity_change
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        self.products[product_id].quantity = new_quantity
        self.save_inventory()
    
    def remove_product(self, product_id: str) -> None:
        """Remove product from inventory.
        
        Args:
            product_id: ID of product to remove
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]
        self.save_inventory()
    
    def get_product(self, product_id: str) -> Optional[ConfectioneryProduct]:
        """Get product by ID.
        
        Args:
            product_id: ID of product to retrieve
            
        Returns:
            Product if found, None otherwise
        """
        return self.products.get(product_id)
    
    def list_products(self) -> List[ConfectioneryProduct]:
        """List all products in inventory.
        
        Returns:
            List of all products
        """
        return list(self.products.values())
    
    def get_products_by_category(self, category: str) -> List[ConfectioneryProduct]:
        """Get products filtered by category.
        
        Args:
            category: Category to filter by
            
        Returns:
            List of products in specified category
        """
        return [
            product for product in self.products.values() 
            if product.category.lower() == category.lower()
        ]

def main_menu() -> None:
    """Display main menu and handle user input."""
    manager = InventoryManager()
    
    while True:
        print("\nJai Gurudev Industries - Confectionery Inventory Management")
        print("1. Add Product")
        print("2. Update Product Quantity")
        print("3. Remove Product")
        print("4. View Product Details")
        print("5. List All Products")
        print("6. List Products by Category")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        try:
            if choice == '1':
                add_product_menu(manager)
            elif choice == '2':
                update_quantity_menu(manager)
            elif choice == '3':
                remove_product_menu(manager)
            elif choice == '4':
                view_product_menu(manager)
            elif choice == '5':
                list_products_menu(manager)
            elif choice == '6':
                list_by_category_menu(manager)
            elif choice == '7':
                print("Exiting inventory management system.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except Exception as e:
            print(f"Error: {e}")

def add_product_menu(manager: InventoryManager) -> None:
    """Handle product addition."""
    print("\nAdd New Product")
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    category = input("Enter product category (candy/toffee/lollipop): ")
    quantity = int(input("Enter initial quantity: "))
    price = float(input("Enter price per unit (INR): "))
    
    product = ConfectioneryProduct(product_id, name, category, quantity, price)
    manager.add_product(product)
    print("Product added successfully!")

def update_quantity_menu(manager: InventoryManager) -> None:
    """Handle quantity updates."""
    print("\nUpdate Product Quantity")
    product_id = input("Enter product ID: ")
    change = int(input("Enter quantity change (+/-): "))
    
    manager.update_product_quantity(product_id, change)
    print("Quantity updated successfully!")

def remove_product_menu(manager: InventoryManager) -> None:
    """Handle product removal."""
    print("\nRemove Product")
    product_id = input("Enter product ID to remove: ")
    
    manager.remove_product(product_id)
    print("Product removed successfully!")

def view_product_menu(manager: InventoryManager) -> None:
    """Display product details."""
    print("\nView Product Details")
    product_id = input("Enter product ID: ")
    
    product = manager.get_product(product_id)
    if product:
        print("\nProduct Details:")
        print(f"ID: {product.product_id}")
        print(f"Name: {product.name}")
        print(f"Category: {product.category}")
        print(f"Quantity: {product.quantity}")
        print(f"Price per unit: ₹{product.price_per_unit:.2f}")
    else:
        print("Product not found.")

def list_products_menu(manager: InventoryManager) -> None:
    """List all products."""
    print("\nAll Products in Inventory:")
    products = manager.list_products()
    if not products:
        print("No products in inventory.")
        return
    
    for product in products:
        print(f"{product.product_id}: {product.name} ({product.category}) - "
              f"Qty: {product.quantity}, Price: ₹{product.price_per_unit:.2f}")

def list_by_category_menu(manager: InventoryManager) -> None:
    """List products by category."""
    print("\nList Products by Category")
    category = input("Enter category (candy/toffee/lollipop): ")
    
    products = manager.get_products_by_category(category)
    if not products:
        print(f"No products found in category '{category}'.")
        return
    
    print(f"\nProducts in category '{category}':")
    for product in products:
        print(f"{product.product_id}: {product.name} - "
              f"Qty: {product.quantity}, Price: ₹{product.price_per_unit:.2f}")

if __name__ == "__main__":
    main_menu()
```
