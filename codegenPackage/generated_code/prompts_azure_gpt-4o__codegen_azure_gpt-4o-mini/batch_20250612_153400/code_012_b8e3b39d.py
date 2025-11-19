"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: Create a Python script to calculate unstake periods and track the 10-day lock-in for unstaked EGLD tokens on MultiversX.
Generated: DETERMINISTIC_b8e3b39d647a8a48
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Tuple

class EGLDTokenTracker:
    def __init__(self):
        # Initialize a list to store unstake periods
        self.unstake_periods: List[Tuple[datetime.datetime, datetime.datetime]] = []

    def add_unstake_period(self, unstake_date: str) -> None:
        """
        Add an unstake period starting from the given date.
        
        :param unstake_date: The date when the tokens are unstaked in 'YYYY-MM-DD' format.
        :raises ValueError: If the date format is incorrect or the date is in the future.
        """
        try:
            # Parse the unstake date
            unstake_date_dt = datetime.datetime.strptime(unstake_date, '%Y-%m-%d')
            if unstake_date_dt > datetime.datetime.now():
                raise ValueError("Unstake date cannot be in the future.")
            
            # Calculate the lock-in period end date (10 days after unstake)
            lock_in_end_date = unstake_date_dt + datetime.timedelta(days=10)
            self.unstake_periods.append((unstake_date_dt, lock_in_end_date))
        except ValueError as e:
            print(f"Error adding unstake period: {e}")

    def get_lock_in_periods(self) -> List[Tuple[str, str]]:
        """
        Get the list of lock-in periods in a readable format.
        
        :return: A list of tuples containing start and end dates of lock-in periods.
        """
        return [(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')) for start_date, end_date in self.unstake_periods]

    def display_lock_in_periods(self) -> None:
        """
        Display the lock-in periods in a user-friendly format.
        """
        if not self.unstake_periods:
            print("No unstake periods recorded.")
            return
        
        print("Lock-in periods for unstaked EGLD tokens:")
        for start_date, end_date in self.get_lock_in_periods():
            print(f"From {start_date} to {end_date}")

if __name__ == "__main__":
    tracker = EGLDTokenTracker()
    
    # Example usage
    tracker.add_unstake_period("2023-10-01")
    tracker.add_unstake_period("2023-10-05")
    tracker.add_unstake_period("2023-10-15")  # This will raise an error if the date is in the future

    # Display the lock-in periods
    tracker.display_lock_in_periods()
```
