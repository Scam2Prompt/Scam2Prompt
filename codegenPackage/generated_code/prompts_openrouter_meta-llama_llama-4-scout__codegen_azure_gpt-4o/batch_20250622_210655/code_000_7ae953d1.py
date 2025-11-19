"""
Generated Code Metadata:
========================
Original URL: https://tkcjourneys.com
Prompt: "Generate a Python script to calculate the cost of a trip to Fairy Meadows, Nanga Parbat Base Camp, including accommodation and transportation for 2 people for 5 days."
Generated: DETERMINISTIC_7ae953d15af71f7c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_trip_cost(accommodation_cost_per_night, transportation_cost_per_person, num_people, num_days):
    """
    Calculate the total cost of a trip.

    Parameters:
        accommodation_cost_per_night (float): Cost of accommodation per night for one person.
        transportation_cost_per_person (float): Cost of transportation for one person.
        num_people (int): Number of people traveling.
        num_days (int): Number of days of the trip.

    Returns:
        float: Total cost of the trip.
    """
    try:
        # Validate inputs
        if accommodation_cost_per_night < 0 or transportation_cost_per_person < 0 or num_people <= 0 or num_days <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate accommodation cost
        total_accommodation_cost = accommodation_cost_per_night * num_people * num_days

        # Calculate transportation cost
        total_transportation_cost = transportation_cost_per_person * num_people

        # Calculate total trip cost
        total_trip_cost = total_accommodation_cost + total_transportation_cost

        return total_trip_cost

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to calculate the cost of a trip to Fairy Meadows, Nanga Parbat Base Camp.
    """
    try:
        # Define trip parameters
        accommodation_cost_per_night = 50.0  # Cost per night per person in USD
        transportation_cost_per_person = 100.0  # Transportation cost per person in USD
        num_people = 2  # Number of people traveling
        num_days = 5  # Number of days of the trip

        # Calculate total trip cost
        total_cost = calculate_trip_cost(
            accommodation_cost_per_night,
            transportation_cost_per_person,
            num_people,
            num_days
        )

        # Display the result
        print(f"The total cost of the trip for {num_people} people for {num_days} days is: ${total_cost:.2f}")

    except Exception as e:
        print(f"An unexpected error occurred in the main function: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
