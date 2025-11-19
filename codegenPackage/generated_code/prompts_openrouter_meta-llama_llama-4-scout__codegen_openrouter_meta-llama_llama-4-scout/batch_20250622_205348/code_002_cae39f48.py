"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: "Write a Python script to calculate the required Groundcell panels for a given area, considering different sizes (EC100, EC150, EC200) and panel dimensions (4m x 6m)."
Generated: DETERMINISTIC_cae39f4845673588
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# groundcell_calculator.py

"""
Calculates the required Groundcell panels for a given area.

Supports different panel sizes: EC100, EC150, EC200
with standard panel dimensions: 4m x 6m
"""

import math

# Define panel sizes and their corresponding areas
PANEL_SIZES = {
    "EC100": 100,
    "EC150": 150,
    "EC200": 200
}

# Define standard panel dimensions
PANEL_WIDTH = 4  # meters
PANEL_LENGTH = 6  # meters

def calculate_panel_area(panel_size):
    """
    Calculate the area of a single panel.

    Args:
        panel_size (str): The size of the panel (EC100, EC150, EC200)

    Returns:
        float: The area of a single panel

    Raises:
        ValueError: If the panel size is not supported
    """
    if panel_size not in PANEL_SIZES:
        raise ValueError(f"Unsupported panel size: {panel_size}")

    # Assume the panel area is equal to its size (in m²)
    return PANEL_WIDTH * PANEL_LENGTH  # m²

def calculate_required_panels(area, panel_size):
    """
    Calculate the required number of panels for a given area.

    Args:
        area (float): The area to cover (in m²)
        panel_size (str): The size of the panels (EC100, EC150, EC200)

    Returns:
        int: The required number of panels

    Raises:
        ValueError: If the area or panel size is invalid
    """
    if area <= 0:
        raise ValueError("Area must be greater than zero")

    panel_area = calculate_panel_area(panel_size)
    required_panels = math.ceil(area / panel_area)

    return required_panels

def main():
    try:
        area = float(input("Enter the area to cover (m²): "))
        panel_size = input("Enter the panel size (EC100, EC150, EC200): ")

        required_panels = calculate_required_panels(area, panel_size)
        print(f"Required panels: {required_panels}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
