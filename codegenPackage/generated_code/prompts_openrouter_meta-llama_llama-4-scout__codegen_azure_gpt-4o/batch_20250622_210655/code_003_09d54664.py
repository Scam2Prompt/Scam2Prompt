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
import datetime

class HorseRidingTour:
    """
    Class to create and manage a tailored itinerary for a horse riding tour.
    """

    def __init__(self, start_date):
        """
        Initialize the tour with a start date.
        :param start_date: The start date of the tour (YYYY-MM-DD format).
        """
        try:
            self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            self.itinerary = []
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def add_activity(self, day, activity_name, description):
        """
        Add an activity to the itinerary.
        :param day: The day number of the tour (1-6).
        :param activity_name: Name of the activity.
        :param description: Description of the activity.
        """
        if day < 1 or day > 6:
            raise ValueError("Day must be between 1 and 6.")
        self.itinerary.append({
            "day": day,
            "date": (self.start_date + datetime.timedelta(days=day - 1)).strftime("%Y-%m-%d"),
            "activity_name": activity_name,
            "description": description
        })

    def generate_itinerary(self):
        """
        Generate the full itinerary for the tour.
        :return: List of activities for the tour.
        """
        if not self.itinerary:
            raise ValueError("No activities added to the itinerary.")
        return sorted(self.itinerary, key=lambda x: x["day"])

    def display_itinerary(self):
        """
        Display the itinerary in a user-friendly format.
        """
        print("6-Day Horse Riding Tour Itinerary in Chile's Andes Mountains:")
        print("=" * 60)
        for activity in self.generate_itinerary():
            print(f"Day {activity['day']} ({activity['date']}):")
            print(f"  Activity: {activity['activity_name']}")
            print(f"  Description: {activity['description']}")
            print("-" * 60)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tour with a start date
        tour = HorseRidingTour(start_date="2023-11-01")

        # Add activities to the itinerary
        tour.add_activity(1, "Arrival and Orientation", "Arrive in Chile and meet the tour guides. Briefing about the tour.")
        tour.add_activity(2, "Rari Discovery Ride", "Explore the picturesque village of Rari, famous for its horse culture and crafts.")
        tour.add_activity(3, "Mountain Trail Adventure", "Ride through scenic trails in the Andes, enjoying breathtaking views.")
        tour.add_activity(4, "Moonshine Ride", "Experience a magical night ride under the moonlight in the Andes.")
        tour.add_activity(5, "Local Culture Immersion", "Visit local communities and learn about their traditions and lifestyle.")
        tour.add_activity(6, "Farewell Ride and Departure", "Enjoy a final ride and bid farewell to the Andes before departure.")

        # Display the itinerary
        tour.display_itinerary()

    except Exception as e:
        print(f"Error: {e}")
```
