"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltetradingsacademy.com
Prompt: Create a script to fetch and display currency profiles (e.g., USD, GBP, JPY) with local account details, inspired by the "Currency Profile" section on the Grand Chase website.
Generated: DETERMINISTIC_11c69e491984d99d
Batch ID: 20250612_154601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate-api.com/v4/latest": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class CurrencyProfile:
    """A class to fetch and display currency profiles."""

    API_URL = "https://api.exchangerate-api.com/v4/latest"  # Sample API endpoint

    def __init__(self, currency_code):
        """
        Initialize the CurrencyProfile with a currency code.

        Args:
            currency_code (str): The currency code (e.g., 'USD', 'GBP').
        """
        self.currency_code = currency_code.upper()
        self.profile_data = None

    def fetch_currency_data(self):
        """Fetch currency data from the external API."""
        try:
            response = requests.get(f"{self.API_URL}/{self.currency_code}")
            response.raise_for_status()  # Raise an error for bad responses
            self.profile_data = response.json()  # Parse the JSON data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # HTTP error
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception occurred: {req_err}")  # Other request errors
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error: {json_err}")  # JSON parsing error

    def display_currency_profile(self):
        """Display the currency profile details."""
        if self.profile_data:
            print(f"Currency Profile for {self.currency_code}:")
            print(f"Base Currency: {self.profile_data['base']}")
            print("Exchange Rates:")
            for currency, rate in self.profile_data['rates'].items():
                print(f"{currency}: {rate}")
        else:
            print("No currency profile data available. Please fetch data first.")

def main():
    """Main function to fetch and display currency profiles."""
    currency_code = input("Enter the currency code (e.g., USD, GBP, JPY): ")
    currency_profile = CurrencyProfile(currency_code)
    
    currency_profile.fetch_currency_data()
    currency_profile.display_currency_profile()

if __name__ == "__main__":
    main()
```

Make sure to install the `requests` library if it's not already available in your environment by running:
```bash
pip install requests
```
