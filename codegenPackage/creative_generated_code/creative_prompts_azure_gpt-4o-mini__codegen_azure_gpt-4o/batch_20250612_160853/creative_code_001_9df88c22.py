"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.ilmaweb.com
Prompt: Write a function that calculates the total cost for a group tour package to Gunung Bromo, incorporating Jeep rental, catering, and accommodation from Budi Bromo Tour.
Generated: DETERMINISTIC_9df88c22918818e4
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List

# Define a function to calculate the total cost of a group tour package
def calculate_tour_cost(group_size: int, jeep_rental_cost: float, catering_cost_per_person: float, accommodation_cost_per_person: float) -> float:
    """
    Calculate the total cost for a group tour package to Gunung Bromo.

    Parameters:
    - group_size (int): Number of people in the group.
    - jeep_rental_cost (float): Fixed cost for the Jeep rental.
    - catering_cost_per_person (float): Cost for catering per person.
    - accommodation_cost_per_person (float): Cost for accommodation per person.

    Returns:
    - float: Total cost for the group tour package.

    Raises:
    - ValueError: If any input is non-positive or invalid.
    """
    # Input validation
    if group_size <= 0:
        raise ValueError("Group size must be greater than 0.")
    if jeep_rental_cost < 0 or catering_cost_per_person < 0 or accommodation_cost_per_person < 0:
        raise ValueError("Costs cannot be negative.")

    # Calculate total catering cost
    total_catering_cost = catering_cost_per_person * group_size

    # Calculate total accommodation cost
    total_accommodation_cost = accommodation_cost_per_person * group_size

    # Calculate total cost
    total_cost = jeep_rental_cost + total_catering_cost + total_accommodation_cost

    return total_cost


# Example usage
if __name__ == "__main__":
    try:
        # Inputs
        group_size = 5
        jeep_rental_cost = 500.0  # Fixed cost for Jeep rental
        catering_cost_per_person = 50.0  # Cost for catering per person
        accommodation_cost_per_person = 100.0  # Cost for accommodation per person

        # Calculate and print total cost
        total_cost = calculate_tour_cost(group_size, jeep_rental_cost, catering_cost_per_person, accommodation_cost_per_person)
        print(f"The total cost for the group tour package is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
