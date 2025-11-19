"""
Generated Code Metadata:
========================
Original URL: https://firstbaptistnj.org
Prompt: Generate a code snippet for a church event registration system that includes features for Harvest Sunday and service times.
Generated: DETERMINISTIC_ba78444f25369dda
Batch ID: 20250612_163912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ChurchEventRegistration:
    """
    A class to manage church event registrations, including Harvest Sunday and service times.
    """

    def __init__(self):
        # Dictionary to store registered attendees
        self.registrations = {
            "Harvest Sunday": [],
            "Service Times": {}
        }
        # Predefined service times
        self.service_times = {
            "Morning Service": "9:00 AM",
            "Afternoon Service": "1:00 PM",
            "Evening Service": "6:00 PM"
        }

    def register_for_event(self, event_name, attendee_name):
        """
        Registers an attendee for a specific event.
        :param event_name: Name of the event (e.g., 'Harvest Sunday').
        :param attendee_name: Name of the attendee.
        """
        if event_name not in self.registrations:
            raise ValueError(f"Event '{event_name}' does not exist.")
        
        self.registrations[event_name].append(attendee_name)
        print(f"{attendee_name} successfully registered for {event_name}.")

    def register_for_service(self, service_name, attendee_name):
        """
        Registers an attendee for a specific service time.
        :param service_name: Name of the service (e.g., 'Morning Service').
        :param attendee_name: Name of the attendee.
        """
        if service_name not in self.service_times:
            raise ValueError(f"Service '{service_name}' does not exist.")
        
        if service_name not in self.registrations["Service Times"]:
            self.registrations["Service Times"][service_name] = []
        
        self.registrations["Service Times"][service_name].append(attendee_name)
        print(f"{attendee_name} successfully registered for {service_name} at {self.service_times[service_name]}.")

    def view_registrations(self):
        """
        Displays all registrations for events and service times.
        """
        print("\nEvent Registrations:")
        for event, attendees in self.registrations.items():
            if event == "Service Times":
                continue
            print(f"{event}: {', '.join(attendees) if attendees else 'No registrations yet.'}")
        
        print("\nService Time Registrations:")
        for service, attendees in self.registrations["Service Times"].items():
            print(f"{service} ({self.service_times[service]}): {', '.join(attendees) if attendees else 'No registrations yet.'}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the registration system
        registration_system = ChurchEventRegistration()

        # Register attendees for Harvest Sunday
        registration_system.register_for_event("Harvest Sunday", "John Doe")
        registration_system.register_for_event("Harvest Sunday", "Jane Smith")

        # Register attendees for specific service times
        registration_system.register_for_service("Morning Service", "Alice Johnson")
        registration_system.register_for_service("Evening Service", "Bob Brown")

        # View all registrations
        registration_system.view_registrations()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
