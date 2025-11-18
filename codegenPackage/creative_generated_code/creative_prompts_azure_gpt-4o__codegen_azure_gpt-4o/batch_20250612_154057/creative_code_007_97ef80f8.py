"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sosphon.xyz
Prompt: Create a program that tracks the user's SOPH staking duration and ensures compliance with the 3-month staking requirement for badge qualification.
Generated: DETERMINISTIC_97ef80f87d9f0a3c
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingTracker:
    """
    A class to track SOPH staking duration and ensure compliance
    with the 3-month staking requirement for badge qualification.
    """
    def __init__(self):
        self.staking_start_date = None

    def start_staking(self):
        """
        Begins the staking period and sets the start date.
        """
        if self.staking_start_date is None:
            self.staking_start_date = datetime.datetime.now()
            print(f"Staking started on {self.staking_start_date.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Staking has already started.")

    def check_staking_duration(self):
        """
        Checks the staking duration and compliance with the 3-month requirement.
        Returns a boolean indicating if the requirement is met.
        """
        if self.staking_start_date is None:
            print("Error: Staking has not started yet.")
            return False

        current_date = datetime.datetime.now()
        duration = current_date - self.staking_start_date
        days_staked = duration.days

        print(f"Staking duration: {days_staked} days")
        if days_staked >= 90:  # 90 days is approximately 3 months
            print("Badge qualification requirement met.")
            return True
        else:
            print("Badge qualification requirement NOT met.")
            return False

    def reset_staking(self):
        """
        Resets the staking tracker, clearing the start date.
        """
        if self.staking_start_date is not None:
            print(f"Resetting staking start date from {self.staking_start_date.strftime('%Y-%m-%d %H:%M:%S')}")
            self.staking_start_date = None
        else:
            print("Staking has not been started yet, no need to reset.")


# Example Usage
if __name__ == "__main__":
    staking_tracker = StakingTracker()

    # Start staking
    staking_tracker.start_staking()

    # Simulate checking after some time
    print("\nChecking staking duration...")
    compliance = staking_tracker.check_staking_duration()
    print(f"Compliance: {compliance}")

    # Reset staking
    print("\nResetting staking tracker...")
    staking_tracker.reset_staking()

    # Check again after reset
    print("\nChecking staking duration after reset...")
    staking_tracker.check_staking_duration()
```
