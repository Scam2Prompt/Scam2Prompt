"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Write a program to simulate meal-sharing schedules in Kallimos Commons, allowing neighbors to opt into community meals while maintaining privacy.
Generated: DETERMINISTIC_99deac6b1215d544
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random
import uuid
from enum import Enum

class MealType(Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"

class PrivacyLevel(Enum):
    PUBLIC = "public"       # Visible to all community members
    SEMI_PRIVATE = "semi-private"  # Visible only to participants
    PRIVATE = "private"     # Not visible in schedules (direct invites only)

class Participant:
    def __init__(self, user_id: str, dietary_restrictions: List[str] = None):
        self.user_id = user_id
        self.dietary_restrictions = dietary_restrictions or []
    
    def to_dict(self) -> Dict:
        return {
            "user_id": self.user_id,
            "dietary_restrictions": self.dietary_restrictions
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Participant':
        return cls(
            user_id=data["user_id"],
            dietary_restrictions=data.get("dietary_restrictions", [])
        )

class MealEvent:
    def __init__(
        self,
        event_id: str,
        host_id: str,
        meal_type: MealType,
        datetime: datetime,
        max_participants: int,
        privacy_level: PrivacyLevel,
        description: str = "",
        location: str = "",
        participants: List[Participant] = None
    ):
        self.event_id = event_id
        self.host_id = host_id
        self.meal_type = meal_type
        self.datetime = datetime
        self.max_participants = max_participants
        self.privacy_level = privacy_level
        self.description = description
        self.location = location
        self.participants = participants or []
    
    def add_participant(self, participant: Participant) -> bool:
        if len(self.participants) >= self.max_participants:
            return False
        self.participants.append(participant)
        return True
    
    def remove_participant(self, user_id: str) -> bool:
        for i, participant in enumerate(self.participants):
            if participant.user_id == user_id:
                self.participants.pop(i)
                return True
        return False
    
    def is_visible_to(self, user_id: str) -> bool:
        if self.privacy_level == PrivacyLevel.PUBLIC:
            return True
        if self.privacy_level == PrivacyLevel.PRIVATE:
            return False
        # SEMI_PRIVATE - only visible to host and participants
        return user_id == self.host_id or any(p.user_id == user_id for p in self.participants)
    
    def to_dict(self) -> Dict:
        return {
            "event_id": self.event_id,
            "host_id": self.host_id,
            "meal_type": self.meal_type.value,
            "datetime": self.datetime.isoformat(),
            "max_participants": self.max_participants,
            "privacy_level": self.privacy_level.value,
            "description": self.description,
            "location": self.location,
            "participants": [p.to_dict() for p in self.participants]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MealEvent':
        return cls(
            event_id=data["event_id"],
            host_id=data["host_id"],
            meal_type=MealType(data["meal_type"]),
            datetime=datetime.fromisoformat(data["datetime"]),
            max_participants=data["max_participants"],
            privacy_level=PrivacyLevel(data["privacy_level"]),
            description=data.get("description", ""),
            location=data.get("location", ""),
            participants=[Participant.from_dict(p) for p in data.get("participants", [])]
        )

class MealSchedule:
    def __init__(self, community_id: str):
        self.community_id = community_id
        self.events: Dict[str, MealEvent] = {}
    
    def add_event(self, event: MealEvent) -> bool:
        if event.event_id in self.events:
            return False
        self.events[event.event_id] = event
        return True
    
    def remove_event(self, event_id: str) -> bool:
        if event_id not in self.events:
            return False
        del self.events[event_id]
        return True
    
    def get_events_for_user(self, user_id: str, start_date: datetime, end_date: datetime) -> List[MealEvent]:
        visible_events = []
        for event in self.events.values():
            if (start_date <= event.datetime <= end_date and 
                event.is_visible_to(user_id)):
                visible_events.append(event)
        return visible_events
    
    def join_event(self, event_id: str, participant: Participant) -> bool:
        if event_id not in self.events:
            return False
        return self.events[event_id].add_participant(participant)
    
    def leave_event(self, event_id: str, user_id: str) -> bool:
        if event_id not in self.events:
            return False
        return self.events[event_id].remove_participant(user_id)
    
    def to_dict(self) -> Dict:
        return {
            "community_id": self.community_id,
            "events": {eid: event.to_dict() for eid, event in self.events.items()}
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MealSchedule':
        schedule = cls(data["community_id"])
        schedule.events = {
            eid: MealEvent.from_dict(event_data) 
            for eid, event_data in data["events"].items()
        }
        return schedule

class MealScheduleManager:
    def __init__(self):
        self.communities: Dict[str, MealSchedule] = {}
    
    def create_community_schedule(self, community_id: str) -> bool:
        if community_id in self.communities:
            return False
        self.communities[community_id] = MealSchedule(community_id)
        return True
    
    def get_community_schedule(self, community_id: str) -> Optional[MealSchedule]:
        return self.communities.get(community_id)
    
    def save_to_file(self, filename: str) -> bool:
        try:
            with open(filename, 'w') as f:
                json.dump(
                    {cid: s.to_dict() for cid, s in self.communities.items()},
                    f,
                    indent=2
                )
            return True
        except (IOError, json.JSONDecodeError):
            return False
    
    def load_from_file(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.communities = {
                    cid: MealSchedule.from_dict(schedule_data)
                    for cid, schedule_data in data.items()
                }
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return False

def generate_sample_data(manager: MealScheduleManager):
    """Helper function to generate sample data for testing"""
    manager.create_community_schedule("kallimos_1")
    schedule = manager.get_community_schedule("kallimos_1")
    
    if not schedule:
        return
    
    # Generate some sample events
    now = datetime.now()
    for i in range(5):
        event = MealEvent(
            event_id=str(uuid.uuid4()),
            host_id=f"user_{random.randint(1, 10)}",
            meal_type=random.choice(list(MealType)),
            datetime=now + timedelta(days=i),
            max_participants=random.randint(2, 6),
            privacy_level=random.choice(list(PrivacyLevel)),
            description=f"Community meal #{i+1}",
            location=f"Home {random.randint(1, 20)}"
        )
        
        # Add some participants
        for j in range(random.randint(0, event.max_participants - 1)):
            participant = Participant(
                user_id=f"user_{random.randint(1, 10)}",
                dietary_restrictions=random.sample(
                    ["vegetarian", "vegan", "gluten-free", "nut-free"],
                    random.randint(0, 2)
                )
            )
            event.add_participant(participant)
        
        schedule.add_event(event)

def main():
    manager = MealScheduleManager()
    
    # Try to load existing data
    if not manager.load_from_file("meal_schedules.json"):
        print("No existing data found, generating sample data...")
        generate_sample_data(manager)
        manager.save_to_file("meal_schedules.json")
    
    # Example usage
    community_id = "kallimos_1"
    user_id = "user_1"
    
    schedule = manager.get_community_schedule(community_id)
    if schedule:
        today = datetime.now()
        next_week = today + timed
