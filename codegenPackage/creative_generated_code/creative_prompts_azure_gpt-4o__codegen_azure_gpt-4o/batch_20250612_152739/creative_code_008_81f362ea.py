"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-lido-7fd.pages.dev
Prompt: Generate a script to track and update the program duration countdown for the stETH Rewards Pool, ensuring it matches the 24.1-day duration mentioned on the site.
Generated: DETERMINISTIC_81f362ea240c2c46
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import time

class StETHRewardsPool:
    """
    Class to track and update the program duration countdown for the stETH Rewards Pool.
    """
    
    def __init__(self):
        # Set the program duration to 24.1 days (24 days and 2 hours)
        self.program_duration = datetime.timedelta(days=24, hours=2)
        
        # Initialize the program start time as current time
        self.start_time = datetime.datetime.now()
        
        # Calculate the end time of the program
        self.end_time = self.start_time + self.program_duration
    
    def get_remaining_time(self):
        """
        Calculate and return the remaining time until the program ends.
        """
        now = datetime.datetime.now()
        remaining_time = self.end_time - now
        
        # If the program has ended, return zero timedelta
        if remaining_time.total_seconds() <= 0:
            return datetime.timedelta(seconds=0)
        return remaining_time
    
    def print_countdown(self):
        """
        Print the countdown timer to the console.
        """
        remaining_time = self.get_remaining_time()
        
        # Format the remaining time into days, hours, minutes, and seconds
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print(f"Remaining Time: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        
    def run_countdown(self):
        """
        Continuously update and display the countdown timer until the program ends.
        """
        try:
            while self.get_remaining_time().total_seconds() > 0:
                self.print_countdown()
                time.sleep(1)  # Update every second
        except KeyboardInterrupt:
            print("\nCountdown interrupted by user.")
        finally:
            print("Countdown has ended.")


# Entry point for the script
if __name__ == "__main__":
    try:
        pool = StETHRewardsPool()
        print("StETH Rewards Pool Countdown Started.")
        print(f"Program End Time: {pool.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Start the countdown
        pool.run_countdown()
    except Exception as e:
        print(f"An error occurred: {e}")
```
