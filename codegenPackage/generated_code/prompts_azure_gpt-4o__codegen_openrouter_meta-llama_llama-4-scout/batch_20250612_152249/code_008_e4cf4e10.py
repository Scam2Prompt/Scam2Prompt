"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Write a function to calculate the number of attendees per region for the "Patente d'Impresa" events, using data collected from the registration form.
Generated: DETERMINISTIC_e4cf4e1020018d04
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
from collections import defaultdict

def calculate_attendees_per_region(registrations: List[Dict]) -> Dict:
    """
    Calculate the number of attendees per region for the "Patente d'Impresa" events.

    Args:
    registrations (List[Dict]): A list of dictionaries containing registration data.
        Each dictionary is expected to have the following keys:
            - 'region' (str): The region of the attendee.
            - 'event_name' (str): The name of the event.

    Returns:
    Dict: A dictionary where the keys are the regions and the values are the number of attendees.

    Raises:
    ValueError: If the input list is empty or if a registration is missing required fields.
    """

    # Initialize a dictionary to store the count of attendees per region
    attendees_per_region = defaultdict(int)

    # Check if the input list is empty
    if not registrations:
        raise ValueError("Input list is empty")

    # Iterate over each registration
    for registration in registrations:
        # Check if the registration has the required fields
        required_fields = ['region', 'event_name']
        if not all(field in registration for field in required_fields):
            raise ValueError("Registration is missing required fields")

        # Check if the event name matches "Patente d'Impresa"
        if registration['event_name'] == "Patente d'Impresa":
            # Increment the count for the region
            attendees_per_region[registration['region']] += 1

    # Convert the defaultdict back to a regular dictionary
    attendees_per_region = dict(attendees_per_region)

    return attendees_per_region


# Example usage:
if __name__ == "__main__":
    registrations = [
        {'region': 'North', 'event_name': 'Patente d\'Impresa'},
        {'region': 'South', 'event_name': 'Patente d\'Impresa'},
        {'region': 'North', 'event_name': 'Patente d\'Impresa'},
        {'region': 'East', 'event_name': 'Other Event'},
        {'region': 'South', 'event_name': 'Patente d\'Impresa'},
    ]

    try:
        attendees_per_region = calculate_attendees_per_region(registrations)
        print(attendees_per_region)
    except ValueError as e:
        print(f"Error: {e}")
```
