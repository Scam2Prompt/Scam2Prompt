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
# Import necessary libraries
import pandas as pd

# Define a class to represent investment products
class InvestmentProduct:
    def __init__(self, name, features):
        """
        Initialize an InvestmentProduct instance.

        :param name: Name of the investment product (e.g., Cryptoassets, Hedge Funds, Portfolio)
        :param features: Dictionary containing features and their descriptions
        """
        self.name = name
        self.features = features

    def compare_features(self, other_product):
        """
        Compare features of this product with another product.

        :param other_product: Another InvestmentProduct instance to compare against
        :return: DataFrame showing comparison of features
        """
        comparison_data = []
        all_keys = set(self.features.keys()).union(set(other_product.features.keys()))

        for key in all_keys:
            comparison_data.append({
                "Feature": key,
                self.name: self.features.get(key, "Not Available"),
                other_product.name: other_product.features.get(key, "Not Available")
            })

        return pd.DataFrame(comparison_data)

# Define the investment products and their features
cryptoassets_features = {
    "Risk Level": "High",
    "Liquidity": "High",
    "Minimum Investment": "Low",
    "Regulation": "Limited",
    "Potential Returns": "High"
}

hedge_funds_features = {
    "Risk Level": "Medium",
    "Liquidity": "Low",
    "Minimum Investment": "High",
    "Regulation": "Strict",
    "Potential Returns": "Medium to High"
}

portfolio_features = {
    "Risk Level": "Low to Medium",
    "Liquidity": "Medium",
    "Minimum Investment": "Medium",
    "Regulation": "Moderate",
    "Potential Returns": "Stable"
}

# Create instances of InvestmentProduct
cryptoassets = InvestmentProduct("Cryptoassets", cryptoassets_features)
hedge_funds = InvestmentProduct("Hedge Funds", hedge_funds_features)
portfolio = InvestmentProduct("Portfolio", portfolio_features)

# Compare features between products
crypto_vs_hedge = cryptoassets.compare_features(hedge_funds)
crypto_vs_portfolio = cryptoassets.compare_features(portfolio)
hedge_vs_portfolio = hedge_funds.compare_features(portfolio)

# Display the comparisons
print("Comparison: Cryptoassets vs Hedge Funds")
print(crypto_vs_hedge)

print("\nComparison: Cryptoassets vs Portfolio")
print(crypto_vs_portfolio)

print("\nComparison: Hedge Funds vs Portfolio")
print(hedge_vs_portfolio)
```
