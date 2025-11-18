"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xotanex.com
Prompt: Generate code to track and log recent trading activity on Xotanex, including user actions like buying shares in prediction markets.
Generated: DETERMINISTIC_46d3fac1b954f5dd
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging to log to a file with a specific format
logging.basicConfig(
    filename='trading_activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TradeLogger:
    """Class to log trading activities for users in the Xotanex platform."""
    
    def __init__(self):
        """Initialize the TradeLogger."""
        self.actions = []

    def log_trade(self, user_id, action, shares, price):
        """
        Log a trading action.

        Parameters:
            user_id (str): The ID of the user performing the action.
            action (str): The action performed (e.g., 'buy', 'sell').
            shares (int): The number of shares involved in the trade.
            price (float): The price per share at which the trade occurred.
        """
        try:
            # Validate inputs
            if shares <= 0:
                raise ValueError("Shares must be greater than zero.")
            if price <= 0.0:
                raise ValueError("Price must be greater than zero.")

            # Prepare the log entry
            entry = {
                'user_id': user_id,
                'action': action,
                'shares': shares,
                'price': price,
                'timestamp': datetime.now().isoformat()
            }
            self.actions.append(entry)
            logging.info(f"Trade logged: {entry}")
        except Exception as e:
            logging.error(f"Error logging trade: {str(e)}")

    def get_recent_trades(self):
        """Retrieve recent trade actions."""
        return self.actions

# Example usage
if __name__ == "__main__":
    trade_logger = TradeLogger()
    
    # Simulate user actions
    try:
        trade_logger.log_trade(user_id="user123", action="buy", shares=10, price=15.5)
        trade_logger.log_trade(user_id="user456", action="sell", shares=5, price=20.0)
        
        # Print recent trades
        recent_trades = trade_logger.get_recent_trades()
        for trade in recent_trades:
            print(trade)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
