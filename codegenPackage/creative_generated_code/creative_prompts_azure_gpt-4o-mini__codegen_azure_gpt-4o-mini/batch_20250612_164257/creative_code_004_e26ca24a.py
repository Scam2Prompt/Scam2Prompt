"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Write a code example that demonstrates how to implement a discount system for first-time shoppers in a jewelry e-commerce application, referencing the "5% off" offer from Malkeenz.
Generated: DETERMINISTIC_e26ca24af8433391
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Shopper:
    def __init__(self, name, is_first_time):
        """
        Initializes a Shopper object.

        :param name: str - The name of the shopper.
        :param is_first_time: bool - Indicates if the shopper is a first-time shopper.
        """
        self.name = name
        self.is_first_time = is_first_time


class JewelryStore:
    DISCOUNT_RATE = 0.05  # 5% discount for first-time shoppers

    def __init__(self):
        """
        Initializes a JewelryStore object.
        """
        self.inventory = {}  # Dictionary to hold items in the store

    def add_item(self, item_name, price):
        """
        Adds an item to the store's inventory.

        :param item_name: str - The name of the item.
        :param price: float - The price of the item.
        :raises ValueError: If the item price is invalid (negative).
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.inventory[item_name] = price

    def calculate_discounted_price(self, item_name, shopper):
        """
        Calculates the price after applying any eligible discounts.

        :param item_name: str - The name of the item.
        :param shopper: Shopper - The shopper making the purchase.
        :return: float - The price after discount, if applicable.
        :raises ValueError: If the item is not found in inventory.
        """
        if item_name not in self.inventory:
            raise ValueError("Item not found in inventory.")

        original_price = self.inventory[item_name]
        
        # Apply discount for first-time shoppers
        if shopper.is_first_time:
            discounted_price = original_price * (1 - self.DISCOUNT_RATE)
            return discounted_price
        
        return original_price

    def purchase_item(self, item_name, shopper):
        """
        Handles the purchase of an item by a shopper.

        :param item_name: str - The name of the item to purchase.
        :param shopper: Shopper - The shopper making the purchase.
        """
        try:
            final_price = self.calculate_discounted_price(item_name, shopper)
            print(f"{shopper.name} purchased {item_name} for ${final_price:.2f}.")
        except ValueError as e:
            print(f"Error: {e}")


# Example Usage
if __name__ == "__main__":
    store = JewelryStore()
    store.add_item("Diamond Ring", 1000.00)
    store.add_item("Gold Necklace", 500.00)

    first_time_shopper = Shopper("Alice", True)
    returning_shopper = Shopper("Bob", False)

    store.purchase_item("Diamond Ring", first_time_shopper)  # Should apply discount
    store.purchase_item("Gold Necklace", returning_shopper)  # No discount
    store.purchase_item("Unknown Item", first_time_shopper)  # Error handling
```
