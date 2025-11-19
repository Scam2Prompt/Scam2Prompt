"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Generate a Python script to calculate the optimal tractor model for agricultural tasks based on user input, considering SCOUT's specifications and features.
Generated: DETERMINISTIC_bc19267b0aa81484
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate the optimal tractor model for agricultural tasks
based on user input, considering SCOUT's specifications and features.
"""

import sys

def get_user_input():
    """
    Collects user input for agricultural requirements.

    Returns:
        dict: A dictionary containing user preferences and task requirements.
    """
    print("Welcome to Tractor Selector!")
    try:
        task_type = input("Enter the type of agricultural task (e.g., plowing, harvesting, hauling): ").strip().lower()
        terrain_type = input("Enter the terrain type (e.g., flat, hilly, rocky): ").strip().lower()
        budget = float(input("Enter your budget (in USD): "))
        horsepower_required = int(input("Enter the minimum horsepower needed: "))
        fuel_efficiency_preference = input("Do you prioritize fuel efficiency? (yes/no): ").strip().lower()
        return {
            "task_type": task_type,
            "terrain_type": terrain_type,
            "budget": budget,
            "horsepower_required": horsepower_required,
            "fuel_efficiency_preference": fuel_efficiency_preference
        }
    except ValueError as ve:
        print(f"Error in input: {ve}")
        sys.exit(1)


def calculate_optimal_tractor(user_requirements, tractor_database):
    """
    Calculates the optimal tractor model from the given tractor database.

    Args:
        user_requirements (dict): User's agricultural requirements.
        tractor_database (list of dict): Available tractor models with specifications.

    Returns:
        dict: The optimal tractor model or None if no suitable model is found.
    """
    optimal_tractor = None

    for tractor in tractor_database:
        # Check budget
        if tractor['price'] > user_requirements['budget']:
            continue

        # Check horsepower
        if tractor['horsepower'] < user_requirements['horsepower_required']:
            continue

        # Check terrain compatibility
        if user_requirements['terrain_type'] not in tractor['terrain']:
            continue

        # Check fuel efficiency preference
        if user_requirements['fuel_efficiency_preference'] == 'yes' and not tractor['fuel_efficient']:
            continue

        # If a better match is found, update the optimal tractor
        if optimal_tractor is None or tractor['score'] > optimal_tractor['score']:
            optimal_tractor = tractor

    return optimal_tractor


def main():
    """
    Main program execution.
    """
    # Sample database of tractor models (mock data for demonstration purposes)
    tractor_database = [
        {
            "model": "SCOUT-X1",
            "price": 25000,
            "horsepower": 120,
            "terrain": ["flat", "hilly"],
            "fuel_efficient": True,
            "score": 90
        },
        {
            "model": "SCOUT-X2",
            "price": 30000,
            "horsepower": 150,
            "terrain": ["flat", "hilly", "rocky"],
            "fuel_efficient": False,
            "score": 85
        },
        {
            "model": "SCOUT-X3",
            "price": 20000,
            "horsepower": 100,
            "terrain": ["flat"],
            "fuel_efficient": True,
            "score": 70
        },
    ]

    # Get user input
    user_requirements = get_user_input()

    # Calculate optimal tractor
    optimal_tractor = calculate_optimal_tractor(user_requirements, tractor_database)

    # Display results
    if optimal_tractor:
        print("\nOptimal Tractor Found:")
        print(f"Model: {optimal_tractor['model']}")
        print(f"Price: ${optimal_tractor['price']}")
        print(f"Horsepower: {optimal_tractor['horsepower']} HP")
        print(f"Compatible Terrain: {', '.join(optimal_tractor['terrain'])}")
        print(f"Fuel Efficient: {'Yes' if optimal_tractor['fuel_efficient'] else 'No'}")
    else:
        print("\nNo suitable tractor model found within the given requirements.")


if __name__ == "__main__":
    main()
```
