"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatefrontier.app
Prompt: Create a program that simulates cryptocurrency portfolio management, incorporating Immediate Frontier's structured learning approach to risk assessment and diversification.
Generated: DETERMINISTIC_27300d43f215dfca
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class Cryptocurrency:
    """
    Represents a cryptocurrency with its attributes.
    """
    
    def __init__(self, name: str, symbol: str, price: float, risk_factor: float):
        """
        Initializes the Cryptocurrency instance.

        :param name: The full name of the cryptocurrency.
        :param symbol: The symbol for the cryptocurrency.
        :param price: The current price of the cryptocurrency.
        :param risk_factor: The associated risk factor of the cryptocurrency (0.0 to 1.0).
        """
        self.name = name
        self.symbol = symbol
        self.price = price
        self.risk_factor = risk_factor

class Portfolio:
    """
    Manages a cryptocurrency portfolio.
    """

    def __init__(self):
        """ Initializes an empty portfolio. """
        self.assets: Dict[str, float] = {}  # Stores cryptocurrency symbols and their quantities

    def add_asset(self, crypto: Cryptocurrency, quantity: float):
        """
        Adds a cryptocurrency to the portfolio.

        :param crypto: The cryptocurrency to add.
        :param quantity: The amount of the cryptocurrency to add.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.assets[crypto.symbol] = self.assets.get(crypto.symbol, 0) + quantity

    def total_value(self, market_data: Dict[str, float]) -> float:
        """
        Calculates the total value of the portfolio based on current market prices.

        :param market_data: Dictionary of cryptocurrency symbols and their current market prices.
        :return: Total value of the portfolio.
        """
        total = 0.0
        for symbol, quantity in self.assets.items():
            price = market_data.get(symbol)
            if price is None:
                raise ValueError(f"Market data for {symbol} is not available.")
            total += price * quantity
        return total

    def assess_risk(self) -> float:
        """
        Assesses the overall risk of the portfolio based on the risk factors of the assets.

        :return: Overall risk score (0.0 - 1.0).
        """
        if not self.assets:
            return 0.0
        
        total_risk = 0.0
        total_assets = len(self.assets)

        for symbol in self.assets:
            # Randomly simulate risk factor for demonstration; in reality, fetch actual data
            risk_factor = random.uniform(0.0, 1.0)  
            total_risk += risk_factor
        
        return total_risk / total_assets if total_assets > 0 else 0.0

def main():
    """
    Main function to simulate cryptocurrency portfolio management.
    """
    try:
        # Sample cryptocurrencies
        bitcoin = Cryptocurrency("Bitcoin", "BTC", 50000, 0.8)
        ethereum = Cryptocurrency("Ethereum", "ETH", 4000, 0.6)
        litecoin = Cryptocurrency("Litecoin", "LTC", 200, 0.4)

        # Create a portfolio and add assets
        portfolio = Portfolio()
        portfolio.add_asset(bitcoin, 0.5)
        portfolio.add_asset(ethereum, 2)
        portfolio.add_asset(litecoin, 10)

        # Simulated market data
        market_data = {
            "BTC": 51000,
            "ETH": 4100,
            "LTC": 210,
        }

        # Calculate total value and assess risk
        total_portfolio_value = portfolio.total_value(market_data)
        portfolio_risk = portfolio.assess_risk()

        print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")
        print(f"Portfolio Risk Assessment: {portfolio_risk:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
