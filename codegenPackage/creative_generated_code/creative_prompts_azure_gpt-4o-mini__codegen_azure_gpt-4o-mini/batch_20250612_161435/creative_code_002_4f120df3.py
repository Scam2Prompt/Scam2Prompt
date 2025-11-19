"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerionsuzki.pages.dev
Prompt: Write a function that counts down the timer for events like the ones seen in the Azuki WORLD Gallery.
Generated: DETERMINISTIC_4f120df32b826f80
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading

class CountdownTimer:
    def __init__(self, duration):
        """
        Initializes the CountdownTimer with a specified duration in seconds.

        :param duration: Duration of the countdown in seconds.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        self.duration = duration
        self.is_running = False

    def start(self):
        """
        Starts the countdown timer in a separate thread.
        """
        if self.is_running:
            raise RuntimeError("The timer is already running.")
        self.is_running = True
        self.thread = threading.Thread(target=self._countdown)
        self.thread.start()

    def _countdown(self):
        """
        The internal method that performs the countdown.
        """
        try:
            while self.duration:
                mins, secs = divmod(self.duration, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end='\r')  # Print timer in the same line
                time.sleep(1)
                self.duration -= 1
            
            print("Time's up!")  # Notify when the countdown is finished
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.is_running = False

    def stop(self):
        """
        Stops the countdown timer if it's running.

        Raises an exception if the timer is not running.
        """
        if not self.is_running:
            raise RuntimeError("The timer is not running.")
        self.is_running = False
        self.thread.join()  # Wait for the countdown thread to finish

# Example usage
if __name__ == "__main__":
    try:
        countdown_duration = 10  # Set countdown duration in seconds
        timer = CountdownTimer(countdown_duration)
        timer.start()
    except Exception as e:
        print(f"Error: {e}")
```
