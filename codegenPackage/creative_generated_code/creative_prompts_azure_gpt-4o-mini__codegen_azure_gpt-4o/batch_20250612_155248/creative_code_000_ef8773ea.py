"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://localtravelcoupons.com
Prompt: Generate a code snippet for a travel booking application that allows users to customize travel packages based on their budget, similar to the services offered by Local Travel Coupons.
Generated: DETERMINISTIC_ef8773ea265bbaa2
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TravelPackage:
    """
    Class representing a travel package.
    Allows customization based on budget and preferences.
    """
    def __init__(self, destination, base_price, activities):
        """
        Initialize a travel package.
        :param destination: The name of the destination.
        :param base_price: The base price of the package.
        :param activities: A dictionary of activities with their prices.
        """
        self.destination = destination
        self.base_price = base_price
        self.activities = activities

    def calculate_total_price(self, selected_activities):
        """
        Calculate the total price based on selected activities.
        :param selected_activities: A list of activity names to include in the package.
        :return: Total price of the package.
        """
        total_price = self.base_price
        for activity in selected_activities:
            if activity in self.activities:
                total_price += self.activities[activity]
        return total_price


def customize_travel_package(packages, budget, destination, preferences):
    """
    Customize a travel package based on user budget and preferences.
    :param packages: List of TravelPackage objects available.
    :param budget: User's budget.
    :param destination: Desired destination.
    :param preferences: List of preferred activities.
    :return: JSON string with the customized package details or an error message.
    """
    try:
        # Find the package matching the destination
        selected_package = next(
            (package for package in packages if package.destination.lower() == destination.lower()), None
        )

        if not selected_package:
            raise ValueError("Destination not available.")

        # Calculate total price with preferred activities
        total_price = selected_package.calculate_total_price(preferences)

        if total_price > budget:
            return json.dumps({
                "error": "Budget exceeded.",
                "details": {
                    "total_price": total_price,
                    "budget": budget
                }
            }, indent=4)

        # Return the customized package details
        return json.dumps({
            "destination": selected_package.destination,
            "base_price": selected_package.base_price,
            "selected_activities": preferences,
            "total_price": total_price
        }, indent=4)

    except Exception as e:
        # Handle unexpected errors
        return json.dumps({
            "error": "An error occurred while customizing the travel package.",
            "details": str(e)
        }, indent=4)


# Example usage
if __name__ == "__main__":
    # Define available travel packages
    available_packages = [
        TravelPackage(
            destination="Hawaii",
            base_price=500,
            activities={
                "Snorkeling": 50,
                "Surfing": 75,
                "Volcano Tour": 100
            }
        ),
        TravelPackage(
            destination="Paris",
            base_price=700,
            activities={
                "Eiffel Tower Visit": 30,
                "Wine Tasting": 50,
                "Museum Tour": 40
            }
        )
    ]

    # User preferences
    user_budget = 600
    user_destination = "Hawaii"
    user_preferences = ["Snorkeling", "Surfing"]

    # Generate customized travel package
    result = customize_travel_package(available_packages, user_budget, user_destination, user_preferences)
    print(result)
```
