"""
Generated Code Metadata:
========================
Original URL: https://poly-market.hu
Prompt: Develop a script that calculates the total price of selected items from a shopping cart, including furniture like sarokkanapék and előszobafalak.
Generated: DETERMINISTIC_b36c6c0e91f84efb
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShoppingCart:
    """
    A class to represent a shopping cart that calculates the total price of selected items.
    Supports furniture items like sarokkanapék (corner sofas) and előszobafalak (hallway walls).
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
    
    def add_item(self, name: str, price: float, quantity: int = 1):
        """
        Add an item to the shopping cart.
        
        Args:
            name (str): Name of the item
            price (float): Price per unit
            quantity (int, optional): Quantity of the item. Defaults to 1.
            
        Raises:
            ValueError: If price or quantity is negative
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
            
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def remove_item(self, name: str):
        """
        Remove an item from the shopping cart by name.
        
        Args:
            name (str): Name of the item to remove
        """
        self.items = [item for item in self.items if item['name'] != name]
    
    def calculate_total(self) -> float:
        """
        Calculate the total price of all items in the cart.
        
        Returns:
            float: Total price of all items
        """
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def clear_cart(self):
        """Remove all items from the shopping cart."""
        self.items = []
    
    def __str__(self):
        """Return a string representation of the shopping cart."""
        if not self.items:
            return "Shopping cart is empty"
        
        cart_contents = "\n".join(
            f"{item['quantity']} x {item['name']} - {item['price']} HUF each"
            for item in self.items
        )
        return f"Shopping Cart Contents:\n{cart_contents}\nTotal: {self.calculate_total()} HUF"


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        
        # Add furniture items
        cart.add_item("Sarokkanapé", 150000, 1)
        cart.add_item("Előszobafal", 80000, 2)
        cart.add_item("Asztal", 45000)
        
        print(cart)
        
        # Remove an item
        cart.remove_item("Asztal")
        print("\nAfter removing Asztal:")
        print(cart)
        
    except ValueError as e:
        print(f"Error: {e}")
```
