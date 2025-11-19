"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Generate a Python script to calculate the optimal cooler size for a camping trip based on the Engel Coolers product line.
Generated: DETERMINISTIC_cc921f6640a3becf
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_cooler_size(number_of_people, days, meals_per_day, extra_space_factor=0.2):
    """
    Calculate the optimal cooler size for a camping trip based on number of people, days, and meals.
    
    Parameters:
        number_of_people (int): Number of people going on the trip.
        days (int): Number of days for the camping trip.
        meals_per_day (int): Number of meals per person per day.
        extra_space_factor (float): Additional space factor for drinks, ice, and miscellaneous items (default is 0.2).
        
    Returns:
        float: Suggested cooler size in quarts.
    """
    try:
        # Sanity check for input values
        if number_of_people <= 0 or days <= 0 or meals_per_day <= 0:
            raise ValueError("Number of people, days, and meals per day must all be positive integers.")
        
        # Average space required per meal (approximate value in quarts)
        space_per_meal = 0.75  # Adjust based on Engel Cooler guidelines or user preference
        
        # Total food space required
        total_food_space = number_of_people * days * meals_per_day * space_per_meal
        
        # Include extra space for drinks, ice, and miscellaneous items
        total_space_with_extra = total_food_space * (1 + extra_space_factor)
        
        # Round up to nearest whole number for practical cooler sizing
        suggested_cooler_size = math.ceil(total_space_with_extra)
        
        return suggested_cooler_size
    
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


def main():
    """
    Main function to interactively calculate cooler size for camping trip.
    """
    print("Welcome to the Engel Coolers Size Calculator!")
    try:
        # Gather user input
        number_of_people = int(input("Enter the number of people going on the trip: "))
        days = int(input("Enter the number of days for the camping trip: "))
        meals_per_day = int(input("Enter the number of meals per person per day: "))
        extra_space_factor = float(input("Enter extra space factor (default is 0.2): ") or 0.2)
        
        # Calculate cooler size
        suggested_size = calculate_cooler_size(number_of_people, days, meals_per_day, extra_space_factor)
        
        # Display result
        print(f"\nBased on your inputs, the suggested cooler size is: {suggested_size} quarts.")
        print("Explore Engel Coolers product line to find a cooler matching this size!")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
```
