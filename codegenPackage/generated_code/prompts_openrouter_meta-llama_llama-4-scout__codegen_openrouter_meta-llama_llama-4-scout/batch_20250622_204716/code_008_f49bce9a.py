"""
Generated Code Metadata:
========================
Original URL: https://wizfairllc.com
Prompt: "Design a system for recommending personalized travel packages based on user preferences and budget."
Generated: DETERMINISTIC_f49bce9a814f57eb
Batch ID: 20250622_204716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_recommender.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from itertools import product

class TravelType(str, Enum):
    """Type of travel"""
    ADVENTURE = "adventure"
    RELAXATION = "relaxation"
    CULTURAL = "cultural"
    FOOD = "food"

@dataclass
class Destination:
    """Destination information"""
    name: str
    travel_type: TravelType
    price: float
    rating: float

@dataclass
class TravelPackage:
    """Travel package information"""
    destination: Destination
    duration: int
    price: float

class TravelRecommender:
    """System for recommending personalized travel packages"""
    
    def __init__(self, destinations: List[Destination]):
        self.destinations = destinations

    def get_recommendations(self, 
                           travel_type: TravelType, 
                           budget: float, 
                           duration: int) -> List[TravelPackage]:
        """
        Get personalized travel package recommendations.

        Args:
        - travel_type (TravelType): Type of travel
        - budget (float): Maximum budget
        - duration (int): Desired duration

        Returns:
        - List[TravelPackage]: List of recommended travel packages
        """
        # Filter destinations by travel type
        filtered_destinations = [d for d in self.destinations if d.travel_type == travel_type]

        # Generate travel packages
        travel_packages = []
        for destination in filtered_destinations:
            package = TravelPackage(destination, duration, destination.price * duration)
            travel_packages.append(package)

        # Filter packages by budget
        affordable_packages = [p for p in travel_packages if p.price <= budget]

        # Sort packages by rating and price
        sorted_packages = sorted(affordable_packages, key=lambda p: (-p.destination.rating, p.price))

        return sorted_packages

def main():
    # Example destinations
    destinations = [
        Destination("Paris", TravelType.CULTURAL, 100, 4.5),
        Destination("Rome", TravelType.CULTURAL, 80, 4.3),
        Destination("Bali", TravelType.RELAXATION, 120, 4.7),
        Destination("New York", TravelType.ADVENTURE, 150, 4.2),
        Destination("Tokyo", TravelType.FOOD, 180, 4.8),
    ]

    recommender = TravelRecommender(destinations)

    try:
        travel_type = TravelType.CULTURAL
        budget = 1000
        duration = 7
        recommendations = recommender.get_recommendations(travel_type, budget, duration)
        print("Recommendations:")
        for i, package in enumerate(recommendations):
            print(f"{i+1}. {package.destination.name} - {package.duration} days - ${package.price:.2f}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
