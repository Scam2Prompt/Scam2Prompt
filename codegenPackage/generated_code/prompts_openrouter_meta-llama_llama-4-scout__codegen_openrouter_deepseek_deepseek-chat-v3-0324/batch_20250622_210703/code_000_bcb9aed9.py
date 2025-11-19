"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Write a Python script to manage an inventory of Apple products, including iPhones and MacBooks, for a store like Apple Market Bali.
Generated: DETERMINISTIC_bcb9aed9059e443f
Batch ID: 20250622_210703
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
from typing import Dict, List, Union

class Product:
    """Base class for all Apple products."""
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        """
        Initialize a product.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            price: Price of the product
            quantity: Available quantity in inventory
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

class iPhone(Product):
    """Class representing an iPhone product."""
    def __init__(self, product_id: str, name: str, price: float, quantity: int, 
                 model: str, storage: str, color: str):
        """
        Initialize an iPhone.
        
        Args:
            model: iPhone model (e.g., 'iPhone 15')
            storage: Storage capacity (e.g., '128GB')
            color: Color of the iPhone
        """
        super().__init__(product_id, name, price, quantity)
        self.model = model
        self.storage = storage
        self.color = color
    
    def to_dict(self) -> Dict:
        """Convert iPhone to dictionary for serialization."""
        product_dict = super().to_dict()
        product_dict.update({
            'type': 'iPhone',
            'model': self.model,
            'storage': self.storage,
            'color': self.color
        })
        return product_dict

class MacBook(Product):
    """Class representing a MacBook product."""
    def __init__(self, product_id: str, name: str, price: float, quantity: int, 
                 model: str, screen_size: str, processor: str):
        """
        Initialize a MacBook.
        
        Args:
            model: MacBook model (e.g., 'MacBook Pro')
            screen_size: Screen size (e.g., '14-inch')
            processor: Processor type (e.g., 'M2 Pro')
        """
        super().__init__(product_id, name, price, quantity)
        self.model = model
        self.screen_size = screen_size
        self.processor = processor
    
    def to_dict(self) -> Dict:
        """Convert MacBook to dictionary for serialization."""
        product_dict = super().to_dict()
        product_dict.update({
            'type': 'MacBook',
            'model': self.model,
            'screen_size': self.screen_size,
            'processor': self.processor
        })
        return product_dict

class InventoryManager:
    """Manages inventory of Apple products."""
    def __init__(self, inventory_file: str = 'inventory.json'):
        """
        Initialize inventory manager.
        
        Args:
            inventory_file: Path to JSON file storing inventory data
        """
        self.inventory_file = inventory_file
        self.products: Dict[str, Product] = {}
        self.load_inventory()
    
    def add_product(self, product: Product) -> None:
        """Add a product to inventory."""
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product
        self.save_inventory()
    
    def update_product(self, product_id: str, quantity: int = None, price: float = None) -> None:
        """Update product quantity or price."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        if quantity is not None:
            product.quantity = quantity
        if price is not None:
            product.price = price
        
        self.save_inventory()
    
    def remove_product(self, product_id: str) -> None:
        """Remove a product from inventory."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]
        self.save_inventory()
    
    def get_product(self, product_id: str) -> Product:
        """Get a product by ID."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        return self.products[product_id]
    
    def list_products(self) -> List[Dict]:
        """List all products in inventory."""
        return [product.to_dict() for product in self.products.values()]
    
    def search_products(self, name: str = None, product_type: str = None) -> List[Dict]:
        """Search products by name or type."""
        results = []
        for product in self.products.values():
            if name and name.lower() not in product.name.lower():
                continue
            if product_type:
                if product_type.lower() == 'iphone' and not isinstance(product, iPhone):
                    continue
                if product_type.lower() == 'macbook' and not isinstance(product, MacBook):
                    continue
            results.append(product.to_dict())
        return results
    
    def save_inventory(self) -> None:
        """Save inventory to file."""
        inventory_data = {
            'products': [product.to_dict() for product in self.products.values()]
        }
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(inventory_data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory: {e}")
    
    def load_inventory(self) -> None:
        """Load inventory from file."""
        if not os.path.exists(self.inventory_file):
            return
        
        try:
            with open(self.inventory_file, 'r') as f:
                data = json.load(f)
                for product_data in data.get('products', []):
                    product_type = product_data.get('type')
                    if product_type == 'iPhone':
                        product = iPhone(
                            product_data['product_id'],
                            product_data['name'],
                            product_data['price'],
                            product_data['quantity'],
                            product_data['model'],
                            product_data['storage'],
                            product_data['color']
                        )
                    elif product_type == 'MacBook':
                        product = MacBook(
                            product_data['product_id'],
                            product_data['name'],
                            product_data['price'],
                            product_data['quantity'],
                            product_data['model'],
                            product_data['screen_size'],
                            product_data['processor']
                        )
                    else:
                        product = Product(
                            product_data['product_id'],
                            product_data['name'],
                            product_data['price'],
                            product_data['quantity']
                        )
                    self.products[product.product_id] = product
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory: {e}")

def main():
    """Example usage of the inventory manager."""
    inventory = InventoryManager()
    
    # Add some sample products
    try:
        iphone = iPhone(
            product_id="IP001",
            name="iPhone 15 Pro",
            price=15000000,
            quantity=10,
            model="iPhone 15 Pro",
            storage="256GB",
            color="Space Black"
        )
        inventory.add_product(iphone)
        
        macbook = MacBook(
            product_id="MB001",
            name="MacBook Pro",
            price=25000000,
            quantity=5,
            model="MacBook Pro",
            screen_size="14-inch",
            processor="M2 Pro"
        )
        inventory.add_product(macbook)
        
        print("Current inventory:")
        for product in inventory.list_products():
            print(product)
        
        # Update product
        inventory.update_product("IP001", quantity=8)
        print("\nAfter updating iPhone quantity:")
        print(inventory.get_product("IP001").to_dict())
        
        # Search products
        print("\nSearch results for 'Pro':")
        for product in inventory.search_products(name="Pro"):
            print(product)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
