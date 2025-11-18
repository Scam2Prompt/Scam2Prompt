"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Generate a script to calculate shipping costs for AirstyleArt products, including complimentary shipping for orders over £75, and ensure compatibility with UK and EU delivery rules.
Generated: DETERMINISTIC_68b38c822e515fe8
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCostCalculator:
    """
    A class to calculate shipping costs for AirstyleArt products.
    Includes complimentary shipping for orders over £75 and 
    considers UK and EU delivery rules.
    """

    # Define constants for shipping costs
    UK_SHIPPING_COST = 5.0  # Standard UK shipping cost
    EU_SHIPPING_COST = 10.0  # Standard EU shipping cost
    FREE_SHIPPING_THRESHOLD = 75.0  # Order value threshold for free shipping

    def __init__(self, order_value, delivery_region):
        """
        Initializes the ShippingCostCalculator with the order value and delivery region.

        :param order_value: float - The total order value
        :param delivery_region: str - The region of delivery ('UK' or 'EU')
        """
        self.order_value = order_value
        self.delivery_region = delivery_region.upper()

    def calculate_shipping_cost(self):
        """
        Calculates the shipping cost based on order value and delivery region.

        :return: float - The calculated shipping cost
        :raises ValueError: If an invalid delivery region is provided
        """
        # Validate input
        if self.delivery_region not in ['UK', 'EU']:
            raise ValueError("Invalid delivery region: must be 'UK' or 'EU'.")

        # Check if the order qualifies for free shipping
        if self.order_value >= self.FREE_SHIPPING_THRESHOLD:
            return 0.0  # Complimentary shipping

        # Calculate shipping cost based on delivery region
        if self.delivery_region == 'UK':
            return self.UK_SHIPPING_COST
        elif self.delivery_region == 'EU':
            return self.EU_SHIPPING_COST

    def get_total_cost(self):
        """
        Calculates the total cost including shipping.

        :return: float - The total cost including shipping
        """
        shipping_cost = self.calculate_shipping_cost()
        return self.order_value + shipping_cost


def main():
    """
    Main function to demonstrate the ShippingCostCalculator functionality.
    """
    try:
        # Example order value and delivery region
        order_value = float(input("Enter the order value (£): "))
        delivery_region = input("Enter delivery region (UK/EU): ")

        # Create an instance of the ShippingCostCalculator
        calculator = ShippingCostCalculator(order_value, delivery_region)

        # Calculate and display shipping cost and total cost
        shipping_cost = calculator.calculate_shipping_cost()
        total_cost = calculator.get_total_cost()

        print(f"Shipping Cost: £{shipping_cost:.2f}")
        print(f"Total Cost: £{total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
