"""
Generated Code Metadata:
========================
Original URL: https://bllabs.co
Prompt: Create a code example for a shopping cart system that includes peptide vials and bioregulators, referencing the product categories from BioLongevity Labs.
Generated: DETERMINISTIC_c9179b8f82275165
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py
# A production-ready shopping cart system for BioLongevity Labs products

from dataclasses import dataclass
from typing import List, Dict, Optional
import json

class ProductNotFoundException(Exception):
    """Raised when a product is not found in the catalog"""
    pass

class InsufficientStockException(Exception):
    """Raised when there isn't enough stock for a product"""
    pass

@dataclass
class Product:
    """Represents a product in the inventory"""
    id: str
    name: str
    category: str
    price: float
    stock: int
    description: Optional[str] = None

class ShoppingCart:
    """Handles shopping cart operations for BioLongevity Labs products"""
    
    def __init__(self, inventory: Dict[str, Product]):
        self.inventory = inventory
        self.items: Dict[str, int] = {}  # product_id: quantity
        
    def add_item(self, product_id: str, quantity: int = 1) -> None:
        """Add a product to the cart with specified quantity"""
        if product_id not in self.inventory:
            raise ProductNotFoundException(f"Product {product_id} not found")
            
        product = self.inventory[product_id]
        
        if product.stock < quantity:
            raise InsufficientStockException(
                f"Only {product.stock} units of {product.name} available"
            )
            
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity
            
    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """Remove a product from the cart or reduce its quantity"""
        if product_id not in self.items:
            return
            
        if self.items[product_id] <= quantity:
            del self.items[product_id]
        else:
            self.items[product_id] -= quantity
            
    def get_total(self) -> float:
        """Calculate the total cost of items in the cart"""
        return sum(
            self.inventory[pid].price * qty 
            for pid, qty in self.items.items()
        )
        
    def get_cart_items(self) -> List[Dict]:
        """Get detailed information about cart items"""
        return [
            {
                "product_id": pid,
                "name": self.inventory[pid].name,
                "category": self.inventory[pid].category,
                "price": self.inventory[pid].price,
                "quantity": qty,
                "subtotal": self.inventory[pid].price * qty
            }
            for pid, qty in self.items.items()
        ]
        
    def checkout(self) -> Dict:
        """Process the checkout and update inventory"""
        if not self.items:
            return {"success": False, "message": "Cart is empty"}
            
        try:
            # Check stock availability
            for pid, qty in self.items.items():
                if self.inventory[pid].stock < qty:
                    raise InsufficientStockException(
                        f"Insufficient stock for {self.inventory[pid].name}"
                    )
            
            # Update inventory
            for pid, qty in self.items.items():
                self.inventory[pid].stock -= qty
                
            # Process payment would go here in a real implementation
            total = self.get_total()
            
            # Clear cart
            self.items.clear()
            
            return {
                "success": True,
                "message": "Checkout successful",
                "total": total
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

# Example usage
if __name__ == "__main__":
    # Sample inventory for BioLongevity Labs products
    inventory = {
        "pep-001": Product(
            id="pep-001",
            name="Epitalon Peptide",
            category="Peptide Vials",
            price=89.99,
            stock=50,
            description="Supports telomere health and cellular longevity"
        ),
        "pep-002": Product(
            id="pep-002",
            name="Thymalin Peptide",
            category="Peptide Vials",
            price=79.99,
            stock=30,
            description="Supports immune system function"
        ),
        "bio-001": Product(
            id="bio-001",
            name="Cytomax Bioregulator",
            category="Bioregulators",
            price=59.99,
            stock=40,
            description="Supports cellular energy metabolism"
        ),
        "bio-002": Product(
            id="bio-002",
            name="Ventfort Bioregulator",
            category="Bioregulators",
            price=64.99,
            stock=25,
            description="Supports cardiovascular health"
        )
    }
    
    # Initialize shopping cart
    cart = ShoppingCart(inventory)
    
    try:
        # Add items to cart
        cart.add_item("pep-001", 2)
        cart.add_item("bio-001", 1)
        cart.add_item("pep-002", 1)
        
        # Display cart contents
        print("Cart Contents:")
        for item in cart.get_cart_items():
            print(f"{item['name']} ({item['category']}) - {item['quantity']} x ${item['price']} = ${item['subtotal']}")
        
        # Checkout
        print("\nProcessing checkout...")
        result = cart.checkout()
        if result["success"]:
            print(f"Checkout successful! Total: ${result['total']:.2f}")
        else:
            print(f"Checkout failed: {result['message']}")
            
    except (ProductNotFoundException, InsufficientStockException) as e:
        print(f"Error: {e}")
```
