"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: Write a function that automates the scheduling of entertainers for various events, inspired by the services offered by Jam UAE.
Generated: DETERMINISTIC_aa8dce38eb860a39
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import random

class EventType(Enum):
    WEDDING = "Wedding"
    CORPORATE = "Corporate Event"
    BIRTHDAY = "Birthday Party"
    CONCERT = "Concert"
    OTHER = "Other"

class EntertainerType(Enum):
    SINGER = "Singer"
    BAND = "Band"
    DJ = "DJ"
    MAGICIAN = "Magician"
    COMEDIAN = "Comedian"
    DANCER = "Dancer"

@dataclass
class Entertainer:
    id: str
    name: str
    type: EntertainerType
    hourly_rate: float
    availability: List[datetime.date]
    genres: List[str]
    rating: float

@dataclass
class Event:
    id: str
    name: str
    type: EventType
    date: datetime.date
    duration_hours: int
    budget: float
    preferred_entertainer_types: List[EntertainerType]
    preferred_genres: List[str]

class Scheduler:
    def __init__(self, entertainers: List[Entertainer]):
        self.entertainers = entertainers

    def _is_entertainer_available(self, entertainer: Entertainer, event_date: datetime.date) -> bool:
        return event_date in entertainer.availability

    def _is_within_budget(self, entertainer: Entertainer, event: Event) -> bool:
        total_cost = entertainer.hourly_rate * event.duration_hours
        return total_cost <= event.budget

    def _matches_preferences(self, entertainer: Entertainer, event: Event) -> bool:
        type_match = entertainer.type in event.preferred_entertainer_types
        genre_match = any(genre in event.preferred_genres for genre in entertainer.genres)
        return type_match and genre_match

    def find_available_entertainers(self, event: Event) -> List[Entertainer]:
        available_entertainers = []
        for entertainer in self.entertainers:
            if (self._is_entertainer_available(entertainer, event.date) and
                self._is_within_budget(entertainer, event) and
                self._matches_preferences(entertainer, event)):
                available_entertainers.append(entertainer)
        return available_entertainers

    def schedule_entertainer(self, event: Event, entertainer_id: str) -> Optional[Entertainer]:
        for entertainer in self.entertainers:
            if (entertainer.id == entertainer_id and
                self._is_entertainer_available(entertainer, event.date) and
                self._is_within_budget(entertainer, event)):
                entertainer.availability.remove(event.date)
                return entertainer
        return None

    def recommend_entertainers(self, event: Event, top_n: int = 3) -> List[Entertainer]:
        available = self.find_available_entertainers(event)
        # Sort by rating (descending) and then by cost (ascending)
        available.sort(key=lambda x: (-x.rating, x.hourly_rate))
        return available[:top_n]

def generate_sample_entertainers() -> List[Entertainer]:
    entertainers = []
    types = list(EntertainerType)
    genres = ["Pop", "Rock", "Jazz", "Hip Hop", "Classical", "Arabic", "Electronic"]
    
    for i in range(1, 21):
        entertainer_type = random.choice(types)
        available_dates = [
            datetime.date.today() + datetime.timedelta(days=random.randint(1, 30))
            for _ in range(random.randint(3, 10))
        ]
        entertainer = Entertainer(
            id=f"ENT-{i:03d}",
            name=f"Entertainer {i}",
            type=entertainer_type,
            hourly_rate=random.uniform(50, 500),
            availability=available_dates,
            genres=random.sample(genres, random.randint(1, 3)),
            rating=random.uniform(3.0, 5.0)
        )
        entertainers.append(entertainer)
    return entertainers

# Example usage
if __name__ == "__main__":
    # Sample data setup
    entertainers = generate_sample_entertainers()
    scheduler = Scheduler(entertainers)
    
    # Create a sample event
    event = Event(
        id="EVT-001",
        name="Corporate Gala Dinner",
        type=EventType.CORPORATE,
        date=datetime.date.today() + datetime.timedelta(days=7),
        duration_hours=4,
        budget=2000,
        preferred_entertainer_types=[EntertainerType.BAND, EntertainerType.SINGER, EntertainerType.DJ],
        preferred_genres=["Jazz", "Pop"]
    )
    
    # Find available entertainers
    available = scheduler.find_available_entertainers(event)
    print(f"Found {len(available)} available entertainers for the event")
    
    # Get recommendations
    recommendations = scheduler.recommend_entertainers(event)
    print("\nTop recommendations:")
    for i, ent in enumerate(recommendations, 1):
        print(f"{i}. {ent.name} ({ent.type.value}) - ${ent.hourly_rate}/hr - Rating: {ent.rating:.1f}")
    
    # Schedule an entertainer
    if recommendations:
        scheduled = scheduler.schedule_entertainer(event, recommendations[0].id)
        if scheduled:
            print(f"\nSuccessfully scheduled {scheduled.name} for the event!")
```
