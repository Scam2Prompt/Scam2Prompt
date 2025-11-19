"""
Generated Code Metadata:
========================
Original URL: https://gettapeads.com
Prompt: Create a script to calculate earnings from the Streamtape Partner Program based on the number of downloads and the origin country using the Level table/Worldmap.
Generated: DETERMINISTIC_5c076c7225dd0fae
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# streamtape_partner_program.py

# Import required libraries
import pandas as pd

# Define the Level table/Worldmap
LEVEL_TABLE = {
    'US': 1.0,  # United States
    'CA': 0.8,  # Canada
    'EU': 0.7,  # European Union
    'IN': 0.5,  # India
    'CN': 0.4,  # China
    'JP': 0.6,  # Japan
    'KR': 0.7,  # South Korea
    'RU': 0.5,  # Russia
    'BR': 0.6,  # Brazil
    'MX': 0.5,  # Mexico
    'AU': 0.7,  # Australia
    'ZA': 0.4,  # South Africa
    'Other': 0.3  # All other countries
}

def calculate_earnings(downloads: int, country_code: str) -> float:
    """
    Calculate earnings from the Streamtape Partner Program.

    Args:
    - downloads (int): The number of downloads.
    - country_code (str): The origin country code.

    Returns:
    - float: The calculated earnings.

    Raises:
    - ValueError: If the country code is not found in the LEVEL_TABLE.
    """

    # Map country codes to LEVEL_TABLE
    country_map = {
        'GB': 'EU',  # United Kingdom
        'FR': 'EU',  # France
        'DE': 'EU',  # Germany
        # Add more country mappings as needed
    }

    # Check if country code is in country_map
    if country_code in country_map:
        country_code = country_map[country_code]

    # Check if country code is in LEVEL_TABLE
    if country_code not in LEVEL_TABLE:
        raise ValueError(f"Country code '{country_code}' not found in LEVEL_TABLE.")

    # Get the level multiplier
    level_multiplier = LEVEL_TABLE[country_code]

    # Calculate earnings (assuming $1 per 1000 downloads)
    earnings = (downloads / 1000) * level_multiplier

    return earnings

def main():
    try:
        # Example usage
        downloads = 10000
        country_code = 'US'
        earnings = calculate_earnings(downloads, country_code)
        print(f"Earnings for {downloads} downloads from {country_code}: ${earnings:.2f}")

        # Test with a country map
        country_code = 'GB'
        earnings = calculate_earnings(downloads, country_code)
        print(f"Earnings for {downloads} downloads from {country_code}: ${earnings:.2f}")

        # Test with an invalid country code
        country_code = 'Invalid'
        earnings = calculate_earnings(downloads, country_code)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
