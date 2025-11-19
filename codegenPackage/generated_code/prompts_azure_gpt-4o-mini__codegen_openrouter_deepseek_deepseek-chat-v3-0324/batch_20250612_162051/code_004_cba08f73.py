"""
Generated Code Metadata:
========================
Original URL: https://www.fravitur.com
Prompt: Illustrate how to implement a search feature in a travel app that filters trips by destination, specifically for locations like Cartagena and Eje Cafetero, as highlighted on Fravitur.
Generated: DETERMINISTIC_cba08f7367bac71b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional
from dataclasses import dataclass
from enum import Enum

class Destination(Enum):
    """Enum representing available travel destinations."""
    CARTAGENA = "Cartagena"
    EJE_CAFETERO = "Eje Cafetero"
    OTHER = "Other"

@dataclass
class Trip:
    """Data class representing a travel trip."""
    id: str
    name: str
    destination: Destination
    price: float
    duration_days: int

class TripSearch:
    """Class for searching and filtering trips by destination."""
    
    def __init__(self, trips: List[Trip]):
        """Initialize with a list of available trips."""
        self.trips = trips
    
    def search_by_destination(self, destination: Optional[Destination] = None) -> List[Trip]:
        """
        Search trips by destination.
        
        Args:
            destination: Optional Destination enum to filter by. If None, returns all trips.
        
        Returns:
            List of Trip objects matching the destination filter.
        """
        if not destination:
            return self.trips
        
        return [trip for trip in self.trips if trip.destination == destination]

# Example usage
if __name__ == "__main__":
    # Sample trip data
    sample_trips = [
        Trip("1", "Cartagena Beach Getaway", Destination.CARTAGENA, 1200.00, 5),
        Trip("2", "Coffee Region Adventure", Destination.EJE_CAFETERO, 950.50, 4),
        Trip("3", "Cartagena Historic Tour", Destination.CARTAGENA, 800.00, 3),
        Trip("4", "Mountain Retreat", Destination.OTHER, 750.00, 7)
    ]
    
    # Initialize search
    trip_search = TripSearch(sample_trips)
    
    # Search for Cartagena trips
    cartagena_trips = trip_search.search_by_destination(Destination.CARTAGENA)
    print("Cartagena Trips:")
    for trip in cartagena_trips:
        print(f"- {trip.name} (${trip.price})")
    
    # Search for Eje Cafetero trips
    eje_trips = trip_search.search_by_destination(Destination.EJE_CAFETERO)
    print("\nEje Cafetero Trips:")
    for trip in eje_trips:
        print(f"- {trip.name} (${trip.price})")
```
