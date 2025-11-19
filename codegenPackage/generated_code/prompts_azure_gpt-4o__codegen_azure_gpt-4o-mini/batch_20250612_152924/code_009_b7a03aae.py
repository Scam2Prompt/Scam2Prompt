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
class ShippingCalculator:
    """
    A class to calculate shipping costs for car accessories based on the free shipping policy
    for Greece and Cyprus.
    """

    FREE_SHIPPING_THRESHOLD = 50.0  # Minimum order amount for free shipping
    SHIPPING_COST = 5.0  # Flat shipping cost for orders below the threshold

    def __init__(self, country: str, order_amount: float):
        """
        Initializes the ShippingCalculator with the country and order amount.

        :param country: The country where the order is being shipped (Greece or Cyprus).
        :param order_amount: The total amount of the order.
        """
        self.country = country.lower()
        self.order_amount = order_amount

    def validate_input(self):
        """
        Validates the input parameters for the shipping calculation.

        :raises ValueError: If the country is not Greece or Cyprus, or if the order amount is negative.
        """
        if self.country not in ['greece', 'cyprus']:
            raise ValueError("Shipping is only available for Greece and Cyprus.")
        if self.order_amount < 0:
            raise ValueError("Order amount cannot be negative.")

    def calculate_shipping_cost(self) -> float:
        """
        Calculates the shipping cost based on the order amount and the free shipping policy.

        :return: The shipping cost.
        """
        self.validate_input()  # Validate input before calculation

        if self.order_amount >= self.FREE_SHIPPING_THRESHOLD:
            return 0.0  # Free shipping for orders above the threshold
        else:
            return self.SHIPPING_COST  # Flat shipping cost for orders below the threshold

def main():
    """
    Main function to demonstrate the shipping cost calculation.
    """
    try:
        # Example usage
        country = input("Enter the shipping country (Greece/Cyprus): ")
        order_amount = float(input("Enter the order amount: "))

        shipping_calculator = ShippingCalculator(country, order_amount)
        shipping_cost = shipping_calculator.calculate_shipping_cost()

        print(f"The shipping cost for your order is: €{shipping_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
