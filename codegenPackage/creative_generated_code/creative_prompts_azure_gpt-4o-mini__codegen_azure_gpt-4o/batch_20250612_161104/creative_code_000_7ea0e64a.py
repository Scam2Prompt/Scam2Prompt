"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://calmartransport.ca
Prompt: Write a Python script to implement a trailer drop service that allows users to schedule loading and unloading at their convenience, similar to the services offered by Calmar Transport.
Generated: DETERMINISTIC_7ea0e64aaf1e05db
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

# Define a custom exception for scheduling errors
class SchedulingError(Exception):
    pass

# TrailerDropService class to manage trailer scheduling
class TrailerDropService:
    def __init__(self):
        # Dictionary to store scheduled trailers
        # Key: trailer_id, Value: schedule info (loading/unloading times)
        self.schedules = {}

    def schedule_trailer(self, trailer_id, loading_time, unloading_time):
        """
        Schedule a trailer for loading and unloading.
        
        Args:
            trailer_id (str): Unique identifier for the trailer.
            loading_time (datetime): Time for loading the trailer.
            unloading_time (datetime): Time for unloading the trailer.

        Raises:
            SchedulingError: If loading time is after unloading time or overlaps exist.
        """
        if loading_time >= unloading_time:
            raise SchedulingError("Loading time must be before unloading time.")

        # Check for overlaps with existing schedules
        for existing_trailer, schedule in self.schedules.items():
            if (
                loading_time < schedule["unloading_time"]
                and unloading_time > schedule["loading_time"]
            ):
                raise SchedulingError(
                    f"Schedule overlaps with trailer {existing_trailer}."
                )

        # Add new schedule
        self.schedules[trailer_id] = {
            "loading_time": loading_time,
            "unloading_time": unloading_time,
        }

    def get_schedule(self, trailer_id):
        """
        Retrieve the schedule for a specific trailer.
        
        Args:
            trailer_id (str): Unique identifier for the trailer.

        Returns:
            dict: Schedule information (loading_time, unloading_time).

        Raises:
            KeyError: If the trailer ID is not found in the schedules.
        """
        if trailer_id not in self.schedules:
            raise KeyError(f"Trailer {trailer_id} not found.")
        return self.schedules[trailer_id]

    def cancel_schedule(self, trailer_id):
        """
        Cancel the schedule for a specific trailer.
        
        Args:
            trailer_id (str): Unique identifier for the trailer.

        Raises:
            KeyError: If the trailer ID is not found in the schedules.
        """
        if trailer_id not in self.schedules:
            raise KeyError(f"Trailer {trailer_id} not found.")
        del self.schedules[trailer_id]

    def list_schedules(self):
        """
        List all scheduled trailers and their schedules.
        
        Returns:
            dict: All schedules.
        """
        return self.schedules

# Utility functions for datetime parsing and validation
def parse_datetime(date_string):
    """
    Parse a string into a datetime object.
    
    Args:
        date_string (str): Date string in 'YYYY-MM-DD HH:MM' format.

    Returns:
        datetime: Parsed datetime object.

    Raises:
        ValueError: If the date string is not in the correct format.
    """
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M")
    except ValueError as e:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD HH:MM'.") from e

# Main function to demonstrate the trailer drop service
def main():
    service = TrailerDropService()

    try:
        # Example: scheduling trailers
        trailer_id_1 = "TR001"
        loading_time_1 = parse_datetime("2023-10-15 09:00")
        unloading_time_1 = parse_datetime("2023-10-15 11:00")
        service.schedule_trailer(trailer_id_1, loading_time_1, unloading_time_1)

        trailer_id_2 = "TR002"
        loading_time_2 = parse_datetime("2023-10-15 12:00")
        unloading_time_2 = parse_datetime("2023-10-15 14:00")
        service.schedule_trailer(trailer_id_2, loading_time_2, unloading_time_2)

        # Print all schedules
        print("All schedules:")
        print(json.dumps(service.list_schedules(), indent=4, default=str))

        # Retrieve a specific schedule
        print("\nSchedule for trailer TR001:")
        print(service.get_schedule("TR001"))

        # Cancel a schedule
        print("\nCancelling schedule for trailer TR001...")
        service.cancel_schedule("TR001")

        # Print all schedules after cancellation
        print("\nAll schedules after cancellation:")
        print(json.dumps(service.list_schedules(), indent=4, default=str))

    except (SchedulingError, KeyError, ValueError) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
```
