"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldiscoveryperu.com
Prompt: Create a function that recommends travel packages based on user preferences for destinations like Puno and Iquitos, inspired by the offerings on World Discovery Peru.
Generated: DETERMINISTIC_97f86c415f13677d
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

# Define a class to represent a travel package
class TravelPackage:
    def __init__(self, name: str, destination: str, activities: List[str], price: float):
        """
        Initialize a new travel package.

        :param name: Name of the travel package
        :param destination: Destination of the travel package
        :param activities: List of activities included in the package
        :param price: Price of the travel package
        """
        self.name = name
        self.destination = destination
        self.activities = activities
        self.price = price

    def __repr__(self):
        return f"{self.name} to {self.destination} - Activities: {', '.join(self.activities)} - Price: ${self.price:.2f}"

# Sample travel packages to recommend
travel_packages = [
    TravelPackage("Mystical Puno Adventure", "Puno", ["Lake Titicaca Tour", "Uros Islands Visit", "Cultural Show"], 499.99),
    TravelPackage("Iquitos Jungle Expedition", "Iquitos", ["Amazon River Cruise", "Wildlife Spotting", "Local Village Visit"], 679.99),
    TravelPackage("Puno Cultural Journey", "Puno", ["Inca Ruins Tour", "Traditional Cuisine Tasting"], 399.99),
    TravelPackage("Iquitos Eco-Tour", "Iquitos", ["Rainforest Hiking", "Bird Watching"], 599.99),
]

def recommend_travel_package(destinations: List[str]) -> List[TravelPackage]:
    """
    Recommend travel packages based on user preferences for destinations.

    :param destinations: List of preferred destinations
    :return: List of recommended travel packages
    """
    try:
        recommendations = []
        
        # Check if the provided destinations are valid
        for destination in destinations:
            # Filter packages that match the user's preferred destinations
            matched_packages = [pkg for pkg in travel_packages if pkg.destination.lower() == destination.lower()]
            recommendations.extend(matched_packages)
            
        # If no packages were found, handle it gracefully
        if not recommendations:
            raise ValueError("No travel packages found for the given destinations.")
        
        return recommendations

    except Exception as e:
        print(f"Error occurred while recommending travel packages: {str(e)}")
        return []

# Example usage
if __name__ == "__main__":
    user_preferences = ["Puno", "Iquitos"]
    recommended_packages = recommend_travel_package(user_preferences)
    
    if recommended_packages:
        print("Recommended Travel Packages:")
        for package in recommended_packages:
            print(package)
    else:
        print("No packages to recommend.")
```
