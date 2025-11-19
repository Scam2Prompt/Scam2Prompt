"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Write a Python script to calculate the distance in miles for a given distance in kilometers, specifically for a 10k marathon, and provide a conversion table for common running distances.
Generated: DETERMINISTIC_5a048af9f9a36c37
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Distance Conversion Script
==========================

This script calculates the distance in miles for a given distance in kilometers.
It also provides a conversion table for common running distances.

Author: [Your Name]
Date: [Today's Date]
"""

def kilometers_to_miles(kilometers):
    """
    Converts kilometers to miles.

    Args:
        kilometers (float): Distance in kilometers.

    Returns:
        float: Distance in miles.
    """
    miles = kilometers * 0.621371
    return miles

def print_conversion_table():
    """
    Prints a conversion table for common running distances.
    """
    distances_km = [5, 10, 15, 21.0975]  # 5K, 10K, 15K, Half Marathon
    print("Common Running Distances Conversion Table:")
    print("-------------------------------------------")
    print("| Distance (km) | Distance (miles) |")
    print("-------------------------------------------")
    for distance_km in distances_km:
        distance_miles = kilometers_to_miles(distance_km)
        print(f"| {distance_km:.2f}       | {distance_miles:.2f}       |")
    print("-------------------------------------------")

def main():
    try:
        # Calculate distance for a 10K marathon
        distance_km = 10
        distance_miles = kilometers_to_miles(distance_km)
        print(f"The distance of a 10K marathon is {distance_miles:.2f} miles.")

        # Print conversion table
        print_conversion_table()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
