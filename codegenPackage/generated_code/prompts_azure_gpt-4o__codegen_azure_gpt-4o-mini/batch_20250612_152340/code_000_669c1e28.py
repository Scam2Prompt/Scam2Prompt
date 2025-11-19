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
class LEDLight:
    """
    A class to represent an LED light with its details and pricing.
    """

    def __init__(self, name: str, price: float, discount: float = 0.0):
        """
        Initializes the LEDLight instance.

        :param name: The name of the LED light.
        :param price: The original price of the LED light.
        :param discount: The discount percentage (0-100) to apply to the price.
        """
        self.name = name
        self.price = price
        self.discount = discount

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price of the LED light.

        :return: The price after applying the discount.
        """
        if not (0 <= self.discount <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        return self.price * (1 - self.discount / 100)


def calculate_total_cost(lights: list) -> float:
    """
    Calculates the total cost of purchasing multiple LED lights.

    :param lights: A list of LEDLight instances.
    :return: The total cost after discounts.
    """
    total_cost = 0.0
    for light in lights:
        total_cost += light.calculate_discounted_price()
    return total_cost


def main():
    """
    Main function to execute the LED light cost calculation.
    """
    try:
        # Define the LED lights with their respective prices and discounts
        lights = [
            LEDLight("Đèn LED Ốp Trần Panasonic Đổi Màu 24w HHGXQ243288", 500000, 10),  # 10% discount
            LEDLight("Đèn Downlight Âm Trần Panasonic Cảm Biến 12W NNNC7640688", 300000, 15)  # 15% discount
        ]

        # Calculate the total cost
        total_cost = calculate_total_cost(lights)

        # Output the total cost
        print(f"Total cost of purchasing the LED lights: {total_cost:.2f} VND")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
