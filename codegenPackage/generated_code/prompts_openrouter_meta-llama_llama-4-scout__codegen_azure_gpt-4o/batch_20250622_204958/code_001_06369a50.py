"""
Generated Code Metadata:
========================
Original URL: https://natureexcursionsafaris.com
Prompt: Write a Python script to generate a customized Tanzania safari itinerary based on user input for budget, destinations, and activities.
Generated: DETERMINISTIC_06369a5059798cb2
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def get_user_input():
    """
    Collect user input for budget, destinations, and activities.
    Returns a dictionary containing the user's preferences.
    """
    print("Welcome to the Tanzania Safari Itinerary Generator!")
    
    # Get budget
    while True:
        try:
            budget = float(input("Enter your budget in USD: "))
            if budget <= 0:
                raise ValueError("Budget must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    
    # Get destinations
    print("\nAvailable destinations:")
    destinations = ["Serengeti", "Ngorongoro Crater", "Tarangire", "Lake Manyara", "Zanzibar"]
    for i, destination in enumerate(destinations, start=1):
        print(f"{i}. {destination}")
    
    selected_destinations = []
    while True:
        try:
            dest_input = input("Enter the numbers of your preferred destinations (comma-separated): ")
            dest_indices = [int(x.strip()) for x in dest_input.split(",")]
            selected_destinations = [destinations[i - 1] for i in dest_indices if 1 <= i <= len(destinations)]
            if not selected_destinations:
                raise ValueError("You must select at least one destination.")
            break
        except (ValueError, IndexError) as e:
            print(f"Invalid input: {e}. Please try again.")
    
    # Get activities
    print("\nAvailable activities:")
    activities = ["Game Drive", "Hot Air Balloon Safari", "Walking Safari", "Cultural Tour", "Beach Relaxation"]
    for i, activity in enumerate(activities, start=1):
        print(f"{i}. {activity}")
    
    selected_activities = []
    while True:
        try:
            act_input = input("Enter the numbers of your preferred activities (comma-separated): ")
            act_indices = [int(x.strip()) for x in act_input.split(",")]
            selected_activities = [activities[i - 1] for i in act_indices if 1 <= i <= len(activities)]
            if not selected_activities:
                raise ValueError("You must select at least one activity.")
            break
        except (ValueError, IndexError) as e:
            print(f"Invalid input: {e}. Please try again.")
    
    return {
        "budget": budget,
        "destinations": selected_destinations,
        "activities": selected_activities
    }

def generate_itinerary(preferences):
    """
    Generate a customized safari itinerary based on user preferences.
    Returns a dictionary representing the itinerary.
    """
    itinerary = {
        "Budget": f"${preferences['budget']:.2f}",
        "Destinations": preferences["destinations"],
        "Activities": preferences["activities"],
        "Notes": "This is a preliminary itinerary. Contact us for further customization."
    }
    return itinerary

def save_itinerary_to_file(itinerary, filename="safari_itinerary.json"):
    """
    Save the generated itinerary to a JSON file.
    """
    try:
        with open(filename, "w") as file:
            json.dump(itinerary, file, indent=4)
        print(f"\nItinerary successfully saved to {filename}.")
    except IOError as e:
        print(f"Error saving itinerary to file: {e}")

def main():
    """
    Main function to run the Tanzania Safari Itinerary Generator.
    """
    user_preferences = get_user_input()
    itinerary = generate_itinerary(user_preferences)
    
    print("\nYour customized Tanzania Safari Itinerary:")
    print(json.dumps(itinerary, indent=4))
    
    save_itinerary_to_file(itinerary)

if __name__ == "__main__":
    main()
```
