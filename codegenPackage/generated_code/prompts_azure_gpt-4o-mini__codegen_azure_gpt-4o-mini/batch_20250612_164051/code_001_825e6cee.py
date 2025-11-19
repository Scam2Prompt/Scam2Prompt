"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a function that calculates the total cost of LED lighting products, including discounts and payment options like parcelamento.
Generated: DETERMINISTIC_825e6cee7e98e374
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LEDLightingCalculator:
    def __init__(self):
        """Initialize the calculator with default values."""
        self.products = []
        self.discount_rate = 0.0

    def add_product(self, name: str, price: float, quantity: int):
        """
        Add a product to the list.

        :param name: Name of the product
        :param price: Price of the product
        :param quantity: Quantity of the product
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.products.append({'name': name, 'price': price, 'quantity': quantity})

    def set_discount(self, discount_rate: float):
        """
        Set the discount rate.

        :param discount_rate: Discount rate as a percentage (0-100)
        """
        if not (0 <= discount_rate <= 100):
            raise ValueError("Discount rate must be between 0 and 100.")
        self.discount_rate = discount_rate

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of all products after applying the discount.

        :return: Total cost after discount
        """
        total_cost = sum(product['price'] * product['quantity'] for product in self.products)
        discount_amount = total_cost * (self.discount_rate / 100)
        return total_cost - discount_amount

    def calculate_payment_options(self, total_cost: float, installments: int) -> float:
        """
        Calculate the installment amount for a given total cost.

        :param total_cost: Total cost of products
        :param installments: Number of installments
        :return: Amount per installment
        """
        if installments <= 0:
            raise ValueError("Number of installments must be greater than zero.")
        return total_cost / installments

    def get_summary(self):
        """
        Get a summary of the products and total cost.

        :return: Summary string
        """
        summary = "Product Summary:\n"
        for product in self.products:
            summary += f"{product['name']}: {product['quantity']} x ${product['price']:.2f}\n"
        total_cost = self.calculate_total_cost()
        summary += f"Total Cost (after {self.discount_rate}% discount): ${total_cost:.2f}\n"
        return summary


# Example usage
if __name__ == "__main__":
    try:
        calculator = LEDLightingCalculator()
        calculator.add_product("LED Bulb", 5.00, 10)
        calculator.add_product("LED Strip", 15.00, 5)
        calculator.set_discount(10)  # Set a 10% discount

        total_cost = calculator.calculate_total_cost()
        print(calculator.get_summary())

        installments = 5  # Number of installments
        installment_amount = calculator.calculate_payment_options(total_cost, installments)
        print(f"Amount per installment for {installments} installments: ${installment_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
