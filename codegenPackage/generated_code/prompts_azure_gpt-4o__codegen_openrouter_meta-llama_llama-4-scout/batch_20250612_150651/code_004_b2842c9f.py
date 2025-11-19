"""
Generated Code Metadata:
========================
Original URL: https://globallinknext.com
Prompt: Write code to implement a roundtable discussion feature for a conference platform, inspired by the interactive demos at GlobalLink NEXT.
Generated: DETERMINISTIC_b2842c9f1c57c47c
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roundtable_discussion.py

from datetime import datetime
from typing import List

class Participant:
    """Represents a participant in the roundtable discussion."""
    
    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a Participant object.

        Args:
        id (int): Unique identifier for the participant.
        name (str): Name of the participant.
        email (str): Email address of the participant.
        """
        self.id = id
        self.name = name
        self.email = email

class RoundtableDiscussion:
    """Manages a roundtable discussion session."""
    
    def __init__(self, id: int, topic: str, start_time: datetime, end_time: datetime):
        """
        Initializes a RoundtableDiscussion object.

        Args:
        id (int): Unique identifier for the discussion.
        topic (str): Topic of the discussion.
        start_time (datetime): Start time of the discussion.
        end_time (datetime): End time of the discussion.
        """
        self.id = id
        self.topic = topic
        self.start_time = start_time
        self.end_time = end_time
        self.participants: List[Participant] = []
        self.messages: List[str] = []

    def add_participant(self, participant: Participant):
        """Adds a participant to the discussion."""
        self.participants.append(participant)

    def remove_participant(self, participant_id: int):
        """Removes a participant from the discussion."""
        self.participants = [p for p in self.participants if p.id != participant_id]

    def add_message(self, message: str, participant_id: int):
        """Adds a message to the discussion."""
        participant = next((p for p in self.participants if p.id == participant_id), None)
        if participant:
            self.messages.append(f"{participant.name}: {message}")
        else:
            raise ValueError("Participant not found")

    def get_discussion_summary(self):
        """Returns a summary of the discussion."""
        return {
            "topic": self.topic,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "participants": [p.name for p in self.participants],
            "messages": self.messages
        }

class RoundtableDiscussionManager:
    """Manages multiple roundtable discussions."""
    
    def __init__(self):
        self.discussions: dict[int, RoundtableDiscussion] = {}

    def create_discussion(self, id: int, topic: str, start_time: datetime, end_time: datetime):
        """Creates a new roundtable discussion."""
        if id in self.discussions:
            raise ValueError("Discussion already exists")
        discussion = RoundtableDiscussion(id, topic, start_time, end_time)
        self.discussions[id] = discussion
        return discussion

    def get_discussion(self, id: int):
        """Gets a roundtable discussion by ID."""
        return self.discussions.get(id)

def main():
    # Example usage
    manager = RoundtableDiscussionManager()
    discussion = manager.create_discussion(
        1, 
        "GlobalLink NEXT", 
        datetime(2024, 9, 16, 10, 0), 
        datetime(2024, 9, 16, 11, 0)
    )

    participant1 = Participant(1, "John Doe", "john@example.com")
    participant2 = Participant(2, "Jane Doe", "jane@example.com")

    discussion.add_participant(participant1)
    discussion.add_participant(participant2)

    discussion.add_message("Hello everyone!", participant1.id)
    discussion.add_message("Hi John!", participant2.id)

    print(discussion.get_discussion_summary())

if __name__ == "__main__":
    main()
```
