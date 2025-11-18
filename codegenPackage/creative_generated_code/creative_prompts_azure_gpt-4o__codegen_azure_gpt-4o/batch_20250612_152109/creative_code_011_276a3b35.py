"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Generate a Python script to calculate the space efficiency of UDIZINE's floor-to-ceiling retail wall display systems for small retail spaces.
Generated: DETERMINISTIC_276a3b35a76d2435
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_space_efficiency(total_wall_area, used_wall_area):
    """
    Calculate the space efficiency of a floor-to-ceiling retail wall display system.

    Parameters:
        total_wall_area (float): The total area of the wall space in square feet.
        used_wall_area (float): The area of the wall space utilized for display in square feet.

    Returns:
        float: The space efficiency as a percentage.
    """
    try:
        # Validate inputs
        if total_wall_area <= 0:
            raise ValueError("Total wall area must be greater than zero.")
        if used_wall_area < 0:
            raise ValueError("Used wall area cannot be negative.")
        if used_wall_area > total_wall_area:
            raise ValueError("Used wall area cannot exceed total wall area.")

        # Calculate and return efficiency percentage
        efficiency = (used_wall_area / total_wall_area) * 100
        return round(efficiency, 2)
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)

def main():
    """
    Main function to interactively calculate the space efficiency of UDIZINE's retail wall systems.
    """
    print("Welcome to the UDIZINE Space Efficiency Calculator!")
    try:
        # Get user inputs
        total_wall_area = float(input("Enter the total wall area in square feet: "))
        used_wall_area = float(input("Enter the used wall area in square feet: "))

        # Calculate space efficiency
        efficiency = calculate_space_efficiency(total_wall_area, used_wall_area)
        print(f"The space efficiency of the display system is {efficiency}%.")
    except ValueError:
        print("Error: Please enter valid numerical values for the wall areas.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
