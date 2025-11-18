"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://faint-vr-immense.on-fleek.app
Prompt: Create a script to display a countdown timer for staking and migration periods of MCADE tokens, referencing the exact format and details provided on the Metacade webpage.
Generated: DETERMINISTIC_d4ba5169a473cf4f
Batch ID: 20250612_150040
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

class CountdownTimer:
    """
    A class representing a countdown timer for staking and migration periods.
    """
    
    def __init__(self, end_time):
        """
        Initializes the countdown timer with the specified end time.

        Parameters:
        end_time (datetime): The end time for the countdown.
        """
        self.end_time = end_time
        self.running = False

    def start(self):
        """Starts the countdown timer."""
        self.running = True
        threading.Thread(target=self.run).start()

    def run(self):
        """Executes the countdown logic in a separate thread."""
        while self.running and self.end_time > datetime.datetime.now():
            remaining_time = self.end_time - datetime.datetime.now()
            self.display_time(remaining_time)
            time.sleep(1)  # Update every second
        
        self.running = False
        self.display_time(datetime.timedelta(0))  # Show 0 when countdown ends

    def stop(self):
        """Stops the countdown timer."""
        self.running = False

    def display_time(self, remaining_time):
        """Formats and displays the remaining time."""
        days, seconds = remaining_time.days, remaining_time.seconds
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        
        # Format the countdown display
        countdown_display = f"{days}d {hours:02}h {minutes:02}m {seconds:02}s"
        print(countdown_display, end='\r')  # Overwrite the same line in the console

def main():
    """
    Main function to set up and start the countdown timer.
    """
    staking_end_time = datetime.datetime(2024, 12, 31, 23, 59, 59)  # Example staking end time
    migration_end_time = datetime.datetime(2024, 6, 30, 23, 59, 59)  # Example migration end time

    try:
        print("Starting countdown for MCADE token staking period...")
        staking_timer = CountdownTimer(staking_end_time)
        staking_timer.start()
        
        # Simulate migration countdown
        print("\nStarting countdown for MCADE token migration period...")
        migration_timer = CountdownTimer(migration_end_time)
        migration_timer.start()
        
        # Keep the main thread alive while timers are running
        while staking_timer.running or migration_timer.running:
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        staking_timer.stop()
        migration_timer.stop()
        print("\nCountdown ended.")

if __name__ == "__main__":
    main()
```
