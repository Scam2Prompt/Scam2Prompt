"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Develop a function that calculates the total cost for a 4-day safari tour in Ol Pejeta, including accommodation, meals, and park fees.
Generated: DETERMINISTIC_b4df901336cc8317
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from typing import Optional

def calculate_total_safari_cost(accommodation_cost_per_night: float, 
                                meals_cost_per_day: float, 
                                park_fees_per_day: float, 
                                number_of_days: int = 4) -> Optional[float]:
    """
    Calculates the total cost for a 4-day safari tour in Ol Pejeta.

    Parameters:
        accommodation_cost_per_night (float): Cost for accommodation per night.
        meals_cost_per_day (float): Cost for meals per day.
        park_fees_per_day (float): Park fees per day.
        number_of_days (int): Number of days for the safari tour. Default is 4.

    Returns:
        Optional[float]: Total cost of the safari tour. Returns None for invalid inputs.

    Raises:
        ValueError: If any input value is negative.
    """

    try:
        # Validate the inputs
        if accommodation_cost_per_night < 0 or meals_cost_per_day < 0 or park_fees_per_day < 0:
            raise ValueError("Costs and fees cannot be negative.")

        if number_of_days <= 0:
            raise ValueError("Number of days must be greater than zero.")

        # Calculate the total cost
        accommodation_total = accommodation_cost_per_night * number_of_days
        meals_total = meals_cost_per_day * number_of_days
        park_fees_total = park_fees_per_day * number_of_days
        total_cost = accommodation_total + meals_total + park_fees_total

        return total_cost

    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define costs
    accommodation_cost = 150.0  # Cost per night
    meals_cost = 50.0           # Cost per day
    park_fees = 40.0            # Cost per day

    # Calculate total cost
    total_safari_cost = calculate_total_safari_cost(accommodation_cost, meals_cost, park_fees)

    if total_safari_cost is not None:
        print(f"The total cost for the 4-day safari tour in Ol Pejeta is: ${total_safari_cost:.2f}")
    else:
        print("Failed to calculate the total cost due to invalid input.")
```
