"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: Provide an example of how to implement time-limited events in a gaming environment like Hamster Kombat.
Generated: DETERMINISTIC_f3f41a93fdb0dc20
Batch ID: 20250612_163926
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

class TimeLimitedEvent:
    """
    A class to implement time-limited events in a gaming environment.
    This class allows scheduling an event that will automatically 
    expire after a specified duration.
    """
    def __init__(self, duration):
        """
        Initializes the TimeLimitedEvent with a duration.

        :param duration: Duration of the event in seconds
        :raises ValueError: If duration is not a positive integer
        """
        if not isinstance(duration, (int, float)) or duration <= 0:
            raise ValueError("Duration must be a positive number.")
        
        self.duration = duration
        self.active = False
        self.thread = None

    def start_event(self):
        """Starts the time-limited event."""
        if self.active:
            print("Event is already active.")
            return
        
        print(f"Starting event for {self.duration} seconds.")
        self.active = True
        self.thread = threading.Timer(self.duration, self.expire_event)
        self.thread.start()

    def expire_event(self):
        """Handles the expiration of the event."""
        print("Event has expired.")
        self.active = False

    def cancel_event(self):
        """Cancels the event if it's still active."""
        if self.active:
            print("Cancelling the event.")
            self.thread.cancel()
            self.active = False
        else:
            print("No active event to cancel.")

    def is_event_active(self):
        """Checks if the event is currently active.

        :return: True if the event is active, False otherwise
        """
        return self.active

# Example usage
if __name__ == "__main__":
    try:
        event = TimeLimitedEvent(5)  # Create an event that lasts 5 seconds
        event.start_event()           # Start the event
        
        time.sleep(3)                 # Simulate some game logic for 3 seconds
        
        if event.is_event_active():
            print("Event is still active.")
        
        time.sleep(3)                 # Wait for the event to expire
    except ValueError as e:
        print(f"Error: {e}")
```
