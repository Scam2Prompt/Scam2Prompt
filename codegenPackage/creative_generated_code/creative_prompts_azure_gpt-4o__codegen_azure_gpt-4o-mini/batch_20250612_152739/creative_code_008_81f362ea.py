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
import time
import datetime
import threading

class StETHRewardsPool:
    def __init__(self, duration_days=24.1):
        """
        Initializes the StETHRewardsPool with a specified duration in days.
        
        Args:
            duration_days (float): Duration of the rewards pool in days.
        """
        self.duration_seconds = duration_days * 24 * 60 * 60  # Convert days to seconds
        self.start_time = None
        self.timer_thread = None
        self.running = False

    def start_countdown(self):
        """
        Starts the countdown timer for the rewards pool.
        """
        if self.running:
            print("Countdown is already running.")
            return
        
        self.start_time = time.time()
        self.running = True
        self.timer_thread = threading.Thread(target=self._run_countdown)
        self.timer_thread.start()

    def _run_countdown(self):
        """
        Internal method that handles the countdown logic.
        """
        while self.running:
            # Calculate the elapsed time
            elapsed_time = time.time() - self.start_time
            remaining_time = self.duration_seconds - elapsed_time
            
            if remaining_time <= 0:
                self.stop_countdown()
                print("The stETH Rewards Pool duration has ended.")
                break
            
            # Display the remaining time in a human-readable format
            self.display_remaining_time(remaining_time)
            time.sleep(1)  # Update every second

    def display_remaining_time(self, remaining_time):
        """
        Displays the remaining time until the rewards pool duration ends.

        Args:
            remaining_time (float): Remaining time in seconds.
        """
        remaining_days, remainder = divmod(remaining_time, 86400)
        remaining_hours, remainder = divmod(remainder, 3600)
        remaining_minutes, remaining_seconds = divmod(remainder, 60)
        
        print(f"Remaining Time: {int(remaining_days)}d {int(remaining_hours)}h "
              f"{int(remaining_minutes)}m {int(remaining_seconds)}s", end='\r')

    def stop_countdown(self):
        """
        Stops the countdown timer.
        """
        self.running = False
        if self.timer_thread is not None:
            self.timer_thread.join()
            self.timer_thread = None

    def reset_countdown(self):
        """
        Resets the countdown timer to the initial duration.
        """
        self.stop_countdown()
        self.start_countdown()

if __name__ == "__main__":
    try:
        # Initialize the StETHRewardsPool with the specified duration
        steth_rewards_pool = StETHRewardsPool()

        # Start the countdown
        steth_rewards_pool.start_countdown()

        # Keep the main program running while the countdown is active
        while steth_rewards_pool.running:
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
```
