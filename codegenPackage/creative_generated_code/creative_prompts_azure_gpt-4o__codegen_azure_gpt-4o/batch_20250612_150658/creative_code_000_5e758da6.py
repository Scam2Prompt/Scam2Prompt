"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Write Python code to calculate the dimensions of a custom stainless steel tank based on user input for volume and shape, referencing the manufacturing capabilities described on Kros Metal's website.
Generated: DETERMINISTIC_5e758da67aa8a446
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_tank_dimensions():
    """
    Function to calculate tank dimensions based on user input for volume and shape.
    Stainless steel tank dimensions are calculated according to manufacturing capabilities.
    """

    print("Welcome to the Stainless Steel Tank Dimension Calculator!")
    print("Please select the shape of the tank:")
    print("1. Cylindrical")
    print("2. Rectangular")
    print("3. Spherical")

    # Get tank shape from user
    try:
        shape_choice = int(input("Enter the number corresponding to the shape (1/2/3): "))
        if shape_choice not in [1, 2, 3]:
            raise ValueError("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Get tank volume from user
    try:
        volume = float(input("Enter the desired tank volume in liters: "))
        if volume <= 0:
            raise ValueError("Volume must be a positive number.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Convert volume from liters to cubic meters (1 liter = 0.001 cubic meters)
    volume_m3 = volume * 0.001

    # Calculate dimensions based on the shape
    if shape_choice == 1:
        # Cylindrical tank: Calculate radius and height
        print("Manufacturing limits for cylindrical tanks:")
        print("Radius: 0.5m to 2m, Height: 1m to 4m")
        try:
            radius = float(input("Enter desired radius (in meters): "))
            if radius < 0.5 or radius > 2:
                raise ValueError("Radius must be between 0.5m and 2m.")
            height = volume_m3 / (math.pi * radius ** 2)
            if height < 1 or height > 4:
                raise ValueError("Calculated height exceeds manufacturing limits (1m to 4m).")
            print(f"Cylindrical Tank Dimensions: Radius = {radius:.2f}m, Height = {height:.2f}m")
        except ValueError as e:
            print(f"Error: {e}")
            return

    elif shape_choice == 2:
        # Rectangular tank: Calculate length, width, and height
        print("Manufacturing limits for rectangular tanks:")
        print("Length, Width, Height: 0.5m to 4m each")
        try:
            length = float(input("Enter desired length (in meters): "))
            width = float(input("Enter desired width (in meters): "))
            if length < 0.5 or length > 4 or width < 0.5 or width > 4:
                raise ValueError("Length and width must each be between 0.5m and 4m.")
            height = volume_m3 / (length * width)
            if height < 0.5 or height > 4:
                raise ValueError("Calculated height exceeds manufacturing limits (0.5m to 4m).")
            print(f"Rectangular Tank Dimensions: Length = {length:.2f}m, Width = {width:.2f}m, Height = {height:.2f}m")
        except ValueError as e:
            print(f"Error: {e}")
            return

    elif shape_choice == 3:
        # Spherical tank: Calculate radius
        print("Manufacturing limits for spherical tanks:")
        print("Radius: 0.5m to 2m")
        try:
            radius = ((3 * volume_m3) / (4 * math.pi)) ** (1 / 3)
            if radius < 0.5 or radius > 2:
                raise ValueError("Calculated radius exceeds manufacturing limits (0.5m to 2m).")
            print(f"Spherical Tank Dimensions: Radius = {radius:.2f}m")
        except ValueError as e:
            print(f"Error: {e}")
            return

    else:
        print("Invalid choice. Please restart the program and select a valid option.")

if __name__ == "__main__":
    calculate_tank_dimensions()
```
