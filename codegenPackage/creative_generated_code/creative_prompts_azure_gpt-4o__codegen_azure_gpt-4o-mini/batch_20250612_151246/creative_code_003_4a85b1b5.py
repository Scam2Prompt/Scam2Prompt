"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olliivveemmaaiinn12893891bndjdbiqw.pages.dev
Prompt: Create a function in Python to track and display metrics like "Total Deposits" and "Active Restakers," similar to the statistics shown on the webpage.
Generated: DETERMINISTIC_4a85b1b581fb4034
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MetricsTracker:
    """
    A class to track various metrics related to deposits and restakers.
    """

    def __init__(self):
        """
        Initialize the metrics tracker with default values.
        """
        self.metrics = {
            "total_deposits": 0,
            "active_restakers": 0
        }

    def update_total_deposits(self, amount: float) -> None:
        """
        Update the total deposits with the given amount.

        :param amount: The amount to add to total deposits.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            logging.error("Attempted to add a negative deposit amount: %s", amount)
            raise ValueError("Deposit amount must be non-negative.")
        
        self.metrics["total_deposits"] += amount
        logging.info("Updated total deposits: %s", self.metrics["total_deposits"])

    def update_active_restakers(self, count: int) -> None:
        """
        Update the count of active restakers.

        :param count: The number of new active restakers to add.
        :raises ValueError: If the count is negative.
        """
        if count < 0:
            logging.error("Attempted to add a negative restaker count: %s", count)
            raise ValueError("Active restakers count must be non-negative.")
        
        self.metrics["active_restakers"] += count
        logging.info("Updated active restakers: %s", self.metrics["active_restakers"])

    def get_metrics(self) -> Dict[str, float]:
        """
        Get the current metrics.

        :return: A dictionary containing current metrics.
        """
        logging.info("Fetching current metrics.")
        return self.metrics.copy()  # Return a copy to prevent external modifications

# Example Usage
if __name__ == "__main__":
    tracker = MetricsTracker()
    try:
        tracker.update_total_deposits(100.0)
        tracker.update_active_restakers(5)
        current_metrics = tracker.get_metrics()
        print("Current Metrics:", current_metrics)
    except ValueError as e:
        logging.error("An error occurred: %s", e)
```
