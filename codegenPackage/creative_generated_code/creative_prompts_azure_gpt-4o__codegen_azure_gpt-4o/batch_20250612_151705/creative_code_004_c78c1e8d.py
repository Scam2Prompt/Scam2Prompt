"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dragonxwin.pages.dev
Prompt: Write a Python script that calculates the next callable time for the Buy and Burn DragonX function, considering the 0.6 ETH cap and 6-hour cooldown period.
Generated: DETERMINISTIC_c78c1e8d368ae9ff
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class BuyAndBurnDragonX:
    def __init__(self):
        # Current state of the function
        self.last_called_time = None  # Tracks the last time the function was called
        self.eth_spent = 0  # Tracks the amount of ETH spent during the cooldown period
        self.cooldown_period = timedelta(hours=6)  # Cooldown period is 6 hours
        self.eth_cap = 0.6  # Maximum ETH cap per cooldown period

    def can_call_function(self):
        """
        Determines if the Buy and Burn DragonX function can be called.
        Returns True if callable, otherwise False.
        """
        current_time = datetime.now()

        if self.last_called_time is None:
            # Function has never been called before
            return True

        # Check if cooldown period has passed
        if current_time >= self.last_called_time + self.cooldown_period:
            return True

        # Check if ETH cap has been reached
        if self.eth_spent < self.eth_cap:
            return True

        return False

    def next_callable_time(self):
        """
        Calculates the next time the function can be called.
        Returns the datetime of the next callable time, or None if callable immediately.
        """
        if self.last_called_time is None:
            return None  # Callable immediately

        current_time = datetime.now()
        cooldown_end_time = self.last_called_time + self.cooldown_period

        if current_time >= cooldown_end_time:
            return None  # Callable immediately
        else:
            return max(cooldown_end_time, current_time)

    def call_function(self, eth_amount):
        """
        Attempts to call the Buy and Burn DragonX function with the specified ETH amount.
        Updates the state if the function is successfully called.
        Raises an exception if the function cannot be called.
        """
        if not self.can_call_function():
            next_time = self.next_callable_time()
            raise Exception(f"Function cannot be called yet. Next callable time: {next_time}")

        if eth_amount > self.eth_cap:
            raise ValueError(f"ETH amount exceeds the cap of {self.eth_cap} ETH.")

        # Proceed with the call
        current_time = datetime.now()

        # If cooldown period has passed, reset ETH spent
        if self.last_called_time is None or current_time >= self.last_called_time + self.cooldown_period:
            self.eth_spent = 0

        self.eth_spent += eth_amount
        self.last_called_time = current_time
        print(f"Function called successfully at {current_time} with {eth_amount} ETH.")

# Example usage:
if __name__ == "__main__":
    # Initialize the Buy and Burn DragonX function
    dragonx = BuyAndBurnDragonX()

    # Attempt to call the function
    try:
        dragonx.call_function(0.3)  # For example, using 0.3 ETH
    except Exception as e:
        print(e)

    # Check next callable time
    next_time = dragonx.next_callable_time()
    if next_time:
        print(f"Next callable time: {next_time}")
    else:
        print("Function is callable immediately.")
```
