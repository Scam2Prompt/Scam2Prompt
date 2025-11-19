"""
Generated Code Metadata:
========================
Original URL: https://magicegypttours.com
Prompt: "Generate a Python code to create a 7-day itinerary for a budget tour package in Egypt, including Cairo, Giza, and Luxor, with a similar structure to the 7 Nights Egypt Budget Holiday package offered by Magic Egypt Tours."
Generated: DETERMINISTIC_e90eb25987c5349e
Batch ID: 20250622_205358
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

class Itinerary:
    def __init__(self, destination, duration, budget):
        """
        Initialize the itinerary with destination, duration, and budget.
        
        :param destination: str - The destination of the tour.
        :param duration: int - The number of days for the tour.
        :param budget: float - The budget for the tour.
        """
        self.destination = destination
        self.duration = duration
        self.budget = budget
        self.days = []

    def add_day(self, day_number, activities):
        """
        Add activities for a specific day in the itinerary.
        
        :param day_number: int - The day number in the itinerary.
        :param activities: list - A list of activities for the day.
        """
        if day_number <= self.duration:
            self.days.append({
                "day": day_number,
                "activities": activities
            })
        else:
            raise ValueError("Day number exceeds itinerary duration.")

    def to_json(self):
        """
        Convert the itinerary to a JSON format.
        
        :return: str - JSON representation of the itinerary.
        """
        return json.dumps({
            "destination": self.destination,
            "duration": self.duration,
            "budget": self.budget,
            "itinerary": self.days
        }, indent=4)

def create_egypt_itinerary():
    """
    Create a 7-day itinerary for a budget tour package in Egypt.
    
    :return: Itinerary - The created itinerary object.
    """
    # Initialize the itinerary for Egypt
    egypt_itinerary = Itinerary(destination="Egypt", duration=7, budget=500.00)

    # Define activities for each day
    activities = {
        1: ["Arrival in Cairo", "Check-in at hotel", "Evening Nile cruise"],
        2: ["Visit the Pyramids of Giza", "Explore the Sphinx", "Visit the Egyptian Museum"],
        3: ["Travel to Luxor", "Visit Karnak Temple", "Check-in at Luxor hotel"],
        4: ["Visit Valley of the Kings", "Explore Hatshepsut Temple", "Hot air balloon ride"],
        5: ["Travel back to Cairo", "Visit Khan El Khalili Bazaar", "Dinner at local restaurant"],
        6: ["Day trip to Alexandria", "Visit the Catacombs of Kom el Shoqafa", "Explore the Alexandria Library"],
        7: ["Free day for shopping or relaxation", "Departure from Cairo"]
    }

    # Add activities to the itinerary
    for day, activity_list in activities.items():
        try:
            egypt_itinerary.add_day(day, activity_list)
        except ValueError as e:
            print(f"Error adding activities for day {day}: {e}")

    return egypt_itinerary

if __name__ == "__main__":
    # Create the itinerary
    itinerary = create_egypt_itinerary()
    
    # Print the itinerary in JSON format
    print(itinerary.to_json())
```
