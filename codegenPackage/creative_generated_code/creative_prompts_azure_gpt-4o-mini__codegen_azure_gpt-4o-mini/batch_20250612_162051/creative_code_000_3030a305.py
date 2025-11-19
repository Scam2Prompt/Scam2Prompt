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

```python
class CommunityLeadershipProgram:
    def __init__(self):
        """
        Initializes the Community Leadership Program.

        Attributes:
            participants (list): A list to store participants' information.
            events (list): A list to store information about events.
        """
        self.participants = []
        self.events = []

    def add_participant(self, name, age, skills):
        """
        Adds a participant to the program.

        Args:
            name (str): The name of the participant.
            age (int): The age of the participant.
            skills (list): A list of skills the participant possesses.
        
        Raises:
            ValueError: If age is not a positive integer.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        
        participant = {
            'name': name,
            'age': age,
            'skills': skills
        }
        self.participants.append(participant)
        print(f"Participant {name} added successfully.")

    def schedule_event(self, event_name, date, description):
        """
        Schedules an event for the program.

        Args:
            event_name (str): The name of the event.
            date (str): The date of the event in 'YYYY-MM-DD' format.
            description (str): A brief description of the event.
        
        Raises:
            ValueError: If the date format is incorrect.
        """
        # Simple date validation (not comprehensive)
        try:
            year, month, day = map(int, date.split('-'))
            assert 1 <= month <= 12 and 1 <= day <= 31
        except (ValueError, AssertionError):
            raise ValueError("Date must be in 'YYYY-MM-DD' format and valid.")
        
        event = {
            'event_name': event_name,
            'date': date,
            'description': description
        }
        self.events.append(event)
        print(f"Event '{event_name}' scheduled successfully on {date}.")

    def show_participants(self):
        """Displays the list of participants."""
        if not self.participants:
            print("No participants have been added yet.")
            return
        
        print("Participants:")
        for participant in self.participants:
            print(f"- {participant['name']}, Age: {participant['age']}, Skills: {', '.join(participant['skills'])}")

    def show_events(self):
        """Displays the scheduled events."""
        if not self.events:
            print("No events have been scheduled yet.")
            return
        
        print("Scheduled Events:")
        for event in self.events:
            print(f"- {event['event_name']} on {event['date']}: {event['description']}")

# Example usage
if __name__ == "__main__":
    program = CommunityLeadershipProgram()
    
    # Adding participants
    try:
        program.add_participant("Adaobi", 30, ["Leadership", "Communication"])
        program.add_participant("Chinonso", 25, ["Entrepreneurship", "Cultural Advocacy"])
    except ValueError as e:
        print(f"Error adding participant: {e}")

    # Scheduling events
    try:
        program.schedule_event("Igbo Culture Workshop", "2023-11-15", "A workshop to promote Igbo culture and heritage.")
        program.schedule_event("Leadership Seminar", "2023-12-01", "A seminar focused on developing leadership skills among women.")
    except ValueError as e:
        print(f"Error scheduling event: {e}")

    # Displaying participants and events
    program.show_participants()
    program.show_events()
```
