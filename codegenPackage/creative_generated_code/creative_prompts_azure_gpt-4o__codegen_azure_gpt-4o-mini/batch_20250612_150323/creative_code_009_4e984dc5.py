"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Write a program to simulate a tour itinerary for exploring the Greek archipelago using RIBs, including stops at remote islands and hidden treasures accessible only by boat.
Generated: DETERMINISTIC_4e984dc55617f187
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Class to represent a location in the Greek archipelago
class Location:
    def __init__(self, name, description, coordinates):
        self.name = name
        self.description = description
        self.coordinates = coordinates

    def __str__(self):
        return f"{self.name}: {self.description} (Coordinates: {self.coordinates})"

# Class to represent a tour itinerary
class TourItinerary:
    def __init__(self):
        self.locations = []
    
    def add_location(self, location):
        """Add a location to the itinerary."""
        self.locations.append(location)
    
    def get_random_locations(self, n):
        """Return a random selection of locations from the itinerary."""
        if n > len(self.locations):
            raise ValueError("Requested number of locations exceeds available locations.")
        return random.sample(self.locations, n)

    def show_itinerary(self):
        """Display the full itinerary."""
        if not self.locations:
            print("No locations in itinerary.")
            return
        print("Tour Itinerary:")
        for idx, location in enumerate(self.locations, start=1):
            print(f"{idx}. {location}")

def main():
    try:
        # Create instances of Location
        santorini = Location("Santorini", "Famous for its stunning sunsets and whitewashed buildings.", (36.3932, 25.4615))
        mykonos = Location("Mykonos", "Known for its vibrant nightlife and beautiful beaches.", (37.4467, 25.3289))
        milos = Location("Milos", "Offers unique rock formations and crystal-clear waters.", (36.7034, 24.4780))
        naxos = Location("Naxos", "The largest of the Cyclades, great for hiking and local cuisine.", (37.0997, 25.3902))
        folegandros = Location("Folegandros", "A hidden gem with traditional architecture and serene beaches.", (36.4044, 24.9639))

        # Create the tour itinerary
        itinerary = TourItinerary()
        itinerary.add_location(santorini)
        itinerary.add_location(mykonos)
        itinerary.add_location(milos)
        itinerary.add_location(naxos)
        itinerary.add_location(folegandros)

        # Show the full itinerary
        itinerary.show_itinerary()

        # Get a random selection of 3 locations for a shorter tour
        print("\nRandomly selected locations for a shorter tour:")
        random_locations = itinerary.get_random_locations(3)
        for location in random_locations:
            print(location)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
