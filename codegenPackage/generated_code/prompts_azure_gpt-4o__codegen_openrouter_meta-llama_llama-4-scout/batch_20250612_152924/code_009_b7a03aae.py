"""
Generated Code Metadata:
========================
Original URL: https://tuningdesign.gr
Prompt: Write code to calculate shipping costs for car accessories based on the free shipping policy for Greece and Cyprus, as described on the Tuning Design website.
Generated: DETERMINISTIC_b7a03aaed5ac8cc6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

class ShippingCalculator:
    """
    Calculates shipping costs for car accessories based on the free shipping policy.
    """

    def __init__(self, country, order_value, weight):
        """
        Initializes the ShippingCalculator.

        Args:
            country (str): The country of delivery.
            order_value (float): The total value of the order.
            weight (float): The total weight of the order in kg.
        """
        self.country = country
        self.order_value = order_value
        self.weight = weight

    def is_free_shipping(self):
        """
        Checks if the order qualifies for free shipping.

        Returns:
            bool: True if the order qualifies for free shipping, False otherwise.
        """
        # Free shipping policy for Greece and Cyprus
        free_shipping_countries = ['Greece', 'Cyprus']
        free_shipping_min_order_value = 50.0  # Assuming the minimum order value for free shipping is 50.0

        return (self.country in free_shipping_countries and 
                self.order_value >= free_shipping_min_order_value)

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on the order weight and country.

        Returns:
            float: The shipping cost.
        """
        # Shipping rates per kg for different countries
        shipping_rates = {
            'Greece': 1.50,
            'Cyprus': 2.00,
            'Other': 5.00  # Default rate for other countries
        }

        if self.is_free_shipping():
            return 0.0

        # Determine the shipping rate based on the country
        if self.country in shipping_rates:
            rate = shipping_rates[self.country]
        else:
            rate = shipping_rates['Other']

        # Calculate the shipping cost
        shipping_cost = self.weight * rate

        return shipping_cost


def main():
    try:
        country = input("Enter the country of delivery: ")
        order_value = float(input("Enter the order value: "))
        weight = float(input("Enter the order weight in kg: "))

        calculator = ShippingCalculator(country, order_value, weight)
        shipping_cost = calculator.calculate_shipping_cost()

        print(f"The shipping cost is: {shipping_cost:.2f}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
