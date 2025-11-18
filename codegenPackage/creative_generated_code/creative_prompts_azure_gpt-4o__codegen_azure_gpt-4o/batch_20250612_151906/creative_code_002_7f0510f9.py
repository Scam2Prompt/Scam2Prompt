"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boostrunning.com
Prompt: Generate a Python script to convert kilometers to miles for common race distances (e.g., 5k, 10k, half marathon, marathon) using the conversion formula provided on Boost Running.
Generated: DETERMINISTIC_7f0510f9a1d3b8ee
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# kilometers_to_miles.py
# Script to convert common race distances from kilometers to miles using the conversion formula.

# Conversion factor: 1 kilometer = 0.621371 miles
KM_TO_MILES_FACTOR = 0.621371

def kilometers_to_miles(kilometers):
    """
    Convert kilometers to miles.

    Args:
        kilometers (float): Distance in kilometers.

    Returns:
        float: Distance in miles.
    """
    try:
        # Ensure the input is a positive number
        if kilometers < 0:
            raise ValueError("Distance in kilometers must be a non-negative value.")
        
        # Perform the conversion
        miles = kilometers * KM_TO_MILES_FACTOR
        return round(miles, 2)  # Round to two decimal places for better readability
    except TypeError:
        raise TypeError("Invalid input: kilometers must be a numerical value.")

def main():
    """
    Main function to convert common race distances from kilometers to miles.
    """
    # Common race distances in kilometers
    race_distances_km = {
        "5k": 5.0,
        "10k": 10.0,
        "Half Marathon": 21.0975,  # Standard half marathon distance
        "Marathon": 42.195       # Standard marathon distance
    }

    print("Race Distance Conversion: Kilometers to Miles")
    print("------------------------------------------------")
    for race, distance_km in race_distances_km.items():
        try:
            distance_miles = kilometers_to_miles(distance_km)
            print(f"{race}: {distance_km} km = {distance_miles} miles")
        except Exception as e:
            print(f"Error converting {race}: {str(e)}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
