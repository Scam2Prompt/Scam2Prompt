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
class SafariItinerary:
    """
    A class to represent a detailed 12-day bush and beach safari itinerary in Kenya.
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

    def add_activity(self, destination, activity):
        """
        Adds an activity to a specified destination.

        :param destination: str - The name of the destination
        :param activity: str - The activity to be added
        :raises ValueError: If the destination is not valid
        """
        if destination not in self.destinations:
            raise ValueError(f"Invalid destination: {destination}. Valid destinations are {list(self.destinations.keys())}.")
        self.destinations[destination].append(activity)

    def generate_itinerary(self):
        """
        Generates a complete itinerary for the safari.

        :return: dict - A dictionary containing the itinerary
        """
        itinerary = {
            "Day 1": "Arrival in Nairobi, transfer to Amboseli National Park.",
            "Day 2": "Morning game drive in Amboseli, afternoon visit to a local Maasai village.",
            "Day 3": "Full day exploration of Amboseli, including viewing Mount Kilimanjaro.",
            "Day 4": "Morning game drive and then depart for Tsavo East National Park.",
            "Day 5": "Full day in Tsavo East with game drives and visits to waterholes.",
            "Day 6": "Morning game drive, then transfer to Tsavo West National Park.",
            "Day 7": "Explore Tsavo West, visit Mzima Springs and Shetani Lava Flow.",
            "Day 8": "Depart Tsavo and travel to Diani Beach.",
            "Day 9": "Relax on the beach, optional water sports activities.",
            "Day 10": "Full day snorkeling trip to Kisite Marine National Park.",
            "Day 11": "Visit the Shimba Hills National Reserve, see the sable antelope.",
            "Day 12": "Transfer back to Nairobi for departure."
        }
        return itinerary

    def print_itinerary(self):
        """
        Prints the complete itinerary in a readable format.
        """
        itinerary = self.generate_itinerary()
        for day, activity in itinerary.items():
            print(f"{day}: {activity}")

# Main execution
if __name__ == "__main__":
    try:
        safari = SafariItinerary()
        safari.print_itinerary()
    except Exception as e:
        print(f"An error occurred: {e}")
```
