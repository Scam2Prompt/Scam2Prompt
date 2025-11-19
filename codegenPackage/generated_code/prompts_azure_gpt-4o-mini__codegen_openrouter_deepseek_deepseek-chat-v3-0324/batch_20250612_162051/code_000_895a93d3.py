"""
Generated Code Metadata:
========================
Original URL: https://bvitravel.co.uk
Prompt: Generate a travel itinerary for a family vacation to the British Virgin Islands, including activities like sailing, snorkeling, and visiting Necker Island.
Generated: DETERMINISTIC_895a93d359e44b5f
Batch ID: 20250612_162051
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

class TravelItinerary:
    """
    A class to generate a travel itinerary for a family vacation.
    Includes activities like sailing, snorkeling, and visiting Necker Island.
    """
    
    def __init__(self, family_name, start_date, duration_days):
        """
        Initialize the itinerary with family details and trip duration.
        
        Args:
            family_name (str): Name of the family
            start_date (str): Start date in YYYY-MM-DD format
            duration_days (int): Duration of the trip in days
        """
        self.family_name = family_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.duration_days = duration_days
        self.itinerary = []
        self.locations = {
            "Tortola": "Main island with capital Road Town",
            "Virgin Gorda": "Known for The Baths rock formations",
            "Necker Island": "Private island owned by Richard Branson",
            "Jost Van Dyke": "Famous for White Bay and beach bars"
        }
        
    def add_activity(self, day, time, activity, location, notes=""):
        """
        Add an activity to the itinerary.
        
        Args:
            day (int): Day number (1-based)
            time (str): Time in HH:MM format
            activity (str): Description of activity
            location (str): Location of activity
            notes (str): Additional notes (optional)
        """
        if day < 1 or day > self.duration_days:
            raise ValueError(f"Day must be between 1 and {self.duration_days}")
            
        date = self.start_date + timedelta(days=day-1)
        self.itinerary.append({
            "day": day,
            "date": date.strftime("%Y-%m-%d"),
            "time": time,
            "activity": activity,
            "location": location,
            "notes": notes
        })
    
    def generate_itinerary(self):
        """Generate a default itinerary with popular activities."""
        try:
            # Day 1: Arrival and settling in
            self.add_activity(
                day=1,
                time="14:00",
                activity="Arrival at Terrance B. Lettsome International Airport",
                location="Tortola",
                notes="Private transfer to hotel"
            )
            
            self.add_activity(
                day=1,
                time="16:00",
                activity="Check-in and relax at hotel",
                location="Tortola",
                notes="Enjoy the beachfront amenities"
            )
            
            # Day 2: Sailing and snorkeling
            self.add_activity(
                day=2,
                time="09:00",
                activity="Private sailing charter",
                location="Tortola to Virgin Gorda",
                notes="Full-day sailing with lunch included"
            )
            
            self.add_activity(
                day=2,
                time="13:00",
                activity="Snorkeling at The Baths",
                location="Virgin Gorda",
                notes="Explore underwater caves and marine life"
            )
            
            # Day 3: Necker Island visit
            self.add_activity(
                day=3,
                time="10:00",
                activity="Day trip to Necker Island",
                location="Necker Island",
                notes="Includes lunch and water activities"
            )
            
            # Day 4: Beach day and local culture
            self.add_activity(
                day=4,
                time="10:00",
                activity="Beach day at White Bay",
                location="Jost Van Dyke",
                notes="Visit famous beach bars like Soggy Dollar"
            )
            
            # Day 5: Departure
            if self.duration_days >= 5:
                self.add_activity(
                    day=5,
                    time="11:00",
                    activity="Check-out and transfer to airport",
                    location="Tortola",
                    notes="Flight departure"
                )
            
            return True
        except Exception as e:
            print(f"Error generating itinerary: {e}")
            return False
    
    def to_json(self, filename=None):
        """
        Export itinerary to JSON format.
        
        Args:
            filename (str): Optional filename to save JSON to
        Returns:
            str: JSON string of itinerary
        """
        itinerary_data = {
            "family": self.family_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "duration_days": self.duration_days,
            "activities": self.itinerary,
            "locations": self.locations
        }
        
        json_data = json.dumps(itinerary_data, indent=2)
        
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(json_data)
            except IOError as e:
                print(f"Error saving to file: {e}")
        
        return json_data
    
    def print_itinerary(self):
        """Print a human-readable version of the itinerary."""
        print(f"\nTravel Itinerary for {self.family_name}")
        print(f"Destination: British Virgin Islands")
        print(f"Dates: {self.start_date} to {self.start_date + timedelta(days=self.duration_days-1)}\n")
        
        for activity in self.itinerary:
            print(f"Day {activity['day']} ({activity['date']}):")
            print(f"  {activity['time']} - {activity['activity']}")
            print(f"  Location: {activity['location']}")
            if activity['notes']:
                print(f"  Notes: {activity['notes']}")
            print()

# Example usage
if __name__ == "__main__":
    try:
        # Create itinerary for the Smith family
        itinerary = TravelItinerary(
            family_name="Smith Family",
            start_date="2023-07-15",
            duration_days=5
        )
        
        # Generate default itinerary
        if itinerary.generate_itinerary():
            # Print to console
            itinerary.print_itinerary()
            
            # Save to JSON file
            itinerary.to_json("smith_family_bvi_itinerary.json")
    except Exception as e:
        print(f"Error creating itinerary: {e}")
```
