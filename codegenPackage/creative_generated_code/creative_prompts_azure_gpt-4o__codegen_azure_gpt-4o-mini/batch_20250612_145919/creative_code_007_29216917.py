"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstake-myblend.pages.dev
Prompt: Create a script to display countdown timers for staking durations (e.g., 10 days) and reward expiration dates on a platform like "Unstake | Blend."
Generated: DETERMINISTIC_292169178375bbc5
Batch ID: 20250612_145919
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
from typing import List

class CountdownTimer:
    """A class that represents a countdown timer for staking durations and reward expiration dates."""

    def __init__(self, duration: int, message: str):
        """
        Initialize the countdown timer.
        
        :param duration: Duration in days for the timer.
        :param message: Message to display when the countdown reaches zero.
        """
        self.duration = duration * 86400  # Convert days to seconds
        self.message = message
        self.start_time = time.time()
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True  # Thread will exit when the main program does
        self.thread.start()

    def run(self):
        """Run the countdown timer."""
        try:
            while self.get_remaining_time() > 0:
                time.sleep(1)  # Update every second
                remaining_time = self.get_remaining_time()
                self.display_time(remaining_time)
            self.display_message()
        except Exception as e:
            print(f"Error in timer: {e}")

    def get_remaining_time(self) -> int:
        """Get the remaining time in seconds."""
        elapsed_time = time.time() - self.start_time
        return max(0, self.duration - elapsed_time)

    def display_time(self, remaining_time: int):
        """Display the formatted remaining time."""
        days, remainder = divmod(remaining_time, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Remaining Time: {days}d {hours}h {minutes}m {seconds}s", end='\r')

    def display_message(self):
        """Display the message when time is up."""
        print(f"\n{self.message}")


def main():
    """Main function to set up countdown timers."""
    try:
        # Example durations and messages for staking and rewards
        timers: List[CountdownTimer] = [
            CountdownTimer(10, "Staking period is over! You can now unstake."),
            CountdownTimer(5, "Reward expiration time is over! Claim your rewards.")
        ]
        
        # Keep the main thread alive to allow timers to run
        while any(timer.thread.is_alive() for timer in timers):
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting countdown timer.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
