"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Create a detailed plan for a 12-day bush and beach safari in Kenya, highlighting activities in Amboseli, Diani, and Tsavo.
Generated: DETERMINISTIC_5520107abfb829f1
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SafariItinerary:
    """
    A class to represent a detailed itinerary for a 12-day bush and beach safari in Kenya.
    """

    def __init__(self):
        """
        Initializes the itinerary with destinations and activities.
        """
        self.destinations = {
            "Amboseli": [],
            "Tsavo": [],
            "Diani": []
        }
        self.days = 12

    def add_activity(self, destination, activity):
        """
        Adds an activity to a specific destination.

        :param destination: The destination where the activity will take place.
        :param activity: The activity to be added.
        :raises ValueError: If the destination is not valid.
        """
        if destination not in self.destinations:
            raise ValueError(f"Invalid destination: {destination}. Valid options are: {list(self.destinations.keys())}")
        self.destinations[destination].append(activity)

    def generate_itinerary(self):
        """
        Generates a detailed itinerary for the safari.

        :return: A string representation of the itinerary.
        """
        itinerary = "12-Day Bush and Beach Safari Itinerary in Kenya\n"
        itinerary += "=" * 50 + "\n"
        for destination, activities in self.destinations.items():
            itinerary += f"\nDestination: {destination}\n"
            itinerary += "-" * 30 + "\n"
            for day, activity in enumerate(activities, start=1):
                itinerary += f"Day {day}: {activity}\n"
        return itinerary

    def plan_safari(self):
        """
        Plans the safari by adding activities to each destination.
        """
        try:
            # Amboseli Activities
            self.add_activity("Amboseli", "Day 1: Arrival in Nairobi and transfer to Amboseli.")
            self.add_activity("Amboseli", "Day 2: Morning game drive in Amboseli National Park.")
            self.add_activity("Amboseli", "Day 3: Visit to a Maasai village and cultural experience.")
            self.add_activity("Amboseli", "Day 4: Afternoon game drive and sunset photography.")

            # Tsavo Activities
            self.add_activity("Tsavo", "Day 5: Transfer to Tsavo East National Park.")
            self.add_activity("Tsavo", "Day 6: Full day game drive in Tsavo East.")
            self.add_activity("Tsavo", "Day 7: Visit to the Tsavo River and wildlife viewing.")
            self.add_activity("Tsavo", "Day 8: Night game drive experience.")

            # Diani Activities
            self.add_activity("Diani", "Day 9: Transfer to Diani Beach for relaxation.")
            self.add_activity("Diani", "Day 10: Snorkeling and water sports at Diani Beach.")
            self.add_activity("Diani", "Day 11: Visit to Kisite-Mpunguti Marine National Park.")
            self.add_activity("Diani", "Day 12: Departure from Diani Beach back to Nairobi.")
        
        except ValueError as e:
            print(f"Error planning safari: {e}")

# Create an instance of SafariItinerary
safari = SafariItinerary()
# Plan the safari
safari.plan_safari()
# Generate and print the itinerary
print(safari.generate_itinerary())
```
