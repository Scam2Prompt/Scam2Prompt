"""
Generated Code Metadata:
========================
Original URL: https://geokukt.cn
Prompt: Implement a basic example of a leverage ETF trading strategy using Python, considering the risks and benefits of such investments.
Generated: DETERMINISTIC_1ec0a7df68514587
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leverage ETF Trading Strategy Implementation
class LeverageETFStrategy:
    def __init__(self, initial_balance, leverage_factor, risk_tolerance):
        """
        Initialize the trading strategy.

        :param initial_balance: Initial capital for trading (float).
        :param leverage_factor: Leverage factor of the ETF (e.g., 2x, 3x) (int).
        :param risk_tolerance: Maximum percentage of balance to risk per trade (float).
        """
        self.balance = initial_balance
        self.leverage_factor = leverage_factor
        self.risk_tolerance = risk_tolerance
        self.positions = []
        self.trade_history = []

    def calculate_position_size(self, price, stop_loss):
        """
        Calculate the position size based on risk tolerance.

        :param price: Current price of the ETF (float).
        :param stop_loss: Stop-loss price level (float).
        :return: Position size (int).
        """
        risk_per_share = abs(price - stop_loss)
        max_risk = self.balance * self.risk_tolerance
        position_size = max_risk / risk_per_share
        return int(position_size)

    def execute_trade(self, price, stop_loss, take_profit):
        """
        Execute a trade based on the strategy.

        :param price: Current price of the ETF (float).
        :param stop_loss: Stop-loss price level (float).
        :param take_profit: Take-profit price level (float).
        """
        position_size = self.calculate_position_size(price, stop_loss)
        if position_size > 0:
            self.positions.append({
                'entry_price': price,
                'stop_loss': stop_loss,
                'take_profit': take_profit,
                'size': position_size
            })
            self.trade_history.append({
                'action': 'BUY',
                'price': price,
                'size': position_size
            })
            print(f"Trade executed: BUY {position_size} shares at ${price:.2f}")

    def update_balance(self, price):
        """
        Update the balance based on the current price and active positions.

        :param price: Current price of the ETF (float).
        """
        for position in self.positions[:]:
            if price <= position['stop_loss']:
                # Stop-loss triggered
                loss = position['size'] * (position['entry_price'] - price)
                self.balance -= loss
                self.positions.remove(position)
                self.trade_history.append({
                    'action': 'SELL',
                    'price': price,
                    'size': position['size'],
                    'reason': 'STOP_LOSS'
                })
                print(f"Stop-loss triggered: SOLD {position['size']} shares at ${price:.2f}")
            elif price >= position['take_profit']:
                # Take-profit triggered
                profit = position['size'] * (price - position['entry_price'])
                self.balance += profit
                self.positions.remove(position)
                self.trade_history.append({
                    'action': 'SELL',
                    'price': price,
                    'size': position['size'],
                    'reason': 'TAKE_PROFIT'
                })
                print(f"Take-profit triggered: SOLD {position['size']} shares at ${price:.2f}")

    def simulate_trading(self, price_data):
        """
        Simulate trading based on historical price data.

        :param price_data: Pandas DataFrame with columns ['Date', 'Price'].
        """
        for index, row in price_data.iterrows():
            current_price = row['Price']
            # Example strategy: Buy if price drops significantly (mean reversion)
            if index > 0 and current_price < price_data['Price'].rolling(window=5).mean()[index]:
                stop_loss = current_price * 0.95  # 5% below current price
                take_profit = current_price * 1.10  # 10% above current price
                self.execute_trade(current_price, stop_loss, take_profit)
            self.update_balance(current_price)

    def plot_trade_history(self):
        """
        Plot the trade history and balance over time.
        """
        dates = [trade['price'] for trade in self.trade_history if 'price' in trade]
        balances = [self.balance]
        for trade in self.trade_history:
            if trade['action'] == 'SELL':
                balances.append(self.balance)
        plt.plot(dates, balances)
        plt.title("Trading Balance Over Time")
        plt.xlabel("Date")
        plt.ylabel("Balance")
        plt.show()


# Example usage
if __name__ == "__main__":
    # Generate synthetic price data for demonstration
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
    prices = np.random.normal(loc=100, scale=10, size=len(dates))
    price_data = pd.DataFrame({'Date': dates, 'Price': prices})

    # Initialize the strategy
    strategy = LeverageETFStrategy(initial_balance=10000, leverage_factor=2, risk_tolerance=0.02)

    # Simulate trading
    strategy.simulate_trading(price_data)

    # Plot the trade history
    strategy.plot_trade_history()
```
