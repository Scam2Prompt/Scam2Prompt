"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hildeinox.com
Prompt: Develop a script to calculate the surface area of stainless steel sheets, using the specifications for "Paslanmaz Plaka / Levha" from Hilde Inox.
Generated: DETERMINISTIC_2c4c2981477741a5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the surface area of stainless steel sheets ("Paslanmaz Plaka / Levha").
The script takes dimensions (length, width) and quantity of sheets as input, and calculates 
the total surface area. Proper error handling and validations are included.
"""

def calculate_surface_area(length: float, width: float, quantity: int) -> float:
    """
    Calculate the total surface area of stainless steel sheets.

    Parameters:
    length (float): Length of the sheet (in meters).
    width (float): Width of the sheet (in meters).
    quantity (int): Number of sheets.

    Returns:
    float: Total surface area (in square meters).
    """
    # Validate input values
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    
    # Calculate surface area (length * width * quantity)
    return length * width * quantity


def main():
    """
    Main function to accept user input and calculate surface area.
    """
    print("Calculate Surface Area of Stainless Steel Sheets")
    print("Please provide the following dimensions in meters.")

    try:
        # Accept user input for dimensions and quantity
        length = float(input("Enter the length of the sheet (meters): "))
        width = float(input("Enter the width of the sheet (meters): "))
        quantity = int(input("Enter the quantity of sheets: "))

        # Calculate total surface area
        surface_area = calculate_surface_area(length, width, quantity)
        print(f"\nTotal Surface Area: {surface_area:.2f} square meters")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
