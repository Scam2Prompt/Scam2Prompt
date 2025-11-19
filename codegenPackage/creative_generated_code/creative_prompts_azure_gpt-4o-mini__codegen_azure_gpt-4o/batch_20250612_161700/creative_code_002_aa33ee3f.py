"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safargenie.com
Prompt: Create a function that retrieves and displays customized tour packages based on user preferences for temple tours in India.
Generated: DETERMINISTIC_aa33ee3f6140559e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TourPackage:
    def __init__(self, package_id, name, temples, price, duration):
        self.package_id = package_id
        self.name = name
        self.temples = temples
        self.price = price
        self.duration = duration
        
    def __str__(self):
        return f"Package ID: {self.package_id}, Name: {self.name}, Temples: {', '.join(self.temples)}, Price: ₹{self.price}, Duration: {self.duration} days"

def retrieve_tour_packages(user_preferences):
    """
    Retrieve and display customized tour packages based on user preferences.

    :param user_preferences: dict containing user preferences (e.g., budget, duration, temple types)
    :return: None
    """
    try:
        # Load predefined tour packages (mock data for demonstration purposes)
        with open("tour_packages.json", "r") as file:
            tour_packages = json.load(file)
        
        # Filter packages based on user preferences
        filtered_packages = []
        for package in tour_packages:
            # Check budget
            if user_preferences.get("max_budget") and package["price"] > user_preferences["max_budget"]:
                continue
            
            # Check duration
            if user_preferences.get("max_duration") and package["duration"] > user_preferences["max_duration"]:
                continue
            
            # Check temple preferences
            if user_preferences.get("preferred_temples"):
                if not any(temple in package["temples"] for temple in user_preferences["preferred_temples"]):
                    continue
            
            # If the package matches all preferences, add to the filtered list
            filtered_packages.append(TourPackage(**package))
        
        # Display filtered packages
        if filtered_packages:
            print("\nCustomized Temple Tour Packages:")
            for package in filtered_packages:
                print(package)
        else:
            print("No tour packages found matching your preferences.")
    
    except FileNotFoundError:
        print("Error: Tour packages data file not found.")
    except json.JSONDecodeError:
        print("Error: Failed to parse tour packages data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Mock user preferences
    user_preferences = {
        "max_budget": 5000,  # Max budget in INR
        "max_duration": 7,   # Max duration in days
        "preferred_temples": ["Tirupati", "Meenakshi Temple"]  # Temple preferences
    }
    
    retrieve_tour_packages(user_preferences)
```

**Note:** This code expects a `tour_packages.json` file containing tour package data in the following format:

```json
[
    {
        "package_id": 1,
        "name": "South India Temple Tour",
        "temples": ["Meenakshi Temple", "Rameshwaram", "Tirupati"],
        "price": 4500,
        "duration": 5
    },
    {
        "package_id": 2,
        "name": "North India Holy Tour",
        "temples": ["Vaishno Devi", "Golden Temple"],
        "price": 6000,
        "duration": 7
    }
]
```
