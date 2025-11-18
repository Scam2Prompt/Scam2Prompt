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
import pandas as pd

class StreamtapeEarningsCalculator:
    """
    A class to calculate earnings from the Streamtape Partner Program based on downloads
    and origin country.
    """

    def __init__(self, level_table: pd.DataFrame):
        """
        Initializes the calculator with the provided level table.

        :param level_table: A DataFrame containing the earnings rates per country.
        """
        self.level_table = level_table

    def get_earning_rate(self, country: str) -> float:
        """
        Retrieves the earning rate for a given country.

        :param country: The name of the country.
        :return: The earning rate for the country.
        :raises ValueError: If the country is not found in the level table.
        """
        if country not in self.level_table['Country'].values:
            raise ValueError(f"Earning rate for '{country}' not found.")
        
        # Get the earning rate corresponding to the country
        rate = self.level_table.loc[self.level_table['Country'] == country, 'EarningRate'].values[0]
        return rate

    def calculate_earnings(self, downloads: int, country: str) -> float:
        """
        Calculates the earnings based on the number of downloads and the origin country.

        :param downloads: The number of downloads.
        :param country: The origin country of the downloads.
        :return: The total earnings calculated.
        :raises ValueError: If downloads are negative or country is invalid.
        """
        if downloads < 0:
            raise ValueError("Number of downloads cannot be negative.")
        
        earning_rate = self.get_earning_rate(country)
        total_earnings = downloads * earning_rate
        return total_earnings

def main():
    """
    Main function to execute the earnings calculation.
    """
    # Sample level table data
    data = {
        'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
        'EarningRate': [0.01, 0.008, 0.009, 0.007, 0.006]
    }
    
    # Create a DataFrame for the level table
    level_table = pd.DataFrame(data)

    # Initialize the calculator
    calculator = StreamtapeEarningsCalculator(level_table)

    # Example usage
    try:
        downloads = 1000
        country = 'USA'
        earnings = calculator.calculate_earnings(downloads, country)
        print(f"Earnings for {downloads} downloads from {country}: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
