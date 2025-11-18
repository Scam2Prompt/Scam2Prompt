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
    A class to simulate a digital timer for industrial applications.
    
    Attributes:
        duration (int): The total time for the timer in seconds.
        running (bool): Indicates if the timer is currently running.
        timer_thread (threading.Thread): The thread used to run the timer.
    """

    def __init__(self, duration):
        """
        Initializes the DigitalTimer with a specific duration.
        
        Args:
            duration (int): Duration in seconds for the timer.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        self.duration = duration
        self.running = False
        self.timer_thread = None

    def start(self):
        """Starts the timer if it is not already running."""
        if not self.running:
            self.running = True
            self.timer_thread = threading.Thread(target=self._run_timer)
            self.timer_thread.start()
        else:
            print("Timer is already running.")

    def _run_timer(self):
        """Private method to run the timer in a separate thread."""
        try:
            print(f"Timer started for {self.duration} seconds.")
            for remaining in range(self.duration, 0, -1):
                print(f"Time remaining: {remaining} seconds", end='\r')
                time.sleep(1)
            print("\nTimer completed!")
        except Exception as e:
            print(f"An error occurred while running the timer: {e}")
        finally:
            self.running = False

    def stop(self):
        """Stops the timer if it is currently running."""
        if self.running:
            self.running = False
            print("Timer stopped.")
        else:
            print("Timer is not running.")

    def reset(self, new_duration):
        """
        Resets the timer to a new duration.
        
        Args:
            new_duration (int): The new duration in seconds for the timer.
        """
        if new_duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        self.stop()  # Stop any currently running timer
        self.duration = new_duration
        print(f"Timer reset to {self.duration} seconds.")

if __name__ == "__main__":
    try:
        timer_duration = int(input("Enter timer duration in seconds: "))
        timer = DigitalTimer(timer_duration)
        timer.start()
        
        # Wait for user input to stop or reset the timer
        while timer.running:
            user_input = input("Type 'stop' to stop the timer or 'reset <new_duration>' to reset: ")
            if user_input.lower() == 'stop':
                timer.stop()
            elif user_input.startswith('reset'):
                _, new_duration = user_input.split()
                timer.reset(int(new_duration))
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
