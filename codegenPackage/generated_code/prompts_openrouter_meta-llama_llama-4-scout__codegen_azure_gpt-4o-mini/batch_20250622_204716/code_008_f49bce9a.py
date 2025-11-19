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
import json
from typing import List, Dict, Any

class TravelPackage:
    """Class representing a travel package."""
    
    def __init__(self, destination: str, price: float, activities: List[str]):
        self.destination = destination
        self.price = price
        self.activities = activities

    def to_dict(self) -> Dict[str, Any]:
        """Convert the travel package to a dictionary."""
        return {
            "destination": self.destination,
            "price": self.price,
            "activities": self.activities
        }

class UserPreferences:
    """Class representing user preferences for travel."""
    
    def __init__(self, budget: float, preferred_activities: List[str]):
        self.budget = budget
        self.preferred_activities = preferred_activities

class TravelRecommendationSystem:
    """System for recommending travel packages based on user preferences."""
    
    def __init__(self, packages: List[TravelPackage]):
        self.packages = packages

    def recommend(self, user_preferences: UserPreferences) -> List[TravelPackage]:
        """Recommend travel packages based on user preferences."""
        recommendations = []
        
        for package in self.packages:
            if package.price <= user_preferences.budget and \
               any(activity in package.activities for activity in user_preferences.preferred_activities):
                recommendations.append(package)
        
        return recommendations

def load_travel_packages(file_path: str) -> List[TravelPackage]:
    """Load travel packages from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [TravelPackage(**pkg) for pkg in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    """Main function to run the travel recommendation system."""
    # Load travel packages from a JSON file
    travel_packages = load_travel_packages('travel_packages.json')
    
    # Define user preferences
    user_preferences = UserPreferences(budget=1500.0, preferred_activities=['hiking', 'beach'])

    # Create the recommendation system
    recommendation_system = TravelRecommendationSystem(travel_packages)

    # Get recommendations
    recommendations = recommendation_system.recommend(user_preferences)

    # Display recommendations
    if recommendations:
        print("Recommended Travel Packages:")
        for pkg in recommendations:
            print(pkg.to_dict())
    else:
        print("No travel packages match your preferences.")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `travel_packages.json` file exists in the same directory as this script and contains valid JSON data representing travel packages.
