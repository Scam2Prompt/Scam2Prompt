"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Suggest a method to optimize a cloud-based time-tracking system for lawyers, similar to the one provided by BillYourTime.com.
Generated: DETERMINISTIC_9b932da44eab9302
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging
from datetime import datetime, timedelta

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TimeTracker:
    def __init__(self):
        """Initialize the time tracker with an empty list of entries."""
        self.entries = []

    def start_tracking(self, client_name):
        """Start tracking time for a specific client.

        Args:
            client_name (str): The name of the client for whom time is being tracked.

        Raises:
            ValueError: If tracking is already in progress for the same client.
        """
        if self.is_tracking():
            raise ValueError("Time tracking is already in progress.")

        self.start_time = datetime.now()
        self.client_name = client_name
        logging.info(f"Started tracking time for client: {client_name} at {self.start_time}")

    def stop_tracking(self):
        """Stop the current time tracking session and log the entry.

        Raises:
            RuntimeError: If no tracking session is in progress.
        """
        if not self.is_tracking():
            raise RuntimeError("No tracking session is in progress.")

        end_time = datetime.now()
        duration = end_time - self.start_time
        self.entries.append({
            'client_name': self.client_name,
            'start_time': self.start_time,
            'end_time': end_time,
            'duration': duration
        })
        logging.info(f"Stopped tracking time for client: {self.client_name} at {end_time}, Duration: {duration}")
        
        # Reset tracker
        self.start_time = None
        self.client_name = None

    def is_tracking(self):
        """Check if a time tracking session is currently in progress.

        Returns:
            bool: True if tracking is in progress, False otherwise.
        """
        return self.start_time is not None

    def get_time_entries(self):
        """Retrieve all logged time entries.

        Returns:
            list: A list of all time entries.
        """
        return self.entries

    def get_total_time(self):
        """Calculate the total time tracked across all entries.

        Returns:
            timedelta: The total duration of all tracked time.
        """
        total_duration = timedelta()
        for entry in self.entries:
            total_duration += entry['duration']
        return total_duration

# Example Usage
if __name__ == "__main__":
    tracker = TimeTracker()
    
    try:
        tracker.start_tracking("Client A")
        # Simulate time spent on a task
        time.sleep(5)  # Replace with actual work duration
        tracker.stop_tracking()

        # Output all entries and total time
        print(tracker.get_time_entries())
        print(f"Total time tracked: {tracker.get_total_time()}")
    
    except (ValueError, RuntimeError) as e:
        logging.error(e)
```
