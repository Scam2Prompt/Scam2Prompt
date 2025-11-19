"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.punpuntoy.com
Prompt: Develop a code snippet that calculates the optimal layout for a preschool playground using PunPun's design guidelines.
Generated: DETERMINISTIC_12bc086b477b33d7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_playground_layout(area, num_zones, min_zone_area):
    """
    Calculate the optimal layout for a preschool playground based on given guidelines.

    Parameters:
    - area (float): Total area of the playground in square meters.
    - num_zones (int): Number of zones to divide the playground into.
    - min_zone_area (float): Minimum area per zone in square meters.

    Returns:
    - dict: A dictionary containing the dimensions and area of each zone.
    """

    # Input validation
    if area <= 0 or num_zones <= 0 or min_zone_area <= 0:
        raise ValueError("All input values must be positive and non-zero.")
    
    if min_zone_area * num_zones > area:
        raise ValueError("The total area is insufficient to meet the minimum zone area requirements.")

    # Calculate the optimal layout
    zone_area = area / num_zones  # Equal area allocation per zone
    zone_width = math.sqrt(zone_area)  # Assuming square zones for simplicity
    zone_height = zone_width  # Square shape ensures optimal use of space

    # Prepare layout details
    layout = {}
    for i in range(1, num_zones + 1):
        layout[f"Zone {i}"] = {
            "Width (m)": round(zone_width, 2),
            "Height (m)": round(zone_height, 2),
            "Area (m²)": round(zone_area, 2)
        }

    return layout


def main():
    """
    Main function to execute the playground layout calculation.
    """
    try:
        # Example input for playground parameters
        total_area = 500  # Total playground area in square meters
        number_of_zones = 5  # Number of zones in the playground
        minimum_zone_area = 50  # Minimum area per zone in square meters

        # Calculate the layout
        optimal_layout = calculate_playground_layout(total_area, number_of_zones, minimum_zone_area)
        
        # Print the results
        print("Optimal Playground Layout:")
        for zone, details in optimal_layout.items():
            print(f"{zone}: {details}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    main()
```
