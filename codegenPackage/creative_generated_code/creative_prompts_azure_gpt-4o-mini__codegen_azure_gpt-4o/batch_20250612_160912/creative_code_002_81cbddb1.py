"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Write a code snippet to calculate the total cost for a family tour package from Chennai to Kodaikanal using the pricing details from Balaji Tours and Travels.
Generated: DETERMINISTIC_81cbddb1663e65db
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# TourCostCalculator.py

# Import necessary modules
import sys

def calculate_tour_cost(num_adults, num_children, is_peak_season):
    """
    Calculate the total cost of a family tour package based on the number
    of adults and children, and whether it is peak season.
    
    Pricing Details:
    - Adults: ₹2000 per person (regular), ₹2500 per person (peak season)
    - Children: ₹1500 per person (regular), ₹2000 per person (peak season)
    - Transportation: ₹5000 (fixed cost)
    - Accommodation: ₹8000 (fixed cost)
    
    Args:
        num_adults (int): Number of adults in the family.
        num_children (int): Number of children in the family.
        is_peak_season (bool): True if traveling during peak season, False otherwise.
    
    Returns:
        float: Total cost of the tour package.
    """
    
    try:
        # Validate inputs
        if num_adults < 0 or num_children < 0:
            raise ValueError("Number of adults and children cannot be negative.")
        
        # Pricing constants
        ADULT_COST_REGULAR = 2000
        ADULT_COST_PEAK = 2500
        CHILD_COST_REGULAR = 1500
        CHILD_COST_PEAK = 2000
        TRANSPORTATION_COST = 5000
        ACCOMMODATION_COST = 8000

        # Determine pricing based on season
        adult_cost = ADULT_COST_PEAK if is_peak_season else ADULT_COST_REGULAR
        child_cost = CHILD_COST_PEAK if is_peak_season else CHILD_COST_REGULAR

        # Calculate total cost
        total_adult_cost = num_adults * adult_cost
        total_child_cost = num_children * child_cost
        total_cost = total_adult_cost + total_child_cost + TRANSPORTATION_COST + ACCOMMODATION_COST

        return total_cost

    except ValueError as e:
        # Handle input validation errors
        print(f"Error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

# Main function to demonstrate the usage of the calculator
if __name__ == "__main__":
    # Example inputs
    num_adults = 2
    num_children = 2
    is_peak_season = True

    # Calculate total cost
    tour_cost = calculate_tour_cost(num_adults, num_children, is_peak_season)

    # Display result
    if tour_cost is not None:
        print(f"Total cost for the family tour package: ₹{tour_cost}")
    else:
        print("Failed to calculate the tour cost due to an error.")
```
