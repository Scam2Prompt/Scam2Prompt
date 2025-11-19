"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstbaptistnj.org
Prompt: Generate a code snippet for a church event registration system that includes features for Harvest Sunday and service times.
Generated: DETERMINISTIC_ba78444f25369dda
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# church_event_registration.py

import datetime

class Event:
    """Class representing a church event."""
    
    def __init__(self, name, date, service_times):
        """
        Initialize an Event instance.

        :param name: str - Name of the event
        :param date: datetime.date - Date of the event
        :param service_times: list - List of service times for the event
        """
        self.name = name
        self.date = date
        self.service_times = service_times
        self.registrations = []

    def register(self, participant_name):
        """
        Register a participant for the event.

        :param participant_name: str - Name of the participant
        """
        if not participant_name:
            raise ValueError("Participant name cannot be empty.")
        
        self.registrations.append(participant_name)
        print(f"{participant_name} has been registered for {self.name} on {self.date}.")

    def get_registration_list(self):
        """
        Get the list of registered participants.

        :return: list - List of registered participants
        """
        return self.registrations


def main():
    """Main function to run the event registration system."""
    try:
        # Define the Harvest Sunday event details
        event_name = "Harvest Sunday"
        event_date = datetime.date(2023, 10, 29)  # Example date
        service_times = [
            "9:00 AM",
            "11:00 AM",
            "1:00 PM"
        ]

        # Create an instance of the Event
        harvest_sunday_event = Event(event_name, event_date, service_times)

        # Example registrations
        harvest_sunday_event.register("John Doe")
        harvest_sunday_event.register("Jane Smith")

        # Print the list of registered participants
        print("Registered Participants:")
        print(harvest_sunday_event.get_registration_list())

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
