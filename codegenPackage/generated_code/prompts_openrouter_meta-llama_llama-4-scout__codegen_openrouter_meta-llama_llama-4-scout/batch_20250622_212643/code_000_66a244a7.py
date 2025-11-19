"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: "Generate a Python script to create a customized itinerary for a 9-day Kenyan safari trip, including destinations like Amboseli, Masai Mara, Naivasha, and Nakuru."
Generated: DETERMINISTIC_66a244a7b784871c
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# kenyan_safari_itinerary.py

class Destination:
    """Represents a destination in the Kenyan safari trip."""

    def __init__(self, name, description, activities):
        """
        Initializes a Destination object.

        Args:
            name (str): Name of the destination.
            description (str): Brief description of the destination.
            activities (list): List of activities to do at the destination.
        """
        self.name = name
        self.description = description
        self.activities = activities


class Itinerary:
    """Represents a 9-day Kenyan safari trip itinerary."""

    def __init__(self):
        """Initializes an Itinerary object with destinations."""
        self.destinations = [
            Destination("Amboseli", "Known for its elephant population and stunning views of Mount Kilimanjaro.", ["Game drive", "Sunset drive"]),
            Destination("Masai Mara", "Famous for its annual wildebeest migration and abundant wildlife.", ["Game drive", "Walking safari"]),
            Destination("Naivasha", "A haven for birdwatchers and home to Lake Naivasha.", ["Boat tour", "Hiking"]),
            Destination("Nakuru", "Home to Lake Nakuru National Park and the endangered Rothschild's giraffe.", ["Game drive", "Birdwatching"]),
        ]

    def print_itinerary(self):
        """Prints the 9-day itinerary."""
        for i, destination in enumerate(self.destinations, start=1):
            print(f"**Day {i}: {destination.name}**")
            print(f"{destination.description}")
            print("Activities:")
            for activity in destination.activities:
                print(f"- {activity}")
            print()  # Empty line for readability


def main():
    try:
        itinerary = Itinerary()
        itinerary.print_itinerary()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
