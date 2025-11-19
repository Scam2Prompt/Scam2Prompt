"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bvitravel.co.uk
Prompt: Generate a travel itinerary for a family vacation to the British Virgin Islands, including activities like sailing, snorkeling, and visiting Necker Island.
Generated: DETERMINISTIC_895a93d359e44b5f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ItineraryPlanner:
    """
    A class to generate a travel itinerary for a family vacation to the British Virgin Islands.
    Includes activities like sailing, snorkeling, and visiting Necker Island.
    """

    def __init__(self, start_date, end_date):
        """
        Initialize the itinerary planner with start and end dates.
        :param start_date: Vacation start date (YYYY-MM-DD)
        :param end_date: Vacation end date (YYYY-MM-DD)
        """
        try:
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            if self.start_date >= self.end_date:
                raise ValueError("End date must be after start date.")
        except ValueError as e:
            raise ValueError(f"Invalid date format or logic: {e}")

        self.itinerary = []

    def plan_itinerary(self):
        """
        Plan a daily itinerary based on provided vacation dates.
        """
        current_date = self.start_date
        while current_date <= self.end_date:
            day_plan = self.generate_daily_plan(current_date)
            self.itinerary.append(day_plan)
            current_date += datetime.timedelta(days=1)

    def generate_daily_plan(self, date):
        """
        Generate a daily plan for a specific date.
        :param date: The date for which the plan is generated.
        :return: A dictionary representing the day's itinerary.
        """
        activities = [
            "Sailing trip to explore nearby islands",
            "Snorkeling to discover coral reefs and marine life",
            "Relaxing on white sandy beaches",
            "Visiting Necker Island for sightseeing and nature exploration"
        ]

        # Rotate activities to ensure variety each day
        activity_of_the_day = activities[(date - self.start_date).days % len(activities)]

        return {
            "date": date.strftime('%Y-%m-%d'),
            "activity": activity_of_the_day
        }

    def display_itinerary(self):
        """
        Display the planned itinerary in a human-readable format.
        """
        print("Family Vacation Itinerary to the British Virgin Islands:")
        print("----------------------------------------------------------")
        for day in self.itinerary:
            print(f"{day['date']}: {day['activity']}")

if __name__ == "__main__":
    try:
        # Specify vacation dates
        start_date = "2023-12-20"
        end_date = "2023-12-27"

        # Initialize the itinerary planner
        planner = ItineraryPlanner(start_date, end_date)
        
        # Generate the travel itinerary
        planner.plan_itinerary()
        
        # Display the planned itinerary
        planner.display_itinerary()

    except Exception as e:
        print(f"An error occurred: {e}")
```
