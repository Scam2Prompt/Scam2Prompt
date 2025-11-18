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
import os

# Set up logging
LOG_FILE = "trading_activity.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define a TradingActivity class to encapsulate the logic
class TradingActivityTracker:
    def __init__(self):
        # Initialize an empty list to hold recent trading activities
        self.recent_activities = []

    def log_activity(self, username, action, market, shares, price):
        """
        Logs a trading activity and keeps a record of recent activities.
        
        :param username: The name of the user performing the action
        :param action: The action performed (e.g., "buy", "sell")
        :param market: The prediction market involved
        :param shares: The number of shares involved
        :param price: The price per share
        """
        try:
            # Create a record of the activity
            activity = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "username": username,
                "action": action,
                "market": market,
                "shares": shares,
                "price": price
            }

            # Log the activity to file
            logging.info(
                f"User '{username}' performed '{action}' on market '{market}' with {shares} shares at ${price:.2f}/share."
            )

            # Store activity in memory (recent activities list)
            self.recent_activities.append(activity)

            # Limit the size of the recent activities list to the last 50
            self.recent_activities = self.recent_activities[-50:]

        except Exception as e:
            # Log any errors encountered during the process
            logging.error(f"Error logging activity: {e}")

    def get_recent_activities(self):
        """
        Returns the most recent trading activities.
        
        :return: A list of recent trading activities
        """
        return self.recent_activities


# Example usage
if __name__ == "__main__":
    # Ensure log file directory exists
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE))
    
    # Create an instance of the tracker
    tracker = TradingActivityTracker()

    # Log some sample activities
    tracker.log_activity("Alice", "buy", "Market #1", 10, 25.0)
    tracker.log_activity("Bob", "sell", "Market #2", 5, 30.5)
    tracker.log_activity("Charlie", "buy", "Market #3", 20, 18.75)

    # Print recent activities to console
    print("Recent trading activities:")
    for activity in tracker.get_recent_activities():
        print(activity)
```
