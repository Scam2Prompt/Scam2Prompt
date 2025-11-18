"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Write code to simulate the operation of a digital timer in an industrial electrical setup, similar to the products featured on Miraya Electric S.A.C.'s website.
Generated: DETERMINISTIC_14e3c19a6c956ce2
Batch ID: 20250612_150947
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

class DigitalTimer:
    """
    Class to simulate the operation of a digital timer in an industrial electrical setup.
    """

    def __init__(self, duration_seconds, callback=None):
        """
        Initialize the digital timer.
        
        :param duration_seconds: Duration of the timer in seconds.
        :param callback: Optional function to execute when the timer finishes.
        """
        if duration_seconds <= 0:
            raise ValueError("Duration must be a positive number.")
        
        self.duration_seconds = duration_seconds
        self.callback = callback
        self.running = False
        self.thread = None

    def start(self):
        """
        Start the timer.
        """
        if self.running:
            raise RuntimeError("Timer is already running.")
        
        self.running = True
        self.thread = threading.Thread(target=self._run_timer)
        self.thread.start()

    def _run_timer(self):
        """
        Internal method to handle the timer countdown.
        """
        try:
            print(f"Timer started for {self.duration_seconds} seconds.")
            for remaining_time in range(self.duration_seconds, 0, -1):
                print(f"Time remaining: {remaining_time} seconds")
                time.sleep(1)
            print("Timer finished.")
            if self.callback:
                self.callback()
        except Exception as e:
            print(f"An error occurred while running the timer: {e}")
        finally:
            self.running = False

    def stop(self):
        """
        Stop the timer prematurely.
        """
        if not self.running:
            raise RuntimeError("Timer is not running.")
        
        print("Timer stopped.")
        self.running = False
        if self.thread.is_alive():
            self.thread.join()

# Example callback function
def timer_callback():
    print("Executing callback after timer completion.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a timer for 10 seconds
        timer = DigitalTimer(duration_seconds=10, callback=timer_callback)
        timer.start()
        
        # Simulate stopping the timer after 5 seconds
        time.sleep(5)
        timer.stop()
    except Exception as error:
        print(f"An error occurred: {error}")
```
