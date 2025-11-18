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
# Import necessary modules
import sys

def calculate_cost(screen_type: str, width: float, height: float) -> float:
    """
    Calculates the cost estimate for installing retractable window screens.

    Args:
        screen_type (str): The type of screen ("standard" or "motorized").
        width (float): The width of the window in inches.
        height (float): The height of the window in inches.

    Returns:
        float: The estimated cost in dollars.

    Raises:
        ValueError: If screen_type is invalid or dimensions are not positive.
    """
    # Validate inputs
    if screen_type.lower() not in {"standard", "motorized"}:
        raise ValueError("Invalid screen type. Choose 'standard' or 'motorized'.")
    if width <= 0 or height <= 0:
        raise ValueError("Window dimensions must be positive numbers.")

    # Define cost per square inch for each type of screen
    cost_per_sq_inch = {
        "standard": 0.05,  # $0.05 per square inch for standard screens
        "motorized": 0.10  # $0.10 per square inch for motorized screens
    }

    # Calculate the area of the window
    area = width * height  # Area in square inches

    # Calculate the base cost
    base_cost = area * cost_per_sq_inch[screen_type.lower()]

    # Add installation fee ($50 for standard, $100 for motorized)
    installation_fee = 50 if screen_type.lower() == "standard" else 100

    # Calculate the total cost
    total_cost = base_cost + installation_fee

    return round(total_cost, 2)  # Return the cost rounded to 2 decimal places


# Example usage (uncomment to test):
# try:
#     cost = calculate_cost(screen_type="motorized", width=48, height=36)
#     print(f"Total cost: ${cost}")
# except ValueError as e:
#     print(f"Error: {e}", file=sys.stderr)
```
