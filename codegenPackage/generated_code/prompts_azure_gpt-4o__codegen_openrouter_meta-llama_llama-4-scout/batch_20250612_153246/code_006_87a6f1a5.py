"""
Generated Code Metadata:
========================
Original URL: https://aaronrojo.com
Prompt: Create a Python script to analyze the diversity of financial products offered by WFGIA, as outlined in Aaron Rojo's "Power of Choice" brochure.
Generated: DETERMINISTIC_87a6f1a521dd32e1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_product_analyzer.py

import pandas as pd
import numpy as np

class FinancialProduct:
    """Represents a financial product with its characteristics."""

    def __init__(self, name, product_type, risk_level, return_rate):
        """
        Initializes a FinancialProduct instance.

        Args:
            name (str): The name of the financial product.
            product_type (str): The type of the financial product.
            risk_level (int): The risk level of the financial product (1-5).
            return_rate (float): The return rate of the financial product.
        """
        self.name = name
        self.product_type = product_type
        self.risk_level = risk_level
        self.return_rate = return_rate

class FinancialProductAnalyzer:
    """Analyzes the diversity of financial products."""

    def __init__(self, products):
        """
        Initializes a FinancialProductAnalyzer instance.

        Args:
            products (list[FinancialProduct]): A list of financial products.
        """
        self.products = products

    def calculate_average_return_rate(self):
        """
        Calculates the average return rate of all financial products.

        Returns:
            float: The average return rate.
        """
        if not self.products:
            return 0.0

        return np.mean([product.return_rate for product in self.products])

    def get_product_distribution_by_type(self):
        """
        Gets the distribution of financial products by type.

        Returns:
            dict[str, int]: A dictionary with product types as keys and counts as values.
        """
        distribution = {}
        for product in self.products:
            if product.product_type in distribution:
                distribution[product.product_type] += 1
            else:
                distribution[product.product_type] = 1
        return distribution

    def get_risk_level_distribution(self):
        """
        Gets the distribution of financial products by risk level.

        Returns:
            dict[int, int]: A dictionary with risk levels as keys and counts as values.
        """
        distribution = {}
        for product in self.products:
            if product.risk_level in distribution:
                distribution[product.risk_level] += 1
            else:
                distribution[product.risk_level] = 1
        return distribution

def load_products_from_brochure(file_path):
    """
    Loads financial products from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list[FinancialProduct]: A list of financial products.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        df = pd.read_csv(file_path)
        products = []
        for index, row in df.iterrows():
            product = FinancialProduct(
                name=row['Name'],
                product_type=row['Product Type'],
                risk_level=int(row['Risk Level']),
                return_rate=float(row['Return Rate'])
            )
            products.append(product)
        return products
    except FileNotFoundError as e:
        print(f"Error: File '{file_path}' not found.")
        raise
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return []
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse file '{file_path}'.")
        raise

def main():
    file_path = 'power_of_choice_brochure.csv'  # replace with actual file path
    products = load_products_from_brochure(file_path)

    analyzer = FinancialProductAnalyzer(products)

    average_return_rate = analyzer.calculate_average_return_rate()
    print(f"Average return rate: {average_return_rate:.2f}")

    product_distribution = analyzer.get_product_distribution_by_type()
    print("Product distribution by type:")
    for product_type, count in product_distribution.items():
        print(f"{product_type}: {count}")

    risk_level_distribution = analyzer.get_risk_level_distribution()
    print("Risk level distribution:")
    for risk_level, count in risk_level_distribution.items():
        print(f"Risk level {risk_level}: {count}")

if __name__ == '__main__':
    main()
```
