"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.panasonics.com.vn
Prompt: Write Python code to calculate the total cost of purchasing multiple Panasonic LED lights, including discounted prices for items like "Đèn LED Ốp Trần Panasonic Đổi Màu 24w HHGXQ243288" and "Đèn Downlight Âm Trần Panasonic Cảm Biến 12W NNNC7640688."
Generated: DETERMINISTIC_669c1e2851b9a168
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LEDLight:
    """Class to represent an LED light with a name, price, and discount."""

    def __init__(self, name: str, price: float, discount: float = 0.0):
        """
        Initialize the LED light with name, price, and discount.
        
        :param name: Name of the LED light
        :param price: Original price of the LED light
        :param discount: Discount applied to the LED light (as a percentage)
        """
        self.name = name
        self.price = price
        self.discount = discount

    def calculate_discounted_price(self) -> float:
        """
        Calculate the discounted price of the LED light.
        
        :return: Price after discount
        """
        if self.discount < 0 or self.discount > 100:
            raise ValueError("Discount must be between 0 and 100.")
        return self.price * (1 - self.discount / 100)


class ShoppingCart:
    """Class to represent a shopping cart for purchasing LED lights."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.lights = []

    def add_light(self, light: LEDLight):
        """
        Add an LED light to the shopping cart.
        
        :param light: LEDLight instance to add
        """
        self.lights.append(light)

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of all LED lights in the cart.
        
        :return: Total cost after discounts
        """
        total_cost = 0.0
        for light in self.lights:
            total_cost += light.calculate_discounted_price()
        return total_cost


def main():
    """Main function to execute the shopping cart functionality."""
    try:
        # Create instances of LED lights with their respective prices and discounts
        light1 = LEDLight("Đèn LED Ốp Trần Panasonic Đổi Màu 24w HHGXQ243288", 150.0, 10.0)  # 10% discount
        light2 = LEDLight("Đèn Downlight Âm Trần Panasonic Cảm Biến 12W NNNC7640688", 200.0, 15.0)  # 15% discount
        
        # Create a shopping cart and add lights to it
        cart = ShoppingCart()
        cart.add_light(light1)
        cart.add_light(light2)

        # Calculate and print the total cost
        total_cost = cart.calculate_total_cost()
        print(f"Total cost of purchasing the LED lights: {total_cost:.2f} VND")

    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
