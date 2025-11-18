"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarlado.com
Prompt: Write a script to simulate leverage-based trading for CFDs, incorporating risk management strategies similar to those described on Emarlado's website.
Generated: DETERMINISTIC_4af9a4b2458fa7e3
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CFDTradingSimulator:
    def __init__(self, initial_balance, leverage, risk_per_trade):
        """
        Initializes the CFD Trading Simulator.

        :param initial_balance: Starting balance for the trading account.
        :param leverage: Leverage ratio (e.g., 10 for 10:1 leverage).
        :param risk_per_trade: Percentage of balance to risk on each trade (0-1).
        """
        self.balance = initial_balance
        self.leverage = leverage
        self.risk_per_trade = risk_per_trade
        self.position_size = 0
        self.trade_history = []

    def calculate_position_size(self):
        """
        Calculates the position size based on the risk management strategy.
        This uses the formula: Position Size = (Balance * Risk Per Trade) / Stop Loss
        For this simulation, we'll assume a fixed stop loss distance.
        """
        stop_loss = 50  # Assume a fixed stop loss distance of 50 pips
        risk_amount = self.balance * self.risk_per_trade
        self.position_size = risk_amount / stop_loss

    def open_trade(self, direction, entry_price):
        """
        Opens a trade in the specified direction.

        :param direction: 'buy' or 'sell' to indicate the direction of the trade.
        :param entry_price: Price at which the trade is opened.
        """
        if self.balance <= 0:
            raise ValueError("Insufficient balance to open a trade.")
        
        self.calculate_position_size()
        trade_value = self.position_size * self.leverage
        
        # Simulating price movement for the trade
        price_movement = random.uniform(-100, 100)  # Random price movement in pips
        exit_price = entry_price + price_movement if direction == 'buy' else entry_price - price_movement
        
        # Calculate profit or loss
        if direction == 'buy':
            profit_loss = (exit_price - entry_price) * self.position_size
        else:
            profit_loss = (entry_price - exit_price) * self.position_size

        # Update balance
        self.balance += profit_loss
        self.trade_history.append({
            'direction': direction,
            'entry_price': entry_price,
            'exit_price': exit_price,
            'profit_loss': profit_loss,
            'balance_after_trade': self.balance
        })

    def print_trade_history(self):
        """Prints the trade history in a readable format."""
        for trade in self.trade_history:
            print(f"Trade: {trade['direction'].capitalize()}, Entry: {trade['entry_price']}, "
                  f"Exit: {trade['exit_price']}, P/L: {trade['profit_loss']:.2f}, "
                  f"Balance: {trade['balance_after_trade']:.2f}")

def main():
    try:
        # Initialize the trading simulator with an initial balance, leverage, and risk per trade
        simulator = CFDTradingSimulator(initial_balance=10000, leverage=10, risk_per_trade=0.02)

        # Simulating a series of trades
        trades_to_simulate = 10
        for _ in range(trades_to_simulate):
            direction = random.choice(['buy', 'sell'])
            entry_price = random.uniform(100, 200)  # Random entry price
            simulator.open_trade(direction, entry_price)

        # Print trade history and final balance
        simulator.print_trade_history()
        print(f"Final Balance: {simulator.balance:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
