"""
Generated Code Metadata:
========================
Original URL: https://vidrosdu.blogspot.com
Prompt: Generate code for a simple calculator to determine the correct glass size for a given installation location, considering factors like frame size and glass type.
Generated: DETERMINISTIC_72a5333cec874727
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# glass_calculator.py

# Import necessary modules
import sys

# Define constants for glass types and their thickness
GLASS_TYPES = {
    "standard": 4,  # Standard glass thickness in mm
    "tempered": 6,  # Tempered glass thickness in mm
    "laminated": 8  # Laminated glass thickness in mm
}

def calculate_glass_size(frame_width, frame_height, glass_type):
    """
    Calculate the glass size based on frame dimensions and glass type.

    Args:
        frame_width (float): Width of the frame in mm.
        frame_height (float): Height of the frame in mm.
        glass_type (str): Type of glass (standard, tempered, laminated).

    Returns:
        dict: A dictionary containing the glass width, height, and thickness.
    """
    # Validate glass type
    if glass_type not in GLASS_TYPES:
        raise ValueError(f"Invalid glass type '{glass_type}'. Valid types are: {', '.join(GLASS_TYPES.keys())}")

    # Subtract a small margin (e.g., 5 mm) for fitting the glass into the frame
    margin = 5
    glass_width = frame_width - margin
    glass_height = frame_height - margin
    glass_thickness = GLASS_TYPES[glass_type]

    # Ensure dimensions are positive
    if glass_width <= 0 or glass_height <= 0:
        raise ValueError("Frame dimensions are too small to fit the glass.")

    return {
        "width": glass_width,
        "height": glass_height,
        "thickness": glass_thickness
    }

def main():
    """
    Main function to interact with the user and calculate glass size.
    """
    try:
        # Get user input for frame dimensions and glass type
        frame_width = float(input("Enter the frame width (in mm): "))
        frame_height = float(input("Enter the frame height (in mm): "))
        glass_type = input("Enter the glass type (standard, tempered, laminated): ").strip().lower()

        # Calculate glass size
        glass_size = calculate_glass_size(frame_width, frame_height, glass_type)

        # Display the result
        print("\nCalculated Glass Size:")
        print(f"Width: {glass_size['width']} mm")
        print(f"Height: {glass_size['height']} mm")
        print(f"Thickness: {glass_size['thickness']} mm")

    except ValueError as ve:
        # Handle invalid input or calculation errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Glass Size Calculator.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
