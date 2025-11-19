"""
Generated Code Metadata:
========================
Original URL: https://czanr.cn
Prompt: What are the advantages of using OKX's unified trading account for managing a portfolio of cryptocurrencies and derivatives, and how does it differ from traditional exchange accounts?
Generated: DETERMINISTIC_572d8599a1853be6
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UnifiedTradingAccount:
    """
    A class to represent a unified trading account for managing a portfolio of cryptocurrencies and derivatives.
    """

    def __init__(self):
        """
        Initializes the unified trading account with empty portfolios for cryptocurrencies and derivatives.
        """
        self.crypto_portfolio = {}
        self.derivative_portfolio = {}

    def add_crypto(self, asset: str, amount: float):
        """
        Adds a specified amount of a cryptocurrency to the portfolio.

        :param asset: The cryptocurrency asset to add.
        :param amount: The amount of the cryptocurrency to add.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        if asset in self.crypto_portfolio:
            self.crypto_portfolio[asset] += amount
        else:
            self.crypto_portfolio[asset] = amount

    def add_derivative(self, asset: str, amount: float):
        """
        Adds a specified amount of a derivative to the portfolio.

        :param asset: The derivative asset to add.
        :param amount: The amount of the derivative to add.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        if asset in self.derivative_portfolio:
            self.derivative_portfolio[asset] += amount
        else:
            self.derivative_portfolio[asset] = amount

    def get_portfolio_summary(self):
        """
        Returns a summary of the current portfolios for cryptocurrencies and derivatives.

        :return: A dictionary containing the summary of both portfolios.
        """
        return {
            "cryptocurrencies": self.crypto_portfolio,
            "derivatives": self.derivative_portfolio
        }

    def total_value(self, crypto_prices: dict, derivative_prices: dict) -> float:
        """
        Calculates the total value of the portfolios based on current market prices.

        :param crypto_prices: A dictionary mapping cryptocurrency assets to their current prices.
        :param derivative_prices: A dictionary mapping derivative assets to their current prices.
        :return: The total value of the portfolios.
        :raises KeyError: If an asset in the portfolio does not have a corresponding price.
        """
        total = 0.0
        
        # Calculate total value of cryptocurrencies
        for asset, amount in self.crypto_portfolio.items():
            if asset not in crypto_prices:
                raise KeyError(f"Price for {asset} not found.")
            total += amount * crypto_prices[asset]

        # Calculate total value of derivatives
        for asset, amount in self.derivative_portfolio.items():
            if asset not in derivative_prices:
                raise KeyError(f"Price for {asset} not found.")
            total += amount * derivative_prices[asset]

        return total

# Example usage
if __name__ == "__main__":
    try:
        trading_account = UnifiedTradingAccount()
        trading_account.add_crypto("BTC", 0.5)
        trading_account.add_crypto("ETH", 2.0)
        trading_account.add_derivative("BTC-Options", 1)
        
        print("Portfolio Summary:", trading_account.get_portfolio_summary())
        
        # Example market prices
        crypto_prices = {"BTC": 60000, "ETH": 4000}
        derivative_prices = {"BTC-Options": 500}
        
        total_value = trading_account.total_value(crypto_prices, derivative_prices)
        print("Total Portfolio Value:", total_value)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
