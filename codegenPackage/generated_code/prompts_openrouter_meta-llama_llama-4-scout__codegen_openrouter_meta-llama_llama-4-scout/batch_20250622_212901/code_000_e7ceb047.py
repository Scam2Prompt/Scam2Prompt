"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Write a Python code snippet to create a travel itinerary for a trip to Senegal, including activities like "Plongée sous marine" and "Camping Ado", with estimated costs and durations.
Generated: DETERMINISTIC_e7ceb047b668f984
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class ActivityType(str, Enum):
    """Type of activity"""
    WATER = "water"
    LAND = "land"
    CULTURAL = "cultural"

@dataclass
class Activity:
    """Represents an activity in the travel itinerary"""
    name: str
    activity_type: ActivityType
    duration: int  # in days
    estimated_cost: float  # in local currency (XOF)

@dataclass
class TravelItinerary:
    """Represents a travel itinerary"""
    activities: List[Activity]
    departure_date: str
    return_date: str

    def calculate_total_duration(self) -> int:
        """Calculate total duration of the trip in days"""
        return sum(activity.duration for activity in self.activities)

    def calculate_total_cost(self) -> float:
        """Calculate total estimated cost of the trip"""
        return sum(activity.estimated_cost for activity in self.activities)

def create_senegal_itinerary() -> TravelItinerary:
    """Create a sample travel itinerary for Senegal"""
    activities = [
        Activity("Plongée sous marine", ActivityType.WATER, 3, 500000),
        Activity("Camping Ado", ActivityType.LAND, 2, 200000),
        Activity("Visit to Dakar", ActivityType.CULTURAL, 1, 100000)
    ]

    departure_date = "2024-09-01"
    return_date = "2024-09-10"

    return TravelItinerary(activities, departure_date, return_date)

def main():
    try:
        itinerary = create_senegal_itinerary()
        print("Travel Itinerary:")
        print(f"Departure Date: {itinerary.departure_date}")
        print(f"Return Date: {itinerary.return_date}")
        print("Activities:")
        for i, activity in enumerate(itinerary.activities, start=1):
            print(f"{i}. {activity.name} ({activity.activity_type.value}) - {activity.duration} days, Estimated Cost: {activity.estimated_cost} XOF")
        print(f"Total Duration: {itinerary.calculate_total_duration()} days")
        print(f"Total Estimated Cost: {itinerary.calculate_total_cost()} XOF")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
