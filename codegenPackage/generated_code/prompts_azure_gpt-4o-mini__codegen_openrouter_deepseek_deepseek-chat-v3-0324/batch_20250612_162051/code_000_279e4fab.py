"""
Generated Code Metadata:
========================
Original URL: https://www.matinshop.dk
Prompt: Generate a code snippet to integrate a shopping cart feature for hair and beard care products similar to those offered by Matin Shop.
Generated: DETERMINISTIC_279e4fab8de5c0ed
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Product:
    """Represents a hair or beard care product."""
    id: str
    name: str
    price: float
    description: str
    category: str  # e.g., 'hair', 'beard'
    stock: int

@dataclass
class CartItem:
    """Represents an item in the shopping cart."""
    product: Product
    quantity: int

class ShoppingCart:
    """Manages the shopping cart operations."""
    
    def __init__(self):
        self.items: List[CartItem] = []
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Adds a product to the cart or updates its quantity if already present.
        
        Args:
            product: The product to add.
            quantity: The quantity to add (default: 1).
            
        Raises:
            ValueError: If quantity is <= 0 or product is out of stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if product.stock <= 0:
            raise ValueError("Product is out of stock.")
        if quantity > product.stock:
            raise ValueError("Not enough stock available.")
            
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                return
                
        self.items.append(CartItem(product=product, quantity=quantity))
    
    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """Removes a product from the cart or reduces its quantity.
        
        Args:
            product_id: The ID of the product to remove.
            quantity: The quantity to remove (default: 1).
            
        Raises:
            ValueError: If product not found or invalid quantity.
        """
        for index, item in enumerate(self.items):
            if item.product.id == product_id:
                if quantity <= 0:
                    raise ValueError("Quantity must be positive.")
                if quantity >= item.quantity:
                    self.items.pop(index)
                else:
                    item.quantity -= quantity
                return
        raise ValueError("Product not found in cart.")
    
    def update_item_quantity(self, product_id: str, new_quantity: int) -> None:
        """Updates the quantity of a product in the cart.
        
        Args:
            product_id: The ID of the product to update.
            new_quantity: The new quantity.
            
        Raises:
            ValueError: If product not found or invalid quantity.
        """
        if new_quantity <= 0:
            raise ValueError("Quantity must be positive.")
            
        for item in self.items:
            if item.product.id == product_id:
                if new_quantity > item.product.stock:
                    raise ValueError("Not enough stock available.")
                item.quantity = new_quantity
                return
        raise ValueError("Product not found in cart.")
    
    def clear_cart(self) -> None:
        """Removes all items from the cart."""
        self.items.clear()
    
    def get_total(self) -> float:
        """Calculates the total cost of items in the cart.
        
        Returns:
            The total cost as a float.
        """
        return sum(item.product.price * item.quantity for item in self.items)
    
    def get_item_count(self) -> int:
        """Gets the total number of items in the cart.
        
        Returns:
            The total quantity of items.
        """
        return sum(item.quantity for item in self.items)
    
    def get_cart_summary(self) -> List[Dict[str, any]]:
        """Gets a summary of the cart items.
        
        Returns:
            A list of dictionaries containing item details.
        """
        return [
            {
                "id": item.product.id,
                "name": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity,
                "subtotal": item.product.price * item.quantity
            }
            for item in self.items
        ]

# Example usage
if __name__ == "__main__":
    # Sample products
    products = [
        Product(
            id="prod1",
            name="Beard Oil",
            price=24.99,
            description="Nourishing oil for beard care",
            category="beard",
            stock=50
        ),
        Product(
            id="prod2",
            name="Shampoo",
            price=19.99,
            description="Gentle cleansing shampoo",
            category="hair",
            stock=30
        )
    ]
    
    # Create cart and add items
    cart = ShoppingCart()
    try:
        cart.add_item(products[0], 2)
        cart.add_item(products[1], 1)
        
        # Print cart summary
        print("Cart Summary:")
        for item in cart.get_cart_summary():
            print(f"{item['name']} x{item['quantity']} - ${item['subtotal']:.2f}")
        
        print(f"Total: ${cart.get_total():.2f}")
        print(f"Item Count: {cart.get_item_count()}")
        
        # Update quantity
        cart.update_item_quantity("prod1", 1)
        print("\nAfter updating quantity:")
        print(f"Total: ${cart.get_total():.2f}")
        
        # Remove item
        cart.remove_item("prod2")
        print("\nAfter removing shampoo:")
        print(f"Total: ${cart.get_total():.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
