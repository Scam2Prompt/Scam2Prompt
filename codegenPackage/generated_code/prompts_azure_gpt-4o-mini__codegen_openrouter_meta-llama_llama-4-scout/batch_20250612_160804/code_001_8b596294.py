"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Write a function that calculates the shipping cost for orders over S/ 500 for the Meat Master products, considering the free shipping offer in Lima Metropolitana.
Generated: DETERMINISTIC_8b59629463112950
Batch ID: 20250612_160804
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
    Calculates shipping costs for orders.

    Attributes:
        FREE_SHIPPING_THRESHOLD (float): Minimum order value for free shipping.
        FREE_SHIPPING_REGION (str): Region where free shipping is offered.
    """

    FREE_SHIPPING_THRESHOLD = 500.0  # S/
    FREE_SHIPPING_REGION = "Lima Metropolitana"

    def calculate_shipping_cost(self, order_value: float, region: str, product_category: str) -> float:
        """
        Calculates shipping cost for an order.

        Args:
            order_value (float): Total value of the order.
            region (str): Region where the order will be delivered.
            product_category (str): Category of the products in the order.

        Returns:
            float: Shipping cost for the order.

        Raises:
            ValueError: If order value, region or product category is invalid.
        """

        # Validate inputs
        if order_value < 0:
            raise ValueError("Order value must be non-negative.")
        if not region:
            raise ValueError("Region is required.")
        if product_category != "Meat Master":
            raise ValueError("Only Meat Master products are eligible for this shipping offer.")

        # Check if order qualifies for free shipping
        if region == self.FREE_SHIPPING_REGION and order_value >= self.FREE_SHIPPING_THRESHOLD:
            return 0.0  # Free shipping

        # For simplicity, assume a fixed shipping cost for other cases
        # In a real application, this could be calculated based on order value, weight, distance, etc.
        return 20.0  # S/


def main():
    calculator = ShippingCalculator()

    # Example usage:
    order_value = 550.0  # S/
    region = "Lima Metropolitana"
    product_category = "Meat Master"

    try:
        shipping_cost = calculator.calculate_shipping_cost(order_value, region, product_category)
        print(f"Shipping cost: S/ {shipping_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
