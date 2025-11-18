"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Generate a script for automating event management and registration workflows in a CMS system tailored for cooperatives.
Generated: DETERMINISTIC_0a87da666661d58d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Set up logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Event:
    """
    Class to represent an event in the cooperative CMS.
    """
    def __init__(self, title, description, start_date, end_date):
        self.title = title
        self.description = description
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.participants = []

    def validate_date(self, date_str):
        """
        Validates the date format and ensures the end date is after the start date.
        """
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            return date_obj
        except ValueError as e:
            logging.error(f"Invalid date format for {date_str}: {e}")
            raise

    def add_participant(self, participant):
        """
        Adds a participant to the event.
        """
        self.participants.append(participant)
        logging.info(f"Participant {participant} added to event {self.title}.")

    def __str__(self):
        return f"Event: {self.title}, Description: {self.description}, Start: {self.start_date}, End: {self.end_date}, Participants: {len(self.participants)}"


class EventManager:
    """
    Class to manage events and registrations.
    """
    def __init__(self):
        self.events = []

    def create_event(self, title, description, start_date, end_date):
        """
        Creates a new event and adds it to the event list.
        """
        try:
            new_event = Event(title, description, start_date, end_date)
            self.events.append(new_event)
            logging.info(f"Event created: {new_event}")
            return new_event
        except Exception as e:
            logging.error(f"Failed to create event: {e}")

    def register_participant(self, event_title, participant):
        """
        Registers a participant for a given event.
        """
        for event in self.events:
            if event.title == event_title:
                event.add_participant(participant)
                return
        logging.warning(f"Event '{event_title}' not found for registration.")

    def list_events(self):
        """
        Lists all events currently managed by the EventManager.
        """
        return [str(event) for event in self.events]


# Example Usage
if __name__ == "__main__":
    manager = EventManager()

    # Creating events
    manager.create_event("Cooperative Annual Meeting", "Discuss annual goals and achievements.", "2023-10-01", "2023-10-02")
    manager.create_event("Workshop on Cooperative Management", "Hands-on workshop to improve management skills.", "2023-11-15", "2023-11-15")

    # Registering participants
    manager.register_participant("Cooperative Annual Meeting", "Alice Smith")
    manager.register_participant("Cooperative Annual Meeting", "Bob Johnson")

    # Listing all events
    events = manager.list_events()
    for event in events:
        print(event)
```
