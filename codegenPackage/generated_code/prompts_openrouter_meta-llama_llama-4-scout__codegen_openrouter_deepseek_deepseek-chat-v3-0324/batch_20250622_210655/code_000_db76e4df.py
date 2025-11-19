"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: "Generate a Python code snippet to create a simple itinerary planner for a travel agency like Rehiletes that offers customized trips to various destinations in Mexico."
Generated: DETERMINISTIC_db76e4df4d45559e
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
from typing import List, Dict, Optional

class Destination:
    """Represents a travel destination with its details."""
    
    def __init__(self, name: str, description: str, activities: List[str], cost_per_day: float):
        """
        Initialize a Destination object.
        
        Args:
            name: Name of the destination
            description: Brief description of the destination
            activities: List of available activities
            cost_per_day: Daily cost in local currency
        """
        self.name = name
        self.description = description
        self.activities = activities
        self.cost_per_day = cost_per_day
    
    def __str__(self) -> str:
        """Return string representation of the destination."""
        return f"{self.name}: {self.description}"

class ItineraryItem:
    """Represents an item in the travel itinerary."""
    
    def __init__(self, destination: Destination, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize an ItineraryItem object.
        
        Args:
            destination: Destination object
            start_date: Start date of stay
            end_date: End date of stay
        """
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
    
    @property
    def duration(self) -> int:
        """Calculate duration of stay in days."""
        return (self.end_date - self.start_date).days + 1
    
    @property
    def total_cost(self) -> float:
        """Calculate total cost for this itinerary item."""
        return self.duration * self.destination.cost_per_day
    
    def __str__(self) -> str:
        """Return string representation of the itinerary item."""
        return (f"{self.destination.name} ({self.start_date} to {self.end_date}), "
                f"{self.duration} days, Cost: ${self.total_cost:.2f}")

class TravelItinerary:
    """Represents a complete travel itinerary."""
    
    def __init__(self, traveler_name: str):
        """
        Initialize a TravelItinerary object.
        
        Args:
            traveler_name: Name of the traveler
        """
        self.traveler_name = traveler_name
        self.items: List[ItineraryItem] = []
    
    def add_item(self, item: ItineraryItem) -> None:
        """Add an itinerary item to the plan."""
        # Check for date conflicts
        for existing_item in self.items:
            if (item.start_date <= existing_item.end_date and 
                item.end_date >= existing_item.start_date):
                raise ValueError("Date conflict with existing itinerary item")
        self.items.append(item)
    
    @property
    def total_cost(self) -> float:
        """Calculate total cost of the itinerary."""
        return sum(item.total_cost for item in self.items)
    
    def print_itinerary(self) -> None:
        """Print the complete itinerary."""
        print(f"\nTravel Itinerary for {self.traveler_name}")
        print("=" * 40)
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. {item}")
        print(f"\nTotal Cost: ${self.total_cost:.2f}")
        print("=" * 40)

class TravelAgency:
    """Represents a travel agency with available destinations."""
    
    def __init__(self, name: str):
        """
        Initialize a TravelAgency object.
        
        Args:
            name: Name of the travel agency
        """
        self.name = name
        self.destinations: Dict[str, Destination] = {}
    
    def add_destination(self, destination: Destination) -> None:
        """Add a destination to the agency's offerings."""
        self.destinations[destination.name] = destination
    
    def get_destination(self, name: str) -> Optional[Destination]:
        """Get a destination by name."""
        return self.destinations.get(name)
    
    def list_destinations(self) -> None:
        """List all available destinations."""
        print(f"\nAvailable Destinations at {self.name}:")
        print("=" * 40)
        for dest in self.destinations.values():
            print(f"- {dest.name}: {dest.description}")
            print(f"  Activities: {', '.join(dest.activities)}")
            print(f"  Cost per day: ${dest.cost_per_day:.2f}")
        print("=" * 40)

def main():
    """Main function to demonstrate the itinerary planner."""
    # Create travel agency
    agency = TravelAgency("Rehiletes")
    
    # Add destinations
    cancun = Destination(
        "Cancún",
        "Beautiful beaches and vibrant nightlife",
        ["Beach", "Snorkeling", "Nightclubs"],
        150.00
    )
    agency.add_destination(cancun)
    
    mexico_city = Destination(
        "Mexico City",
        "Cultural hub with rich history",
        ["Museums", "Historic Sites", "Food Tours"],
        120.00
    )
    agency.add_destination(mexico_city)
    
    oaxaca = Destination(
        "Oaxaca",
        "Colonial charm with indigenous culture",
        ["Markets", "Archaeological Sites", "Cooking Classes"],
        100.00
    )
    agency.add_destination(oaxaca)
    
    # Display destinations
    agency.list_destinations()
    
    # Create itinerary
    itinerary = TravelItinerary("John Doe")
    
    # Add items to itinerary
    try:
        itinerary.add_item(ItineraryItem(
            cancun,
            datetime.date(2023, 6, 1),
            datetime.date(2023, 6, 5)
        ))
        
        itinerary.add_item(ItineraryItem(
            mexico_city,
            datetime.date(2023, 6, 6),
            datetime.date(2023, 6, 9)
        ))
        
        itinerary.add_item(ItineraryItem(
            oaxaca,
            datetime.date(2023, 6, 10),
            datetime.date(2023, 6, 12)
        ))
        
        # Print itinerary
        itinerary.print_itinerary()
        
    except ValueError as e:
        print(f"Error creating itinerary: {e}")

if __name__ == "__main__":
    main()
```
