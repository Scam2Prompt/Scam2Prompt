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
# distance_converter.py

def kilometers_to_miles(kilometers):
    """
    Convert kilometers to miles.

    Parameters:
    kilometers (float): The distance in kilometers.

    Returns:
    float: The distance in miles.
    """
    if kilometers < 0:
        raise ValueError("Distance cannot be negative.")
    
    miles = kilometers * 0.621371
    return miles

def generate_conversion_table(distances_km):
    """
    Generate a conversion table from kilometers to miles.

    Parameters:
    distances_km (list): A list of distances in kilometers.

    Returns:
    dict: A dictionary with distances in kilometers as keys and miles as values.
    """
    conversion_table = {}
    for km in distances_km:
        try:
            miles = kilometers_to_miles(km)
            conversion_table[km] = miles
        except ValueError as e:
            print(f"Error converting {km} km: {e}")
    return conversion_table

def main():
    """
    Main function to execute the distance conversion and display the conversion table.
    """
    # Common running distances in kilometers
    common_distances_km = [5, 10, 21.1, 42.2]  # 5k, 10k, Half Marathon, Full Marathon

    # Generate the conversion table
    conversion_table = generate_conversion_table(common_distances_km)

    # Display the conversion table
    print("Distance Conversion Table (Kilometers to Miles):")
    print("Kilometers\tMiles")
    print("-----------------------")
    for km, miles in conversion_table.items():
        print(f"{km:.1f}\t\t{miles:.2f}")

if __name__ == "__main__":
    main()
```
