"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ontariooffers.com
Prompt: Provide a Python function that calculates the cost estimate for installing retractable window screens based on user-provided dimensions and screen type (e.g., motorized or standard).
Generated: DETERMINISTIC_5ae829096e828301
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScreenType:
    """Enumeration for screen types."""
    STANDARD = 'standard'
    MOTORIZED = 'motorized'


def calculate_screen_cost(width: float, height: float, screen_type: str) -> float:
    """
    Calculate the cost estimate for installing retractable window screens.

    Args:
        width (float): The width of the window in inches.
        height (float): The height of the window in inches.
        screen_type (str): The type of screen ('standard' or 'motorized').

    Returns:
        float: Estimated cost of the screen installation.

    Raises:
        ValueError: If width or height is negative, or if an invalid screen type is provided.
    """

    # Validate input dimensions
    if width <= 0:
        raise ValueError("Width must be a positive value.")
    if height <= 0:
        raise ValueError("Height must be a positive value.")

    # Cost per square inch for different screen types
    cost_per_square_inch = {
        ScreenType.STANDARD: 0.5,  # Cost for standard screens
        ScreenType.MOTORIZED: 1.0   # Cost for motorized screens
    }

    # Validate screen type
    if screen_type not in cost_per_square_inch:
        raise ValueError("Invalid screen type. Choose 'standard' or 'motorized'.")

    # Calculate area in square inches
    area = width * height

    # Calculate total cost based on area and screen type
    total_cost = area * cost_per_square_inch[screen_type]

    return total_cost


# Example usage:
if __name__ == "__main__":
    try:
        width_input = float(input("Enter the width of the window in inches: "))
        height_input = float(input("Enter the height of the window in inches: "))
        screen_type_input = input("Enter the screen type (standard/motorized): ").lower()

        estimated_cost = calculate_screen_cost(width_input, height_input, screen_type_input)
        print(f"The estimated cost for installing a {screen_type_input} screen is: ${estimated_cost:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
```
