"""
Generated Code Metadata:
========================
Original URL: https://bvitravel.co.uk
Prompt: "Generate a travel itinerary for a family vacation in the British Virgin Islands, including activities like sailing and visiting Necker Island."
Generated: DETERMINISTIC_d75b48cea6ef3939
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Activity:
    """Represents a travel activity with details."""
    
    def __init__(self, name: str, description: str, duration_hours: float, location: str, cost: Optional[float] = None):
        """
        Initialize an activity.
        
        Args:
            name: Name of the activity
            description: Description of what the activity entails
            duration_hours: How long the activity lasts in hours
            location: Where the activity takes place
            cost: Optional cost of the activity
        """
        self.name = name
        self.description = description
        self.duration_hours = duration_hours
        self.location = location
        self.cost = cost
    
    def __str__(self) -> str:
        """String representation of the activity."""
        cost_str = f"Cost: ${self.cost:.2f}" if self.cost else "Cost: Not specified"
        return (f"Activity: {self.name}\n"
                f"Description: {self.description}\n"
                f"Duration: {self.duration_hours} hours\n"
                f"Location: {self.location}\n"
                f"{cost_str}\n")

class DayItinerary:
    """Represents a single day's itinerary."""
    
    def __init__(self, date: datetime.date):
        """
        Initialize a day's itinerary.
        
        Args:
            date: The date for this itinerary
        """
        self.date = date
        self.activities: List[Activity] = []
    
    def add_activity(self, activity: Activity) -> None:
        """Add an activity to the day's itinerary."""
        self.activities.append(activity)
    
    def __str__(self) -> str:
        """String representation of the day's itinerary."""
        activities_str = "\n".join([str(activity) for activity in self.activities])
        return f"Date: {self.date.strftime('%A, %B %d, %Y')}\n{activities_str}"

class TravelItinerary:
    """Represents a complete travel itinerary."""
    
    def __init__(self, destination: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize a travel itinerary.
        
        Args:
            destination: The travel destination
            start_date: Start date of the trip
            end_date: End date of the trip
        """
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.days: List[DayItinerary] = []
        
        if start_date > end_date:
            raise ValueError("Start date must be before end date")
        
        # Initialize day itineraries for each day of the trip
        current_date = start_date
        while current_date <= end_date:
            self.days.append(DayItinerary(current_date))
            current_date += datetime.timedelta(days=1)
    
    def add_activity_to_day(self, day_index: int, activity: Activity) -> None:
        """
        Add an activity to a specific day in the itinerary.
        
        Args:
            day_index: Index of the day (0-based)
            activity: Activity to add
        """
        if day_index < 0 or day_index >= len(self.days):
            raise ValueError("Invalid day index")
        self.days[day_index].add_activity(activity)
    
    def __str__(self) -> str:
        """String representation of the complete itinerary."""
        header = f"Travel Itinerary for {self.destination}\n"
        header += f"Dates: {self.start_date.strftime('%m/%d/%Y')} - {self.end_date.strftime('%m/%d/%Y')}\n\n"
        days_str = "\n".join([str(day) for day in self.days])
        return header + days_str

def create_bvi_itinerary() -> TravelItinerary:
    """Create a sample itinerary for a family vacation in the British Virgin Islands."""
    # Trip dates (example: 1 week starting next month)
    today = datetime.date.today()
    start_date = today + datetime.timedelta(days=30)
    end_date = start_date + datetime.timedelta(days=6)
    
    itinerary = TravelItinerary(
        destination="British Virgin Islands",
        start_date=start_date,
        end_date=end_date
    )
    
    # Define activities
    activities = [
        # Day 0: Arrival
        Activity(
            name="Arrival at Tortola",
            description="Check into resort and relax after travel",
            duration_hours=4,
            location="Tortola",
            cost=0
        ),
        
        # Day 1: Sailing
        Activity(
            name="Sailing Excursion",
            description="Full-day sailing trip around the islands with snorkeling stops",
            duration_hours=8,
            location="Various Islands",
            cost=1200
        ),
        
        # Day 2: Beach Day
        Activity(
            name="Beach Day at White Bay",
            description="Relaxing day at one of the most beautiful beaches in Jost Van Dyke",
            duration_hours=6,
            location="Jost Van Dyke",
            cost=0
        ),
        
        # Day 3: Necker Island Visit
        Activity(
            name="Necker Island Day Trip",
            description="Exclusive visit to Richard Branson's private island with lunch included",
            duration_hours=6,
            location="Necker Island",
            cost=1500
        ),
        
        # Day 4: Scuba Diving
        Activity(
            name="Scuba Diving at The Indians",
            description="Guided scuba diving at one of BVI's best dive sites",
            duration_hours=4,
            location="The Indians",
            cost=300
        ),
        
        # Day 5: Island Hopping
        Activity(
            name="Island Hopping Tour",
            description="Visit multiple islands including Virgin Gorda and The Baths",
            duration_hours=7,
            location="Various Islands",
            cost=800
        ),
        
        # Day 6: Departure
        Activity(
            name="Departure",
            description="Transfer to airport and return flight",
            duration_hours=4,
            location="Tortola",
            cost=0
        )
    ]
    
    # Add activities to itinerary
    for i, activity in enumerate(activities):
        itinerary.add_activity_to_day(i, activity)
    
    return itinerary

if __name__ == "__main__":
    try:
        itinerary = create_bvi_itinerary()
        print(itinerary)
    except ValueError as e:
        print(f"Error creating itinerary: {e}")
```
