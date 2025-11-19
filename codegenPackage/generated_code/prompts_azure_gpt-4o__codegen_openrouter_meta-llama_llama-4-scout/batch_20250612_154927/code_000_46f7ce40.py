"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Write a Python script to calculate the dimensions and area required for installing a Phantom oversized retractable screen, ensuring it fits openings up to 15 feet wide and 12 feet high.
Generated: DETERMINISTIC_46f7ce40d4b92f23
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Phantom Oversized Retractable Screen Installation Calculator

Calculates the dimensions and area required for installing a Phantom oversized retractable screen.

Supports openings up to 15 feet wide and 12 feet high.
"""

def calculate_screen_dimensions(width, height):
    """
    Calculates the dimensions and area required for the screen.

    Args:
        width (float): The width of the opening in feet.
        height (float): The height of the opening in feet.

    Returns:
        dict: A dictionary containing the screen width, height, and area.

    Raises:
        ValueError: If the width or height exceeds the maximum supported size.
    """
    # Define the maximum supported dimensions
    max_width = 15  # feet
    max_height = 12  # feet

    # Check if the opening size is within the supported range
    if width > max_width or height > max_height:
        raise ValueError(f"Opening size exceeds maximum supported dimensions ({max_width} x {max_height} feet)")

    # Calculate the screen dimensions (add 1 inch to width and height for proper fit)
    screen_width = width + (1 / 12)  # add 1 inch
    screen_height = height + (1 / 12)  # add 1 inch

    # Calculate the screen area
    screen_area = screen_width * screen_height

    return {
        "screen_width": round(screen_width, 2),
        "screen_height": round(screen_height, 2),
        "screen_area": round(screen_area, 2),
    }


def main():
    try:
        # Get the opening dimensions from the user
        width = float(input("Enter the width of the opening (feet): "))
        height = float(input("Enter the height of the opening (feet): "))

        # Calculate the screen dimensions and area
        screen_dimensions = calculate_screen_dimensions(width, height)

        # Print the results
        print("\nScreen Dimensions and Area:")
        print(f"Width: {screen_dimensions['screen_width']} feet")
        print(f"Height: {screen_dimensions['screen_height']} feet")
        print(f"Area: {screen_dimensions['screen_area']} square feet")

    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
