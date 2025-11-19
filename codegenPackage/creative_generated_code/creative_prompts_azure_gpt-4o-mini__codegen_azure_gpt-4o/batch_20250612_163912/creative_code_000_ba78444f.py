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
from datetime import datetime
import json

# Define the Event class to store event details
class Event:
    def __init__(self, name, date, time, description=None):
        self.name = name
        self.date = date
        self.time = time
        self.description = description

    def to_dict(self):
        """Convert event details to a dictionary for serialization."""
        return {
            "name": self.name,
            "date": self.date.strftime("%Y-%m-%d"),
            "time": self.time.strftime("%H:%M"),
            "description": self.description
        }

# Define the Registration class to handle registrations
class Registration:
    def __init__(self):
        # Store registrations in a list
        self.registrations = []

    def add_registration(self, name, email, event):
        """Add a registration to the event."""
        registration = {
            "name": name,
            "email": email,
            "event": event.to_dict()
        }
        self.registrations.append(registration)
        print(f"Registration successful for {name} for event '{event.name}'.")

    def list_registrations(self):
        """List all registrations."""
        return self.registrations

    def save_to_file(self, file_path):
        """Save registrations to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(self.registrations, file, indent=4)
            print(f"Registrations saved to {file_path}")
        except IOError as e:
            print(f"Error saving to file: {e}")

# Example usage of the event registration system
if __name__ == "__main__":
    # Initialize the registration system
    registration_system = Registration()

    # Create events
    harvest_sunday = Event(
        name="Harvest Sunday",
        date=datetime(2023, 11, 5),
        time=datetime.strptime("10:00", "%H:%M"),
        description="A special Harvest Sunday event with lunch provided."
    )

    morning_service = Event(
        name="Morning Service",
        date=datetime(2023, 11, 12),
        time=datetime.strptime("09:00", "%H:%M"),
        description="Traditional worship service."
    )

    evening_service = Event(
        name="Evening Service",
        date=datetime(2023, 11, 12),
        time=datetime.strptime("18:00", "%H:%M"),
        description="Contemporary worship service."
    )

    # Add registrations for events
    registration_system.add_registration(
        name="John Doe",
        email="john.doe@example.com",
        event=harvest_sunday
    )

    registration_system.add_registration(
        name="Jane Smith",
        email="jane.smith@example.com",
        event=morning_service
    )

    registration_system.add_registration(
        name="Emily Johnson",
        email="emily.johnson@example.com",
        event=evening_service
    )

    # List all registrations
    all_registrations = registration_system.list_registrations()
    print("Current Registrations:")
    print(json.dumps(all_registrations, indent=4))

    # Save registrations to a file
    registration_system.save_to_file("registrations.json")
```
