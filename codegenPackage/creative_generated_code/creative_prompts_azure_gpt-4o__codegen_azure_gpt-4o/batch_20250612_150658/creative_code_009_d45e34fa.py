"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonroll.cc
Prompt: Develop a risk management algorithm for a cryptocurrency trading app that limits losses to 2% per transaction and diversifies trades across multiple professional traders, as described on the Earnie website.
Generated: DETERMINISTIC_d45e34fae90bf346
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class RiskManagement:
    """
    A class to manage risk in cryptocurrency trading.
    Ensures trades are limited to a maximum loss of 2% and diversified across multiple traders.
    """

    def __init__(self, total_balance: float, max_loss_percent: float = 2.0):
        """
        Initializes the RiskManagement system.
        
        :param total_balance: The total balance available for trading.
        :param max_loss_percent: The maximum allowable loss per transaction (default is 2%).
        """
        if total_balance <= 0:
            raise ValueError("Total balance must be greater than zero.")
        self.total_balance = total_balance
        self.max_loss = total_balance * (max_loss_percent / 100)
        self.trades = []  # List to store trade details

    def allocate_trade(self, trader_id: str, trade_amount: float, trade_risk_percent: float):
        """
        Allocates a trade to a specific trader ensuring risk constraints are met.
        
        :param trader_id: Unique identifier for the trader.
        :param trade_amount: The amount to be allocated for the trade.
        :param trade_risk_percent: Estimated risk percentage for this trade.
        :raises ValueError: If trade_amount exceeds total_balance or trade_risk_percent violates risk limits.
        """
        if trade_amount > self.total_balance:
            raise ValueError("Trade amount exceeds available balance.")
        if trade_risk_percent > 2.0:
            raise ValueError("Trade risk exceeds 2% limit.")
        
        trade_id = str(uuid.uuid4())  # Generate a unique trade ID
        trade_details = {
            "trade_id": trade_id,
            "trader_id": trader_id,
            "trade_amount": trade_amount,
            "trade_risk_percent": trade_risk_percent,
            "max_loss": trade_amount * (trade_risk_percent / 100)
        }
        
        # Ensure the calculated loss for this trade doesn't exceed the max allowable loss
        if trade_details["max_loss"] > self.max_loss:
            raise ValueError("Trade's max loss exceeds allowable risk limit.")
        
        self.trades.append(trade_details)
        self.total_balance -= trade_amount  # Deduct trade amount from total balance
        return trade_details

    def get_trade_summary(self):
        """
        Provides a summary of all allocated trades.
        
        :return: List of trade details.
        """
        return self.trades

    def reset_system(self, new_total_balance: float):
        """
        Resets the risk management system with a new total balance.
        
        :param new_total_balance: The new total balance to reset the system.
        :raises ValueError: If the new total balance is invalid.
        """
        if new_total_balance <= 0:
            raise ValueError("New total balance must be greater than zero.")
        
        self.total_balance = new_total_balance
        self.trades = []  # Clear all existing trades


# Example usage (should be removed in production code):
if __name__ == "__main__":
    try:
        # Initialize risk management system with a $10,000 balance
        risk_manager = RiskManagement(total_balance=10000)

        # Allocate trades (example values)
        trade1 = risk_manager.allocate_trade(trader_id="Trader1", trade_amount=2000, trade_risk_percent=1.5)
        trade2 = risk_manager.allocate_trade(trader_id="Trader2", trade_amount=1500, trade_risk_percent=2.0)

        # Print trade summary
        print("Trade Summary:", risk_manager.get_trade_summary())

        # Reset system with new balance
        risk_manager.reset_system(new_total_balance=12000)
        print("System reset. New balance:", risk_manager.total_balance)

    except ValueError as e:
        print("Error:", str(e))
```
