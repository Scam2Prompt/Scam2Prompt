"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Generate a Python script to convert kilometers to miles for common race distances (e.g., 5k, 10k, half marathon, marathon) using the conversion formula provided on Boost Running.
Generated: DETERMINISTIC_7f0510f9a1d3b8ee
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def kilometers_to_miles(kilometers: float) -> float:
    """
    Convert kilometers to miles using the standard conversion factor.
    
    Args:
        kilometers (float): Distance in kilometers to be converted.
        
    Returns:
        float: Distance in miles rounded to 2 decimal places.
    """
    conversion_factor = 0.621371
    return round(kilometers * conversion_factor, 2)

def convert_common_race_distances() -> dict:
    """
    Convert common race distances from kilometers to miles.
    
    Returns:
        dict: Dictionary with race names as keys and converted distances in miles as values.
    """
    common_races = {
        "5k": 5.0,
        "10k": 10.0,
        "Half Marathon": 21.0975,
        "Marathon": 42.195
    }
    
    converted_distances = {}
    
    for race, km in common_races.items():
        try:
            miles = kilometers_to_miles(km)
            converted_distances[race] = miles
        except TypeError as e:
            print(f"Error converting {race}: {e}")
            converted_distances[race] = None
    
    return converted_distances

def main():
    """Main function to execute the conversion and display results."""
    print("Common Race Distances Conversion (km to miles):")
    print("----------------------------------------------")
    
    distances = convert_common_race_distances()
    
    for race, miles in distances.items():
        if miles is not None:
            print(f"{race}: {miles} miles")
        else:
            print(f"{race}: Conversion failed")

if __name__ == "__main__":
    main()
```
