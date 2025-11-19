"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nkatandiinyom.com
Prompt: How can I implement a community leadership program that empowers women while preserving Igbo culture, as described by Nkata ndi Inyom Igbo?
Generated: DETERMINISTIC_3030a305c4938658
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a registration and event management system for a community leadership program that empowers women while preserving Igbo culture, inspired by Nkata ndi Inyom Igbo.

```python
import json
import datetime


class CommunityLeadershipProgram:
    """
    A class to manage the community leadership program, including registration of participants 
    and organizing events that preserve Igbo culture and empower women.
    """

    def __init__(self):
        # Initialize participants and events data
        self.participants = []
        self.events = []

    def register_participant(self, name, age, contact, skills):
        """
        Register a new participant in the program.
        :param name: Full name of the participant
        :param age: Age of the participant
        :param contact: Contact information of the participant
        :param skills: Skills or areas of expertise of the participant
        """
        if age < 18:
            raise ValueError("Participant must be at least 18 years old.")

        participant = {
            "name": name,
            "age": age,
            "contact": contact,
            "skills": skills,
            "registration_date": datetime.date.today().isoformat()
        }

        self.participants.append(participant)
        self._save_to_file()

    def create_event(self, title, description, date, venue):
        """
        Create a new event for the program.
        :param title: Title of the event
        :param description: Description of the event
        :param date: Date of the event (YYYY-MM-DD)
        :param venue: Venue for the event
        """
        try:
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if event_date < datetime.date.today():
            raise ValueError("Event date cannot be in the past.")

        event = {
            "title": title,
            "description": description,
            "date": event_date.isoformat(),
            "venue": venue
        }

        self.events.append(event)
        self._save_to_file()

    def view_participants(self):
        """
        View all registered participants.
        :return: List of participants
        """
        return self.participants

    def view_events(self):
        """
        View all created events.
        :return: List of events
        """
        return self.events

    def _save_to_file(self):
        """
        Save participants and events data to a file for persistence.
        """
        data = {
            "participants": self.participants,
            "events": self.events
        }

        with open("community_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def _load_from_file(self):
        """
        Load participants and events data from the file.
        """
        try:
            with open("community_data.json", "r") as file:
                data = json.load(file)
                self.participants = data.get("participants", [])
                self.events = data.get("events", [])
        except (FileNotFoundError, json.JSONDecodeError):
            # If file does not exist or has invalid data, initialize empty lists
            self.participants = []
            self.events = []


# Example usage
if __name__ == "__main__":
    try:
        program = CommunityLeadershipProgram()
        program._load_from_file()

        # Register participants
        program.register_participant(
            name="Adaobi Njoku",
            age=35,
            contact="adaobi.njoku@example.com",
            skills=["Leadership", "Community Advocacy"]
        )

        # Create events
        program.create_event(
            title="Igbo Culture Workshop",
            description="A workshop to teach Igbo language and traditional practices.",
            date="2024-03-15",
            venue="Community Hall, Enugu"
        )

        # View participants
        participants = program.view_participants()
        print("Registered Participants:")
        for participant in participants:
            print(participant)

        # View events
        events = program.view_events()
        print("\nScheduled Events:")
        for event in events:
            print(event)

    except Exception as e:
        print(f"Error: {e}")
```

This code is production-ready, handles errors gracefully, and follows Python best practices. It uses JSON files for data persistence, allowing the program's data to be reused across sessions.
