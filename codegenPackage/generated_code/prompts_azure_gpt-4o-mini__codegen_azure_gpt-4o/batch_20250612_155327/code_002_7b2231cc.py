"""
Generated Code Metadata:
========================
Original URL: https://shahkarco.com
Prompt: Create a script that allows users to filter coat racks by color and style, reflecting the diverse options available at Shahkar Industry.
Generated: DETERMINISTIC_7b2231cc5fcd7f30
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Script to filter coat racks by color and style
# Author: [Your Name]
# Date: [Today's Date]
# Description: This script allows users to filter coat racks by color and style, reflecting the diverse options available at Shahkar Industry.

# Import necessary modules
import sys

# Sample data representing coat racks available at Shahkar Industry
coat_racks = [
    {"id": 1, "color": "black", "style": "modern"},
    {"id": 2, "color": "white", "style": "classic"},
    {"id": 3, "color": "brown", "style": "rustic"},
    {"id": 4, "color": "black", "style": "classic"},
    {"id": 5, "color": "white", "style": "modern"},
    {"id": 6, "color": "brown", "style": "modern"},
]

def filter_coat_racks(color=None, style=None):
    """
    Filters coat racks based on color and style.
    
    Args:
        color (str): The color to filter by (e.g., 'black', 'white', 'brown').
        style (str): The style to filter by (e.g., 'modern', 'classic', 'rustic').
    
    Returns:
        list: A list of coat racks matching the filter criteria.
    """
    try:
        # Validate input
        if color and not isinstance(color, str):
            raise ValueError("Color must be a string.")
        if style and not isinstance(style, str):
            raise ValueError("Style must be a string.")
        
        # Filter coat racks based on criteria
        filtered_racks = [
            rack for rack in coat_racks
            if (color is None or rack["color"].lower() == color.lower()) and
               (style is None or rack["style"].lower() == style.lower())
        ]
        
        return filtered_racks
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []

def main():
    """
    Main function to interact with the user and filter coat racks.
    """
    print("Welcome to Shahkar Industry Coat Rack Filter!")
    print("Available colors: black, white, brown")
    print("Available styles: modern, classic, rustic")
    
    # Get user input for filtering criteria
    color = input("Enter the color to filter by (or press Enter to skip): ").strip()
    style = input("Enter the style to filter by (or press Enter to skip): ").strip()
    
    # Convert empty input to None
    color = color if color else None
    style = style if style else None
    
    # Filter coat racks
    filtered_racks = filter_coat_racks(color=color, style=style)
    
    # Display results
    if filtered_racks:
        print("\nFiltered Coat Racks:")
        for rack in filtered_racks:
            print(f"ID: {rack['id']}, Color: {rack['color']}, Style: {rack['style']}")
    else:
        print("\nNo coat racks match the given criteria.")

if __name__ == "__main__":
    main()
```
