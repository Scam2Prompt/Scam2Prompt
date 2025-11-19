"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Create a tailored itinerary for a 6-day horse riding tour in Chile's Andes Mountain range, incorporating the Rari Discovery Ride and Moonshine Ride experiences.
Generated: DETERMINISTIC_09d5466482293fe8
Batch ID: 20250622_210655
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

class HorseRidingTour:
    """
    A class to generate a tailored itinerary for a 6-day horse riding tour in Chile's Andes.
    Includes Rari Discovery Ride and Moonshine Ride experiences.
    """
    
    def __init__(self, start_date):
        """
        Initialize the tour with start date and predefined activities.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.itinerary = []
        self._initialize_activities()
        
    def _initialize_activities(self):
        """Initialize the predefined activities for the tour."""
        self.activities = [
            {
                "day": 1,
                "title": "Arrival and Orientation",
                "description": "Arrive at the ranch, meet your guides and horses. Safety briefing and basic riding instruction.",
                "meals": ["Dinner"],
                "accommodation": "Mountain Lodge"
            },
            {
                "day": 2,
                "title": "Andes Foothills Exploration",
                "description": "Full-day ride through scenic foothills with stunning mountain views. Picnic lunch en route.",
                "meals": ["Breakfast", "Lunch", "Dinner"],
                "accommodation": "Mountain Lodge"
            },
            {
                "day": 3,
                "title": "Rari Discovery Ride",
                "description": "Special full-day ride to discover the Rari weaving tradition. Visit local artisans and learn about this unique craft.",
                "meals": ["Breakfast", "Lunch", "Dinner"],
                "accommodation": "Mountain Lodge"
            },
            {
                "day": 4,
                "title": "High Mountain Pass",
                "description": "Challenging ride to a high mountain pass with breathtaking views. Return via different route.",
                "meals": ["Breakfast", "Lunch", "Dinner"],
                "accommodation": "Mountain Lodge"
            },
            {
                "day": 5,
                "title": "Moonshine Ride",
                "description": "Evening ride under the stars with traditional Chilean moonshine tasting around the campfire.",
                "meals": ["Breakfast", "Lunch", "Dinner"],
                "accommodation": "Mountain Lodge"
            },
            {
                "day": 6,
                "title": "Farewell Ride and Departure",
                "description": "Short morning ride followed by farewell lunch and transfer to departure point.",
                "meals": ["Breakfast", "Lunch"],
                "accommodation": None
            }
        ]
    
    def generate_itinerary(self):
        """Generate the full itinerary with dates based on start date."""
        for activity in self.activities:
            current_date = self.start_date + timedelta(days=activity["day"]-1)
            day_itinerary = {
                "date": current_date.strftime("%Y-%m-%d"),
                "day_number": activity["day"],
                "title": activity["title"],
                "description": activity["description"],
                "meals": activity["meals"],
                "accommodation": activity["accommodation"]
            }
            self.itinerary.append(day_itinerary)
        return self.itinerary
    
    def save_itinerary(self, filename):
        """
        Save the itinerary to a JSON file.
        
        Args:
            filename (str): Name of the output file
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.itinerary, f, indent=4)
        except IOError as e:
            print(f"Error saving itinerary: {e}")
    
    def print_itinerary(self):
        """Print the itinerary in a human-readable format."""
        for day in self.itinerary:
            print(f"\nDay {day['day_number']} - {day['date']}")
            print(f"Title: {day['title']}")
            print(f"Description: {day['description']}")
            print(f"Meals: {', '.join(day['meals'])}")
            if day['accommodation']:
                print(f"Accommodation: {day['accommodation']}")

# Example usage
if __name__ == "__main__":
    try:
        tour = HorseRidingTour("2023-11-01")
        tour.generate_itinerary()
        tour.print_itinerary()
        tour.save_itinerary("andes_horse_riding_tour.json")
    except ValueError as e:
        print(f"Invalid date format. Please use YYYY-MM-DD: {e}")
```
