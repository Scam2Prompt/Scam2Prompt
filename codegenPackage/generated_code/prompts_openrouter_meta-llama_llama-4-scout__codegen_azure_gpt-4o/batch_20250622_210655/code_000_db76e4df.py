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
import json

class ItineraryPlanner:
    """
    A simple itinerary planner for a travel agency offering customized trips to destinations in Mexico.
    """

    def __init__(self):
        # Initialize destinations and activities database
        self.destinations = {
            "Cancun": ["Beach day", "Snorkeling", "Visit Mayan ruins"],
            "Mexico City": ["City tour", "Museum visit", "Food tasting"],
            "Guadalajara": ["Tequila tour", "Historic sites", "Mariachi experience"],
            "Oaxaca": ["Cultural tour", "Cooking class", "Visit Monte Albán"],
        }

    def display_destinations(self):
        """
        Display available destinations to the user.
        """
        print("Available destinations:")
        for destination in self.destinations:
            print(f"- {destination}")

    def get_activities(self, destination):
        """
        Get available activities for a given destination.
        :param destination: str - Name of the destination
        :return: list - List of activities
        """
        return self.destinations.get(destination, [])

    def create_itinerary(self):
        """
        Create a customized itinerary based on user input.
        """
        try:
            # Display destinations
            self.display_destinations()

            # Get user-selected destination
            destination = input("\nEnter your chosen destination: ").strip()
            if destination not in self.destinations:
                raise ValueError("Invalid destination selected. Please choose from the available options.")

            # Display activities for the selected destination
            activities = self.get_activities(destination)
            print(f"\nAvailable activities in {destination}:")
            for idx, activity in enumerate(activities, start=1):
                print(f"{idx}. {activity}")

            # Get user-selected activities
            selected_activities = input("\nEnter the numbers of the activities you'd like to include (comma-separated): ").strip()
            activity_indices = [int(i) - 1 for i in selected_activities.split(",")]

            # Validate activity indices
            if any(idx < 0 or idx >= len(activities) for idx in activity_indices):
                raise ValueError("Invalid activity selection. Please choose valid activity numbers.")

            # Generate itinerary
            itinerary = {
                "Destination": destination,
                "Activities": [activities[idx] for idx in activity_indices]
            }

            # Display and save itinerary
            print("\nYour customized itinerary:")
            print(json.dumps(itinerary, indent=4))

            # Save itinerary to a file
            with open("itinerary.json", "w") as file:
                json.dump(itinerary, file, indent=4)
            print("\nItinerary saved to 'itinerary.json'.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Main execution
if __name__ == "__main__":
    planner = ItineraryPlanner()
    planner.create_itinerary()
```
