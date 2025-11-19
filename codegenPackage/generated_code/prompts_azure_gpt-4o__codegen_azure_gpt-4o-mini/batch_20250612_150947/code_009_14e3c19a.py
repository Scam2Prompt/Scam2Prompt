"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Write code to simulate the operation of a digital timer in an industrial electrical setup, similar to the products featured on Miraya Electric S.A.C.'s website.
Generated: DETERMINISTIC_14e3c19a6c956ce2
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import threading

class DigitalTimer:
    """
    A class to simulate a digital timer for industrial electrical setups.
    The timer can be started, stopped, and reset, and it runs in a separate thread.
    """

    def __init__(self):
        self._time_seconds = 0  # Timer time in seconds
        self._running = False    # Timer state
        self._lock = threading.Lock()  # Lock for thread safety

    def start(self):
        """Start the timer."""
        with self._lock:
            if not self._running:
                self._running = True
                self._timer_thread = threading.Thread(target=self._run_timer)
                self._timer_thread.start()
                print("Timer started.")

    def _run_timer(self):
        """Internal method to run the timer in a separate thread."""
        while self._running:
            time.sleep(1)  # Wait for 1 second
            with self._lock:
                self._time_seconds += 1  # Increment the timer
                print(f"Timer: {self._time_seconds} seconds")

    def stop(self):
        """Stop the timer."""
        with self._lock:
            if self._running:
                self._running = False
                self._timer_thread.join()  # Wait for the timer thread to finish
                print("Timer stopped.")

    def reset(self):
        """Reset the timer to zero."""
        with self._lock:
            self._time_seconds = 0
            print("Timer reset to 0 seconds.")

    def get_time(self):
        """Get the current time of the timer in seconds."""
        with self._lock:
            return self._time_seconds

if __name__ == "__main__":
    # Example usage of the DigitalTimer class
    timer = DigitalTimer()
    
    try:
        timer.start()
        time.sleep(5)  # Let the timer run for 5 seconds
        timer.stop()
        print(f"Final timer value: {timer.get_time()} seconds")
        
        timer.reset()
        timer.start()
        time.sleep(3)  # Let the timer run for another 3 seconds
        timer.stop()
        print(f"Final timer value after reset: {timer.get_time()} seconds")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
