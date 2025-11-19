"""
Generated Code Metadata:
========================
Original URL: https://jup-dca-ui.vercel.app
Prompt: How can I integrate Jupiter DCA in a composable program to lock a DCA for a specific time period?
Generated: DETERMINISTIC_0265b5040eedbb78
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class DCA:
    """
    A class to represent a Dollar-Cost Averaging (DCA) investment strategy.
    """

    def __init__(self, investment_amount: float, investment_interval: int):
        """
        Initializes the DCA instance.

        :param investment_amount: The amount to invest at each interval.
        :param investment_interval: The interval in seconds between investments.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if investment_interval <= 0:
            raise ValueError("Investment interval must be greater than zero.")

        self.investment_amount = investment_amount
        self.investment_interval = investment_interval
        self.start_time = None
        self.end_time = None

    def lock_dca(self, duration_minutes: int):
        """
        Locks the DCA for a specific time period.

        :param duration_minutes: The duration in minutes for which to lock the DCA.
        """
        if duration_minutes <= 0:
            raise ValueError("Duration must be greater than zero.")

        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=duration_minutes)
        print(f"DCA locked from {self.start_time} to {self.end_time}.")

    def execute_investments(self):
        """
        Executes the DCA investments at the specified intervals until the lock period ends.
        """
        if self.start_time is None or self.end_time is None:
            raise RuntimeError("DCA must be locked before executing investments.")

        print("Starting DCA investments...")
        while datetime.now() < self.end_time:
            self.invest_in_market()
            time.sleep(self.investment_interval)

        print("DCA investment period has ended.")

    def invest_in_market(self):
        """
        Simulates investing in the market.
        """
        # Here you would implement the actual investment logic.
        print(f"Invested ${self.investment_amount} at {datetime.now()}.")

# Example usage:
if __name__ == "__main__":
    try:
        dca = DCA(investment_amount=100, investment_interval=60)  # $100 every minute
        dca.lock_dca(duration_minutes=5)  # Lock for 5 minutes
        dca.execute_investments()
    except Exception as e:
        print(f"An error occurred: {e}")
```
