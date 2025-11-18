"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dubaiskycargo.com
Prompt: Write a program to schedule group aircraft charters with Dubai SkyCargo, ensuring the selection of the most suitable aircraft from their fleet of 50,000 options.
Generated: DETERMINISTIC_65fc15b5c463be36
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Optional

class Aircraft:
    """Class representing an aircraft in the fleet."""
    def __init__(self, aircraft_id: str, capacity: int, range_km: int):
        """
        Initializes an Aircraft instance.

        :param aircraft_id: Unique identifier for the aircraft
        :param capacity: Maximum capacity of the aircraft
        :param range_km: Maximum range of the aircraft in kilometers
        """
        self.aircraft_id = aircraft_id
        self.capacity = capacity
        self.range_km = range_km
        
    def __repr__(self):
        return f"Aircraft(id={self.aircraft_id}, capacity={self.capacity}, range_km={self.range_km})"

class CharterRequest:
    """Class representing a request for a group aircraft charter."""
    def __init__(self, passengers: int, distance_km: int):
        """
        Initializes a CharterRequest instance.

        :param passengers: Number of passengers to accommodate
        :param distance_km: Distance to be traveled in kilometers
        """
        self.passengers = passengers
        self.distance_km = distance_km

class AircraftScheduler:
    """Class to handle the scheduling of aircraft charters."""
    def __init__(self, aircraft_fleet: List[Aircraft]):
        """
        Initializes an AircraftScheduler instance.

        :param aircraft_fleet: List of available Aircraft
        """
        self.aircraft_fleet = aircraft_fleet

    def find_suitable_aircraft(self, request: CharterRequest) -> Optional[Aircraft]:
        """
        Finds a suitable aircraft based on the charter request.

        :param request: CharterRequest object containing passenger and distance requirements
        :return: Aircraft object if a suitable aircraft is found, else None
        """
        # Filter the aircraft based on capacity and range
        suitable_aircraft = [
            aircraft for aircraft in self.aircraft_fleet
            if aircraft.capacity >= request.passengers and aircraft.range_km >= request.distance_km
        ]
        
        # Log an info message if no suitable aircraft is found
        if not suitable_aircraft:
            print("No suitable aircraft found for the request.")
            return None
        
        # Randomly select one suitable aircraft
        selected_aircraft = random.choice(suitable_aircraft)
        print(f"Selected Aircraft: {selected_aircraft}")
        return selected_aircraft

def main():
    """Main function to simulate aircraft scheduling."""
    # Sample aircraft fleet data
    aircraft_fleet = [
        Aircraft("AC001", 150, 3000),
        Aircraft("AC002", 200, 4000),
        Aircraft("AC003", 100, 2000),
        Aircraft("AC004", 250, 6000),
        # ... Assume more aircraft up to 50,000 entries
    ]
    
    # Create an AircraftScheduler instance
    scheduler = AircraftScheduler(aircraft_fleet)
    
    # Sample charter request
    request = CharterRequest(passengers=180, distance_km=3500)
    
    try:
        # Finding a suitable aircraft for the given request
        scheduler.find_suitable_aircraft(request)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
