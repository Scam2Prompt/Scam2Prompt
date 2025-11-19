"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Create a detailed plan for a 12-day bush and beach safari in Kenya, highlighting activities in Amboseli, Diani, and Tsavo.
Generated: DETERMINISTIC_5520107abfb829f1
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to generate a detailed 12-day Bush and Beach Safari itinerary in Kenya
# The program highlights activities in Amboseli, Diani, and Tsavo
# Written in Python, adheres to best practices, and includes error handling

from datetime import datetime, timedelta

class SafariPlanner:
    """
    SafariPlanner class generates a detailed 12-day itinerary for a bush and beach safari.
    """

    def __init__(self, start_date):
        """
        Initialize the SafariPlanner with a start_date.
        :param start_date: str, starting date of the safari in 'YYYY-MM-DD' format
        """
        try:
            self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

        self.itinerary = []

    def add_day_activity(self, day, location, activities):
        """
        Add an activity for a specific day in the itinerary.
        :param day: int, day number starting from 1
        :param location: str, location of the day's activities
        :param activities: list, list of activities planned for the day
        """
        if not isinstance(day, int) or day < 1 or day > 12:
            raise ValueError("Day must be an integer between 1 and 12.")
        
        if not isinstance(location, str) or not location.strip():
            raise ValueError("Location must be a non-empty string.")
        
        if not isinstance(activities, list) or not all(isinstance(activity, str) for activity in activities):
            raise ValueError("Activities must be a list of non-empty strings.")
        
        itinerary_day = {
            "Day": day,
            "Date": (self.start_date + timedelta(days=day - 1)).strftime('%Y-%m-%d'),
            "Location": location,
            "Activities": activities
        }
        self.itinerary.append(itinerary_day)

    def generate_itinerary(self):
        """
        Generate the safari itinerary.
        :return: list, complete safari itinerary
        """
        if not self.itinerary:
            raise ValueError("Itinerary is empty. Add activities before generating.")
        
        return self.itinerary

    def print_itinerary(self):
        """
        Print the generated itinerary in a readable format.
        """
        if not self.itinerary:
            print("No itinerary generated. Please add activities first.")
            return
        
        print("12-Day Bush and Beach Safari Itinerary")
        print("="*40)
        for day_plan in self.itinerary:
            print(f"Day {day_plan['Day']} - {day_plan['Date']}")
            print(f"  Location: {day_plan['Location']}")
            print("  Activities:")
            for activity in day_plan['Activities']:
                print(f"    - {activity}")
            print("-"*40)

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the safari planner with a start date
        safari = SafariPlanner("2024-01-01")
        
        # Add activities for each day
        safari.add_day_activity(1, "Amboseli National Park", [
            "Arrival and check-in",
            "Evening game drive",
            "Welcome dinner"
        ])
        safari.add_day_activity(2, "Amboseli National Park", [
            "Morning game drive",
            "Visit to Maasai village",
            "Relaxation at the lodge"
        ])
        safari.add_day_activity(3, "Amboseli National Park", [
            "Full day game drive",
            "Photography at Observation Hill",
            "Sunset dinner"
        ])
        safari.add_day_activity(4, "Tsavo West National Park", [
            "Transfer to Tsavo West",
            "Visit to Mzima Springs",
            "Evening game drive"
        ])
        safari.add_day_activity(5, "Tsavo East National Park", [
            "Morning transfer to Tsavo East",
            "Game drive featuring lions and elephants",
            "Dinner under the stars"
        ])
        safari.add_day_activity(6, "Tsavo East National Park", [
            "Morning game drive",
            "Relaxation at the lodge",
            "Bird watching activity"
        ])
        safari.add_day_activity(7, "Diani Beach", [
            "Transfer to Diani Beach",
            "Relaxation at the beachfront resort",
            "Dinner with coastal cuisine"
        ])
        safari.add_day_activity(8, "Diani Beach", [
            "Snorkeling and diving",
            "Beach relaxation",
            "Sunset dhow cruise"
        ])
        safari.add_day_activity(9, "Diani Beach", [
            "Visit to Colobus Conservation",
            "Shopping at local markets",
            "Evening beach bonfire"
        ])
        safari.add_day_activity(10, "Diani Beach", [
            "Deep sea fishing",
            "Relaxation and spa treatments",
            "Farewell dinner"
        ])
        safari.add_day_activity(11, "Diani Beach", [
            "Optional water sports",
            "Beach relaxation",
            "Leisure activities"
        ])
        safari.add_day_activity(12, "Diani Beach", [
            "Breakfast by the beach",
            "Check-out and departure"
        ])

        # Generate and print the complete itinerary
        safari.print_itinerary()

    except Exception as e:
        print(f"An error occurred: {e}")
```
