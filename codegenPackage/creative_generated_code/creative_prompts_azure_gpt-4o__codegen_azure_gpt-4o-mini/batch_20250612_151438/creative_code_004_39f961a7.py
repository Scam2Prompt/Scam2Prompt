"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Provide code to calculate the monthly installment amount for purchasing "04 X Junção Branca Sanfonada P/ Luminaria Circular (redonda)" with a 5% discount and 12 interest-free payments.
Generated: DETERMINISTIC_39f961a7245abaac
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InstallmentCalculator:
    """
    A class to calculate the monthly installment amount for a product purchase.
    """

    def __init__(self, product_name, product_price, discount_rate, installments):
        """
        Initializes the InstallmentCalculator with product details.

        :param product_name: str - Name of the product
        :param product_price: float - Original price of the product
        :param discount_rate: float - Discount rate (as a percentage)
        :param installments: int - Number of installments for payment
        """
        self.product_name = product_name
        self.product_price = product_price
        self.discount_rate = discount_rate
        self.installments = installments

    def calculate_discounted_price(self):
        """
        Calculates the price after applying the discount.

        :return: float - Discounted product price
        """
        if not (0 <= self.discount_rate <= 100):
            raise ValueError("Discount rate must be between 0 and 100.")
        
        discount_amount = (self.discount_rate / 100) * self.product_price
        discounted_price = self.product_price - discount_amount
        return discounted_price

    def calculate_monthly_installment(self):
        """
        Calculates the monthly installment amount based on the discounted price.

        :return: float - Monthly installment amount
        """
        if self.installments <= 0:
            raise ValueError("Number of installments must be greater than 0.")
        
        discounted_price = self.calculate_discounted_price()
        monthly_installment = discounted_price / self.installments
        return monthly_installment

# Example usage:
if __name__ == "__main__":
    try:
        product_name = "04 X Junção Branca Sanfonada P/ Luminaria Circular (redonda)"
        product_price = 200.00  # Example price
        discount_rate = 5.0      # 5% discount
        installments = 12         # 12 interest-free payments

        calculator = InstallmentCalculator(product_name, product_price, discount_rate, installments)
        monthly_installment = calculator.calculate_monthly_installment()

        print(f"The monthly installment amount for '{product_name}' is: R$ {monthly_installment:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
