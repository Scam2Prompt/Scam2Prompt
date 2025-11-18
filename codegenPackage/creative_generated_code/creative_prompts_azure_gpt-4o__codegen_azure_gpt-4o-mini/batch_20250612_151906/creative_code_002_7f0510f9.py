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

def kilometers_to_miles(kilometers):
    """
    Convert kilometers to miles.

    :param kilometers: Distance in kilometers (float or int)
    :return: Distance in miles (float)
    :raises ValueError: If kilometers is negative
    """
    if kilometers < 0:
        raise ValueError("Distance cannot be negative.")
    
    # Conversion factor from kilometers to miles
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles


def display_race_distances():
    """
    Display common race distances in kilometers and their equivalents in miles.
    """
    # Define common race distances in kilometers
    race_distances_km = {
        "5k": 5,
        "10k": 10,
        "Half Marathon": 21.0975,
        "Marathon": 42.195
    }

    print("Race Distances:")
    print(f"{'Distance (km)':<15} {'Distance (miles)':<15}")
    print("=" * 30)

    for race, km in race_distances_km.items():
        try:
            miles = kilometers_to_miles(km)
            print(f"{race:<15} {miles:<15.2f}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    display_race_distances()
```
