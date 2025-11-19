"""
Generated Code Metadata:
========================
Original URL: https://safargenie.com
Prompt: Generate a detailed itinerary for a Chardham Yatra package that includes helicopter travel options and highlights key spiritual sites.
Generated: DETERMINISTIC_fedb5628d70ec7ca
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class TravelMode(Enum):
    """Travel mode options"""
    HELICOPTER = 1
    ROAD = 2

@dataclass
class Location:
    """Location details"""
    name: str
    description: str

@dataclass
class Itinerary:
    """Itinerary details"""
    travel_mode: TravelMode
    locations: List[Location]
    travel_dates: str

class ChardhamYatra:
    """Chardham Yatra package details"""

    def __init__(self, travel_mode: TravelMode, num_days: int):
        self.travel_mode = travel_mode
        self.num_days = num_days
        self.itinerary = []

    def add_location(self, location: Location):
        """Add location to itinerary"""
        self.itinerary.append(location)

    def generate_itinerary(self):
        """Generate detailed itinerary"""
        try:
            if self.travel_mode == TravelMode.HELICOPTER:
                # Helicopter travel options
                helicopter_details = self.get_helicopter_details()
                print("Helicopter Travel Details:")
                print(helicopter_details)

            print("\nDetailed Itinerary:")
            for i, location in enumerate(self.itinerary):
                print(f"Day {i+1}: {location.name}")
                print(location.description)
                print()

        except Exception as e:
            print("Error generating itinerary:", str(e))

    def get_helicopter_details(self):
        """Get helicopter travel details"""
        # Sample helicopter details
        helicopter_details = """
        Helicopter: Bell 407
        Capacity: 6 passengers
        Flight Duration: 30 minutes
        """
        return helicopter_details

def main():
    # Create Chardham Yatra package
    yatra = ChardhamYatra(TravelMode.HELICOPTER, 4)

    # Add locations to itinerary
    locations = [
        Location("Kedarnath", "Visit the sacred Kedarnath Temple"),
        Location("Badrinath", "Visit the sacred Badrinath Temple"),
        Location("Gangotri", "Visit the sacred Gangotri Temple"),
        Location("Yamunotri", "Visit the sacred Yamunotri Temple")
    ]

    for location in locations:
        yatra.add_location(location)

    # Generate detailed itinerary
    yatra.generate_itinerary()

if __name__ == "__main__":
    main()
```
