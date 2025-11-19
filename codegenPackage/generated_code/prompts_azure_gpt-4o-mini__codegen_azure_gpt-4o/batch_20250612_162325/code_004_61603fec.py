"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Illustrate how to integrate sports programs into youth empowerment initiatives, using examples from Child Nepal's approach.
Generated: DETERMINISTIC_61603fec479e0bf3
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to integrate sports programs into youth empowerment initiatives.
It uses a simplified example inspired by Child Nepal's approach, focusing on organizing sports events
and tracking participation to promote teamwork, leadership, and personal growth among youth.
"""

import logging
from datetime import datetime

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("sports_program.log"), logging.StreamHandler()]
)

class YouthEmpowermentProgram:
    """
    A class to represent a youth empowerment program that integrates sports activities.
    """

    def __init__(self, program_name):
        """
        Initialize the program with a name and an empty list of participants and events.
        """
        self.program_name = program_name
        self.participants = []
        self.events = []
        logging.info(f"Program '{self.program_name}' initialized.")

    def add_participant(self, name, age):
        """
        Add a participant to the program.
        :param name: Name of the participant
        :param age: Age of the participant
        """
        if age < 5 or age > 25:
            logging.error("Age must be between 5 and 25.")
            raise ValueError("Age must be between 5 and 25.")
        self.participants.append({"name": name, "age": age})
        logging.info(f"Participant '{name}' added to the program.")

    def create_event(self, event_name, date, sport_type):
        """
        Create a sports event.
        :param event_name: Name of the event
        :param date: Date of the event (YYYY-MM-DD)
        :param sport_type: Type of sport (e.g., football, basketball)
        """
        try:
            event_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            logging.error("Invalid date format. Use YYYY-MM-DD.")
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        self.events.append({
            "event_name": event_name,
            "date": event_date,
            "sport_type": sport_type,
            "participants": []
        })
        logging.info(f"Event '{event_name}' created for {sport_type} on {date}.")

    def register_participant_to_event(self, participant_name, event_name):
        """
        Register a participant to a specific event.
        :param participant_name: Name of the participant
        :param event_name: Name of the event
        """
        participant = next((p for p in self.participants if p["name"] == participant_name), None)
        if not participant:
            logging.error(f"Participant '{participant_name}' not found.")
            raise ValueError(f"Participant '{participant_name}' not found.")
        
        event = next((e for e in self.events if e["event_name"] == event_name), None)
        if not event:
            logging.error(f"Event '{event_name}' not found.")
            raise ValueError(f"Event '{event_name}' not found.")
        
        event["participants"].append(participant)
        logging.info(f"Participant '{participant_name}' registered for event '{event_name}'.")

    def list_events(self):
        """
        List all events with their details.
        """
        logging.info("Listing all events:")
        for event in self.events:
            logging.info(f"Event: {event['event_name']}, Date: {event['date'].strftime('%Y-%m-%d')}, Sport: {event['sport_type']}, Participants: {len(event['participants'])}")

    def list_participants(self):
        """
        List all participants in the program.
        """
        logging.info("Listing all participants:")
        for participant in self.participants:
            logging.info(f"Name: {participant['name']}, Age: {participant['age']}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the program
        program = YouthEmpowermentProgram("Child Nepal Sports Initiative")

        # Add participants
        program.add_participant("Alice", 15)
        program.add_participant("Bob", 20)

        # Create events
        program.create_event("Football Tournament", "2023-11-15", "Football")
        program.create_event("Basketball Workshop", "2023-12-01", "Basketball")

        # Register participants to events
        program.register_participant_to_event("Alice", "Football Tournament")
        program.register_participant_to_event("Bob", "Basketball Workshop")

        # List events and participants
        program.list_events()
        program.list_participants()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
