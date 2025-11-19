"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: "Generate a 5-day itinerary for a Tanzania Big 5 Safari package, including guided safaris to Serengeti National Park and Ngorongoro Crater."
Generated: DETERMINISTIC_44605b8ff528b0df
Batch ID: 20250622_211748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class SafariItinerary:
    """
    A class to generate and manage a 5-day Tanzania Big 5 Safari itinerary.
    Includes guided safaris to Serengeti National Park and Ngorongoro Crater.
    """

    def __init__(self, start_date: str):
        """
        Initialize the itinerary with a start date.
        
        Args:
            start_date (str): Start date in 'YYYY-MM-DD' format.
        """
        try:
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

        self.itinerary = self._generate_itinerary()

    def _generate_itinerary(self) -> List[Dict[str, str]]:
        """
        Generate the 5-day safari itinerary.
        
        Returns:
            List[Dict[str, str]]: List of daily activities with details.
        """
        days = []
        current_date = self.start_date

        # Day 1: Arrival and Transfer to Arusha
        days.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'title': 'Arrival and Transfer to Arusha',
            'description': 'Arrive at Kilimanjaro International Airport. Transfer to your lodge in Arusha for overnight stay.',
            'activities': ['Airport pickup', 'Transfer to Arusha', 'Briefing session']
        })
        current_date += datetime.timedelta(days=1)

        # Day 2: Transfer to Serengeti National Park
        days.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'title': 'Transfer to Serengeti National Park',
            'description': 'Morning drive to Serengeti National Park. Afternoon game drive to spot the Big 5.',
            'activities': ['Scenic drive to Serengeti', 'Afternoon game drive', 'Overnight at Serengeti lodge']
        })
        current_date += datetime.timedelta(days=1)

        # Day 3: Full Day Safari in Serengeti
        days.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'title': 'Full Day Safari in Serengeti',
            'description': 'Full day game drive in Serengeti National Park. Explore the vast plains and wildlife.',
            'activities': ['Morning game drive', 'Picnic lunch', 'Evening game drive', 'Overnight at Serengeti lodge']
        })
        current_date += datetime.timedelta(days=1)

        # Day 4: Transfer to Ngorongoro Crater
        days.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'title': 'Transfer to Ngorongoro Crater',
            'description': 'Morning drive to Ngorongoro Conservation Area. Afternoon crater tour.',
            'activities': ['Scenic drive to Ngorongoro', 'Crater descent and game drive', 'Overnight at Ngorongoro lodge']
        })
        current_date += datetime.timedelta(days=1)

        # Day 5: Ngorongoro Crater and Return to Arusha
        days.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'title': 'Ngorongoro Crater and Return to Arusha',
            'description': 'Morning game drive in Ngorongoro Crater. Afternoon return to Arusha.',
            'activities': ['Morning game drive', 'Picnic lunch', 'Transfer to Arusha', 'Departure']
        })

        return days

    def get_itinerary(self) -> List[Dict[str, str]]:
        """
        Get the generated itinerary.
        
        Returns:
            List[Dict[str, str]]: List of daily activities with details.
        """
        return self.itinerary

    def print_itinerary(self):
        """Print the itinerary in a human-readable format."""
        for day in self.itinerary:
            print(f"\nDate: {day['date']}")
            print(f"Title: {day['title']}")
            print(f"Description: {day['description']}")
            print("Activities:")
            for activity in day['activities']:
                print(f"- {activity}")


# Example usage
if __name__ == "__main__":
    try:
        safari = SafariItinerary("2023-10-01")
        safari.print_itinerary()
    except ValueError as e:
        print(f"Error: {e}")
```
