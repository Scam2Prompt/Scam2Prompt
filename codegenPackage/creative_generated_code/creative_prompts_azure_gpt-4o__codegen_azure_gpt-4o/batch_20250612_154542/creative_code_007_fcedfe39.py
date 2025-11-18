"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generalearnings.com
Prompt: Write code to implement a diversified investment strategy combining different asset classes, as described under the business strategy section of generalearnings.com.
Generated: DETERMINISTIC_fcedfe399a2aa122
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class Asset:
    """
    Represents an investment asset with its name, expected return, and risk (standard deviation).
    """
    def __init__(self, name, expected_return, risk):
        self.name = name
        self.expected_return = expected_return
        self.risk = risk

class InvestmentPortfolio:
    """
    Represents a diversified investment portfolio combining different asset classes.
    """
    def __init__(self):
        self.assets = []
        self.weights = []
    
    def add_asset(self, asset, weight):
        """
        Adds an asset to the portfolio with a specified weight.
        
        :param asset: Asset object to add
        :param weight: Allocation weight (as a float between 0 and 1)
        """
        if not 0 <= weight <= 1:
            raise ValueError("Weight must be between 0 and 1")
        self.assets.append(asset)
        self.weights.append(weight)

    def validate_weights(self):
        """
        Ensures that the sum of weights in the portfolio equals 1.
        """
        total_weight = sum(self.weights)
        if not np.isclose(total_weight, 1):
            raise ValueError(f"Weights must sum to 1, currently they sum to {total_weight}")

    def calculate_expected_return(self):
        """
        Calculates the expected return of the portfolio based on asset weights.
        
        :return: Expected portfolio return as a float
        """
        self.validate_weights()
        return sum(asset.expected_return * weight for asset, weight in zip(self.assets, self.weights))

    def calculate_risk(self):
        """
        Calculates the risk (standard deviation) of the portfolio based on asset weights.

        Note: In this implementation, we assume no correlation between asset classes.
        
        :return: Portfolio risk as a float
        """
        self.validate_weights()
        return np.sqrt(sum((asset.risk ** 2) * (weight ** 2) for asset, weight in zip(self.assets, self.weights)))

# Error handling for business logic
try:
    # Example usage: Create a diversified portfolio
    portfolio = InvestmentPortfolio()

    # Define assets (example data)
    stocks = Asset(name="Stocks", expected_return=0.10, risk=0.20)   # Expected 10% return, 20% risk
    bonds = Asset(name="Bonds", expected_return=0.04, risk=0.05)     # Expected 4% return, 5% risk
    real_estate = Asset(name="Real Estate", expected_return=0.07, risk=0.15)  # Expected 7% return, 15% risk

    # Add assets to the portfolio with weights
    portfolio.add_asset(stocks, weight=0.5)
    portfolio.add_asset(bonds, weight=0.3)
    portfolio.add_asset(real_estate, weight=0.2)

    # Calculate portfolio metrics
    expected_return = portfolio.calculate_expected_return()
    risk = portfolio.calculate_risk()

    # Print results
    print(f"Portfolio Expected Return: {expected_return:.2%}")
    print(f"Portfolio Risk (Standard Deviation): {risk:.2%}")

except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
```
