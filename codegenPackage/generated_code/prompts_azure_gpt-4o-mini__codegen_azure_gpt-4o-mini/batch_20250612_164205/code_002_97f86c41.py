"""
Generated Code Metadata:
========================
Original URL: https://worldiscoveryperu.com
Prompt: Create a function that recommends travel packages based on user preferences for destinations like Puno and Iquitos, inspired by the offerings on World Discovery Peru.
Generated: DETERMINISTIC_97f86c415f13677d
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

# Define a class to represent a travel package
class TravelPackage:
    def __init__(self, destination: str, activities: List[str], price: float):
        self.destination = destination
        self.activities = activities
        self.price = price

    def __repr__(self):
        return f"TravelPackage(destination={self.destination}, activities={self.activities}, price={self.price})"

# Function to recommend travel packages based on user preferences
def recommend_travel_packages(preferred_destinations: List[str], budget: float) -> List[TravelPackage]:
    """
    Recommends travel packages based on user preferences for destinations and budget.

    :param preferred_destinations: List of preferred travel destinations
    :param budget: Maximum budget for the travel package
    :return: List of recommended travel packages
    """
    
    # Sample travel packages data
    travel_packages = [
        TravelPackage("Puno", ["Lake Titicaca Tour", "Cultural Experience"], 300.0),
        TravelPackage("Iquitos", ["Amazon Rainforest Tour", "Wildlife Watching"], 450.0),
        TravelPackage("Puno", ["Isla del Sol Visit", "Local Cuisine Tasting"], 250.0),
        TravelPackage("Iquitos", ["Jungle Trekking", "Indigenous Community Visit"], 500.0),
        TravelPackage("Cusco", ["Machu Picchu Tour", "Sacred Valley Exploration"], 600.0),
    ]

    # Filter packages based on user preferences and budget
    recommended_packages = []
    for package in travel_packages:
        if package.destination in preferred_destinations and package.price <= budget:
            recommended_packages.append(package)

    # If no packages are found, raise an exception
    if not recommended_packages:
        raise ValueError("No travel packages found matching your preferences and budget.")

    return recommended_packages

# Example usage
if __name__ == "__main__":
    try:
        user_preferences = ["Puno", "Iquitos"]
        user_budget = 400.0
        recommendations = recommend_travel_packages(user_preferences, user_budget)
        print("Recommended Travel Packages:")
        for package in recommendations:
            print(package)
    except ValueError as e:
        print(f"Error: {e}")
```
