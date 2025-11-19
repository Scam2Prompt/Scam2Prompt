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
import json
from typing import Dict, Optional

# Streamtape Partner Program earnings calculator
class StreamtapeEarningsCalculator:
    """
    Calculates earnings based on Streamtape's Partner Program rates.
    Uses the Level table/Worldmap to determine rates per country.
    """

    # Default rates per 1000 downloads (in USD) based on country levels
    # Level 1: $20, Level 2: $10, Level 3: $5, Level 4: $1
    DEFAULT_RATES = {
        "Level1": 20.0,
        "Level2": 10.0,
        "Level3": 5.0,
        "Level4": 1.0
    }

    # Example country to level mapping (should be expanded with complete data)
    COUNTRY_LEVEL_MAP = {
        "US": "Level1",
        "CA": "Level1",
        "UK": "Level1",
        "DE": "Level1",
        "FR": "Level2",
        "JP": "Level2",
        "AU": "Level2",
        "BR": "Level3",
        "IN": "Level3",
        "RU": "Level3",
        "NG": "Level4",
        "PK": "Level4",
        "BD": "Level4"
    }

    def __init__(self, custom_rates: Optional[Dict[str, float]] = None, 
                 custom_country_map: Optional[Dict[str, str]] = None):
        """
        Initialize the calculator with optional custom rates and country mappings.
        
        Args:
            custom_rates: Dictionary of custom rates per level (e.g., {"Level1": 25.0})
            custom_country_map: Dictionary of custom country to level mappings
        """
        self.rates = custom_rates if custom_rates else self.DEFAULT_RATES
        self.country_level_map = custom_country_map if custom_country_map else self.COUNTRY_LEVEL_MAP

    def get_country_level(self, country_code: str) -> str:
        """
        Get the level for a given country code.
        
        Args:
            country_code: ISO 2-letter country code
            
        Returns:
            The country's level (e.g., "Level1")
            
        Raises:
            ValueError: If country code is not found in the mapping
        """
        country_code = country_code.upper()
        if country_code not in self.country_level_map:
            raise ValueError(f"Country code '{country_code}' not found in level mapping")
        return self.country_level_map[country_code]

    def calculate_earnings(self, downloads: int, country_code: str) -> float:
        """
        Calculate earnings for a given number of downloads from a country.
        
        Args:
            downloads: Number of downloads
            country_code: ISO 2-letter country code
            
        Returns:
            Earnings in USD
            
        Raises:
            ValueError: If downloads is negative or country code is invalid
        """
        if downloads < 0:
            raise ValueError("Downloads cannot be negative")
        
        level = self.get_country_level(country_code)
        rate_per_1000 = self.rates.get(level, 0.0)
        
        earnings = (downloads / 1000) * rate_per_1000
        return round(earnings, 2)

    def calculate_earnings_bulk(self, downloads_per_country: Dict[str, int]) -> Dict[str, float]:
        """
        Calculate earnings for multiple countries at once.
        
        Args:
            downloads_per_country: Dictionary of {country_code: downloads}
            
        Returns:
            Dictionary of {country_code: earnings}
            
        Raises:
            ValueError: If any country code is invalid or downloads are negative
        """
        results = {}
        for country, downloads in downloads_per_country.items():
            results[country] = self.calculate_earnings(downloads, country)
        return results

    def save_country_mapping(self, file_path: str) -> None:
        """
        Save the country-level mapping to a JSON file.
        
        Args:
            file_path: Path to save the JSON file
        """
        with open(file_path, 'w') as f:
            json.dump(self.country_level_map, f, indent=4)

    def load_country_mapping(self, file_path: str) -> None:
        """
        Load a country-level mapping from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file is not valid JSON
        """
        with open(file_path, 'r') as f:
            self.country_level_map = json.load(f)


# Example usage
if __name__ == "__main__":
    try:
        calculator = StreamtapeEarningsCalculator()
        
        # Single calculation
        earnings = calculator.calculate_earnings(5000, "US")
        print(f"Earnings from US: ${earnings}")
        
        # Bulk calculation
        downloads_data = {
            "US": 10000,
            "FR": 5000,
            "BR": 3000,
            "PK": 2000
        }
        bulk_earnings = calculator.calculate_earnings_bulk(downloads_data)
        print("Bulk earnings:")
        for country, amount in bulk_earnings.items():
            print(f"{country}: ${amount}")
            
        total_earnings = sum(bulk_earnings.values())
        print(f"Total earnings: ${round(total_earnings, 2)}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
