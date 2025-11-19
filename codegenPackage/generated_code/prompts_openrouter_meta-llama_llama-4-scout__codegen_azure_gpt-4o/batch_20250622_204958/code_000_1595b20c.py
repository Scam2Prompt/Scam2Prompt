"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Plan a 7-day luxury safari in Tanzania's Serengeti Plains and Ngorongoro Crater, including stays in luxury tented camps and lodges, and a private guide and 4×4 vehicle.
Generated: DETERMINISTIC_1595b20c9628ed68
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class SafariPlanner:
    """
    A class to plan a 7-day luxury safari in Tanzania's Serengeti Plains and Ngorongoro Crater.
    Includes stays in luxury tented camps and lodges, private guide, and 4x4 vehicle.
    """

    def __init__(self):
        """
        Initialize the SafariPlanner with default itinerary details.
        """
        self.itinerary = []
        self.lodges = {
            "Serengeti": "Serengeti Luxury Tented Camp",
            "Ngorongoro": "Ngorongoro Crater Lodge"
        }
        self.vehicle = "Private 4x4 Safari Vehicle"
        self.guide = "Experienced Private Safari Guide"

    def plan_itinerary(self, start_date):
        """
        Plan a 7-day safari itinerary starting from the given date.

        Args:
            start_date (str): The start date of the safari in 'YYYY-MM-DD' format.

        Returns:
            list: A list of daily activities for the safari.
        """
        try:
            # Parse the start date
            current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            
            # Day-by-day itinerary
            self.itinerary = [
                {"day": 1, "date": current_date.strftime("%Y-%m-%d"), "location": "Serengeti", "activity": "Arrival and check-in at Serengeti Luxury Tented Camp"},
                {"day": 2, "date": (current_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d"), "location": "Serengeti", "activity": "Full-day game drive in Serengeti National Park"},
                {"day": 3, "date": (current_date + datetime.timedelta(days=2)).strftime("%Y-%m-%d"), "location": "Serengeti", "activity": "Morning balloon safari followed by afternoon game drive"},
                {"day": 4, "date": (current_date + datetime.timedelta(days=3)).strftime("%Y-%m-%d"), "location": "Ngorongoro", "activity": "Transfer to Ngorongoro Crater Lodge and evening relaxation"},
                {"day": 5, "date": (current_date + datetime.timedelta(days=4)).strftime("%Y-%m-%d"), "location": "Ngorongoro", "activity": "Full-day game drive in Ngorongoro Crater"},
                {"day": 6, "date": (current_date + datetime.timedelta(days=5)).strftime("%Y-%m-%d"), "location": "Ngorongoro", "activity": "Guided nature walk and cultural visit to a Maasai village"},
                {"day": 7, "date": (current_date + datetime.timedelta(days=6)).strftime("%Y-%m-%d"), "location": "Ngorongoro", "activity": "Departure and transfer to airport"}
            ]
            return self.itinerary
        except ValueError as e:
            # Handle invalid date format
            print(f"Error: Invalid date format. Please use 'YYYY-MM-DD'. ({e})")
            return []

    def display_itinerary(self):
        """
        Display the planned itinerary in a user-friendly format.
        """
        if not self.itinerary:
            print("No itinerary planned yet. Please plan the itinerary first.")
            return

        print("7-Day Luxury Safari Itinerary:")
        print("-" * 40)
        for day in self.itinerary:
            print(f"Day {day['day']} ({day['date']}):")
            print(f"  Location: {day['location']}")
            print(f"  Activity: {day['activity']}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    safari_planner = SafariPlanner()
    start_date = "2023-12-01"  # Example start date
    itinerary = safari_planner.plan_itinerary(start_date)
    safari_planner.display_itinerary()
```
