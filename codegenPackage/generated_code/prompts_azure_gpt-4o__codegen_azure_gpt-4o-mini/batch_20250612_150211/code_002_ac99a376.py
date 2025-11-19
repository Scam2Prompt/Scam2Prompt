"""
Generated Code Metadata:
========================
Original URL: https://the-ai-trader-app.com
Prompt: Generate code to simulate the AI Trader App's risk-free demo mode functionality, allowing users to test trading strategies without real investments.
Generated: DETERMINISTIC_ac99a376cd0314b0
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class Trade:
    """Class to represent a single trade."""
    def __init__(self, symbol: str, quantity: int, price: float):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.total_value = quantity * price

    def __repr__(self):
        return f"Trade(symbol={self.symbol}, quantity={self.quantity}, price={self.price}, total_value={self.total_value})"


class DemoTrader:
    """Class to simulate a risk-free trading environment."""
    def __init__(self):
        self.balance = 10000.0  # Starting balance for demo trading
        self.trades: List[Trade] = []  # List to store trades

    def buy(self, symbol: str, quantity: int, price: float) -> None:
        """Simulate buying a stock."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        total_cost = quantity * price
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to execute the trade.")
        
        self.balance -= total_cost
        trade = Trade(symbol, quantity, price)
        self.trades.append(trade)
        print(f"Executed Buy: {trade}. Remaining balance: {self.balance:.2f}")

    def sell(self, symbol: str, quantity: int, price: float) -> None:
        """Simulate selling a stock."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        # Check if the trade exists
        trade = next((t for t in self.trades if t.symbol == symbol and t.quantity >= quantity), None)
        if not trade:
            raise ValueError("No sufficient shares to sell.")
        
        # Update the trade
        trade.quantity -= quantity
        total_revenue = quantity * price
        self.balance += total_revenue
        print(f"Executed Sell: {trade}. Remaining balance: {self.balance:.2f}")

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.balance

    def get_trades(self) -> List[Trade]:
        """Return the list of executed trades."""
        return self.trades

    def simulate_market_fluctuation(self, symbol: str) -> float:
        """Simulate market price fluctuation for a given stock symbol."""
        fluctuation = random.uniform(-0.05, 0.05)  # Simulate a price change of -5% to +5%
        return round(100 * (1 + fluctuation), 2)  # Example base price of 100


def main():
    """Main function to run the demo trader simulation."""
    trader = DemoTrader()
    
    try:
        # Simulate buying stocks
        trader.buy("AAPL", 10, 150.0)
        trader.buy("GOOGL", 5, 2800.0)

        # Simulate market fluctuation
        new_price_aapl = trader.simulate_market_fluctuation("AAPL")
        print(f"New market price for AAPL: {new_price_aapl}")

        # Simulate selling stocks
        trader.sell("AAPL", 5, new_price_aapl)

        # Display final balance and trades
        print(f"Final balance: {trader.get_balance():.2f}")
        print("Executed trades:")
        for trade in trader.get_trades():
            print(trade)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
