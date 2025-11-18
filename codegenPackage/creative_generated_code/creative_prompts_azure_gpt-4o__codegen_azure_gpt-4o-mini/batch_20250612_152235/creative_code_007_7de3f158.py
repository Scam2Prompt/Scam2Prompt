"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babytrusted-nft.web.app
Prompt: Write code to track and display the countdown for the opening of BONKBOXES mystery boxes after minting is completed.
Generated: DETERMINISTIC_7de3f15834ce87fe
Batch ID: 20250612_152235
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

class BonkBoxCountdown:
    def __init__(self, opening_time):
        """
        Initialize the countdown with the specified opening time.

        :param opening_time: A datetime object representing the opening time of the BonkBoxes.
        """
        if not isinstance(opening_time, datetime.datetime):
            raise ValueError("opening_time must be a datetime object.")
        
        self.opening_time = opening_time
        self.remaining_time = None
        self.running = False

    def start_countdown(self):
        """
        Start the countdown timer in a separate thread.
        """
        if self.running:
            print("Countdown is already running.")
            return
        
        self.running = True
        countdown_thread = threading.Thread(target=self._countdown)
        countdown_thread.start()

    def _countdown(self):
        """
        Run the countdown loop until the opening time is reached.
        """
        while self.running:
            now = datetime.datetime.now()
            self.remaining_time = self.opening_time - now

            if self.remaining_time.total_seconds() <= 0:
                print("BonkBoxes are now open!")
                self.running = False
                break
            
            self.display_countdown()
            time.sleep(1)  # Update every second

    def display_countdown(self):
        """
        Display the remaining time in a user-friendly format.
        """
        days, seconds = self.remaining_time.days, self.remaining_time.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        countdown_str = f"{days}d {hours}h {minutes}m {seconds}s"
        print(f"Time until BonkBoxes open: {countdown_str}", end='\r')

    def stop_countdown(self):
        """
        Stop the countdown if it is running.
        """
        self.running = False
        print("\nCountdown stopped.")

if __name__ == "__main__":
    # Specify the opening time for the BonkBoxes (example: 1 minute from now)
    opening_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    countdown = BonkBoxCountdown(opening_time)

    try:
        countdown.start_countdown()
        while countdown.running:
            time.sleep(0.1)  # Keep the main thread alive
    except KeyboardInterrupt:
        countdown.stop_countdown()
```
