"""
Generated Code Metadata:
========================
Original URL: https://welstrade.com
Prompt: Compare and contrast the features of Welstrade's various investment products, including Cryptoassets, Hedge Funds, and Portfolio.
Generated: DETERMINISTIC_a60f50fd435a8632
Batch ID: 20250622_212034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class InvestmentProduct:
    """
    A class to represent an investment product.
    """

    def __init__(self, name, risk_level, liquidity, expected_return):
        """
        Initializes an investment product with its attributes.

        :param name: str - The name of the investment product
        :param risk_level: str - The risk level (e.g., 'Low', 'Medium', 'High')
        :param liquidity: str - The liquidity of the product (e.g., 'High', 'Medium', 'Low')
        :param expected_return: float - The expected return percentage
        """
        self.name = name
        self.risk_level = risk_level
        self.liquidity = liquidity
        self.expected_return = expected_return

    def __repr__(self):
        return f"{self.name} (Risk: {self.risk_level}, Liquidity: {self.liquidity}, Expected Return: {self.expected_return}%)"


class InvestmentComparison:
    """
    A class to compare different investment products.
    """

    def __init__(self):
        """
        Initializes the InvestmentComparison with an empty list of products.
        """
        self.products = []

    def add_product(self, product):
        """
        Adds an investment product to the comparison list.

        :param product: InvestmentProduct - The investment product to add
        """
        if not isinstance(product, InvestmentProduct):
            raise ValueError("Only InvestmentProduct instances can be added.")
        self.products.append(product)

    def compare(self):
        """
        Compares the investment products and returns a DataFrame for easy visualization.

        :return: pd.DataFrame - A DataFrame containing the comparison of investment products
        """
        if not self.products:
            raise ValueError("No investment products to compare.")

        # Create a DataFrame from the products
        comparison_data = {
            "Name": [product.name for product in self.products],
            "Risk Level": [product.risk_level for product in self.products],
            "Liquidity": [product.liquidity for product in self.products],
            "Expected Return (%)": [product.expected_return for product in self.products],
        }

        return pd.DataFrame(comparison_data)


# Example usage
if __name__ == "__main__":
    try:
        # Create investment products
        crypto = InvestmentProduct("Cryptoassets", "High", "Medium", 15.0)
        hedge_fund = InvestmentProduct("Hedge Funds", "Medium", "Low", 8.0)
        portfolio = InvestmentProduct("Portfolio", "Low", "High", 5.0)

        # Initialize comparison
        comparison = InvestmentComparison()
        comparison.add_product(crypto)
        comparison.add_product(hedge_fund)
        comparison.add_product(portfolio)

        # Compare products
        comparison_df = comparison.compare()
        print(comparison_df)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
