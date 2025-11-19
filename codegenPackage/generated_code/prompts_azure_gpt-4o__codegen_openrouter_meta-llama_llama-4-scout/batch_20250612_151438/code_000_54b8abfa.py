"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write Python code to calculate the total cost of purchasing 10 units of "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017" with a 5% discount applied, and display the cost per installment if paid in 12 interest-free payments.
Generated: DETERMINISTIC_54b8abfa95d3fc16
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to calculate purchase costs
class PurchaseCalculator:
    def __init__(self, product_name, unit_price, quantity, discount_rate, installment_count):
        """
        Initialize the PurchaseCalculator.

        Args:
            product_name (str): Name of the product.
            unit_price (float): Price of a single unit of the product.
            quantity (int): Number of units being purchased.
            discount_rate (float): Discount rate as a decimal (e.g., 5% = 0.05).
            installment_count (int): Number of interest-free payments.
        """
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.discount_rate = discount_rate
        self.installment_count = installment_count

    def calculate_subtotal(self):
        """
        Calculate the subtotal before discount.

        Returns:
            float: Subtotal before discount.
        """
        return self.unit_price * self.quantity

    def calculate_discount(self):
        """
        Calculate the discount amount.

        Returns:
            float: Discount amount.
        """
        subtotal = self.calculate_subtotal()
        return subtotal * self.discount_rate

    def calculate_total_cost(self):
        """
        Calculate the total cost after discount.

        Returns:
            float: Total cost after discount.
        """
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        return subtotal - discount

    def calculate_installment_cost(self):
        """
        Calculate the cost per installment.

        Returns:
            float: Cost per installment.
        """
        total_cost = self.calculate_total_cost()
        return total_cost / self.installment_count


def main():
    product_name = "Fonte Para Led Slim 12v Nordecor 5a/60w Cod.7017"
    unit_price = 50.0  # Assuming the unit price is R$ 50.00
    quantity = 10
    discount_rate = 0.05  # 5% discount
    installment_count = 12

    calculator = PurchaseCalculator(product_name, unit_price, quantity, discount_rate, installment_count)

    print(f"Product: {calculator.product_name}")
    print(f"Quantity: {calculator.quantity} units")
    print(f"Unit Price: R$ {calculator.unit_price:.2f}")
    print(f"Subtotal: R$ {calculator.calculate_subtotal():.2f}")
    print(f"Discount ({discount_rate*100}%): R$ {calculator.calculate_discount():.2f}")
    print(f"Total Cost: R$ {calculator.calculate_total_cost():.2f}")
    print(f"Installment Count: {calculator.installment_count} payments")
    print(f"Installment Cost: R$ {calculator.calculate_installment_cost():.2f}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
