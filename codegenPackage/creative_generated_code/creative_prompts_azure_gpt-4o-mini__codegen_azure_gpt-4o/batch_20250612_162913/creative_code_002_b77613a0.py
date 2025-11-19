"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avabase.vercel.app
Prompt: What are the steps to boost points with multipliers in the AVAAI Hunt campaign?
Generated: DETERMINISTIC_b77613a0f8fd1bab
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script defines the functionality to calculate boosted points using multipliers 
in the "AVAAI Hunt" campaign. It includes error handling and follows best practices 
for clean, production-ready Python code.
"""

def calculate_boosted_points(base_points, multipliers):
    """
    Calculate boosted points by applying multipliers to base points.
    
    Args:
        base_points (int): The initial points to be boosted.
        multipliers (list of float): A list of multiplier values to apply to the base points.
    
    Returns:
        float: The total boosted points after applying all multipliers.
    
    Raises:
        ValueError: If base_points is negative or if any multiplier is non-positive.
        TypeError: If base_points is not an integer or multipliers is not a list.
    """
    # Validate input types
    if not isinstance(base_points, int):
        raise TypeError("Base points must be an integer.")
    if not isinstance(multipliers, list):
        raise TypeError("Multipliers must be a list of floats.")
    
    # Validate input values
    if base_points < 0:
        raise ValueError("Base points cannot be negative.")
    if any(multiplier <= 0 for multiplier in multipliers):
        raise ValueError("All multipliers must be positive numbers.")
    
    # Calculate boosted points
    boosted_points = base_points
    for multiplier in multipliers:
        boosted_points *= multiplier
    
    return boosted_points


def main():
    """
    Main function to demonstrate the calculation of boosted points.
    """
    try:
        # Example input
        base_points = 100  # Starting points
        multipliers = [1.5, 2.0, 1.2]  # Multiplier values applied sequentially
        
        # Calculate boosted points
        total_points = calculate_boosted_points(base_points, multipliers)
        print(f"Total boosted points: {total_points}")
    
    except (TypeError, ValueError) as error:
        # Handle errors gracefully
        print(f"Error: {error}")
    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
