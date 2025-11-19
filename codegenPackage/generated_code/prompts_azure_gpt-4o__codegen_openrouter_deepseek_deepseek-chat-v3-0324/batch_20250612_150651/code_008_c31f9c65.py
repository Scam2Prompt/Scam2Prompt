"""
Generated Code Metadata:
========================
Original URL: https://globallinknext.com
Prompt: Write code to simulate a networking feature for professionals attending a virtual conference, based on the networking opportunities described at GlobalLink NEXT.
Generated: DETERMINISTIC_c31f9c659a80480e
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import uuid
from enum import Enum, auto


class User:
    def __init__(self, user_id: str, name: str, email: str, company: str, title: str, 
                 interests: List[str], availability: Dict[str, List[str]]):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.company = company
        self.title = title
        self.interests = interests
        self.availability = availability
        self.connections = []

    def add_connection(self, user_id: str):
        if user_id not in self.connections:
            self.connections.append(user_id)

    def __repr__(self):
        return f"User(name='{self.name}', company='{self.company}')"


class EventType(Enum):
    ONE_ON_ONE = auto()
    GROUP_SESSION = auto()
    ROUNDTABLE = auto()
    SPEED_NETWORKING = auto()


class NetworkingEvent:
    def __init__(self, event_id: str, event_type: EventType, participants: List[str], 
                 scheduled_time: datetime, duration: int, topic: Optional[str] = None):
        self.event_id = event_id
        self.event_type = event_type
        self.participants = participants
        self.scheduled_time = scheduled_time
        self.duration = duration
        self.topic = topic
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __repr__(self):
        return (f"NetworkingEvent(type={self.event_type.name}, "
                f"time={self.scheduled_time}, participants={len(self.participants)})")


class NetworkingEngine:
    def __init__(self):
        self.users = {}
        self.events = {}
        self.interest_groups = {}

    def register_user(self, user: User):
        if user.user_id in self.users:
            raise ValueError("User already registered")
        self.users[user.user_id] = user
        
        # Add user to interest groups
        for interest in user.interests:
            if interest not in self.interest_groups:
                self.interest_groups[interest] = []
            self.interest_groups[interest].append(user.user_id)

    def find_potential_matches(self, user_id: str, max_matches: int = 5) -> List[User]:
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        potential_matches = []
        
        # Find users with matching interests who aren't already connected
        for interest in user.interests:
            for other_user_id in self.interest_groups.get(interest, []):
                if (other_user_id != user_id and 
                    other_user_id not in user.connections and
                    other_user_id not in potential_matches):
                    potential_matches.append(self.users[other_user_id])
                    if len(potential_matches) >= max_matches:
                        return potential_matches
        
        return potential_matches

    def schedule_one_on_one(self, user1_id: str, user2_id: str, duration: int = 30) -> NetworkingEvent:
        if user1_id not in self.users or user2_id not in self.users:
            raise ValueError("One or both users not found")
        
        # Find common availability
        user1 = self.users[user1_id]
        user2 = self.users[user2_id]
        
        common_slots = self._find_common_availability(user1, user2)
        if not common_slots:
            raise ValueError("No common availability found")
        
        # Pick the first available slot
        date, time_slot = common_slots[0]
        start_time = datetime.strptime(f"{date} {time_slot.split('-')[0]}", "%Y-%m-%d %H:%M")
        
        event_id = str(uuid.uuid4())
        event = NetworkingEvent(
            event_id=event_id,
            event_type=EventType.ONE_ON_ONE,
            participants=[user1_id, user2_id],
            scheduled_time=start_time,
            duration=duration
        )
        
        self.events[event_id] = event
        return event

    def schedule_group_session(self, user_ids: List[str], duration: int = 60, 
                              topic: Optional[str] = None) -> NetworkingEvent:
        if not all(uid in self.users for uid in user_ids):
            raise ValueError("One or more users not found")
        
        if len(user_ids) < 3:
            raise ValueError("Group sessions require at least 3 participants")
        
        # Find common availability among all participants
        common_slots = None
        for user_id in user_ids:
            user = self.users[user_id]
            if common_slots is None:
                common_slots = set(user.availability.items())
            else:
                user_slots = set(user.availability.items())
                common_slots.intersection_update(user_slots)
        
        if not common_slots:
            raise ValueError("No common availability found among participants")
        
        # Pick the first available slot
        date, time_slots = next(iter(common_slots))
        time_slot = time_slots[0]
        start_time = datetime.strptime(f"{date} {time_slot.split('-')[0]}", "%Y-%m-%d %H:%M")
        
        event_id = str(uuid.uuid4())
        event = NetworkingEvent(
            event_id=event_id,
            event_type=EventType.GROUP_SESSION,
            participants=user_ids,
            scheduled_time=start_time,
            duration=duration,
            topic=topic
        )
        
        self.events[event_id] = event
        return event

    def schedule_speed_networking(self, user_ids: List[str], rounds: int = 5, 
                                 duration_per_round: int = 5) -> List[NetworkingEvent]:
        if len(user_ids) < 2:
            raise ValueError("Need at least 2 participants for speed networking")
        
        # Find common availability
        common_slots = None
        for user_id in user_ids:
            user = self.users[user_id]
            if common_slots is None:
                common_slots = set(user.availability.items())
            else:
                user_slots = set(user.availability.items())
                common_slots.intersection_update(user_slots)
        
        if not common_slots:
            raise ValueError("No common availability found among participants")
        
        # Pick the first available slot
        date, time_slots = next(iter(common_slots))
        time_slot = time_slots[0]
        start_time = datetime.strptime(f"{date} {time_slot.split('-')[0]}", "%Y-%m-%d %H:%M")
        
        events = []
        for i in range(rounds):
            # Shuffle participants for each round
            shuffled = random.sample(user_ids, len(user_ids))
            
            # Pair up participants
            for j in range(0, len(shuffled), 2):
                if j+1 >= len(shuffled):
                    break  # Odd number of participants
                
                pair = [shuffled[j], shuffled[j+1]]
                event_id = str(uuid.uuid4())
                event = NetworkingEvent(
                    event_id=event_id,
                    event_type=EventType.SPEED_NETWORKING,
                    participants=pair,
                    scheduled_time=start_time + timedelta(minutes=i * duration_per_round),
                    duration=duration_per_round
                )
                self.events[event_id] = event
                events.append(event)
        
        return events

    def _find_common_availability(self, user1: User, user2: User) -> List[tuple]:
        common_slots = []
        
        # Check for common dates
        common_dates = set(user1.availability.keys()) & set(user2.availability.keys())
        for date in common_dates:
            # Check for overlapping time slots
            user1_slots = user1.availability[date]
            user2_slots = user2.availability[date]
            
            common_time_slots = set(user1_slots) & set(user2_slots)
            if common_time_slots:
                common_slots.append((date, list(common_time_slots)[0]))
        
        return common_slots

    def complete_event(self, event_id: str):
        if event_id not in self.events:
            raise ValueError("Event not found")
        
        event = self.events[event_id]
        if event.is_completed:
            return
        
        # Add connections for participants
        for user_id in event.participants:
            user = self.users[user_id]
            for other_user_id in event.participants:
                if other_user_id != user_id:
                    user.add_connection(other_user_id)
        
        event.mark_completed()

    def get_user_schedule(self, user_id: str) -> List[NetworkingEvent]:
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user_events = []
        for event in self.events.values():
            if user
