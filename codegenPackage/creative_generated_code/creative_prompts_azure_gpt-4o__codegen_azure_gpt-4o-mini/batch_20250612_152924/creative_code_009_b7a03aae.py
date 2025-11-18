"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Write code to calculate shipping costs for car accessories based on the free shipping policy for Greece and Cyprus, as described on the Tuning Design website.
Generated: DETERMINISTIC_b7a03aaed5ac8cc6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShippingCalculator:
    """
    A class to calculate shipping costs for car accessories based on the free shipping policy.
    """

    def __init__(self, country: str, order_total: float):
        """
        Initialize the shipping calculator with the destination country and order total.

        :param country: The destination country (Greece or Cyprus).
        :param order_total: The total amount of the order.
        """
        self.country = country.lower()
        self.order_total = order_total
        self.free_shipping_threshold = 50.00  # Free shipping threshold in local currency
        self.shipping_cost = 5.00  # Flat shipping cost for orders below the threshold

    def validate_input(self):
        """
        Validate the input parameters to ensure they are within acceptable ranges.

        :raises ValueError: If the country is not supported or the order total is negative.
        """
        if self.country not in ["greece", "cyprus"]:
            raise ValueError("Unsupported country. Only Greece and Cyprus are supported.")
        if self.order_total < 0:
            raise ValueError("Order total must not be negative.")

    def calculate_shipping_cost(self) -> float:
        """
        Calculate the shipping cost based on the order total and free shipping policy.

        :return: The shipping cost as a float.
        """
        self.validate_input()  # Validate input before calculation
        
        # Determine if order qualifies for free shipping
        if self.order_total >= self.free_shipping_threshold:
            return 0.00  # Free shipping
        else:
            return self.shipping_cost  # Flat shipping fee

def main():
    """
    Main function to execute the shipping cost calculation.
    """
    try:
        # Example usage
        country = "Greece"
        order_total = 45.00  # Example order total

        shipping_calculator = ShippingCalculator(country, order_total)
        shipping_cost = shipping_calculator.calculate_shipping_cost()

        print(f"The shipping cost for your order to {country} is: €{shipping_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
