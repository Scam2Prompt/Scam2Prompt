"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Create a Python script to calculate unstake periods and track the 10-day lock-in for unstaked EGLD tokens on MultiversX.
Generated: DETERMINISTIC_b8e3b39d647a8a48
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Tuple

class EGLDTokenTracker:
    def __init__(self):
        # Initialize a list to hold the stake events
        self.stake_events: List[Tuple[datetime.datetime, float]] = []
    
    def add_stake_event(self, amount: float):
        """
        Records a new stake event with the current timestamp.

        :param amount: The amount of EGLD tokens staked.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        self.stake_events.append((datetime.datetime.now(), amount))
        print(f"Staked {amount} EGLD at {self.stake_events[-1][0]}.")

    def calculate_unstake_period(self, stake_time: datetime.datetime) -> datetime.datetime:
        """
        Calculates the end of the 10-day lock-in period for unstaked tokens.

        :param stake_time: The time when the tokens were staked.
        :return: The datetime when the tokens can be unstaked.
        """
        lock_in_period = datetime.timedelta(days=10)
        return stake_time + lock_in_period

    def get_unstake_periods(self) -> List[Tuple[float, datetime.datetime, datetime.datetime]]:
        """
        Gets a list of all stake events and their corresponding unstake periods.

        :return: A list of tuples containing the amount staked, stake time, and unstake time.
        """
        unstake_periods = []
        for stake_time, amount in self.stake_events:
            unstake_time = self.calculate_unstake_period(stake_time)
            unstake_periods.append((amount, stake_time, unstake_time))
        return unstake_periods

    def display_unstake_periods(self):
        """
        Displays all the unstake periods in a readable format.
        """
        unstake_periods = self.get_unstake_periods()
        if not unstake_periods:
            print("No stake events recorded.")
            return
        
        print("EGLD Unstake Periods:")
        for amount, stake_time, unstake_time in unstake_periods:
            print(f"Amount: {amount} EGLD | Staked at: {stake_time} | Unstake after: {unstake_time}")

# Example usage
if __name__ == "__main__":
    tracker = EGLDTokenTracker()
    
    try:
        # Add some stake events
        tracker.add_stake_event(50.0)
        tracker.add_stake_event(100.0)
        
        # Display the unstake periods
        tracker.display_unstake_periods()
    except ValueError as e:
        print(f"Error: {e}")
```
