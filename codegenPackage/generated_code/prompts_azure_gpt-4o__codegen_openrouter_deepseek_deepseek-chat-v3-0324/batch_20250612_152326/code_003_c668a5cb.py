"""
Generated Code Metadata:
========================
Original URL: https://mainnet-nobody.pages.dev
Prompt: Generate code to schedule events (e.g., minting, raffles, airdrops, refunds) based on UTC+8 time zones, as outlined in the "Nobody NFT" minting timeline.
Generated: DETERMINISTIC_c668a5cb49ee4dc0
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import pytz
from typing import Callable, Dict, Optional
from enum import Enum

class EventType(Enum):
    MINTING = "Minting"
    RAFFLE = "Raffle"
    AIRDROP = "Airdrop"
    REFUND = "Refund"

class EventScheduler:
    """
    A scheduler for NFT-related events based on UTC+8 timezone.
    """
    
    def __init__(self):
        self._events: Dict[EventType, Dict[str, datetime.datetime]] = {}
        self._callbacks: Dict[EventType, Callable] = {}
        self._timezone = pytz.timezone('Asia/Singapore')  # Singapore is UTC+8
        
    def add_event(
        self,
        event_type: EventType,
        event_name: str,
        event_time: datetime.datetime,
        callback: Optional[Callable] = None
    ) -> None:
        """
        Add an event to the scheduler.
        
        Args:
            event_type: Type of event (Minting, Raffle, etc.)
            event_name: Name/identifier for the event
            event_time: Time of the event (naive datetime assumed to be UTC+8)
            callback: Optional function to call when event occurs
        """
        if not event_time.tzinfo:
            event_time = self._timezone.localize(event_time)
        
        if event_type not in self._events:
            self._events[event_type] = {}
            
        self._events[event_type][event_name] = event_time
        
        if callback:
            self._callbacks[event_type] = callback
    
    def check_events(self) -> None:
        """
        Check if any scheduled events should be triggered based on current time.
        """
        now = datetime.datetime.now(self._timezone)
        
        for event_type, events in self._events.items():
            for event_name, event_time in events.items():
                if now >= event_time:
                    self._trigger_event(event_type, event_name)
    
    def _trigger_event(self, event_type: EventType, event_name: str) -> None:
        """
        Trigger an event and its associated callback if it exists.
        
        Args:
            event_type: Type of event being triggered
            event_name: Name of the event being triggered
        """
        print(f"Triggering event: {event_type.value} - {event_name}")
        
        if event_type in self._callbacks:
            try:
                self._callbacks[event_type]()
            except Exception as e:
                print(f"Error executing callback for {event_type.value}: {str(e)}")
        
        # Remove the triggered event
        del self._events[event_type][event_name]
        if not self._events[event_type]:
            del self._events[event_type]
            if event_type in self._callbacks:
                del self._callbacks[event_type]
    
    def get_upcoming_events(self) -> Dict[EventType, Dict[str, datetime.datetime]]:
        """
        Get all upcoming events that haven't been triggered yet.
        
        Returns:
            Dictionary of event types to event names and their times
        """
        return self._events.copy()

# Example usage
if __name__ == "__main__":
    def minting_callback():
        print("Executing minting process...")
    
    def raffle_callback():
        print("Executing raffle process...")
    
    scheduler = EventScheduler()
    
    # Add events (times are in UTC+8)
    minting_time = datetime.datetime(2023, 12, 25, 14, 0)  # Dec 25, 2023 2:00 PM UTC+8
    raffle_time = datetime.datetime(2023, 12, 26, 10, 0)   # Dec 26, 2023 10:00 AM UTC+8
    
    scheduler.add_event(EventType.MINTING, "Nobody NFT Mint", minting_time, minting_callback)
    scheduler.add_event(EventType.RAFFLE, "Nobody NFT Raffle", raffle_time, raffle_callback)
    
    # In a real application, you would call check_events() periodically
    # For demo purposes, we'll just print upcoming events
    print("Upcoming events:")
    for event_type, events in scheduler.get_upcoming_events().items():
        for name, time in events.items():
            print(f"{event_type.value}: {name} at {time}")
```
