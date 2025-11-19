"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Write a Python script to manage an inventory of hair care products, including tracking stock levels and product prices, inspired by the product offerings on Zento Cosmetic.
Generated: DETERMINISTIC_d6e73d91147d11de
Batch ID: 20250622_205514
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

class HairCareProduct:
    """Class representing a hair care product."""
    
    def __init__(self, product_id: str, name: str, price: float, stock: int, category: str):
        """
        Initialize a hair care product.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            price: Price of the product
            stock: Current stock quantity
            category: Product category (e.g., shampoo, conditioner)
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'category': self.category
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'HairCareProduct':
        """Create product from dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            stock=data['stock'],
            category=data['category']
        )

class InventoryManager:
    """Class to manage hair care product inventory."""
    
    def __init__(self, data_file: str = 'inventory.json'):
        """
        Initialize inventory manager.
        
        Args:
            data_file: Path to JSON file for storing inventory data
        """
        self.data_file = data_file
        self.products: Dict[str, HairCareProduct] = {}
        self.load_inventory()
    
    def add_product(self, product: HairCareProduct) -> None:
        """
        Add a new product to inventory.
        
        Args:
            product: HairCareProduct instance to add
        """
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product
        self.save_inventory()
    
    def update_product(self, product_id: str, **kwargs) -> None:
        """
        Update product attributes.
        
        Args:
            product_id: ID of product to update
            kwargs: Attributes to update (name, price, stock, category)
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        
        self.save_inventory()
    
    def remove_product(self, product_id: str) -> None:
        """
        Remove product from inventory.
        
        Args:
            product_id: ID of product to remove
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        del self.products[product_id]
        self.save_inventory()
    
    def get_product(self, product_id: str) -> Optional[HairCareProduct]:
        """
        Get product by ID.
        
        Args:
            product_id: ID of product to retrieve
        
        Returns:
            HairCareProduct instance or None if not found
        """
        return self.products.get(product_id)
    
    def list_products(self, category: Optional[str] = None) -> List[HairCareProduct]:
        """
        List all products, optionally filtered by category.
        
        Args:
            category: Optional category filter
        
        Returns:
            List of HairCareProduct instances
        """
        if category:
            return [p for p in self.products.values() if p.category.lower() == category.lower()]
        return list(self.products.values())
    
    def restock_product(self, product_id: str, quantity: int) -> None:
        """
        Restock a product by adding to its current stock.
        
        Args:
            product_id: ID of product to restock
            quantity: Amount to add to current stock
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive")
        
        self.products[product_id].stock += quantity
        self.save_inventory()
    
    def sell_product(self, product_id: str, quantity: int) -> float:
        """
        Sell a product and update stock.
        
        Args:
            product_id: ID of product to sell
            quantity: Quantity sold
        
        Returns:
            Total price of the sale
        
        Raises:
            ValueError: If product not found or insufficient stock
        """
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        if quantity <= 0:
            raise ValueError("Sale quantity must be positive")
        if self.products[product_id].stock < quantity:
            raise ValueError("Insufficient stock")
        
        product = self.products[product_id]
        product.stock -= quantity
        self.save_inventory()
        return product.price * quantity
    
    def save_inventory(self) -> None:
        """Save inventory to JSON file."""
        data = {
            'products': [product.to_dict() for product in self.products.values()]
        }
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory: {str(e)}")
    
    def load_inventory(self) -> None:
        """Load inventory from JSON file."""
        if not os.path.exists(self.data_file):
            return
        
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.products = {
                    p['product_id']: HairCareProduct.from_dict(p)
                    for p in data.get('products', [])
                }
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load inventory: {str(e)}")

def main():
    """Example usage of the inventory management system."""
    manager = InventoryManager()
    
    # Example products
    shampoo = HairCareProduct(
        product_id="SH100",
        name="Hydrating Shampoo",
        price=12.99,
        stock=50,
        category="shampoo"
    )
    
    conditioner = HairCareProduct(
        product_id="CO200",
        name="Repairing Conditioner",
        price=14.99,
        stock=30,
        category="conditioner"
    )
    
    # Add products
    try:
        manager.add_product(shampoo)
        manager.add_product(conditioner)
    except ValueError as e:
        print(f"Error adding product: {e}")
    
    # List all products
    print("All Products:")
    for product in manager.list_products():
        print(f"{product.name} - ${product.price} ({product.stock} in stock)")
    
    # Sell some products
    try:
        total = manager.sell_product("SH100", 2)
        print(f"Sold 2 shampoos for ${total:.2f}")
    except ValueError as e:
        print(f"Error selling product: {e}")
    
    # Restock a product
    try:
        manager.restock_product("CO200", 10)
        print("Restocked conditioner")
    except ValueError as e:
        print(f"Error restocking product: {e}")
    
    # Get product details
    product = manager.get_product("SH100")
    if product:
        print(f"Product details: {product.name}, ${product.price}, {product.stock} left")

if __name__ == "__main__":
    main()
```
