"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifesty.com.br
Prompt: What are the steps to calculate the amount of food and drinks needed for an event, as suggested by Ifesty's blog?
Generated: DETERMINISTIC_92ba7ac18446796c
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
Event Food and Drink Calculator

This script calculates the amount of food and drinks needed for an event based on the number
of attendees and the duration of the event. The algorithm is inspired by guidelines from Ifesty's blog.

Key assumptions:
1. Food is calculated based on a per-person-per-hour basis.
2. Drinks are calculated based on a per-person-per-hour basis with adjustments for alcohol/non-alcohol preferences.
3. Configurations are adjustable for different event types.
"""

# Import necessary libraries
import math

# Constants (modifiable based on event type or preferences)
FOOD_PER_PERSON_PER_HOUR = 0.5  # kilograms of food per person per hour
DRINKS_PER_PERSON_PER_HOUR = 1  # liters of drinks per person per hour
ALCOHOL_RATIO = 0.5  # Percentage of drinks that are alcoholic (50%)

def calculate_event_needs(attendees, duration_hours):
    """
    Calculates the total amount of food and drinks needed for an event.

    Args:
        attendees (int): Number of people attending the event.
        duration_hours (float): Duration of the event in hours.

    Returns:
        dict: A dictionary containing the total food and drink quantities.
    """
    try:
        # Validate inputs
        if attendees <= 0 or duration_hours <= 0:
            raise ValueError("Attendees and duration must be positive numbers.")

        # Calculate food requirements
        total_food = attendees * duration_hours * FOOD_PER_PERSON_PER_HOUR

        # Calculate drink requirements
        total_drinks = attendees * duration_hours * DRINKS_PER_PERSON_PER_HOUR
        alcoholic_drinks = total_drinks * ALCOHOL_RATIO
        non_alcoholic_drinks = total_drinks * (1 - ALCOHOL_RATIO)

        # Round quantities for practical purposes
        total_food = round(total_food, 2)
        alcoholic_drinks = round(alcoholic_drinks, 2)
        non_alcoholic_drinks = round(non_alcoholic_drinks, 2)

        return {
            "total_food_kg": total_food,
            "alcoholic_drinks_liters": alcoholic_drinks,
            "non_alcoholic_drinks_liters": non_alcoholic_drinks
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example Usage
if __name__ == "__main__":
    try:
        # Prompt user for input
        attendees = int(input("Enter the number of attendees: "))
        duration_hours = float(input("Enter the duration of the event (in hours): "))

        # Calculate requirements
        requirements = calculate_event_needs(attendees, duration_hours)

        if requirements:
            print("\nEvent Requirements:")
            print(f"Total Food: {requirements['total_food_kg']} kg")
            print(f"Alcoholic Drinks: {requirements['alcoholic_drinks_liters']} liters")
            print(f"Non-Alcoholic Drinks: {requirements['non_alcoholic_drinks_liters']} liters")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
