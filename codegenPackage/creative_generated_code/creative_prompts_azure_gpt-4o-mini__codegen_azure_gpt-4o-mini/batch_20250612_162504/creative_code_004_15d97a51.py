"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lowbrowartcompany.com
Prompt: Illustrate how to implement a shopping cart feature for the Black Market Art Company site, focusing on adding and removing items like the "Asian Scorned" T-shirt.
Generated: DETERMINISTIC_15d97a51f9fed392
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    """Represents a shopping cart for the Black Market Art Company."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}
    
    def add_item(self, item_name, price, quantity=1):
        """Adds an item to the shopping cart.
        
        Args:
            item_name (str): The name of the item to add.
            price (float): The price of the item.
            quantity (int): The number of items to add (default is 1).
        
        Raises:
            ValueError: If the quantity or price is less than zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} of {item_name} at ${price:.2f} each to the cart.")

    def remove_item(self, item_name, quantity=1):
        """Removes an item from the shopping cart.
        
        Args:
            item_name (str): The name of the item to remove.
            quantity (int): The number of items to remove (default is 1).
        
        Raises:
            ValueError: If the quantity is less than one or the item does not exist.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if item_name not in self.items:
            raise ValueError("Item not found in the cart.")
        
        if self.items[item_name]['quantity'] < quantity:
            raise ValueError("Not enough quantity to remove.")
        
        self.items[item_name]['quantity'] -= quantity
        
        if self.items[item_name]['quantity'] == 0:
            del self.items[item_name]
            print(f"Removed all {item_name} from the cart.")
        else:
            print(f"Removed {quantity} of {item_name} from the cart.")

    def view_cart(self):
        """Displays the contents of the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
            return
        
        print("Shopping Cart Contents:")
        for item_name, item_info in self.items.items():
            print(f"{item_name}: {item_info['quantity']} at ${item_info['price']:.2f} each")
    
    def total_cost(self):
        """Calculates the total cost of items in the shopping cart.
        
        Returns:
            float: The total cost of the items.
        """
        total = sum(item_info['price'] * item_info['quantity'] for item_info in self.items.values())
        print(f"Total cost: ${total:.2f}")
        return total

# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Asian Scorned T-shirt", 19.99, 2)
    cart.view_cart()
    cart.total_cost()
    cart.remove_item("Asian Scorned T-shirt", 1)
    cart.view_cart()
    cart.total_cost()
    cart.remove_item("Asian Scorned T-shirt", 1)
    cart.view_cart()
```
