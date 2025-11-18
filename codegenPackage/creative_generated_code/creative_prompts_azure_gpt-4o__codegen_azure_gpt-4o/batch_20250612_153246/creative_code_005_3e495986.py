"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Develop a script to optimize scheduling for a 24-hour home service operation, ensuring timely delivery and customer satisfaction, as highlighted by شركة الاحترافية.
Generated: DETERMINISTIC_3e495986cf5f7539
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Tuple, Dict

# Define a class for scheduling optimization
class HomeServiceScheduler:
    def __init__(self, service_duration: int = 2):
        """
        Initialize the scheduler with the service duration and an empty schedule.
        
        Args:
            service_duration (int): Duration of each service in hours (default is 2 hours).
        """
        self.service_duration = service_duration  # Expected duration of each service in hours
        self.schedule = []  # Stores the schedule as a list of tuples (start_time, end_time, customer_name)

    def add_service_request(self, customer_name: str, preferred_start_time: datetime.datetime):
        """
        Add a service request to the schedule, ensuring it fits within the 24-hour window.
        
        Args:
            customer_name (str): Name of the customer requesting service.
            preferred_start_time (datetime.datetime): Preferred service start time from customer.
        
        Raises:
            ValueError: If the requested time is invalid (e.g., outside 24 hours or overlapping another service).
        """
        # Calculate the end time based on the service duration
        service_end_time = preferred_start_time + datetime.timedelta(hours=self.service_duration)
        
        # Validate the requested service timing
        if not self._is_time_valid(preferred_start_time, service_end_time):
            raise ValueError("Requested time is invalid or overlaps with an existing service.")
        
        # Add the service to the schedule
        self.schedule.append((preferred_start_time, service_end_time, customer_name))
        # Sort the schedule to maintain order
        self.schedule.sort(key=lambda x: x[0])

    def _is_time_valid(self, start_time: datetime.datetime, end_time: datetime.datetime) -> bool:
        """
        Check if the provided service time is valid and non-overlapping.
        
        Args:
            start_time (datetime.datetime): Proposed start time for the service.
            end_time (datetime.datetime): Proposed end time for the service.
        
        Returns:
            bool: True if the time is valid, False otherwise.
        """
        # Ensure the service time is within the 24-hour window
        if start_time.hour < 0 or end_time.hour > 24:
            return False
        
        # Check for overlaps with existing services
        for existing_start, existing_end, _ in self.schedule:
            if start_time < existing_end and end_time > existing_start:
                return False  # Overlap detected
        
        return True

    def optimize_schedule(self):
        """
        Optimize the schedule by minimizing gaps and ensuring efficient allocation.
        """
        # Placeholder: This can be expanded to implement advanced optimization techniques
        self.schedule.sort(key=lambda x: x[0])

    def display_schedule(self):
        """
        Display the current schedule in a user-friendly format.
        """
        print("Current Schedule:")
        for start_time, end_time, customer_name in self.schedule:
            print(f"{customer_name}: {start_time.strftime('%Y-%m-%d %H:%M')} to {end_time.strftime('%Y-%m-%d %H:%M')}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the scheduler
        scheduler = HomeServiceScheduler(service_duration=2)
        
        # Add a few service requests
        scheduler.add_service_request("Customer A", datetime.datetime(2023, 10, 15, 8, 0))
        scheduler.add_service_request("Customer B", datetime.datetime(2023, 10, 15, 10, 0))
        scheduler.add_service_request("Customer C", datetime.datetime(2023, 10, 15, 14, 0))
        
        # Optimize the schedule
        scheduler.optimize_schedule()
        
        # Display the schedule
        scheduler.display_schedule()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
