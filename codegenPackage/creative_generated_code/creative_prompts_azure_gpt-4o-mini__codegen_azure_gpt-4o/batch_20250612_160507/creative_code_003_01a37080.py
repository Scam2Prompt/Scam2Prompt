"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appbalancer.pages.dev
Prompt: Develop a script that lists delivery areas for a takeaway service, inspired by the delivery areas mentioned for Rob N Roll in Kirkcudbright and Auchenlarie.
Generated: DETERMINISTIC_01a370802b211ab3
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to list delivery areas for a takeaway service.
Inspired by Rob N Roll's delivery areas in Kirkcudbright and Auchenlarie.

Author: [Your Name]
Date: [Date]
"""

# Import necessary libraries
import sys

def list_delivery_areas():
    """
    Returns a list of delivery areas for the takeaway service.
    """
    # Define delivery areas (static list for simplicity)
    delivery_areas = [
        "Kirkcudbright",
        "Auchenlarie",
        "Twynholm",
        "Gatehouse of Fleet",
        "Castle Douglas",
        "Borgue",
    ]
    return delivery_areas

def display_delivery_areas(areas):
    """
    Displays the list of delivery areas in a user-friendly format.
    Args:
        areas (list): List of delivery area names.
    """
    print("Delivery Areas:")
    print("-" * 20)
    for index, area in enumerate(areas, start=1):
        print(f"{index}. {area}")
    print("-" * 20)

def main():
    """
    Main function to execute the script.
    """
    try:
        # Fetch delivery areas
        areas = list_delivery_areas()
        
        # Display the delivery areas
        display_delivery_areas(areas)

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
