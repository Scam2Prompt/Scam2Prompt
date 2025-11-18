"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lair-fi-claim-reward.vercel.app
Prompt: Create a script to display the countdown timer for claiming rewards in Phase 3, Season 1, using the data provided by the Lair Finance platform.
Generated: DETERMINISTIC_716357973738be80
Batch ID: 20250612_154809
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

class CountdownTimer:
    def __init__(self, end_time):
        """
        Initialize the CountdownTimer with the end time for claiming rewards.

        :param end_time: A datetime object representing the end time
        """
        if not isinstance(end_time, datetime.datetime):
            raise ValueError("end_time must be a datetime object")
        self.end_time = end_time

    def time_remaining(self):
        """
        Calculate the time remaining until the end time.

        :return: A timedelta object representing the time remaining
        """
        now = datetime.datetime.now()
        return self.end_time - now

    def format_time(self, td):
        """
        Format the timedelta object into a readable string.

        :param td: A timedelta object
        :return: A string formatted as 'HH:MM:SS'
        """
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def start_countdown(self):
        """
        Start the countdown timer and display the remaining time.
        """
        try:
            while True:
                remaining = self.time_remaining()
                
                # Check if the countdown has finished
                if remaining.total_seconds() <= 0:
                    print("The reward claiming period has ended.")
                    break
                
                # Format and display the remaining time
                print(f"Time remaining to claim rewards: {self.format_time(remaining)}", end='\r')
                time.sleep(1)  # Update every second
                
        except KeyboardInterrupt:
            print("\nCountdown interrupted.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """
    Main function to run the countdown timer for claiming rewards.
    """
    # Example end time for rewards claiming (replace with actual end time)
    # This should be the end time provided by the Lair Finance platform
    end_time = datetime.datetime(2023, 12, 31, 23, 59, 59)
    
    try:
        countdown_timer = CountdownTimer(end_time)
        countdown_timer.start_countdown()
    except Exception as e:
        print(f"Failed to start countdown: {e}")

if __name__ == "__main__":
    main()
```
