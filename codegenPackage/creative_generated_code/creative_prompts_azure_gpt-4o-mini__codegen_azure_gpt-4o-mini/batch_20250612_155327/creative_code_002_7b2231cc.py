"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shahkarco.com
Prompt: Create a script that allows users to filter coat racks by color and style, reflecting the diverse options available at Shahkar Industry.
Generated: DETERMINISTIC_7b2231cc5fcd7f30
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# coat_rack_filter.py

# Import necessary libraries
from typing import List, Dict, Any

# Define a class to represent a coat rack
class CoatRack:
    def __init__(self, color: str, style: str):
        """
        Initialize a CoatRack instance.

        Args:
            color (str): The color of the coat rack.
            style (str): The style of the coat rack.
        """
        self.color = color
        self.style = style

    def __repr__(self) -> str:
        """Return a string representation of the coat rack."""
        return f"CoatRack(color='{self.color}', style='{self.style}')"


# Function to filter coat racks by color and style
def filter_coat_racks(coat_racks: List[CoatRack], color: str = None, style: str = None) -> List[CoatRack]:
    """
    Filter a list of coat racks by color and/or style.

    Args:
        coat_racks (List[CoatRack]): A list of coat racks to filter.
        color (str, optional): The desired color to filter by. Defaults to None.
        style (str, optional): The desired style to filter by. Defaults to None.

    Returns:
        List[CoatRack]: A list of filtered coat racks.
    """
    # Validate inputs
    if not isinstance(coat_racks, list):
        raise ValueError("The coat_racks argument must be a list.")
    if color is not None and not isinstance(color, str):
        raise ValueError("The color argument must be a string.")
    if style is not None and not isinstance(style, str):
        raise ValueError("The style argument must be a string.")

    # Filter coat racks based on provided criteria
    filtered_racks = []
    for rack in coat_racks:
        if (color is None or rack.color.lower() == color.lower()) and \
           (style is None or rack.style.lower() == style.lower()):
            filtered_racks.append(rack)

    return filtered_racks


# Main function to demonstrate filtering coat racks
def main():
    # Sample coat racks available at Shahkar Industry
    coat_racks = [
        CoatRack(color="Red", style="Modern"),
        CoatRack(color="Blue", style="Classic"),
        CoatRack(color="Green", style="Rustic"),
        CoatRack(color="Red", style="Vintage"),
        CoatRack(color="Yellow", style="Modern"),
        CoatRack(color="Blue", style="Modern"),
    ]

    # User inputs for filtering
    user_color = input("Enter the color you want to filter by (or press Enter to skip): ").strip() or None
    user_style = input("Enter the style you want to filter by (or press Enter to skip): ").strip() or None

    try:
        # Filter coat racks based on user input
        filtered_racks = filter_coat_racks(coat_racks, user_color, user_style)

        # Output the filtered coat racks
        if filtered_racks:
            print("Filtered Coat Racks:")
            for rack in filtered_racks:
                print(rack)
        else:
            print("No coat racks found with the specified criteria.")

    except ValueError as e:
        print(f"Error: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
