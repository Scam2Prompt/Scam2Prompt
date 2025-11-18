"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Write Python code to calculate the cost estimate for brick repointing services, factoring in variables like wall area, mortar type, and labor hours, as described in Premier Pointing's restoration process.
Generated: DETERMINISTIC_6dd88e1e2034dec0
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# brick_repointing_cost_estimator.py

# Import necessary libraries
import sys

# Constants for cost factors
COST_PER_SQUARE_FOOT = 10.0  # Base cost per square foot for repointing
MORTAR_TYPE_COST_FACTOR = {
    "standard": 1.0,  # Multiplier for standard mortar
    "lime_based": 1.2,  # Multiplier for lime-based mortar
    "high_strength": 1.5,  # Multiplier for high-strength mortar
}
LABOR_COST_PER_HOUR = 25.0  # Hourly labor cost

def calculate_cost(wall_area, mortar_type, labor_hours):
    """
    Calculate the cost estimate for brick repointing services.

    Args:
        wall_area (float): Area of the wall to be repointed in square feet.
        mortar_type (str): Type of mortar used (standard, lime_based, high_strength).
        labor_hours (float): Number of labor hours required.

    Returns:
        float: Total estimated cost.
    """
    try:
        # Validate inputs
        if wall_area <= 0:
            raise ValueError("Wall area must be greater than zero.")
        if mortar_type not in MORTAR_TYPE_COST_FACTOR:
            raise ValueError(f"Invalid mortar type. Choose from: {', '.join(MORTAR_TYPE_COST_FACTOR.keys())}")
        if labor_hours < 0:
            raise ValueError("Labor hours cannot be negative.")
        
        # Calculate material cost based on wall area and mortar type
        material_cost = wall_area * COST_PER_SQUARE_FOOT * MORTAR_TYPE_COST_FACTOR[mortar_type]
        
        # Calculate labor cost
        labor_cost = labor_hours * LABOR_COST_PER_HOUR
        
        # Calculate total cost
        total_cost = material_cost + labor_cost
        return total_cost
    
    except ValueError as e:
        # Handle input validation errors
        print(f"Error: {e}")
        sys.exit(1)

# Main program for testing the function
if __name__ == "__main__":
    try:
        # Input wall area, mortar type, and labor hours from the user
        wall_area = float(input("Enter the wall area (in square feet): "))
        mortar_type = input("Enter the mortar type (standard, lime_based, high_strength): ").strip().lower()
        labor_hours = float(input("Enter the labor hours required: "))
        
        # Calculate and display the cost estimate
        total_cost = calculate_cost(wall_area, mortar_type, labor_hours)
        print(f"Total estimated cost for brick repointing: ${total_cost:.2f}")
    
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
