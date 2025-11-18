"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-intal-24.com
Prompt: Generate code to simulate trades using Immediate Intal 24's demo account feature and test trading strategies without risking real funds.
Generated: DETERMINISTIC_0135126a96fd8cc9
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class TradeSimulator:
    """
    A class to simulate trading on Immediate Intal 24's demo account feature.
    This class allows for testing trading strategies without risking real funds.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes the trade simulator with a given initial balance.
        
        :param initial_balance: Starting balance for the demo account.
        """
        self.balance = initial_balance
        self.trades = []

    def execute_trade(self, instrument, trade_type, amount):
        """
        Executes a simulated trade and updates the account balance.
        
        :param instrument: The trading instrument (e.g., 'EUR/USD').
        :param trade_type: The type of trade ('buy' or 'sell').
        :param amount: The amount to trade.
        """
        if amount <= 0:
            raise ValueError("Trade amount must be positive.")
        
        if trade_type not in ['buy', 'sell']:
            raise ValueError("Trade type must be 'buy' or 'sell'.")
        
        if amount > self.balance:
            raise ValueError("Insufficient balance for the trade.")
        
        price = self.simulate_market_price(instrument)
        trade_result = self.calculate_trade_result(trade_type, price, amount)
        
        # Update balance and record the trade
        self.balance += trade_result
        self.trades.append({
            'instrument': instrument,
            'trade_type': trade_type,
            'amount': amount,
            'price': price,
            'result': trade_result,
            'balance': self.balance
        })
        
        print(f"Executed {trade_type} trade on {instrument} for {amount} at {price}. "
              f"New balance: {self.balance}.")

    def simulate_market_price(self, instrument):
        """
        Simulates the current market price of a given instrument.
        
        :param instrument: The trading instrument.
        :return: A simulated market price.
        """
        # Random price generation for simulation
        return round(random.uniform(1.0, 1.5), 4)  # Simulate price between 1.0 and 1.5

    def calculate_trade_result(self, trade_type, price, amount):
        """
        Calculates the result of the trade based on its type.
        
        :param trade_type: The type of trade ('buy' or 'sell').
        :param price: The market price at which the trade was executed.
        :param amount: The amount of the trade.
        :return: The result of the trade (profit or loss).
        """
        # Simulate a random market movement
        market_movement = random.uniform(-0.05, 0.05)  # Simulate price movement
        final_price = price + market_movement
        
        if trade_type == 'buy':
            return (final_price - price) * amount
        elif trade_type == 'sell':
            return (price - final_price) * amount

    def get_balance(self):
        """
        Returns the current account balance.
        
        :return: The current balance.
        """
        return self.balance

    def get_trade_history(self):
        """
        Returns the history of executed trades.
        
        :return: A list of executed trades.
        """
        return self.trades

if __name__ == "__main__":
    simulator = TradeSimulator()

    # Example trades
    try:
        simulator.execute_trade('EUR/USD', 'buy', 100)
        time.sleep(1)  # Simulate delay between trades
        simulator.execute_trade('EUR/USD', 'sell', 50)
        time.sleep(1)  # Simulate delay between trades
        print("Current balance:", simulator.get_balance())
        print("Trade history:", simulator.get_trade_history())
    except ValueError as e:
        print(f"Error: {e}")
```
