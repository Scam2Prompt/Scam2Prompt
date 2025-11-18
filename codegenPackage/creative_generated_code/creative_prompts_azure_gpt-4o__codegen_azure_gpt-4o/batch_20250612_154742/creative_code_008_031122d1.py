"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Create a Python script to calculate the total cost of a Rajasthan tour package, including transportation costs based on tempo traveler rates provided on the "Best Holidays All India" website.
Generated: DETERMINISTIC_031122d1121d40f5
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_transportation_cost(distance_km, rate_per_km):
    """
    Calculate transportation cost based on distance and rate per kilometer.

    :param distance_km: Total distance to be traveled in kilometers (int or float)
    :param rate_per_km: Rate per kilometer for the vehicle (int or float)
    :return: Transportation cost (float)
    """
    try:
        if distance_km < 0 or rate_per_km < 0:
            raise ValueError("Distance and rate per km must be non-negative.")
        return distance_km * rate_per_km
    except TypeError:
        raise TypeError("Both distance_km and rate_per_km must be numbers.")

def calculate_total_cost(transportation_cost, accommodation_cost, food_cost, sightseeing_cost):
    """
    Calculate the total cost of the Rajasthan tour package.

    :param transportation_cost: Cost of transportation (float)
    :param accommodation_cost: Cost of accommodations (float)
    :param food_cost: Cost of food (float)
    :param sightseeing_cost: Cost of sightseeing (float)
    :return: Total tour package cost (float)
    """
    try:
        if any(cost < 0 for cost in [transportation_cost, accommodation_cost, food_cost, sightseeing_cost]):
            raise ValueError("All cost components must be non-negative.")
        return transportation_cost + accommodation_cost + food_cost + sightseeing_cost
    except TypeError:
        raise TypeError("All cost components must be numbers.")

def main():
    """
    Main function to calculate the total cost of a Rajasthan tour package.
    """
    try:
        # Input values for the tour package (replace these with actual inputs or calculations as required)
        distance = float(input("Enter the total distance to be traveled (in km): "))
        rate_per_km = float(input("Enter the rate per km for the tempo traveler: "))
        accommodation_cost = float(input("Enter the total accommodation cost: "))
        food_cost = float(input("Enter the total food cost: "))
        sightseeing_cost = float(input("Enter the total sightseeing cost: "))

        # Calculate transportation cost
        transportation_cost = calculate_transportation_cost(distance, rate_per_km)

        # Calculate total cost
        total_cost = calculate_total_cost(transportation_cost, accommodation_cost, food_cost, sightseeing_cost)

        # Output the total cost
        print(f"\nTotal Rajasthan Tour Package Cost: ₹{total_cost:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
