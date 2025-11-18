"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Generate a Python script to calculate the optimal cooler size (in quarts) for a camping trip, using Engel Coolers' specifications for ice retention and storage capacity.
Generated: DETERMINISTIC_1a33886cae505b61
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_cooler_size(num_people, num_days, avg_temp):
    """
    Calculate the optimal cooler size for a camping trip based on number of people,
    days of the trip, and average temperature.
    
    Parameters:
        num_people (int): Number of people on the trip.
        num_days (int): Number of days for the camping trip.
        avg_temp (float): Average temperature during the camping trip in Fahrenheit.
    
    Returns:
        float: Recommended cooler size in quarts.
    """
    
    # Engel Coolers specifications (Approximate values)
    ICE_RETENTION_PER_DAY = {
        "low": 2,  # Coolers retain ice better in low temps (<70°F)
        "medium": 1.5,  # Medium temps (70°F - 85°F)
        "high": 1  # Low ice retention in high temps (>85°F)
    }
    ICE_PER_PERSON_PER_DAY = 1.5  # Approximate quarts of ice needed per person per day
    FOOD_STORAGE_PER_PERSON_PER_DAY = 2  # Approximate quarts of food storage needed per person per day

    # Determine ice retention factor based on temperature
    if avg_temp < 70:
        ice_retention_factor = ICE_RETENTION_PER_DAY["low"]
    elif 70 <= avg_temp <= 85:
        ice_retention_factor = ICE_RETENTION_PER_DAY["medium"]
    else:
        ice_retention_factor = ICE_RETENTION_PER_DAY["high"]

    try:
        # Calculate total ice needed
        ice_needed = num_people * num_days * ICE_PER_PERSON_PER_DAY

        # Adjust ice needed based on retention factor
        total_ice_capacity = ice_needed / ice_retention_factor

        # Calculate total food storage capacity needed
        food_storage_capacity = num_people * num_days * FOOD_STORAGE_PER_PERSON_PER_DAY

        # Calculate optimal cooler size (sum of ice + food storage requirements)
        optimal_cooler_size = total_ice_capacity + food_storage_capacity

        # Return rounded up cooler size to the nearest quart
        return math.ceil(optimal_cooler_size)
    
    except Exception as e:
        print(f"Error calculating cooler size: {e}")
        return None


if __name__ == "__main__":
    # Gather user input
    try:
        print("Welcome to the Camping Cooler Size Calculator!")
        num_people = int(input("Enter the number of people attending the camping trip: "))
        num_days = int(input("Enter the number of days for the camping trip: "))
        avg_temp = float(input("Enter the average temperature during the trip (°F): "))

        # Validate input
        if num_people <= 0 or num_days <= 0 or avg_temp <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate and display cooler size
        cooler_size = calculate_cooler_size(num_people, num_days, avg_temp)
        if cooler_size:
            print(f"\nRecommended cooler size for your trip: {cooler_size} quarts")
        else:
            print("\nUnable to calculate cooler size. Please try again.")
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
