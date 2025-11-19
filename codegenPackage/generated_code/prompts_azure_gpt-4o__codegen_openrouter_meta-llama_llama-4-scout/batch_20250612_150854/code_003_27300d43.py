"""
Generated Code Metadata:
========================
Original URL: https://immediatefrontier.app
Prompt: Create a program that simulates cryptocurrency portfolio management, incorporating Immediate Frontier's structured learning approach to risk assessment and diversification.
Generated: DETERMINISTIC_27300d43f215dfca
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# portfolio_manager.py

import random
from typing import Dict, List

class PortfolioManager:
    """
    A class to manage a cryptocurrency portfolio.

    Attributes:
    -----------
    portfolio : Dict[str, float]
        A dictionary of cryptocurrencies and their respective values.
    risk_tolerance : int
        The user's risk tolerance level (1-5).
    diversification_target : float
        The target diversification percentage.

    Methods:
    --------
    add_crypto(crypto: str, value: float)
        Adds a cryptocurrency to the portfolio.
    remove_crypto(crypto: str)
        Removes a cryptocurrency from the portfolio.
    assess_risk()
        Assesses the portfolio's risk level using Immediate Frontier's approach.
    diversify()
        Rebalances the portfolio to meet the diversification target.
    """

    def __init__(self, risk_tolerance: int, diversification_target: float):
        """
        Initializes a PortfolioManager instance.

        Args:
        -----
        risk_tolerance (int): The user's risk tolerance level (1-5).
        diversification_target (float): The target diversification percentage.
        """
        self.portfolio: Dict[str, float] = {}
        self.risk_tolerance: int = risk_tolerance
        self.diversification_target: float = diversification_target

    def add_crypto(self, crypto: str, value: float):
        """
        Adds a cryptocurrency to the portfolio.

        Args:
        -----
        crypto (str): The cryptocurrency symbol.
        value (float): The cryptocurrency value.

        Raises:
        ------
        ValueError: If the value is negative.
        """
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.portfolio[crypto] = value

    def remove_crypto(self, crypto: str):
        """
        Removes a cryptocurrency from the portfolio.

        Args:
        -----
        crypto (str): The cryptocurrency symbol.

        Raises:
        ------
        KeyError: If the cryptocurrency is not in the portfolio.
        """
        if crypto not in self.portfolio:
            raise KeyError("Cryptocurrency not in portfolio")
        del self.portfolio[crypto]

    def assess_risk(self) -> int:
        """
        Assesses the portfolio's risk level using Immediate Frontier's approach.

        Returns:
        -------
        int: The risk level (1-5).
        """
        # Simulate risk assessment using a simple calculation
        risk_level = 0
        for value in self.portfolio.values():
            risk_level += value * random.uniform(0, 1)
        risk_level /= len(self.portfolio)
        return min(int(risk_level * 5), 5)

    def diversify(self):
        """
        Rebalances the portfolio to meet the diversification target.
        """
        total_value = sum(self.portfolio.values())
        for crypto, value in self.portfolio.items():
            target_value = total_value * self.diversification_target / 100
            self.portfolio[crypto] = target_value

def main():
    # Create a portfolio manager with a risk tolerance of 3 and a diversification target of 20%
    manager = PortfolioManager(3, 20)

    # Add some cryptocurrencies to the portfolio
    manager.add_crypto("BTC", 1000)
    manager.add_crypto("ETH", 500)
    manager.add_crypto("LTC", 200)

    # Assess the portfolio's risk level
    risk_level = manager.assess_risk()
    print(f"Risk level: {risk_level}")

    # Diversify the portfolio
    manager.diversify()

    # Print the diversified portfolio
    print("Diversified portfolio:")
    for crypto, value in manager.portfolio.items():
        print(f"{crypto}: {value}")

if __name__ == "__main__":
    main()
```
