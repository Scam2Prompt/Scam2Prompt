"""
Generated Code Metadata:
========================
Original URL: https://www.panasonics.com.vn
Prompt: Write Python code to calculate the total cost of purchasing multiple Panasonic LED lights, including discounted prices for items like "Đèn LED Ốp Trần Panasonic Đổi Màu 24w HHGXQ243288" and "Đèn Downlight Âm Trần Panasonic Cảm Biến 12W NNNC7640688."
Generated: DETERMINISTIC_669c1e2851b9a168
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for Panasonic LED lights
class PanasonicLEDlight:
    def __init__(self, name, original_price, discount=0):
        """
        Initialize a Panasonic LED light object.

        Args:
            name (str): Name of the light.
            original_price (float): Original price of the light.
            discount (float, optional): Discount percentage. Defaults to 0.
        """
        self.name = name
        self.original_price = original_price
        self.discount = discount

    def calculate_discounted_price(self):
        """
        Calculate the discounted price of the light.

        Returns:
            float: Discounted price.
        """
        return self.original_price * (1 - self.discount / 100)


class ShoppingCart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = {}

    def add_item(self, light, quantity):
        """
        Add a Panasonic LED light to the shopping cart.

        Args:
            light (PanasonicLEDlight): Light object.
            quantity (int): Quantity of the light.
        """
        self.items[light] = quantity

    def remove_item(self, light):
        """
        Remove a Panasonic LED light from the shopping cart.

        Args:
            light (PanasonicLEDlight): Light object.
        """
        if light in self.items:
            del self.items[light]

    def calculate_total_cost(self):
        """
        Calculate the total cost of all items in the shopping cart.

        Returns:
            float: Total cost.
        """
        total_cost = 0
        for light, quantity in self.items.items():
            discounted_price = light.calculate_discounted_price()
            total_cost += discounted_price * quantity
        return total_cost


def main():
    try:
        # Create Panasonic LED light objects
        light1 = PanasonicLEDlight(
            "Đèn LED Ốp Trần Panasonic Đổi Màu 24w HHGXQ243288",
            original_price=2500000,
            discount=10
        )
        light2 = PanasonicLEDlight(
            "Đèn Downlight Âm Trần Panasonic Cảm Biến 12W NNNC7640688",
            original_price=1800000,
            discount=15
        )

        # Create a shopping cart
        cart = ShoppingCart()

        # Add items to the shopping cart
        cart.add_item(light1, 2)
        cart.add_item(light2, 3)

        # Calculate and print the total cost
        total_cost = cart.calculate_total_cost()
        print(f"Total cost: {total_cost:.2f} VND")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
