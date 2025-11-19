"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Generate a custom itinerary for a 9-day luxury safari in Amboseli and Masai Mara, incorporating exclusive accommodations and top-notch safari guides.
Generated: DETERMINISTIC_9a60453339a76e2d
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that generates a custom 9-day luxury safari itinerary for Amboseli and Masai Mara:

```python
import json
from datetime import datetime, timedelta

class LuxurySafariItinerary:
    """
    A class to generate a 9-day luxury safari itinerary for Amboseli and Masai Mara.
    Includes exclusive accommodations and top-tier safari experiences.
    """
    
    def __init__(self, start_date):
        """
        Initialize the itinerary with start date and default properties.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.itinerary = {
            "title": "9-Day Luxury Safari: Amboseli & Masai Mara",
            "description": "An exclusive luxury safari featuring premium accommodations and expert guides",
            "destinations": ["Amboseli National Park", "Masai Mara National Reserve"],
            "days": []
        }
        
        # Luxury accommodations
        self.accommodations = {
            "Amboseli": {
                "name": "Tortilis Camp Amboseli",
                "type": "Private Luxury Camp",
                "features": ["Elephant views of Kilimanjaro", "Private plunge pools", "Gourmet dining"]
            },
            "Masai Mara": {
                "name": "Angama Mara",
                "type": "Luxury Safari Lodge",
                "features": ["Stunning Mara River views", "Private game drives", "Helicopter transfers available"]
            }
        }
        
        # Safari activities
        self.activities = {
            "Amboseli": [
                "Morning game drive with elephant specialist guide",
                "Bush breakfast with Kilimanjaro views",
                "Sunset photography safari",
                "Cultural visit to Maasai village",
                "Private sundowner experience"
            ],
            "Masai Mara": [
                "Full-day game drive with picnic lunch",
                "Hot air balloon safari with champagne breakfast",
                "Big Five tracking with expert Maasai guide",
                "Riverside bush dinner",
                "Photographic safari with professional equipment"
            ]
        }
    
    def generate_itinerary(self):
        """Generate the 9-day luxury safari itinerary."""
        
        # Day 1: Arrival in Nairobi
        self._add_day(
            day_number=1,
            location="Nairobi",
            title="Arrival and Briefing",
            description="Arrive at Jomo Kenyatta International Airport. Private transfer to luxury boutique hotel for overnight stay and safari briefing.",
            accommodation="The Hemingways Nairobi",
            activities=["Airport transfer", "Safari briefing with head guide", "Welcome dinner"]
        )
        
        # Day 2-4: Amboseli
        for i in range(2, 5):
            day_activities = self._get_daily_activities("Amboseli")
            self._add_day(
                day_number=i,
                location="Amboseli National Park",
                title=f"Amboseli Safari Day {i-1}",
                description=f"Experience the majestic elephants of Amboseli with stunning views of Mount Kilimanjaro. {day_activities['highlight']}",
                accommodation=self.accommodations["Amboseli"]["name"],
                activities=day_activities["list"]
            )
        
        # Day 5: Transfer to Masai Mara
        self._add_day(
            day_number=5,
            location="Enroute",
            title="Scenic Flight to Masai Mara",
            description="Private charter flight from Amboseli to Masai Mara with spectacular aerial views of the Great Rift Valley.",
            accommodation=self.accommodations["Masai Mara"]["name"],
            activities=["Scenic flight transfer", "Afternoon game drive upon arrival", "Bush sundowner"]
        )
        
        # Day 6-8: Masai Mara
        for i in range(6, 9):
            day_activities = self._get_daily_activities("Masai Mara")
            self._add_day(
                day_number=i,
                location="Masai Mara National Reserve",
                title=f"Masai Mara Safari Day {i-5}",
                description=f"Explore the world-famous Masai Mara with expert guides. {day_activities['highlight']}",
                accommodation=self.accommodations["Masai Mara"]["name"],
                activities=day_activities["list"]
            )
        
        # Day 9: Departure
        self._add_day(
            day_number=9,
            location="Nairobi",
            title="Departure",
            description="Morning scenic flight back to Nairobi with day room available before international departure.",
            accommodation="Day room at The Emakoko",
            activities=["Scenic flight to Nairobi", "Farewell breakfast", "Airport transfer"]
        )
    
    def _add_day(self, day_number, location, title, description, accommodation, activities):
        """Add a day to the itinerary."""
        date = (self.start_date + timedelta(days=day_number-1)).strftime("%Y-%m-%d")
        
        day = {
            "day": day_number,
            "date": date,
            "location": location,
            "title": title,
            "description": description,
            "accommodation": accommodation,
            "activities": activities
        }
        
        self.itinerary["days"].append(day)
    
    def _get_daily_activities(self, location):
        """Get a selection of activities for a day with one highlight."""
        import random
        available_activities = self.activities[location].copy()
        highlight = random.choice(available_activities)
        available_activities.remove(highlight)
        
        # Select 2-3 additional activities
        daily_activities = random.sample(available_activities, min(3, len(available_activities)))
        daily_activities.insert(0, highlight)  # Highlight as first activity
        
        return {
            "highlight": f"Today's highlight: {highlight}",
            "list": daily_activities
        }
    
    def save_to_json(self, filename):
        """Save the itinerary to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.itinerary, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving itinerary: {e}")
            return False
    
    def print_itinerary(self):
        """Print the itinerary in a human-readable format."""
        print(f"\n{'='*50}")
        print(f"{self.itinerary['title'].upper():^50}")
        print(f"{'='*50}\n")
        print(self.itinerary['description'])
        print(f"\nDestinations: {', '.join(self.itinerary['destinations'])}\n")
        
        for day in self.itinerary['days']:
            print(f"\nDay {day['day']}: {day['date']} - {day['title']}")
            print(f"Location: {day['location']}")
            print(f"\n{day['description']}")
            print(f"\nAccommodation: {day['accommodation']}")
            print("\nActivities:")
            for i, activity in enumerate(day['activities'], 1):
                print(f"  {i}. {activity}")
            print("-"*50)


# Example usage
if __name__ == "__main__":
    try:
        safari = LuxurySafariItinerary("2024-06-01")
        safari.generate_itinerary()
        safari.print_itinerary()
        safari.save_to_json("9_day_luxury_safari.json")
    except ValueError as e:
        print(f"Invalid date format. Please use YYYY-MM-DD format. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
