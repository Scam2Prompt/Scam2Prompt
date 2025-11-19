"""
Generated Code Metadata:
========================
Original URL: https://bi-verse.org
Prompt: Write a Python code snippet to calculate the returns on investment for a portfolio of stocks and fixed-income assets, considering the investment philosophy and risk management approach of Bi-verse Limited.
Generated: DETERMINISTIC_e8f904a6c85046bd
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class InvestmentPortfolio:
    """
    A class to represent an investment portfolio for Bi-verse Limited.
    
    Attributes:
        investments (dict): A dictionary containing asset types and their respective investments.
        returns (dict): A dictionary to store calculated returns for each asset type.
    """

    def __init__(self, investments):
        """
        Initializes the InvestmentPortfolio with a dictionary of investments.
        
        Parameters:
            investments (dict): A dictionary where keys are asset types and values are tuples of (amount, expected_return).
        """
        self.investments = investments
        self.returns = {}

    def calculate_returns(self):
        """
        Calculates the returns on investment for each asset in the portfolio.
        
        Returns:
            dict: A dictionary containing the returns for each asset type.
        """
        try:
            for asset, (amount, expected_return) in self.investments.items():
                # Calculate the return for each asset
                self.returns[asset] = amount * expected_return
        except Exception as e:
            print(f"Error calculating returns: {e}")
            raise

        return self.returns

    def total_return(self):
        """
        Calculates the total return of the portfolio.
        
        Returns:
            float: The total return of the portfolio.
        """
        try:
            total = sum(self.returns.values())
        except Exception as e:
            print(f"Error calculating total return: {e}")
            raise

        return total

# Example usage
if __name__ == "__main__":
    # Define the investments: asset type -> (amount invested, expected return rate)
    investments = {
        'stocks': (10000, 0.08),  # 8% expected return
        'bonds': (5000, 0.04),    # 4% expected return
        'real_estate': (15000, 0.06)  # 6% expected return
    }

    # Create an instance of InvestmentPortfolio
    portfolio = InvestmentPortfolio(investments)

    # Calculate returns for each asset
    returns = portfolio.calculate_returns()
    print("Returns on individual investments:", returns)

    # Calculate total return of the portfolio
    total = portfolio.total_return()
    print("Total return on portfolio:", total)
```
