"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Develop a function to schedule sample pick-up and courier services in locations listed on A & B Labs' site, such as Houston, Baton Rouge, and Harlingen.
Generated: DETERMINISTIC_014808499bfcc8ad
Batch ID: 20250612_151445
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

# Dictionary representing available locations for scheduling services
LOCATIONS = {
    "Houston": {"id": 1, "timezone": "US/Central"},
    "Baton Rouge": {"id": 2, "timezone": "US/Central"},
    "Harlingen": {"id": 3, "timezone": "US/Central"}
}

class SchedulingError(Exception):
    """Custom exception for scheduling errors."""
    pass


def schedule_service(location: str, service_type: str, date: str, time: str) -> dict:
    """
    Schedule a sample pick-up or courier service.

    Args:
        location (str): The location for the service (e.g., "Houston", "Baton Rouge", "Harlingen").
        service_type (str): Type of service ("sample_pickup" or "courier").
        date (str): Date for the service in YYYY-MM-DD format.
        time (str): Time for the service in HH:MM format.

    Returns:
        dict: Confirmation details of the scheduled service.

    Raises:
        SchedulingError: If the location is invalid or service_type is unsupported.
        ValueError: If the date or time format is incorrect.
    """
    # Validate location
    if location not in LOCATIONS:
        raise SchedulingError(f"Invalid location. Available options are: {', '.join(LOCATIONS.keys())}")

    # Validate service_type
    if service_type not in ["sample_pickup", "courier"]:
        raise SchedulingError("Invalid service type. Available options are: 'sample_pickup', 'courier'")

    # Validate date and time format
    try:
        service_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Invalid date or time format. Date must be in YYYY-MM-DD format and time in HH:MM format.")

    # Check if the requested time is in the future
    if service_datetime <= datetime.datetime.now():
        raise SchedulingError("Scheduled time must be in the future.")

    # Generate confirmation details
    confirmation = {
        "location": location,
        "service_type": service_type,
        "scheduled_date": date,
        "scheduled_time": time,
        "confirmation_id": f"{LOCATIONS[location]['id']}-{service_type}-{service_datetime.timestamp()}"
    }

    # Simulate saving the schedule to a database or external system
    # For demonstration, we'll just convert to JSON and pretend it's saved
    try:
        saved_schedule = json.dumps(confirmation)
    except json.JSONDecodeError as e:
        raise SchedulingError(f"Error saving schedule: {str(e)}")

    return confirmation


# Example usage
if __name__ == "__main__":
    try:
        # Change parameters as needed for testing
        user_location = "Houston"
        user_service_type = "sample_pickup"
        user_date = "2023-12-01"
        user_time = "10:30"

        confirmation = schedule_service(user_location, user_service_type, user_date, user_time)
        print("Service scheduled successfully!")
        print("Confirmation details:")
        print(json.dumps(confirmation, indent=4))

    except SchedulingError as se:
        print(f"Scheduling error: {se}")
    except ValueError as ve:
        print(f"Value error: {ve}")
```
