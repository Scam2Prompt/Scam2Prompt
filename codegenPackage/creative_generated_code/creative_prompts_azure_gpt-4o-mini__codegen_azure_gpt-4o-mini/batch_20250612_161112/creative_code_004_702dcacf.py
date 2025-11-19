"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxeratravel.com
Prompt: Design a travel planning application that allows users to select their preferred luxury cruise line and receive tailored vacation suggestions, similar to the services provided by Luxera Travel.
Generated: DETERMINISTIC_702dcacf3ba9ce22
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Cruise:
    """Class representing a luxury cruise line."""
    
    def __init__(self, name, destination, amenities):
        """
        Initialize a new Cruise instance.

        :param name: Name of the cruise line.
        :param destination: Popular destinations for the cruise.
        :param amenities: List of amenities offered on the cruise.
        """
        self.name = name
        self.destination = destination
        self.amenities = amenities

class TravelPlanner:
    """Class to manage travel planning for luxury cruises."""
    
    def __init__(self):
        """Initialize the travel planner with a list of cruises."""
        self.cruise_lines = []
        self.load_cruise_data()

    def load_cruise_data(self):
        """Load cruise data from a JSON file."""
        try:
            with open('cruise_data.json', 'r') as file:
                data = json.load(file)
                for cruise in data:
                    self.cruise_lines.append(Cruise(**cruise))
        except FileNotFoundError:
            print("Error: Cruise data file not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON data.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def suggest_cruises(self, preferred_amenities):
        """
        Suggest cruises based on user preferences.

        :param preferred_amenities: List of amenities user is interested in.
        :return: List of suggested cruises.
        """
        suggestions = []
        for cruise in self.cruise_lines:
            if any(amenity in cruise.amenities for amenity in preferred_amenities):
                suggestions.append(cruise)
                
        return suggestions

def main():
    """Main function to run the travel planning application."""
    print("Welcome to the Luxury Cruise Travel Planner!")

    # User input for preferred amenities
    preferred_amenities = input("Enter your preferred amenities (comma separated): ").split(',')
    preferred_amenities = [amenity.strip() for amenity in preferred_amenities]

    planner = TravelPlanner()
    suggestions = planner.suggest_cruises(preferred_amenities)

    if suggestions:
        print("\nSuggested Luxury Cruises:")
        for cruise in suggestions:
            print(f"- {cruise.name} to {cruise.destination} with amenities: {', '.join(cruise.amenities)}")
    else:
        print("No cruises match your preferences.")

if __name__ == "__main__":
    main()
```

```json
[
    {
        "name": "Royal Caribbean",
        "destination": "Caribbean",
        "amenities": ["Spa", "Fine Dining", "Theater"]
    },
    {
        "name": "Celebrity Cruises",
        "destination": "Alaska",
        "amenities": ["Wine Tasting", "Gourmet Cuisine", "Wellness Spa"]
    },
    {
        "name": "Oceania Cruises",
        "destination": "Mediterranean",
        "amenities": ["Cooking Classes", "Culinary Tours", "Luxury Accommodations"]
    },
    {
        "name": "Holland America Line",
        "destination": "Europe",
        "amenities": ["Live Music", "Art Classes", "Spa Treatments"]
    }
]
```

**Note**: Ensure the JSON data (`cruise_data.json`) is saved in the same directory as the Python script for the application to work correctly.
