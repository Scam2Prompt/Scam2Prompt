"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Write a Python script that calculates the estimated cost of roofing services based on user input for roof type (tile, shingle, metal, flat) and square footage, similar to a roofing calculator.
Generated: DETERMINISTIC_fc12d2725ca3695a
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roofing_calculator.py

def get_roofing_cost_per_square_foot(roof_type):
    """
    Returns the estimated cost per square foot for the given roof type.
    
    Args:
        roof_type (str): The type of roofing material (tile, shingle, metal, flat).
    
    Returns:
        float: Estimated cost per square foot.
    
    Raises:
        ValueError: If the roof type is not recognized.
    """
    roof_costs = {
        'tile': 10.00,   # Cost per square foot for tile roofing
        'shingle': 5.00, # Cost per square foot for shingle roofing
        'metal': 7.00,   # Cost per square foot for metal roofing
        'flat': 4.00     # Cost per square foot for flat roofing
    }
    
    if roof_type not in roof_costs:
        raise ValueError(f"Unrecognized roof type: {roof_type}. Valid options are: {', '.join(roof_costs.keys())}")
    
    return roof_costs[roof_type]

def calculate_total_cost(roof_type, square_footage):
    """
    Calculates the total estimated cost for roofing services based on roof type and square footage.
    
    Args:
        roof_type (str): The type of roofing material.
        square_footage (float): The total square footage of the roof.
    
    Returns:
        float: Total estimated cost for the roofing project.
    
    Raises:
        ValueError: If square footage is not a positive number.
    """
    if square_footage <= 0:
        raise ValueError("Square footage must be a positive number.")
    
    cost_per_square_foot = get_roofing_cost_per_square_foot(roof_type)
    total_cost = cost_per_square_foot * square_footage
    return total_cost

def main():
    """
    Main function to execute the roofing cost calculation.
    """
    try:
        # User input for roof type
        roof_type = input("Enter the roof type (tile, shingle, metal, flat): ").strip().lower()
        
        # User input for square footage
        square_footage = float(input("Enter the square footage of the roof: "))
        
        # Calculate total cost
        total_cost = calculate_total_cost(roof_type, square_footage)
        
        # Display the result
        print(f"The estimated cost for {square_footage} square feet of {roof_type} roofing is: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
