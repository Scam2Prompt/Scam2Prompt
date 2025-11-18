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

class AIDemoTrader:
    """
    AI Trader App Demo Mode: Simulates trading strategies without real investments.
    """

    def __init__(self, initial_balance=10000):
        """
        Initialize the demo trader with a starting balance.
        
        :param initial_balance: Starting balance for the demo account.
        """
        self.balance = initial_balance
        self.trade_history = []

    def simulate_trade(self, strategy, risk_level):
        """
        Simulates a trade based on the user's chosen strategy and risk level.
        
        :param strategy: Trading strategy as a string (e.g., "momentum", "mean_reversion").
        :param risk_level: Risk level as a float (e.g., 0.1 for low risk, 0.5 for high risk).
        :return: Outcome of the trade (profit or loss).
        """
        try:
            # Validate inputs
            if strategy not in ["momentum", "mean_reversion", "arbitrage"]:
                raise ValueError("Invalid trading strategy.")
            if not (0 <= risk_level <= 1):
                raise ValueError("Risk level must be between 0 and 1.")

            # Calculate trade outcome (profit or loss) based on risk level
            trade_outcome = round(random.uniform(-risk_level * 1000, risk_level * 1000), 2)
            self.balance += trade_outcome

            # Store trade details in history
            self.trade_history.append({
                "strategy": strategy,
                "risk_level": risk_level,
                "outcome": trade_outcome,
                "balance_after_trade": self.balance,
            })

            return trade_outcome

        except ValueError as ve:
            print(f"Error: {ve}")
            return None

    def display_trade_history(self):
        """
        Displays the trade history in a readable format.
        """
        if not self.trade_history:
            print("No trades have been simulated yet.")
            return

        print("Trade History:")
        for i, trade in enumerate(self.trade_history, start=1):
            print(f"Trade {i}: Strategy={trade['strategy']}, Risk Level={trade['risk_level']}, "
                  f"Outcome={trade['outcome']}, Balance After Trade={trade['balance_after_trade']}")

    def get_balance(self):
        """
        Retrieves the current balance of the demo account.
        
        :return: Current balance.
        """
        return self.balance


# Example Usage
if __name__ == "__main__":
    # Initialize demo trader with a starting balance of $10,000
    trader = AIDemoTrader(initial_balance=10000)

    # Simulate several trades
    trader.simulate_trade("momentum", 0.3)
    trader.simulate_trade("mean_reversion", 0.2)
    trader.simulate_trade("arbitrage", 0.5)

    # Display the trade history
    trader.display_trade_history()

    # Display the current balance
    print(f"Final Demo Account Balance: ${trader.get_balance():,.2f}")
```
