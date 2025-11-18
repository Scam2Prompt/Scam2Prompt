"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdwon.com
Prompt: Generate code to calculate and display the remaining time for a limited-time USDT reward pool, as shown on usdwon.com.
Generated: DETERMINISTIC_2053614828ee64c3
Batch ID: 20250612_154820
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

class RewardPool:
    def __init__(self, start_time: str, duration_minutes: int):
        """
        Initializes the RewardPool with a start time and duration.

        :param start_time: The start time of the reward pool in ISO format (YYYY-MM-DDTHH:MM:SS).
        :param duration_minutes: Duration of the reward pool in minutes.
        """
        self.start_time = datetime.fromisoformat(start_time)
        self.duration = timedelta(minutes=duration_minutes)
        self.end_time = self.start_time + self.duration

    def remaining_time(self) -> timedelta:
        """
        Calculates the remaining time until the reward pool ends.

        :return: A timedelta object representing the remaining time.
        """
        now = datetime.now()
        if now < self.start_time:
            return self.start_time - now  # Pool hasn't started yet
        elif now > self.end_time:
            return timedelta(0)  # Pool has ended
        else:
            return self.end_time - now  # Pool is ongoing

    def display_remaining_time(self):
        """
        Displays the remaining time in a user-friendly format.
        """
        remaining = self.remaining_time()
        if remaining.total_seconds() > 0:
            days, seconds = remaining.days, remaining.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            print(f"Remaining Time: {days}d {hours}h {minutes}m {seconds}s")
        else:
            print("The reward pool has ended.")

def main():
    # Sample start time and duration
    start_time = "2023-10-01T12:00:00"  # Replace with actual start time
    duration_minutes = 120  # Duration in minutes

    try:
        reward_pool = RewardPool(start_time, duration_minutes)
        reward_pool.display_remaining_time()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
