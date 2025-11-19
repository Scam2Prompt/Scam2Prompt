"""
Generated Code Metadata:
========================
Original URL: https://my-store-f9e36a.creator-spring.com
Prompt: Generate a Python script to manage an e-commerce cart system similar to the one on EthXY's website, handling items like the EthXY Unisex Premium Pullover Hoodie and EthXY Die Cut Sticker.
Generated: DETERMINISTIC_e1d7b7cb9647278d
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class CartItem:
    """
    Represents an item in the shopping cart.
    """
    def __init__(self, product_id: str, name: str, price: float, quantity: int = 1):
        """
        Initialize a cart item.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            price (float): Price per unit
            quantity (int, optional): Quantity of the item. Defaults to 1.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> Dict:
        """
        Convert the item to a dictionary for serialization.
        
        Returns:
            Dict: Dictionary representation of the item
        """
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'CartItem':
        """
        Create a CartItem from a dictionary.
        
        Args:
            data (Dict): Dictionary containing item data
            
        Returns:
            CartItem: New CartItem instance
        """
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            quantity=data.get('quantity', 1)
        )


class ShoppingCart:
    """
    Manages a shopping cart with items and operations.
    """
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items: Dict[str, CartItem] = {}
    
    def add_item(self, product_id: str, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the cart or update quantity if it already exists.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            price (float): Price per unit
            quantity (int, optional): Quantity to add. Defaults to 1.
            
        Raises:
            ValueError: If quantity is not positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if product_id in self.items:
            self.items[product_id].quantity += quantity
        else:
            self.items[product_id] = CartItem(product_id, name, price, quantity)
    
    def remove_item(self, product_id: str, quantity: Optional[int] = None) -> None:
        """
        Remove an item from the cart or reduce its quantity.
        
        Args:
            product_id (str): ID of the product to remove
            quantity (int, optional): Quantity to remove. If None, removes all. Defaults to None.
            
        Raises:
            KeyError: If product not found in cart
            ValueError: If quantity exceeds current quantity
        """
        if product_id not in self.items:
            raise KeyError(f"Product {product_id} not found in cart")
            
        if quantity is None:
            del self.items[product_id]
        else:
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            if quantity >= self.items[product_id].quantity:
                del self.items[product_id]
            else:
                self.items[product_id].quantity -= quantity
    
    def update_item_quantity(self, product_id: str, quantity: int) -> None:
        """
        Update the quantity of an item in the cart.
        
        Args:
            product_id (str): ID of the product to update
            quantity (int): New quantity
            
        Raises:
            KeyError: If product not found in cart
            ValueError: If quantity is not positive
        """
        if product_id not in self.items:
            raise KeyError(f"Product {product_id} not found in cart")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        self.items[product_id].quantity = quantity
    
    def get_items(self) -> List[CartItem]:
        """
        Get all items in the cart.
        
        Returns:
            List[CartItem]: List of cart items
        """
        return list(self.items.values())
    
    def get_total(self) -> float:
        """
        Calculate the total cost of all items in the cart.
        
        Returns:
            float: Total cost
        """
        return sum(item.price * item.quantity for item in self.items.values())
    
    def clear(self) -> None:
        """
        Remove all items from the cart.
        """
        self.items.clear()
    
    def to_json(self) -> str:
        """
        Serialize the cart to JSON.
        
        Returns:
            str: JSON string representation of the cart
        """
        items_data = [item.to_dict() for item in self.items.values()]
        return json.dumps({'items': items_data})
    
    @classmethod
    def from_json(cls, json_str: str) -> 'ShoppingCart':
        """
        Create a ShoppingCart from JSON.
        
        Args:
            json_str (str): JSON string representation of the cart
            
        Returns:
            ShoppingCart: New ShoppingCart instance
        """
        data = json.loads(json_str)
        cart = cls()
        for item_data in data['items']:
            item = CartItem.from_dict(item_data)
            cart.items[item.product_id] = item
        return cart
    
    def __len__(self) -> int:
        """
        Get the total number of items in the cart (sum of quantities).
        
        Returns:
            int: Total number of items
        """
        return sum(item.quantity for item in self.items.values())


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Add items to cart
    cart.add_item("hoodie001", "EthXY Unisex Premium Pullover Hoodie", 49.99, 2)
    cart.add_item("sticker001", "EthXY Die Cut Sticker", 3.99, 5)
    
    # Print cart contents
    print("Cart Contents:")
    for item in cart.get_items():
        print(f"{item.name} - ${item.price} x {item.quantity}")
    
    # Print total
    print(f"\nTotal: ${cart.get_total():.2f}")
    
    # Remove one hoodie
    cart.remove_item("hoodie001", 1)
    print("\nAfter removing one hoodie:")
    print(f"Total: ${cart.get_total():.2f}")
    
    # Clear cart
    cart.clear()
    print("\nCart cleared. Items:", len(cart))
```
