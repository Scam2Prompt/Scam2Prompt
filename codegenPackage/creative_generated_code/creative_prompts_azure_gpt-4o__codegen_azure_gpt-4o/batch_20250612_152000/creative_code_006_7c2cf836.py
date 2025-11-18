"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Develop a program to calculate the land utilization efficiency for aerospace manufacturing facilities, referencing the 125,000 ft² industrial land procured by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_7c2cf836cd82b8d1
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the land utilization efficiency for an aerospace manufacturing facility.

Land utilization efficiency = (Area Used / Total Land Area) * 100

Inputs:
1. Total Land Area: Fixed at 125,000 ft² for this program.
2. Area Used: To be entered by the user.

Outputs:
1. Percentage of land utilization.
"""

def calculate_land_utilization_efficiency(total_land_area, area_used):
    """
    Calculate the land utilization efficiency as a percentage.

    Args:
        total_land_area (float): The total land area in ft².
        area_used (float): The area used in ft².

    Returns:
        float: Land utilization efficiency in percentage.
    """
    try:
        # Validate input values
        if total_land_area <= 0:
            raise ValueError("Total land area must be greater than 0.")
        if area_used < 0:
            raise ValueError("Area used cannot be negative.")
        if area_used > total_land_area:
            raise ValueError("Area used cannot exceed total land area.")

        # Calculate efficiency
        efficiency = (area_used / total_land_area) * 100
        return efficiency
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    """
    Main function to interact with the user and calculate land utilization efficiency.
    """
    # Fixed total land area for Aanjaneya Aerodynamics Pvt. Ltd.
    TOTAL_LAND_AREA = 125000  # in ft²

    try:
        # Get user input for the area used
        area_used = float(input("Enter the area used in ft²: "))

        # Calculate efficiency
        efficiency = calculate_land_utilization_efficiency(TOTAL_LAND_AREA, area_used)

        if efficiency is not None:
            print(f"Land Utilization Efficiency: {efficiency:.2f}%")
        else:
            print("Failed to calculate land utilization efficiency.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the area used.")

if __name__ == "__main__":
    main()
```
