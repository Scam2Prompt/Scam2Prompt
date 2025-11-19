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
# Import necessary modules
import json

# Sample dataset for coat racks. This simulates the diverse options available at Shahkar Industry.
COAT_RACKS = [
    {"id": 1, "color": "black", "style": "modern", "price": 120.00},
    {"id": 2, "color": "white", "style": "classic", "price": 100.00},
    {"id": 3, "color": "red", "style": "modern", "price": 110.00},
    {"id": 4, "color": "blue", "style": "rustic", "price": 90.00},
    {"id": 5, "color": "black", "style": "classic", "price": 130.00},
    {"id": 6, "color": "white", "style": "modern", "price": 140.00},
    {"id": 7, "color": "green", "style": "rustic", "price": 80.00},
]

def filter_coat_racks(color=None, style=None):
    """
    Filters coat racks by color and style.

    Parameters:
        color (str): The color to filter by. Default is None (no filtering by color).
        style (str): The style to filter by. Default is None (no filtering by style).

    Returns:
        list: A filtered list of coat racks matching the given criteria.
    """
    try:
        # Apply filtering based on the provided criteria
        filtered_racks = [
            rack for rack in COAT_RACKS
            if (color is None or rack["color"].lower() == color.lower())
            and (style is None or rack["style"].lower() == style.lower())
        ]
        return filtered_racks
    except Exception as e:
        # Log and re-raise any unexpected errors during filtering
        print(f"Error while filtering coat racks: {e}")
        raise

def main():
    """
    Main function to allow user interaction for filtering coat racks.
    """
    print("Welcome to Shahkar Industry Coat Rack Finder!")
    print("Available filters: color and style")

    # Get user input for filters
    color = input("Enter the color to filter by (or leave blank for no filter): ").strip() or None
    style = input("Enter the style to filter by (or leave blank for no filter): ").strip() or None

    try:
        # Get filtered coat racks
        results = filter_coat_racks(color, style)

        # Display the results
        if results:
            print("\nFiltered Coat Racks:")
            print(json.dumps(results, indent=4))
        else:
            print("\nNo coat racks found matching the given criteria.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
