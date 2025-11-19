"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write a Python script that calculates the potential returns of a diversified portfolio including real estate and venture capital investments, as suggested by DCL Invest.
Generated: DETERMINISTIC_47a28bafc3aa1ce7
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class Portfolio:
    """
    A class to represent a diversified investment portfolio.

    Attributes
    ----------
    investments : dict
        A dictionary containing investment types and their respective expected returns and risks.
    """

    def __init__(self):
        """
        Initializes the Portfolio with predefined investment types and their expected returns and risks.
        """
        self.investments = {
            'Real Estate': {'expected_return': 0.08, 'risk': 0.15},
            'Venture Capital': {'expected_return': 0.15, 'risk': 0.25},
            'Stocks': {'expected_return': 0.10, 'risk': 0.20},
            'Bonds': {'expected_return': 0.04, 'risk': 0.05}
        }

    def calculate_portfolio_return(self, allocation):
        """
        Calculate the expected return of the portfolio based on the allocation.

        Parameters
        ----------
        allocation : dict
            A dictionary containing the allocation percentages for each investment type.

        Returns
        -------
        float
            The expected return of the portfolio.
        """
        try:
            if not self._validate_allocation(allocation):
                raise ValueError("Allocation percentages must sum to 100.")

            expected_return = sum(
                self.investments[inv]['expected_return'] * (allocation[inv] / 100)
                for inv in allocation
            )
            return expected_return
        except KeyError as e:
            raise KeyError(f"Investment type '{e.args[0]}' not found in portfolio.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating portfolio return: {e}")

    def _validate_allocation(self, allocation):
        """
        Validate that the allocation percentages sum to 100.

        Parameters
        ----------
        allocation : dict
            A dictionary containing the allocation percentages for each investment type.

        Returns
        -------
        bool
            True if the allocation is valid, False otherwise.
        """
        total_allocation = sum(allocation.values())
        return total_allocation == 100

    def calculate_portfolio_risk(self, allocation):
        """
        Calculate the risk of the portfolio based on the allocation.

        Parameters
        ----------
        allocation : dict
            A dictionary containing the allocation percentages for each investment type.

        Returns
        -------
        float
            The risk of the portfolio.
        """
        try:
            if not self._validate_allocation(allocation):
                raise ValueError("Allocation percentages must sum to 100.")

            variance = sum(
                (self.investments[inv]['risk'] ** 2) * (allocation[inv] / 100) ** 2
                for inv in allocation
            )
            return np.sqrt(variance)  # Return standard deviation as risk
        except KeyError as e:
            raise KeyError(f"Investment type '{e.args[0]}' not found in portfolio.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating portfolio risk: {e}")

def main():
    """
    Main function to execute the portfolio calculations.
    """
    portfolio = Portfolio()

    # Example allocation
    allocation = {
        'Real Estate': 40,
        'Venture Capital': 30,
        'Stocks': 20,
        'Bonds': 10
    }

    try:
        expected_return = portfolio.calculate_portfolio_return(allocation)
        risk = portfolio.calculate_portfolio_risk(allocation)

        print(f"Expected Portfolio Return: {expected_return:.2%}")
        print(f"Portfolio Risk (Standard Deviation): {risk:.2%}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
