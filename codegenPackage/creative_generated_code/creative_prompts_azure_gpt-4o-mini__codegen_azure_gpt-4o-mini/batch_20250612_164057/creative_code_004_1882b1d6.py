"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://africarisesafaris.com
Prompt: Outline a sample cultural village tour itinerary that includes visits to local attractions and interactions with the Maasai and Chaga tribes in Tanzania.
Generated: DETERMINISTIC_1882b1d6d39271da
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CulturalVillageTour:
    """
    A class to represent a cultural village tour in Tanzania.
    """
    
    def __init__(self, tour_name, duration_days):
        """
        Initializes the CulturalVillageTour with a name and duration.
        
        :param tour_name: Name of the tour
        :param duration_days: Duration of the tour in days
        """
        self.tour_name = tour_name
        self.duration_days = duration_days
        self.itinerary = []

    def add_activity(self, day, activity):
        """
        Adds an activity to the itinerary for a specific day.
        
        :param day: Day of the tour (1-indexed)
        :param activity: Description of the activity
        """
        if day < 1 or day > self.duration_days:
            raise ValueError(f"Day {day} is out of the tour duration range.")
        
        self.itinerary.append((day, activity))
    
    def get_itinerary(self):
        """
        Returns the complete itinerary for the tour.
        
        :return: List of activities organized by day
        """
        # Sort activities by day
        self.itinerary.sort(key=lambda x: x[0])
        return self.itinerary

    def display_itinerary(self):
        """
        Prints the itinerary in a user-friendly format.
        """
        print(f"Itinerary for '{self.tour_name}':")
        for day, activity in self.get_itinerary():
            print(f"Day {day}: {activity}")


# Sample setup of a cultural village tour itinerary
try:
    # Create a cultural village tour for 5 days
    tour = CulturalVillageTour("Cultural Experience in Tanzania", 5)

    # Add activities to the itinerary
    tour.add_activity(1, "Arrival in Arusha and orientation.")
    tour.add_activity(2, "Visit a Maasai village - Interact with locals and learn about their traditions.")
    tour.add_activity(3, "Explore Mount Meru and engage with Chaga tribe members.")
    tour.add_activity(4, "Participate in a traditional cooking class with the Chaga people.")
    tour.add_activity(5, "Final day - visit local markets and purchase handmade crafts.")

    # Display the complete itinerary
    tour.display_itinerary()

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
