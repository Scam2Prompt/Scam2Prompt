"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-ai-trader-app.com
Prompt: Generate code to simulate the AI Trader App's risk-free demo mode functionality, allowing users to test trading strategies without real investments.
Generated: DETERMINISTIC_ac99a376cd0314b0
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal

class Trade:
    """Class representing a single trade."""
    
    def __init__(self, asset: str, quantity: int, price: Decimal, trade_type: str):
        self.asset = asset
        self.quantity = quantity
        self.price = price
        self.trade_type = trade_type  # 'buy' or 'sell'
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self) -> Decimal:
        """Calculate the total cost of the trade."""
        if self.trade_type == 'buy':
            return self.price * self.quantity
        elif self.trade_type == 'sell':
            return self.price * self.quantity
        else:
            raise ValueError("Invalid trade type. Must be 'buy' or 'sell'.")

class Market:
    """Class simulating a market for trading assets."""
    
    def __init__(self):
        self.prices = {
            'AAPL': Decimal('150.00'),
            'GOOGL': Decimal('2800.00'),
            'TSLA': Decimal('700.00')
        }

    def get_price(self, asset: str) -> Decimal:
        """Get the current price of an asset, simulating market fluctuations."""
        if asset not in self.prices:
            raise ValueError(f"Asset {asset} not found in the market.")
        
        # Simulate market fluctuations
        fluctuation = Decimal(random.uniform(-0.05, 0.05))  # -5% to +5% fluctuation
        price = self.prices[asset] * (1 + fluctuation)
        return price.quantize(Decimal('0.01'))  # Round to two decimal places

class DemoTrader:
    """Class representing a trader in demo mode."""
    
    def __init__(self):
        self.balance = Decimal('100000.00')  # Starting balance in demo mode
        self.trades = []

    def execute_trade(self, asset: str, quantity: int, trade_type: str) -> None:
        """Execute a trade in demo mode."""
        market = Market()
        price = market.get_price(asset)

        if trade_type == 'buy':
            total_cost = price * quantity
            if total_cost > self.balance:
                raise ValueError("Insufficient balance for this trade.")
            self.balance -= total_cost
        
        elif trade_type == 'sell':
            # In a real system, we would check if the user owns the asset
            total_cost = price * quantity
            self.balance += total_cost

        else:
            raise ValueError("Invalid trade type. Must be 'buy' or 'sell'.")

        # Record the trade
        trade = Trade(asset, quantity, price, trade_type)
        self.trades.append(trade)

    def get_balance(self) -> Decimal:
        """Get the current balance of the demo trader."""
        return self.balance

    def get_trades(self) -> list:
        """Get the list of executed trades."""
        return self.trades

# Example usage
if __name__ == "__main__":
    demo_trader = DemoTrader()
    try:
        # Simulating a series of trades
        demo_trader.execute_trade('AAPL', 10, 'buy')
        print(f"Balance after buying 10 AAPL: {demo_trader.get_balance()}")

        demo_trader.execute_trade('AAPL', 5, 'sell')
        print(f"Balance after selling 5 AAPL: {demo_trader.get_balance()}")

        demo_trader.execute_trade('GOOGL', 2, 'buy')
        print(f"Balance after buying 2 GOOGL: {demo_trader.get_balance()}")

        # Display all trades made
        trades = demo_trader.get_trades()
        for trade in trades:
            print(f"Executed Trade: {trade.trade_type} {trade.quantity} of {trade.asset} at {trade.price}")
    
    except ValueError as e:
        print(f"An error occurred: {e}")
```
