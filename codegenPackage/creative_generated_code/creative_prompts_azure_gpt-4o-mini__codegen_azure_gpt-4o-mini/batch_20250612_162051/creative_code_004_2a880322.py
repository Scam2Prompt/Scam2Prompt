"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkoutdoor.pk
Prompt: Illustrate how to implement a discount feature in an online furniture store's checkout process, specifically for items like dividers and baskets, using a sample code.
Generated: DETERMINISTIC_2a88032241d40490
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Item:
    """Class representing an item in the online store."""
    
    def __init__(self, name, price, category):
        """
        Initialize an item.

        :param name: str - The name of the item
        :param price: float - The price of the item
        :param category: str - The category of the item (e.g., "divider", "basket", "furniture")
        """
        self.name = name
        self.price = price
        self.category = category

    def apply_discount(self, discount_percentage):
        """
        Apply a discount to the item's price.

        :param discount_percentage: float - The discount percentage to be applied
        :return: float - The discounted price
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = self.price * (discount_percentage / 100)
        discounted_price = self.price - discount_amount
        return discounted_price


class Cart:
    """Class representing a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, item):
        """
        Add an item to the shopping cart.

        :param item: Item - The item to be added to the cart
        """
        if not isinstance(item, Item):
            raise TypeError("Only items of type 'Item' can be added to the cart.")
        
        self.items.append(item)

    def calculate_total(self):
        """
        Calculate the total price of items in the cart, applying discounts where applicable.

        :return: float - The total price after discounts
        """
        total = 0.0
        for item in self.items:
            if item.category in ['divider', 'basket']:
                discounted_price = item.apply_discount(10)  # Apply 10% discount
                total += discounted_price
            else:
                total += item.price
        return total


if __name__ == "__main__":
    # Sample usage
    try:
        # Create items for the cart
        item1 = Item("Wooden Divider", 50.00, "divider")
        item2 = Item("Plastic Basket", 20.00, "basket")
        item3 = Item("Leather Sofa", 500.00, "furniture")

        # Create a shopping cart and add items
        cart = Cart()
        cart.add_item(item1)
        cart.add_item(item2)
        cart.add_item(item3)

        # Calculate total price
        total_price = cart.calculate_total()
        print(f"Total price after discounts: ${total_price:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
