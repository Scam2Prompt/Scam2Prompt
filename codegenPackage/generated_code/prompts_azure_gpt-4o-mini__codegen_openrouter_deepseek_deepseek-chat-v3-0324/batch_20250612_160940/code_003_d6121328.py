"""
Generated Code Metadata:
========================
Original URL: https://apipoocoin-tk.blogspot.com
Prompt: Develop a travel itinerary for a family vacation at Toca do Caranguejo, including activities to enjoy at Praia do Patacho and nearby attractions.
Generated: DETERMINISTIC_d612132876cc39a4
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Travel Itinerary Generator for Toca do Caranguejo Family Vacation
Includes activities at Praia do Patacho and nearby attractions.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Activity:
    """Represents a single activity in the itinerary."""
    
    def __init__(self, name: str, description: str, duration: timedelta, 
                 location: str, cost: Optional[float] = None):
        """
        Initialize an activity.
        
        Args:
            name: Name of the activity
            description: Description of what the activity entails
            duration: How long the activity takes
            location: Where the activity takes place
            cost: Optional cost per person (in local currency)
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.location = location
        self.cost = cost
    
    def __str__(self) -> str:
        cost_str = f" (Cost: {self.cost} BRL)" if self.cost else ""
        return f"{self.name}{cost_str}: {self.description} at {self.location}"

class DayItinerary:
    """Represents a single day's itinerary."""
    
    def __init__(self, date: datetime):
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
    
    def get_formatted_date(self) -> str:
        """Return the date in a readable format."""
        return self.date.strftime("%A, %B %d, %Y")
    
    def __str__(self) -> str:
        activities_str = "\n".join(f"- {activity}" for activity in self.activities)
        return f"{self.get_formatted_date()}:\n{activities_str}"

class TravelItinerary:
    """Main itinerary class that manages the entire vacation plan."""
    
    def __init__(self, destination: str, start_date: datetime, duration_days: int):
        """
        Initialize the travel itinerary.
        
        Args:
            destination: Name of the destination
            start_date: Start date of the vacation
            duration_days: Number of days for the vacation
        """
        self.destination = destination
        self.start_date = start_date
        self.duration_days = duration_days
        self.days: List[DayItinerary] = []
        
        # Initialize day itineraries
        for day in range(duration_days):
            date = start_date + timedelta(days=day)
            self.days.append(DayItinerary(date))
    
    def add_activity_to_day(self, day_index: int, activity: Activity) -> None:
        """
        Add an activity to a specific day.
        
        Args:
            day_index: Index of the day (0-based)
            activity: Activity to add
            
        Raises:
            IndexError: If day_index is out of range
        """
        if day_index < 0 or day_index >= len(self.days):
            raise IndexError("Day index out of range")
        self.days[day_index].add_activity(activity)
    
    def __str__(self) -> str:
        days_str = "\n\n".join(str(day) for day in self.days)
        return f"Travel Itinerary for {self.destination}:\n\n{days_str}"

def create_toca_do_caranguejo_itinerary() -> TravelItinerary:
    """
    Create a sample itinerary for Toca do Caranguejo family vacation.
    
    Returns:
        A populated TravelItinerary object
    """
    # Vacation parameters
    destination = "Toca do Caranguejo, Praia do Patacho"
    start_date = datetime(2023, 7, 15)  # Example start date
    duration = 7  # 7-day vacation
    
    # Create itinerary
    itinerary = TravelItinerary(destination, start_date, duration)
    
    # Define activities
    activities = [
        # Day 1 - Arrival and beach relaxation
        Activity("Arrival at Toca do Caranguejo", 
                "Check-in and settle into accommodations", 
                timedelta(hours=2), 
                "Toca do Caranguejo"),
        Activity("Beach Relaxation", 
                "Enjoy the pristine sands of Praia do Patacho", 
                timedelta(hours=3), 
                "Praia do Patacho"),
        Activity("Sunset Watching", 
                "Watch the sunset with family", 
                timedelta(hours=1), 
                "Praia do Patacho"),
        
        # Day 2 - Beach activities
        Activity("Morning Swim", 
                "Enjoy the calm morning waters", 
                timedelta(hours=1), 
                "Praia do Patacho"),
        Activity("Stand-up Paddleboarding", 
                "Rent paddleboards and explore the coast", 
                timedelta(hours=2), 
                "Praia do Patacho", 
                50.0),
        Activity("Beach Picnic", 
                "Family picnic on the beach", 
                timedelta(hours=1.5), 
                "Praia do Patacho"),
        
        # Day 3 - Nature exploration
        Activity("Hike to Pontal do Patacho", 
                "Scenic hike to the viewpoint", 
                timedelta(hours=3), 
                "Pontal do Patacho"),
        Activity("Snorkeling", 
                "Explore marine life in the natural pools", 
                timedelta(hours=2), 
                "Praia do Patacho", 
                80.0),
        
        # Day 4 - Nearby attractions
        Activity("Visit Maragogi", 
                "Day trip to the famous beaches of Maragogi", 
                timedelta(hours=6), 
                "Maragogi", 
                120.0),
        
        # Day 5 - Relaxation and local culture
        Activity("Hammock Time", 
                "Relax in the beachfront hammocks", 
                timedelta(hours=2), 
                "Toca do Caranguejo"),
        Activity("Local Cuisine Experience", 
                "Try regional dishes at beachfront restaurants", 
                timedelta(hours=1.5), 
                "Praia do Patacho", 
                60.0),
        
        # Day 6 - Adventure day
        Activity("Buggy Tour", 
                "Explore nearby beaches and landscapes", 
                timedelta(hours=4), 
                "Porto de Pedras area", 
                150.0),
        Activity("Beach Bonfire", 
                "Evening bonfire with music and storytelling", 
                timedelta(hours=2), 
                "Praia do Patacho"),
        
        # Day 7 - Departure
        Activity("Final Beach Walk", 
                "Morning walk to say goodbye to the beach", 
                timedelta(hours=1), 
                "Praia do Patacho"),
        Activity("Check-out", 
                "Pack and prepare for departure", 
                timedelta(hours=1), 
                "Toca do Caranguejo")
    ]
    
    # Add activities to days
    day_assignments = [
        0, 0, 0,  # Day 1 activities
        1, 1, 1,  # Day 2 activities
        2, 2,     # Day 3 activities
        3,        # Day 4 activities
        4, 4,     # Day 5 activities
        5, 5,     # Day 6 activities
        6, 6      # Day 7 activities
    ]
    
    for day_idx, activity in zip(day_assignments, activities):
        itinerary.add_activity_to_day(day_idx, activity)
    
    return itinerary

if __name__ == "__main__":
    # Generate and print the itinerary
    itinerary = create_toca_do_caranguejo_itinerary()
    print(itinerary)
```
