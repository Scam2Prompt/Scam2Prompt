"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Write a script to automate the process of generating quotes for tailored travel packages, specifically for adventure sports and wildlife safaris in Kenya.
Generated: DETERMINISTIC_2cda3e59ad14f913
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import datetime

# Constants for the travel package
DESTINATIONS = ["Maasai Mara", "Amboseli National Park", "Tsavo East", "Lake Nakuru"]
ADVENTURE_SPORTS = ["Hot Air Balloon Safari", "Mountain Climbing", "Zip Lining", "White Water Rafting"]
WILDLIFE_ACTIVITIES = ["Game Drive", "Bird Watching", "Nature Walk", "Night Safari"]
ACCOMMODATION_TYPES = ["Luxury Lodge", "Mid-range Camp", "Budget Tent"]
MEAL_PLANS = ["Full Board", "Half Board", "Bed & Breakfast"]

# Price ranges for different components
PRICE_RANGES = {
    "destination": {"min": 100, "max": 500},
    "adventure_sport": {"min": 50, "max": 200},
    "wildlife_activity": {"min": 30, "max": 150},
    "accommodation": {"min": 50, "max": 300},
    "meal_plan": {"min": 20, "max": 100},
}

# Error handling for invalid inputs
def validate_input(prompt, valid_options):
    """
    Validates user input against a list of valid options.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

# Function to generate a random price within a range
def generate_price(price_range):
    """
    Generates a random price within the given range.
    """
    return random.randint(price_range["min"], price_range["max"])

# Function to generate a tailored travel package quote
def generate_quote():
    """
    Generates a tailored travel package quote based on user preferences.
    """
    print("Welcome to Kenya Travel Package Generator!")
    
    # Get user preferences
    destination = validate_input(
        f"Choose a destination ({', '.join(DESTINATIONS)}): ", DESTINATIONS
    )
    adventure_sport = validate_input(
        f"Choose an adventure sport ({', '.join(ADVENTURE_SPORTS)}): ", ADVENTURE_SPORTS
    )
    wildlife_activity = validate_input(
        f"Choose a wildlife activity ({', '.join(WILDLIFE_ACTIVITIES)}): ", WILDLIFE_ACTIVITIES
    )
    accommodation = validate_input(
        f"Choose an accommodation type ({', '.join(ACCOMMODATION_TYPES)}): ", ACCOMMODATION_TYPES
    )
    meal_plan = validate_input(
        f"Choose a meal plan ({', '.join(MEAL_PLANS)}): ", MEAL_PLANS
    )
    
    # Generate prices for each component
    destination_price = generate_price(PRICE_RANGES["destination"])
    adventure_sport_price = generate_price(PRICE_RANGES["adventure_sport"])
    wildlife_activity_price = generate_price(PRICE_RANGES["wildlife_activity"])
    accommodation_price = generate_price(PRICE_RANGES["accommodation"])
    meal_plan_price = generate_price(PRICE_RANGES["meal_plan"])
    
    # Calculate total price
    total_price = (
        destination_price
        + adventure_sport_price
        + wildlife_activity_price
        + accommodation_price
        + meal_plan_price
    )
    
    # Generate quote details
    quote = {
        "destination": destination,
        "destination_price": destination_price,
        "adventure_sport": adventure_sport,
        "adventure_sport_price": adventure_sport_price,
        "wildlife_activity": wildlife_activity,
        "wildlife_activity_price": wildlife_activity_price,
        "accommodation": accommodation,
        "accommodation_price": accommodation_price,
        "meal_plan": meal_plan,
        "meal_plan_price": meal_plan_price,
        "total_price": total_price,
        "generated_on": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    
    # Display the quote
    print("\nYour tailored travel package quote:")
    print(json.dumps(quote, indent=4))
    
    # Save the quote to a file
    try:
        with open("travel_quote.json", "w") as file:
            json.dump(quote, file, indent=4)
        print("\nQuote saved to 'travel_quote.json'.")
    except Exception as e:
        print(f"Error saving quote to file: {e}")

# Main function to run the script
if __name__ == "__main__":
    try:
        generate_quote()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
