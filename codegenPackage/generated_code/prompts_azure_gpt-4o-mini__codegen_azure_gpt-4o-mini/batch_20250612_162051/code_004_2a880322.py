"""
Generated Code Metadata:
========================
Original URL: https://zkoutdoor.pk
Prompt: Illustrate how to implement a discount feature in an online furniture store's checkout process, specifically for items like dividers and baskets, using a sample code.
Generated: DETERMINISTIC_2a88032241d40490
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Item:
    """Class representing an item in the furniture store."""
    
    def __init__(self, name, price, category):
        """
        Initialize an item with a name, price, and category.
        
        :param name: str - The name of the item
        :param price: float - The price of the item
        :param category: str - The category of the item (e.g., 'divider', 'basket', etc.)
        """
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        """Return a string representation of the item."""
        return f"{self.name} ({self.category}): ${self.price:.2f}"


class Cart:
    """Class representing a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, item):
        """
        Add an item to the cart.
        
        :param item: Item - The item to add to the cart
        """
        if not isinstance(item, Item):
            raise ValueError("Only Item instances can be added to the cart.")
        self.items.append(item)

    def calculate_total(self):
        """
        Calculate the total price of items in the cart, applying discounts where applicable.
        
        :return: float - The total price after discounts
        """
        total = 0.0
        for item in self.items:
            total += item.price
        
        # Apply discounts for specific categories
        discount = self.apply_discount()
        total -= discount
        
        return total

    def apply_discount(self):
        """
        Calculate the total discount for eligible items in the cart.
        
        :return: float - The total discount amount
        """
        discount = 0.0
        for item in self.items:
            if item.category in ['divider', 'basket']:
                discount += item.price * 0.10  # 10% discount for dividers and baskets
        return discount


class Checkout:
    """Class to handle the checkout process."""
    
    def __init__(self, cart):
        """
        Initialize the checkout process with a shopping cart.
        
        :param cart: Cart - The shopping cart to checkout
        """
        if not isinstance(cart, Cart):
            raise ValueError("Invalid cart provided for checkout.")
        self.cart = cart

    def process_payment(self):
        """
        Process the payment for the items in the cart.
        
        :return: str - Confirmation message with total amount
        """
        try:
            total_amount = self.cart.calculate_total()
            if total_amount <= 0:
                raise ValueError("Total amount must be greater than zero.")
            return f"Payment processed successfully. Total amount: ${total_amount:.2f}"
        except Exception as e:
            return f"Error processing payment: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Create items
    item1 = Item("Wooden Divider", 50.00, "divider")
    item2 = Item("Plastic Basket", 20.00, "basket")
    item3 = Item("Office Chair", 150.00, "furniture")

    # Create a shopping cart and add items
    cart = Cart()
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    # Checkout process
    checkout = Checkout(cart)
    print(checkout.process_payment())
```
