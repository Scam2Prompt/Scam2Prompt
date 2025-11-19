"""
Generated Code Metadata:
========================
Original URL: https://linkmp.org
Prompt: What are the unique features of the Link Meeting Planner that can enhance my scheduling process?
Generated: DETERMINISTIC_f6f0e2edecb529b0
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Link Meeting Planner - Feature Demo

```python
"""
Link Meeting Planner - Feature Demonstration

This script demonstrates the unique features of the Link Meeting Planner
that enhance the scheduling process.
"""

from datetime import datetime, timedelta
import json
from typing import List, Dict, Optional
import uuid
from enum import Enum, auto

class Participant:
    """Represents a meeting participant with availability constraints."""
    def __init__(self, name: str, email: str, timezone: str = "UTC"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.timezone = timezone
        self.availability = []
        self.preferences = {}

    def add_availability(self, start: datetime, end: datetime) -> None:
        """Adds a time slot when the participant is available."""
        if start >= end:
            raise ValueError("End time must be after start time")
        self.availability.append((start, end))

    def set_preference(self, key: str, value: str) -> None:
        """Sets a scheduling preference for the participant."""
        self.preferences[key] = value

    def to_dict(self) -> Dict:
        """Serializes participant data to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "timezone": self.timezone,
            "availability": [(s.isoformat(), e.isoformat()) for s, e in self.availability],
            "preferences": self.preferences
        }

class MeetingType(Enum):
    """Enumeration of meeting types."""
    ONE_ON_ONE = auto()
    TEAM = auto()
    INTERVIEW = auto()
    CLIENT = auto()

class Meeting:
    """Represents a meeting with participants and scheduling constraints."""
    def __init__(self, title: str, duration: int, meeting_type: MeetingType = MeetingType.TEAM):
        self.id = str(uuid.uuid4())
        self.title = title
        self.duration = duration  # in minutes
        self.type = meeting_type
        self.participants = []
        self.suggested_times = []
        self.final_time = None
        self.location = None
        self.agenda = []

    def add_participant(self, participant: Participant) -> None:
        """Adds a participant to the meeting."""
        if any(p.id == participant.id for p in self.participants):
            raise ValueError("Participant already added to meeting")
        self.participants.append(participant)

    def find_optimal_time(self, min_participants: int = 1) -> List[datetime]:
        """
        Finds optimal meeting times based on participant availability.
        
        Args:
            min_participants: Minimum number of participants that must be available
            
        Returns:
            List of potential meeting start times
        """
        if len(self.participants) < min_participants:
            raise ValueError(f"Not enough participants (need {min_participants})")

        # Get all availability windows from participants
        all_windows = []
        for participant in self.participants:
            all_windows.extend(participant.availability)

        # Find overlapping availability
        if not all_windows:
            return []

        # Sort by start time
        all_windows.sort(key=lambda x: x[0])

        # Find overlaps that can accommodate the meeting duration
        optimal_times = []
        current_overlap_start, current_overlap_end = all_windows[0]

        for window in all_windows[1:]:
            window_start, window_end = window
            overlap_start = max(current_overlap_start, window_start)
            overlap_end = min(current_overlap_end, window_end)

            if overlap_start < overlap_end:
                current_overlap_start = overlap_start
                current_overlap_end = overlap_end

                delta = overlap_end - overlap_start
                if delta >= timedelta(minutes=self.duration):
                    optimal_times.append(overlap_start)
            else:
                current_overlap_start, current_overlap_end = window

        self.suggested_times = optimal_times
        return optimal_times

    def schedule_meeting(self, start_time: datetime) -> bool:
        """Finalizes a meeting time after confirming participant availability."""
        if not self.suggested_times:
            raise ValueError("No suggested times available. Run find_optimal_time() first.")

        duration = timedelta(minutes=self.duration)
        end_time = start_time + duration

        # Check if selected time is in suggested times
        is_valid = False
        for suggested in self.suggested_times:
            if suggested <= start_time <= suggested + timedelta(minutes=self.duration):
                is_valid = True
                break

        if not is_valid:
            return False

        # Check participant availability
        for participant in self.participants:
            available = False
            for avail_start, avail_end in participant.availability:
                if avail_start <= start_time and end_time <= avail_end:
                    available = True
                    break
            if not available:
                return False

        self.final_time = (start_time, end_time)
        return True

    def add_agenda_item(self, title: str, duration: int, presenter: Optional[Participant] = None) -> None:
        """Adds an item to the meeting agenda."""
        self.agenda.append({
            "title": title,
            "duration": duration,
            "presenter": presenter.id if presenter else None
        })

    def generate_invite(self) -> Dict:
        """Generates a meeting invitation with all details."""
        if not self.final_time:
            raise ValueError("Meeting time not finalized")

        return {
            "meeting_id": self.id,
            "title": self.title,
            "start_time": self.final_time[0].isoformat(),
            "end_time": self.final_time[1].isoformat(),
            "duration": self.duration,
            "type": self.type.name,
            "location": self.location,
            "participants": [p.to_dict() for p in self.participants],
            "agenda": self.agenda
        }

class Scheduler:
    """Core scheduler class with advanced features."""
    def __init__(self):
        self.meetings = []
        self.participants = []

    def create_meeting(self, title: str, duration: int, meeting_type: MeetingType) -> Meeting:
        """Creates a new meeting."""
        meeting = Meeting(title, duration, meeting_type)
        self.meetings.append(meeting)
        return meeting

    def add_participant(self, name: str, email: str, timezone: str = "UTC") -> Participant:
        """Creates and stores a new participant."""
        participant = Participant(name, email, timezone)
        self.participants.append(participant)
        return participant

    def save_schedule(self, filename: str) -> None:
        """Saves all meetings and participants to JSON file."""
        data = {
            "meetings": [m.generate_invite() for m in self.meetings if m.final_time],
            "participants": [p.to_dict() for p in self.participants]
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_schedule(self, filename: str) -> None:
        """Loads meetings and participants from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)

        self.participants = []
        participant_map = {}

        # Load participants first
        for p_data in data.get("participants", []):
            p = Participant(
                name=p_data["name"],
                email=p_data["email"],
                timezone=p_data["timezone"]
            )
            p.id = p_data["id"]
            for s, e in p_data["availability"]:
                p.add_availability(datetime.fromisoformat(s), datetime.fromisoformat(e))
            p.preferences = p_data["preferences"]
            participant_map[p.id] = p
            self.participants.append(p)

        # Load meetings
        self.meetings = []
        for m_data in data.get("meetings", []):
            m = Meeting(
                title=m_data["title"],
                duration=m_data["duration"],
                meeting_type=MeetingType[m_data["type"]]
            )
            m.id = m_data["meeting_id"]
            m.location = m_data["location"]
            m.agenda = m_data["agenda"]
            
            # Set final time
            if "start_time" in m_data and "end_time" in m_data:
                m.final_time = (
                    datetime.fromisoformat(m_data["start_time"]),
                    datetime.fromisoformat(m_data["end_time"])
                )

            # Add participants
            for p_data in m_data["participants"]:
                if p_data["id"] in participant_map:
                    m.add_participant(participant_map[p_data["id"]])

            self.meetings.append(m)

# Example usage demonstrating unique features
def demo_link_meeting_planner_features():
    """Demonstrates the unique features of the Link Meeting Planner."""
    # Initialize scheduler
    scheduler = S
