"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a Python code snippet to calculate the total cost of purchasing 5 units of the `Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017` product with 5% discount and 12x payment plan.
Generated: DETERMINISTIC_73ebd55386b232a0
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    def __init__(self, name, price_per_unit):
        """
        Initializes a new product with a name and price per unit.

        :param name: str - The name of the product
        :param price_per_unit: float - The price of a single unit of the product
        """
        self.name = name
        self.price_per_unit = price_per_unit

    def calculate_total_cost(self, quantity, discount_rate):
        """
        Calculates the total cost after applying the discount.

        :param quantity: int - The number of units to purchase
        :param discount_rate: float - The discount rate as a percentage (e.g., 5 for 5%)
        :return: float - The total cost after discount
        """
        if quantity < 0 or self.price_per_unit < 0:
            raise ValueError("Quantity and price per unit must be non-negative.")
        
        total_cost = self.price_per_unit * quantity
        discount_amount = total_cost * (discount_rate / 100)
        total_cost_after_discount = total_cost - discount_amount
        
        return total_cost_after_discount

    def calculate_monthly_payment(self, total_cost, months):
        """
        Calculates the monthly payment based on the total cost and payment plan duration.

        :param total_cost: float - The total cost to be financed
        :param months: int - The number of months for the payment plan
        :return: float - The monthly payment amount
        """
        if months <= 0:
            raise ValueError("Number of months must be greater than zero.")
        
        return total_cost / months


def main():
    # Product details
    product_name = "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017"
    price_per_unit = 100.0  # Example price per unit in currency

    # Create a product instance
    product = Product(product_name, price_per_unit)

    # Purchase details
    quantity = 5
    discount_rate = 5  # 5% discount
    payment_plan_months = 12

    try:
        # Calculate total cost after discount
        total_cost = product.calculate_total_cost(quantity, discount_rate)
        print(f"Total cost after discount: {total_cost:.2f}")

        # Calculate monthly payment
        monthly_payment = product.calculate_monthly_payment(total_cost, payment_plan_months)
        print(f"Monthly payment for {payment_plan_months} months: {monthly_payment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
