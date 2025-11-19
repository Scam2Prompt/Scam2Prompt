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
# Import necessary modules
def kilometers_to_miles(kilometers):
    """
    Convert kilometers to miles.
    
    Parameters:
        kilometers (float): Distance in kilometers.
    
    Returns:
        float: Distance in miles.
    """
    try:
        # Conversion factor: 1 kilometer = 0.621371 miles
        miles = kilometers * 0.621371
        return round(miles, 2)  # Round to 2 decimal places for readability
    except TypeError:
        raise ValueError("Input must be a number representing kilometers.")

def generate_conversion_table():
    """
    Generate a conversion table for common running distances.
    
    Returns:
        dict: A dictionary with distances in kilometers as keys and miles as values.
    """
    # Common running distances in kilometers
    running_distances_km = [5, 10, 21.0975, 42.195]  # 5k, 10k, Half Marathon, Marathon
    conversion_table = {}
    
    for km in running_distances_km:
        conversion_table[km] = kilometers_to_miles(km)
    
    return conversion_table

def main():
    """
    Main function to calculate the distance for a 10k marathon and display a conversion table.
    """
    # Distance for a 10k marathon
    ten_k_distance_km = 10
    ten_k_distance_miles = kilometers_to_miles(ten_k_distance_km)
    
    print(f"Distance for a 10k marathon: {ten_k_distance_km} km = {ten_k_distance_miles} miles\n")
    
    # Generate and display the conversion table
    print("Conversion Table for Common Running Distances:")
    conversion_table = generate_conversion_table()
    for km, miles in conversion_table.items():
        print(f"{km} km = {miles} miles")

if __name__ == "__main__":
    # Entry point of the script
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
