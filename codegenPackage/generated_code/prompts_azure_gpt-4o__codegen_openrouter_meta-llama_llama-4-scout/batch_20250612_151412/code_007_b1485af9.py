"""
Generated Code Metadata:
========================
Original URL: https://www.klar.com.mx
Prompt: Generate code to calculate GAT Nominal and GAT Real for Klar's investment products, incorporating inflation adjustments.
Generated: DETERMINISTIC_b1485af9f08eca33
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gat_calculations.py

class InvestmentProduct:
    """Represents Klar's investment products."""

    def __init__(self, name, nominal_rate, real_rate, inflation_rate):
        """
        Initializes an InvestmentProduct.

        Args:
            name (str): Name of the investment product.
            nominal_rate (float): Nominal interest rate.
            real_rate (float): Real interest rate.
            inflation_rate (float): Inflation rate.
        """
        self.name = name
        self.nominal_rate = nominal_rate / 100  # Convert to decimal
        self.real_rate = real_rate / 100  # Convert to decimal
        self.inflation_rate = inflation_rate / 100  # Convert to decimal

    def calculate_gat_nominal(self):
        """
        Calculates the GAT Nominal.

        Returns:
            float: GAT Nominal value.
        """
        return self.nominal_rate

    def calculate_gat_real(self):
        """
        Calculates the GAT Real, incorporating inflation adjustments.

        Returns:
            float: GAT Real value.
        """
        try:
            # Apply Fisher equation: (1 + r) = (1 + R) * (1 + i)
            # Where:
            #   r = nominal rate
            #   R = real rate
            #   i = inflation rate
            gat_real = (1 + self.nominal_rate) / (1 + self.inflation_rate) - 1
            return gat_real
        except ZeroDivisionError:
            raise ValueError("Inflation rate cannot be zero or negative.")


class GATCalculator:
    """Calculates GAT Nominal and GAT Real for Klar's investment products."""

    def __init__(self):
        self.investment_products = {}

    def add_investment_product(self, product):
        """
        Adds an investment product.

        Args:
            product (InvestmentProduct): Investment product to add.
        """
        self.investment_products[product.name] = product

    def calculate_gat(self, product_name):
        """
        Calculates GAT Nominal and GAT Real for a given investment product.

        Args:
            product_name (str): Name of the investment product.

        Returns:
            dict: Dictionary containing GAT Nominal and GAT Real values.

        Raises:
            ValueError: If the investment product is not found.
        """
        try:
            product = self.investment_products[product_name]
            gat_nominal = product.calculate_gat_nominal() * 100  # Convert to percentage
            gat_real = product.calculate_gat_real() * 100  # Convert to percentage
            return {
                "GAT Nominal": round(gat_nominal, 2),
                "GAT Real": round(gat_real, 2),
            }
        except KeyError:
            raise ValueError("Investment product not found.")


def main():
    calculator = GATCalculator()

    # Example usage:
    product1 = InvestmentProduct("Product A", 5.0, 3.0, 2.0)
    product2 = InvestmentProduct("Product B", 7.0, 4.0, 3.0)

    calculator.add_investment_product(product1)
    calculator.add_investment_product(product2)

    print(calculator.calculate_gat("Product A"))
    print(calculator.calculate_gat("Product B"))


if __name__ == "__main__":
    main()
```
