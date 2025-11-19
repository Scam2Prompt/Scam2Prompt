"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-lifestyle-pro.com
Prompt: Develop a Python program that demonstrates how to implement demo trading functionality, allowing users to practice cryptocurrency trading with virtual funds before transitioning to live trading.
Generated: DETERMINISTIC_947d15e8afc49b8b
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class DemoTrader:
    """
    A demo trading system that simulates cryptocurrency trading with virtual funds.
    Users can practice trading without risking real money.
    """

    def __init__(self, initial_balance: float = 10000.0):
        """
        Initialize the demo trading account with a virtual balance.

        Args:
            initial_balance (float): Starting virtual balance in USD. Default is 10,000.
        """
        self.balance: float = initial_balance
        self.portfolio: Dict[str, float] = {}  # {crypto_symbol: amount_held}
        self.trade_history: List[Dict] = []
        self.current_prices: Dict[str, float] = self._fetch_current_prices()

    def _fetch_current_prices(self) -> Dict[str, float]:
        """
        Simulate fetching current cryptocurrency prices from an API.
        In a real implementation, this would connect to a price feed API.

        Returns:
            Dict[str, float]: Dictionary of crypto symbols and their current prices.
        """
        # Simulated prices for demo purposes
        return {
            "BTC": random.uniform(35000, 45000),
            "ETH": random.uniform(2000, 3000),
            "SOL": random.uniform(50, 150),
            "ADA": random.uniform(0.3, 0.7),
            "DOGE": random.uniform(0.05, 0.15),
        }

    def _update_prices(self) -> None:
        """Update the current prices with slight random fluctuations."""
        for symbol in self.current_prices:
            current = self.current_prices[symbol]
            self.current_prices[symbol] = current * random.uniform(0.98, 1.02)

    def get_balance(self) -> float:
        """Get the current USD balance."""
        return self.balance

    def get_portfolio(self) -> Dict[str, float]:
        """Get the current cryptocurrency holdings."""
        return self.portfolio

    def get_portfolio_value(self) -> float:
        """Calculate the total value of the portfolio in USD."""
        total = self.balance
        for symbol, amount in self.portfolio.items():
            if symbol in self.current_prices:
                total += amount * self.current_prices[symbol]
        return total

    def get_trade_history(self) -> List[Dict]:
        """Get the history of all trades made."""
        return self.trade_history

    def get_current_price(self, symbol: str) -> Optional[float]:
        """
        Get the current price of a cryptocurrency.

        Args:
            symbol (str): Cryptocurrency symbol (e.g., "BTC").

        Returns:
            Optional[float]: Current price if symbol exists, None otherwise.
        """
        return self.current_prices.get(symbol.upper())

    def buy(self, symbol: str, amount_usd: float) -> Tuple[bool, str]:
        """
        Execute a buy order for a cryptocurrency using virtual funds.

        Args:
            symbol (str): Cryptocurrency symbol to buy.
            amount_usd (float): Amount in USD to spend.

        Returns:
            Tuple[bool, str]: (success, message) indicating trade status.
        """
        symbol = symbol.upper()
        if amount_usd <= 0:
            return False, "Amount must be positive."

        if amount_usd > self.balance:
            return False, "Insufficient funds."

        if symbol not in self.current_prices:
            return False, f"Unsupported cryptocurrency: {symbol}."

        price = self.current_prices[symbol]
        crypto_amount = amount_usd / price

        # Execute trade
        self.balance -= amount_usd
        self.portfolio[symbol] = self.portfolio.get(symbol, 0.0) + crypto_amount

        # Record trade
        trade = {
            "type": "BUY",
            "symbol": symbol,
            "amount_usd": amount_usd,
            "crypto_amount": crypto_amount,
            "price": price,
            "timestamp": datetime.now().isoformat(),
        }
        self.trade_history.append(trade)
        self._update_prices()

        return True, f"Successfully bought {crypto_amount:.6f} {symbol} for ${amount_usd:.2f}."

    def sell(self, symbol: str, amount: float) -> Tuple[bool, str]:
        """
        Execute a sell order for a cryptocurrency.

        Args:
            symbol (str): Cryptocurrency symbol to sell.
            amount (float): Amount of cryptocurrency to sell.

        Returns:
            Tuple[bool, str]: (success, message) indicating trade status.
        """
        symbol = symbol.upper()
        if amount <= 0:
            return False, "Amount must be positive."

        if symbol not in self.portfolio or self.portfolio[symbol] < amount:
            return False, f"Insufficient {symbol} holdings."

        if symbol not in self.current_prices:
            return False, f"Unsupported cryptocurrency: {symbol}."

        price = self.current_prices[symbol]
        usd_amount = amount * price

        # Execute trade
        self.balance += usd_amount
        self.portfolio[symbol] -= amount

        # Clean up if holdings reach zero
        if self.portfolio[symbol] < 1e-8:  # Floating point precision threshold
            del self.portfolio[symbol]

        # Record trade
        trade = {
            "type": "SELL",
            "symbol": symbol,
            "amount_usd": usd_amount,
            "crypto_amount": amount,
            "price": price,
            "timestamp": datetime.now().isoformat(),
        }
        self.trade_history.append(trade)
        self._update_prices()

        return True, f"Successfully sold {amount:.6f} {symbol} for ${usd_amount:.2f}."

    def save_state(self, filename: str = "demo_trader_state.json") -> bool:
        """
        Save the current state of the demo trader to a file.

        Args:
            filename (str): File to save the state to.

        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            state = {
                "balance": self.balance,
                "portfolio": self.portfolio,
                "trade_history": self.trade_history,
                "current_prices": self.current_prices,
            }
            with open(filename, "w") as f:
                json.dump(state, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False

    def load_state(self, filename: str = "demo_trader_state.json") -> bool:
        """
        Load a previously saved state of the demo trader.

        Args:
            filename (str): File to load the state from.

        Returns:
            bool: True if load was successful, False otherwise.
        """
        try:
            with open(filename, "r") as f:
                state = json.load(f)
            self.balance = state["balance"]
            self.portfolio = state["portfolio"]
            self.trade_history = state["trade_history"]
            self.current_prices = state["current_prices"]
            return True
        except FileNotFoundError:
            print("No saved state found. Starting fresh.")
            return False
        except Exception as e:
            print(f"Error loading state: {e}")
            return False


# Example usage
if __name__ == "__main__":
    trader = DemoTrader()

    # Display initial state
    print(f"Initial balance: ${trader.get_balance():.2f}")
    print("Current prices:")
    for symbol, price in trader.current_prices.items():
        print(f"  {symbol}: ${price:.2f}")

    # Execute some trades
    trader.buy("BTC", 1000)
    trader.buy("ETH", 500)
    trader.sell("BTC", 0.02)

    # Display results
    print(f"\nCurrent balance: ${trader.get_balance():.2f}")
    print(f"Portfolio value: ${trader.get_portfolio_value():.2f}")
    print("Portfolio holdings:")
    for symbol, amount in trader.get_portfolio().items():
        print(f"  {symbol}: {amount:.6f}")

    # Save state
    trader.save_state()
```
