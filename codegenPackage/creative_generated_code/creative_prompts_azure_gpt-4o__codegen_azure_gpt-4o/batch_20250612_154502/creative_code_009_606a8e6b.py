"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.traveloagency.com
Prompt: Generate a Python script to calculate the total cost of a round-trip flight, including adult, child, and infant fares, based on Traveloagency's passenger selection options.
Generated: DETERMINISTIC_606a8e6bcff162ab
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total cost of a round-trip flight based on passenger selection.
The calculation includes adult, child, and infant fares.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import required module for error handling
import sys

def calculate_total_cost(adult_count, child_count, infant_count, adult_fare, child_fare, infant_fare):
    """
    Calculate the total cost of a round-trip flight.

    Parameters:
    - adult_count (int): Number of adult passengers.
    - child_count (int): Number of child passengers.
    - infant_count (int): Number of infant passengers.
    - adult_fare (float): Fare for one adult passenger.
    - child_fare (float): Fare for one child passenger.
    - infant_fare (float): Fare for one infant passenger.

    Returns:
    - float: Total cost of the flight.
    """
    try:
        # Ensure all inputs are non-negative
        if any(x < 0 for x in [adult_count, child_count, infant_count, adult_fare, child_fare, infant_fare]):
            raise ValueError("All input values must be non-negative.")

        # Calculate total cost
        total_cost = (adult_count * adult_fare) + (child_count * child_fare) + (infant_count * infant_fare)
        return total_cost

    except TypeError:
        print("Error: All input values must be of the correct data type (integer for counts, float for fares).", file=sys.stderr)
        raise
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        raise

def main():
    """
    Main function to get user input and calculate the flight cost.
    """
    try:
        # Prompt user for input
        print("Enter the number of passengers:")
        adult_count = int(input("Number of adults: "))
        child_count = int(input("Number of children: "))
        infant_count = int(input("Number of infants: "))

        print("\nEnter the fare details (per person):")
        adult_fare = float(input("Adult fare: "))
        child_fare = float(input("Child fare: "))
        infant_fare = float(input("Infant fare: "))

        # Calculate total cost
        total_cost = calculate_total_cost(adult_count, child_count, infant_count, adult_fare, child_fare, infant_fare)

        # Display the result
        print(f"\nTotal cost of the round-trip flight: ${total_cost:.2f}")

    except ValueError:
        print("Error: Invalid input. Please ensure you enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
