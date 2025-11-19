"""
Generated Code Metadata:
========================
Original URL: https://ittastours.com
Prompt: "Generate a Python script to create a travel itinerary for a 7-day trip to Egypt, including visits to Cairo, Luxor, and Hurghada."
Generated: DETERMINISTIC_11839a8d5bb8a2c6
Batch ID: 20250622_210443
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
    A class to generate a travel itinerary for a 7-day trip to Egypt.
    Includes visits to Cairo, Luxor, and Hurghada with activities and transportation details.
    """
    
    def __init__(self, start_date):
        """
        Initialize the itinerary with start date and empty itinerary.
        
        Args:
            start_date (str): Start date in 'YYYY-MM-DD' format
        """
        try:
            self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e
            
        self.itinerary = []
        self.locations = {
            'Cairo': {
                'activities': [
                    'Visit the Pyramids of Giza',
                    'Explore the Egyptian Museum',
                    'Walk through Khan el-Khalili bazaar'
                ],
                'transport': 'Private car with guide'
            },
            'Luxor': {
                'activities': [
                    'Tour Karnak Temple',
                    'Visit Valley of the Kings',
                    'See Luxor Temple at night'
                ],
                'transport': 'Domestic flight from Cairo'
            },
            'Hurghada': {
                'activities': [
                    'Red Sea snorkeling trip',
                    'Desert safari excursion',
                    'Relax at resort beaches'
                ],
                'transport': 'Private car transfer from Luxor'
            }
        }
    
    def generate_itinerary(self):
        """Generate the 7-day itinerary with activities and transportation."""
        current_date = self.start_date
        
        # Day 1-3: Cairo
        for day in range(1, 4):
            self._add_day(day, current_date, 'Cairo')
            current_date += timedelta(days=1)
        
        # Day 4-5: Luxor
        for day in range(4, 6):
            self._add_day(day, current_date, 'Luxor')
            current_date += timedelta(days=1)
        
        # Day 6-7: Hurghada
        for day in range(6, 8):
            self._add_day(day, current_date, 'Hurghada')
            current_date += timedelta(days=1)
    
    def _add_day(self, day_num, date, location):
        """Add a day to the itinerary with location details."""
        day_info = {
            'day': day_num,
            'date': date.strftime('%Y-%m-%d'),
            'location': location,
            'activities': self.locations[location]['activities'],
            'transportation': self.locations[location]['transport']
        }
        self.itinerary.append(day_info)
    
    def save_to_json(self, filename):
        """Save the itinerary to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.itinerary, f, indent=4)
        except IOError as e:
            raise IOError(f"Error saving file: {e}") from e
    
    def print_itinerary(self):
        """Print the itinerary in a readable format."""
        for day in self.itinerary:
            print(f"\nDay {day['day']} ({day['date']}): {day['location']}")
            print("Activities:")
            for activity in day['activities']:
                print(f"- {activity}")
            print(f"Transportation: {day['transportation']}")


def main():
    """Main function to create and display the itinerary."""
    try:
        start_date = input("Enter trip start date (YYYY-MM-DD): ")
        itinerary = TravelItinerary(start_date)
        itinerary.generate_itinerary()
        
        print("\n=== 7-Day Egypt Travel Itinerary ===")
        itinerary.print_itinerary()
        
        save_file = input("\nEnter filename to save itinerary (or press Enter to skip): ")
        if save_file:
            itinerary.save_to_json(save_file)
            print(f"Itinerary saved to {save_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
