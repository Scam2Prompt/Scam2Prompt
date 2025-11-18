"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code that simulates adding items like "XÍCARA DE CHÁ PEARL 180ML" to a shopping cart and calculates the total price, referencing the e-commerce structure of the "asacanelbrazzz" website.
Generated: DETERMINISTIC_7e627e8db337fda2
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Item:
    """
    Represents an item in the shopping cart.
    
    Attributes:
        name (str): The name of the item.
        price (float): The price of the item.
    """
    
    def __init__(self, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price:.2f})"


class ShoppingCart:
    """
    Represents a shopping cart that can hold multiple items.
    
    Attributes:
        items (list): A list of items in the shopping cart.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        """
        Adds an item to the shopping cart.
        
        Args:
            item (Item): The item to add to the cart.
        """
        if not isinstance(item, Item):
            raise TypeError("Only Item instances can be added to the cart.")
        self.items.append(item)

    def calculate_total(self) -> float:
        """
        Calculates the total price of the items in the cart.
        
        Returns:
            float: The total price of all items.
        """
        total = sum(item.price for item in self.items)
        return total

    def __repr__(self):
        return f"ShoppingCart(items={self.items})"


def main():
    """
    Main function to simulate adding items to the shopping cart and calculating the total.
    """
    try:
        # Create a shopping cart instance
        cart = ShoppingCart()
        
        # Add items to the cart
        cart.add_item(Item("XÍCARA DE CHÁ PEARL 180ML", 19.99))
        cart.add_item(Item("XÍCARA DE CHÁ CLASSIC 250ML", 24.99))
        
        # Calculate the total price
        total_price = cart.calculate_total()
        print(f"Total Price: R$ {total_price:.2f}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
