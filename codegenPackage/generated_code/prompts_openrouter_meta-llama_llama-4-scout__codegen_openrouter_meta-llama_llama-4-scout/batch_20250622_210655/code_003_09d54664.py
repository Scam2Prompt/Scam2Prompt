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
# itinerary_generator.py

class HorseRidingTour:
    def __init__(self, days, location):
        """
        Initialize a Horse Riding Tour.

        Args:
            days (int): Number of days for the tour.
            location (str): Location of the tour.

        Raises:
            ValueError: If days or location is invalid.
        """
        if days <= 0:
            raise ValueError("Days must be a positive integer.")
        if not location:
            raise ValueError("Location cannot be empty.")

        self.days = days
        self.location = location
        self.itinerary = []

    def add_experience(self, experience):
        """
        Add an experience to the itinerary.

        Args:
            experience (str): Experience to add.

        Raises:
            ValueError: If experience is empty.
        """
        if not experience:
            raise ValueError("Experience cannot be empty.")

        self.itinerary.append(experience)

    def generate_itinerary(self):
        """
        Generate a tailored itinerary for a 6-day horse riding tour.

        Returns:
            list: Itinerary for the tour.
        """
        # Day 1: Arrival and horse riding introduction
        self.add_experience("Day 1: Arrival in Andes Mountain range, introduction to horse riding")

        # Day 2: Rari Discovery Ride
        self.add_experience("Day 2: Rari Discovery Ride - Explore the scenic trails of Rari")

        # Day 3: Horse riding and local culture
        self.add_experience("Day 3: Horse riding through the Andes, experience local culture")

        # Day 4: Moonshine Ride
        self.add_experience("Day 4: Moonshine Ride - Enjoy the sunset on horseback")

        # Day 5: Horse riding and relaxation
        self.add_experience("Day 5: Horse riding and relaxation in a scenic spot")

        # Day 6: Departure
        self.add_experience("Day 6: Departure from Andes Mountain range")

        return self.itinerary


def main():
    try:
        tour = HorseRidingTour(6, "Andes Mountain range")
        itinerary = tour.generate_itinerary()

        print("Tailored Itinerary:")
        for day, experience in enumerate(itinerary, start=1):
            print(f"Day {day}: {experience}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
