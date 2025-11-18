"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gettapeads.com
Prompt: Create a script to calculate earnings from the Streamtape Partner Program based on the number of downloads and the origin country using the Level table/Worldmap.
Generated: DETERMINISTIC_5c076c7225dd0fae
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_earnings(download_counts, country, level_table):
    """
    Calculates earnings from the Streamtape Partner Program based on 
    downloads and the origin country using the level table/world map.

    Parameters:
    download_counts (int): Total number of downloads.
    country (str): Origin country of the downloads.
    level_table (dict): Dictionary mapping countries to their Level rate.

    Returns:
    float: Total earnings.
    """
    try:
        if not isinstance(download_counts, int) or download_counts < 0:
            raise ValueError("download_counts must be a non-negative integer.")
        
        if not isinstance(country, str) or country.strip() == "":
            raise ValueError("country must be a non-empty string.")
        
        # Normalize country name to match level_table keys
        country = country.strip().capitalize()
        
        if country not in level_table:
            raise KeyError(f"Country '{country}' not found in the level table.")

        # Retrieve rate for the country and calculate earnings
        rate = level_table[country]
        earnings = download_counts * rate

        return earnings

    except KeyError as ke:
        print(f"Error: {ke}")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example Level table (Worldmap) with rates per download in USD
    level_table = {
        "Usa": 0.005,   # United States
        "Canada": 0.004,
        "Germany": 0.0035,
        "India": 0.001,
        "Australia": 0.0045
    }

    # Example data
    try:
        download_counts = int(input("Enter total number of downloads: "))
        country = input("Enter the country of origin: ")

        # Calculate and display earnings
        earnings = calculate_earnings(download_counts, country, level_table)
        print(f"Earnings for {download_counts} downloads from {country}: ${earnings:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
