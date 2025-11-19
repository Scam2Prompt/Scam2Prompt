"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creditu.com.ar
Prompt: Generate a code snippet for an e-commerce application that integrates a financing option for purchasing products like air conditioners and smartphones as described on the Creditu website.
Generated: DETERMINISTIC_c632a5158f23aa9d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from datetime import datetime
from typing import List

class FinancingOption:
    """
    Represents a financing option for an e-commerce product.
    """
    def __init__(self, option_name: str, interest_rate: float, months: int):
        """
        Initializes the financing option.

        :param option_name: Name of the financing plan (e.g., '6 Months EMI').
        :param interest_rate: Annual interest rate (in percentage) for financing.
        :param months: Duration of the financing plan in months.
        """
        self.option_name = option_name
        self.interest_rate = decimal.Decimal(interest_rate) / 100
        self.months = months

    def calculate_monthly_installment(self, price: decimal.Decimal) -> decimal.Decimal:
        """
        Calculates the monthly installment based on the price and financing terms.

        :param price: The price of the product.
        :return: Monthly installment amount.
        """
        try:
            # Formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
            rate_per_month = self.interest_rate / 12
            numerator = price * rate_per_month * (1 + rate_per_month) ** self.months
            denominator = ((1 + rate_per_month) ** self.months) - 1
            emi = numerator / denominator
            return emi.quantize(decimal.Decimal('0.01'))  # Round to two decimal places
        except Exception as e:
            raise ValueError(f"Error calculating monthly installment: {str(e)}")


class Product:
    """
    Represents an e-commerce product.
    """
    def __init__(self, name: str, price: decimal.Decimal):
        """
        Initializes the product.

        :param name: Name of the product (e.g., 'Smartphone').
        :param price: Price of the product.
        """
        self.name = name
        self.price = price


class ECommerceApplication:
    """
    Main application for managing products and financing options.
    """
    def __init__(self):
        """
        Initializes the e-commerce application.
        """
        self.products: List[Product] = []
        self.financing_options: List[FinancingOption] = []

    def add_product(self, product: Product):
        """
        Adds a product to the e-commerce application.

        :param product: Product to be added.
        """
        self.products.append(product)

    def add_financing_option(self, financing_option: FinancingOption):
        """
        Adds a financing option to the e-commerce application.

        :param financing_option: Financing option to be added.
        """
        self.financing_options.append(financing_option)

    def display_financing_options(self, product_name: str):
        """
        Displays all available financing options for a given product.

        :param product_name: Name of the product for which financing options are displayed.
        """
        try:
            product = next((p for p in self.products if p.name == product_name), None)
            if not product:
                raise ValueError(f"Product '{product_name}' not found.")
            
            print(f"Financing Options for '{product.name}' (Price: ${product.price}):")
            for option in self.financing_options:
                monthly_installment = option.calculate_monthly_installment(product.price)
                print(f"  {option.option_name}: ${monthly_installment} per month for {option.months} months")
        except Exception as e:
            print(f"Error displaying financing options: {str(e)}")


# Example Usage
if __name__ == "__main__":
    # Initialize the application
    app = ECommerceApplication()

    # Add products
    app.add_product(Product(name="Air Conditioner", price=decimal.Decimal("1200.00")))
    app.add_product(Product(name="Smartphone", price=decimal.Decimal("800.00")))

    # Add financing options
    app.add_financing_option(FinancingOption(option_name="6 Months EMI", interest_rate=12.0, months=6))
    app.add_financing_option(FinancingOption(option_name="12 Months EMI", interest_rate=14.0, months=12))

    # Display financing options for a product
    app.display_financing_options("Smartphone")
```
