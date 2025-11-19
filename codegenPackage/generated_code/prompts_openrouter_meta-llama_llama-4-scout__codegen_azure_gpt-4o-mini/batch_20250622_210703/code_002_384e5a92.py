"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Write a Python script to manage event registrations for a corporate event in Bogotá, including social event planning and RSVP tracking.
Generated: DETERMINISTIC_384e5a92c35e8753
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class EventManager:
    def __init__(self, event_name, event_date, venue):
        """
        Initialize the EventManager with event details.
        
        :param event_name: Name of the event
        :param event_date: Date of the event (YYYY-MM-DD)
        :param venue: Venue of the event
        """
        self.event_name = event_name
        self.event_date = self._validate_date(event_date)
        self.venue = venue
        self.registrations = []
        self.social_events = []

    def _validate_date(self, date_str):
        """
        Validate the date format and return a datetime object.
        
        :param date_str: Date string in YYYY-MM-DD format
        :return: datetime object
        :raises ValueError: If the date format is incorrect
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    def register_participant(self, name, email):
        """
        Register a participant for the event.
        
        :param name: Name of the participant
        :param email: Email of the participant
        :raises ValueError: If the email is already registered
        """
        if any(reg['email'] == email for reg in self.registrations):
            raise ValueError("Email is already registered.")
        
        self.registrations.append({'name': name, 'email': email})
        print(f"Registered {name} with email {email}.")

    def add_social_event(self, social_event_name, social_event_date):
        """
        Add a social event to the event schedule.
        
        :param social_event_name: Name of the social event
        :param social_event_date: Date of the social event (YYYY-MM-DD)
        """
        social_event_date = self._validate_date(social_event_date)
        self.social_events.append({'name': social_event_name, 'date': social_event_date})
        print(f"Added social event: {social_event_name} on {social_event_date.date()}.")

    def get_registrations(self):
        """
        Get the list of registered participants.
        
        :return: List of registrations
        """
        return self.registrations

    def get_social_events(self):
        """
        Get the list of social events.
        
        :return: List of social events
        """
        return self.social_events

    def save_to_file(self, filename):
        """
        Save event details, registrations, and social events to a JSON file.
        
        :param filename: Name of the file to save the data
        """
        data = {
            'event_name': self.event_name,
            'event_date': self.event_date.strftime('%Y-%m-%d'),
            'venue': self.venue,
            'registrations': self.registrations,
            'social_events': self.social_events
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Data saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        event_manager = EventManager("Corporate Event", "2023-11-15", "Bogotá Convention Center")
        event_manager.register_participant("John Doe", "john.doe@example.com")
        event_manager.add_social_event("Networking Dinner", "2023-11-14")
        print("Registrations:", event_manager.get_registrations())
        print("Social Events:", event_manager.get_social_events())
        event_manager.save_to_file("event_data.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
