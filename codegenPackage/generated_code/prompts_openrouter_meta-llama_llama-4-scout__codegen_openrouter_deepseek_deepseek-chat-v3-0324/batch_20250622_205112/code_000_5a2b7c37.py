"""
Generated Code Metadata:
========================
Original URL: https://netcoworking.ch
Prompt: "Write a Python script to optimize a coworking space's scheduling system, taking into account networking events and productivity time, as discussed on NetCoworking."
Generated: DETERMINISTIC_5a2b7c37f47c27fb
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
from typing import List, Dict, Optional
from enum import Enum
from dataclasses import dataclass
import heapq

class EventType(Enum):
    NETWORKING = "networking"
    PRODUCTIVITY = "productivity"

@dataclass
class Event:
    start_time: datetime.datetime
    end_time: datetime.datetime
    event_type: EventType
    attendees: int
    description: str

class CoworkingSpaceScheduler:
    def __init__(self, space_capacity: int, min_networking_interval: int = 2):
        """
        Initialize the scheduler with space capacity and minimum networking interval (in hours).
        """
        self.space_capacity = space_capacity
        self.min_networking_interval = min_networking_interval
        self.scheduled_events: List[Event] = []
        
    def add_event(self, event: Event) -> bool:
        """
        Add an event to the schedule if it doesn't conflict with existing events.
        Returns True if event was added successfully, False otherwise.
        """
        if not self._validate_event(event):
            return False
            
        if self._check_conflicts(event):
            return False
            
        self.scheduled_events.append(event)
        self.scheduled_events.sort(key=lambda e: e.start_time)
        return True
        
    def _validate_event(self, event: Event) -> bool:
        """Validate event parameters."""
        if event.start_time >= event.end_time:
            return False
            
        if event.attendees > self.space_capacity:
            return False
            
        if event.event_type == EventType.NETWORKING:
            duration = (event.end_time - event.start_time).total_seconds() / 3600
            if duration > self.min_networking_interval:
                return False
                
        return True
        
    def _check_conflicts(self, new_event: Event) -> bool:
        """Check if new event conflicts with existing events."""
        for existing_event in self.scheduled_events:
            if (new_event.start_time < existing_event.end_time and 
                new_event.end_time > existing_event.start_time):
                return True
        return False
        
    def optimize_schedule(self) -> List[Event]:
        """
        Optimize the schedule by:
        1. Ensuring networking events are properly spaced
        2. Maximizing productive hours
        3. Balancing event types
        """
        if not self.scheduled_events:
            return []
            
        # Separate events by type
        networking_events = [e for e in self.scheduled_events if e.event_type == EventType.NETWORKING]
        productivity_events = [e for e in self.scheduled_events if e.event_type == EventType.PRODUCTIVITY]
        
        # Sort events by start time
        networking_events.sort(key=lambda e: e.start_time)
        productivity_events.sort(key=lambda e: e.start_time)
        
        optimized_schedule = []
        
        # Add productivity events first
        optimized_schedule.extend(productivity_events)
        
        # Add networking events with proper spacing
        last_networking_end = None
        for event in networking_events:
            if last_networking_end is None or (event.start_time - last_networking_end).total_seconds() / 3600 >= self.min_networking_interval:
                optimized_schedule.append(event)
                last_networking_end = event.end_time
                
        # Sort all events chronologically
        optimized_schedule.sort(key=lambda e: e.start_time)
        
        return optimized_schedule
        
    def get_schedule_json(self) -> str:
        """Return the current schedule as JSON."""
        schedule_data = []
        for event in self.scheduled_events:
            schedule_data.append({
                "start_time": event.start_time.isoformat(),
                "end_time": event.end_time.isoformat(),
                "event_type": event.event_type.value,
                "attendees": event.attendees,
                "description": event.description
            })
        return json.dumps(schedule_data, indent=2)
        
    def load_schedule_from_json(self, json_str: str) -> bool:
        """Load schedule from JSON string."""
        try:
            schedule_data = json.loads(json_str)
            new_events = []
            for item in schedule_data:
                try:
                    event = Event(
                        start_time=datetime.datetime.fromisoformat(item["start_time"]),
                        end_time=datetime.datetime.fromisoformat(item["end_time"]),
                        event_type=EventType(item["event_type"]),
                        attendees=item["attendees"],
                        description=item["description"]
                    )
                    new_events.append(event)
                except (KeyError, ValueError) as e:
                    print(f"Error parsing event: {e}")
                    continue
                    
            # Clear current schedule and add new events
            self.scheduled_events = []
            for event in new_events:
                if not self.add_event(event):
                    print(f"Failed to add event: {event.description}")
                    
            return True
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            return False

def example_usage():
    """Example usage of the CoworkingSpaceScheduler."""
    scheduler = CoworkingSpaceScheduler(space_capacity=50)
    
    # Create some events
    now = datetime.datetime.now()
    event1 = Event(
        start_time=now + datetime.timedelta(hours=1),
        end_time=now + datetime.timedelta(hours=2),
        event_type=EventType.PRODUCTIVITY,
        attendees=30,
        description="Morning work session"
    )
    
    event2 = Event(
        start_time=now + datetime.timedelta(hours=3),
        end_time=now + datetime.timedelta(hours=4),
        event_type=EventType.NETWORKING,
        attendees=20,
        description="Networking coffee break"
    )
    
    event3 = Event(
        start_time=now + datetime.timedelta(hours=5),
        end_time=now + datetime.timedelta(hours=7),
        event_type=EventType.PRODUCTIVITY,
        attendees=40,
        description="Afternoon deep work"
    )
    
    # Add events to scheduler
    scheduler.add_event(event1)
    scheduler.add_event(event2)
    scheduler.add_event(event3)
    
    # Optimize schedule
    optimized = scheduler.optimize_schedule()
    print("Optimized Schedule:")
    for event in optimized:
        print(f"{event.start_time.time()} - {event.end_time.time()}: {event.description} ({event.event_type.value})")
    
    # Get schedule as JSON
    print("\nSchedule JSON:")
    print(scheduler.get_schedule_json())

if __name__ == "__main__":
    example_usage()
```
