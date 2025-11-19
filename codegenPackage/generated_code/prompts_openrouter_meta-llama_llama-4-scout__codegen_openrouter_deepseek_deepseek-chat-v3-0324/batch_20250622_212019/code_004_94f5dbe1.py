"""
Generated Code Metadata:
========================
Original URL: https://plf3108.com
Prompt: Design a system to manage and update odds in real-time for various sports events, similar to 868's sports betting feature, and provide a code example in a programming language of your choice.
Generated: DETERMINISTIC_94f5dbe1979b0dba
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
from typing import Dict, List, Optional
from dataclasses import dataclass
import random
import json
from datetime import datetime

@dataclass
class Event:
    id: str
    name: str
    sport: str
    start_time: datetime
    participants: List[str]
    current_odds: Dict[str, float]
    status: str  # 'upcoming', 'live', 'completed', 'canceled'

class OddsManager:
    def __init__(self):
        self.events: Dict[str, Event] = {}
        self.lock = threading.Lock()
        self._running = False
        self._update_thread = None

    def add_event(self, event: Event) -> None:
        """Add a new event to be tracked."""
        with self.lock:
            if event.id in self.events:
                raise ValueError(f"Event with ID {event.id} already exists")
            self.events[event.id] = event

    def update_odds(self, event_id: str, new_odds: Dict[str, float]) -> None:
        """Update odds for a specific event."""
        with self.lock:
            if event_id not in self.events:
                raise ValueError(f"Event with ID {event_id} not found")
            if self.events[event_id].status != 'upcoming' and self.events[event_id].status != 'live':
                raise ValueError("Can only update odds for upcoming or live events")
            self.events[event_id].current_odds = new_odds

    def get_event(self, event_id: str) -> Optional[Event]:
        """Get event details by ID."""
        with self.lock:
            return self.events.get(event_id)

    def get_all_events(self) -> List[Event]:
        """Get all events."""
        with self.lock:
            return list(self.events.values())

    def start_auto_updates(self, interval: float = 5.0) -> None:
        """Start automatic odds updates in background thread."""
        if self._running:
            return
            
        self._running = True
        self._update_thread = threading.Thread(
            target=self._auto_update_odds,
            args=(interval,),
            daemon=True
        )
        self._update_thread.start()

    def stop_auto_updates(self) -> None:
        """Stop automatic odds updates."""
        self._running = False
        if self._update_thread:
            self._update_thread.join()

    def _auto_update_odds(self, interval: float) -> None:
        """Background thread to simulate live odds updates."""
        while self._running:
            time.sleep(interval)
            with self.lock:
                for event in self.events.values():
                    if event.status in ('upcoming', 'live'):
                        # Simulate odds fluctuation
                        updated_odds = {
                            participant: max(1.01, odds * random.uniform(0.95, 1.05))
                            for participant, odds in event.current_odds.items()
                        }
                        event.current_odds = updated_odds

    def to_json(self) -> str:
        """Serialize events to JSON."""
        with self.lock:
            return json.dumps({
                event.id: {
                    'name': event.name,
                    'sport': event.sport,
                    'start_time': event.start_time.isoformat(),
                    'participants': event.participants,
                    'current_odds': event.current_odds,
                    'status': event.status
                }
                for event in self.events.values()
            }, indent=2)

# Example usage
if __name__ == "__main__":
    manager = OddsManager()
    
    # Add some sample events
    sample_event1 = Event(
        id="e1",
        name="Manchester United vs Liverpool",
        sport="Football",
        start_time=datetime(2023, 12, 15, 20, 0),
        participants=["Manchester United", "Liverpool"],
        current_odds={"Manchester United": 2.5, "Liverpool": 1.8, "Draw": 3.2},
        status="upcoming"
    )
    
    sample_event2 = Event(
        id="e2",
        name="Lakers vs Warriors",
        sport="Basketball",
        start_time=datetime(2023, 12, 16, 19, 30),
        participants=["Lakers", "Warriors"],
        current_odds={"Lakers": 1.9, "Warriors": 1.9},
        status="upcoming"
    )
    
    manager.add_event(sample_event1)
    manager.add_event(sample_event2)
    
    # Start auto-updating odds
    manager.start_auto_updates(interval=3.0)
    
    try:
        while True:
            time.sleep(5)
            print("Current odds:")
            for event in manager.get_all_events():
                print(f"{event.name}: {event.current_odds}")
            print("\n")
    except KeyboardInterrupt:
        manager.stop_auto_updates()
        print("\nStopped odds updates")
```
