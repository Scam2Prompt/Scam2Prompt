"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code that simulates adding items like "XÍCARA DE CHÁ PEARL 180ML" to a shopping cart and calculates the total price, referencing the e-commerce structure of the "asacanelbrazzz" website.
Generated: DETERMINISTIC_7e627e8db337fda2
Batch ID: 20250612_145249
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
    A class to simulate a shopping cart for an e-commerce website.
    Handles adding items, removing items, and calculating the total price.
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []
    
    def add_item(self, name: str, price: float, quantity: int = 1):
        """
        Add an item to the shopping cart.
        
        Args:
            name (str): The name of the item (e.g., "XÍCARA DE CHÁ PEARL 180ML").
            price (float): The price of the item.
            quantity (int, optional): The quantity to add. Defaults to 1.
            
        Raises:
            ValueError: If price or quantity is not positive.
        """
        if price <= 0:
            raise ValueError("Price must be positive.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
            
        # Check if item already exists in cart
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                return
        
        # Add new item
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def remove_item(self, name: str, quantity: int = 1):
        """
        Remove an item from the shopping cart.
        
        Args:
            name (str): The name of the item to remove.
            quantity (int, optional): The quantity to remove. Defaults to 1.
            
        Raises:
            ValueError: If item is not found or quantity is invalid.
        """
        for item in self.items:
            if item['name'] == name:
                if quantity <= 0:
                    raise ValueError("Quantity must be positive.")
                if quantity >= item['quantity']:
                    self.items.remove(item)
                else:
                    item['quantity'] -= quantity
                return
        raise ValueError(f"Item '{name}' not found in cart.")
    
    def calculate_total(self) -> float:
        """
        Calculate the total price of all items in the cart.
        
        Returns:
            float: The total price.
        """
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def clear_cart(self):
        """Remove all items from the cart."""
        self.items = []
    
    def get_cart_items(self) -> list:
        """
        Get a list of all items in the cart.
        
        Returns:
            list: A list of dictionaries representing cart items.
        """
        return self.items.copy()


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Add items to cart
    try:
        cart.add_item("XÍCARA DE CHÁ PEARL 180ML", 29.90, 2)
        cart.add_item("POTE HERMÉTICO 500ML", 19.90)
        cart.add_item("COLHER DE SILICONE", 9.90, 3)
    except ValueError as e:
        print(f"Error adding item: {e}")
    
    # Display cart items
    print("Cart Items:")
    for item in cart.get_cart_items():
        print(f"{item['name']} - R${item['price']:.2f} x {item['quantity']}")
    
    # Calculate and display total
    total = cart.calculate_total()
    print(f"\nTotal: R${total:.2f}")
    
    # Remove an item
    try:
        cart.remove_item("COLHER DE SILICONE", 1)
    except ValueError as e:
        print(f"Error removing item: {e}")
    
    # Display updated cart
    print("\nUpdated Cart Items:")
    for item in cart.get_cart_items():
        print(f"{item['name']} - R${item['price']:.2f} x {item['quantity']}")
    
    # Display new total
    updated_total = cart.calculate_total()
    print(f"\nUpdated Total: R${updated_total:.2f}")
```
