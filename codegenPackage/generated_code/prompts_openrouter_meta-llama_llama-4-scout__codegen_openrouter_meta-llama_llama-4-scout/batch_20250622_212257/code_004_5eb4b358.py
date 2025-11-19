"""
Generated Code Metadata:
========================
Original URL: https://fomoportfolio.xyz
Prompt: "Design a system to monitor and alert on significant changes in cryptocurrency portfolios using FOMO."
Generated: DETERMINISTIC_5eb4b3586dd914a7
Batch ID: 20250622_212257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import ccxt
import time
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoPortfolioMonitor:
    def __init__(self, exchange_id: str, api_key: str, api_secret: str, portfolio: Dict[str, float]):
        """
        Initialize the CryptoPortfolioMonitor.

        Args:
        - exchange_id (str): The ID of the exchange (e.g., 'binance', 'kraken', etc.)
        - api_key (str): The API key for the exchange
        - api_secret (str): The API secret for the exchange
        - portfolio (Dict[str, float]): A dictionary of cryptocurrencies and their respective amounts
        """
        self.exchange_id = exchange_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.portfolio = portfolio
        self.exchange = self._get_exchange()

    def _get_exchange(self):
        """
        Get the exchange object based on the exchange ID.

        Returns:
        - exchange (ccxt.Exchange): The exchange object
        """
        try:
            exchange = getattr(ccxt, self.exchange_id)({
                'apiKey': self.api_key,
                'apiSecret': self.api_secret,
            })
            exchange.load_markets()
            return exchange
        except AttributeError:
            logging.error(f"Unsupported exchange: {self.exchange_id}")
            raise

    def get_current_prices(self) -> Dict[str, float]:
        """
        Get the current prices of the cryptocurrencies in the portfolio.

        Returns:
        - prices (Dict[str, float]): A dictionary of cryptocurrencies and their current prices
        """
        try:
            prices = {}
            for symbol in self.portfolio:
                ticker = self.exchange.fetch_ticker(symbol)
                prices[symbol] = ticker['close']
            return prices
        except Exception as e:
            logging.error(f"Failed to get current prices: {str(e)}")
            raise

    def calculate_portfolio_value(self, prices: Dict[str, float]) -> float:
        """
        Calculate the total value of the portfolio.

        Args:
        - prices (Dict[str, float]): A dictionary of cryptocurrencies and their current prices

        Returns:
        - portfolio_value (float): The total value of the portfolio
        """
        portfolio_value = 0
        for symbol, amount in self.portfolio.items():
            portfolio_value += amount * prices[symbol]
        return portfolio_value

    def monitor_portfolio(self):
        """
        Monitor the portfolio and alert on significant changes.
        """
        previous_portfolio_value = None
        while True:
            try:
                current_prices = self.get_current_prices()
                current_portfolio_value = self.calculate_portfolio_value(current_prices)
                if previous_portfolio_value is not None:
                    change_percentage = ((current_portfolio_value - previous_portfolio_value) / previous_portfolio_value) * 100
                    if abs(change_percentage) > 5:  # Adjust the threshold as needed
                        logging.warning(f"Significant change in portfolio value: {change_percentage:.2f}%")
                        # Add alerting logic here (e.g., send email, SMS, etc.)
                previous_portfolio_value = current_portfolio_value
            except Exception as e:
                logging.error(f"Failed to monitor portfolio: {str(e)}")
            time.sleep(60)  # Adjust the interval as needed

if __name__ == "__main__":
    # Example usage
    exchange_id = "binance"
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"
    portfolio = {
        "BTC/USDT": 1.0,
        "ETH/USDT": 5.0,
    }

    monitor = CryptoPortfolioMonitor(exchange_id, api_key, api_secret, portfolio)
    monitor.monitor_portfolio()
```
