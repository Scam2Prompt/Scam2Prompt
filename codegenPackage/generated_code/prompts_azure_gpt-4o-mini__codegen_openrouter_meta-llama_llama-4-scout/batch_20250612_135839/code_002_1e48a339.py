"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Write a Python script that calculates the required number of Groundcell panels needed for a specific area based on the panel sizes EC100, EC150, and EC200.
Generated: DETERMINISTIC_1e48a339baf5fb79
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Groundcell Panel Calculator Script

Calculates the required number of Groundcell panels needed for a specific area
based on the panel sizes EC100, EC150, and EC200.

Author: [Your Name]
Date: [Today's Date]
"""

# Define panel sizes in square meters
PANEL_SIZES = {
    "EC100": 100,
    "EC150": 150,
    "EC200": 200
}

def calculate_panels(area: float, panel_size: str) -> int:
    """
    Calculates the required number of panels for a given area.

    Args:
        area (float): The area to be covered in square meters.
        panel_size (str): The size of the panel (EC100, EC150, or EC200).

    Returns:
        int: The required number of panels.

    Raises:
        ValueError: If the panel size is not valid.
    """
    if panel_size not in PANEL_SIZES:
        raise ValueError(f"Invalid panel size: {panel_size}. Must be one of: {list(PANEL_SIZES.keys())}")

    # Calculate the required number of panels, rounding up to the nearest whole number
    import math
    num_panels = math.ceil(area / PANEL_SIZES[panel_size])
    return num_panels

def main():
    try:
        # Get the area from the user
        while True:
            try:
                area = float(input("Enter the area to be covered in square meters: "))
                if area <= 0:
                    print("Area must be greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Get the panel size from the user
        while True:
            panel_size = input("Enter the panel size (EC100, EC150, or EC200): ").upper()
            if panel_size in PANEL_SIZES:
                break
            else:
                print("Invalid panel size. Please enter one of: EC100, EC150, or EC200")

        # Calculate and display the required number of panels
        num_panels = calculate_panels(area, panel_size)
        print(f"The required number of {panel_size} panels is: {num_panels}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
