"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Develop a Python program to convert historical daily exchange rates between USD and EUR, using provided maximum and minimum values for specific dates.
Generated: DETERMINISTIC_a896f3744726381b
Batch ID: 20250612_154901
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate.host/timeseries": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from datetime import datetime, timedelta

class ExchangeRateConverter:
    """
    A class to convert historical daily exchange rates between USD and EUR.
    """

    def __init__(self, start_date: str, end_date: str, min_value: float, max_value: float):
        """
        Initializes the ExchangeRateConverter with the specified date range and exchange rate limits.

        :param start_date: The start date for the exchange rate data in 'YYYY-MM-DD' format.
        :param end_date: The end date for the exchange rate data in 'YYYY-MM-DD' format.
        :param min_value: The minimum exchange rate value.
        :param max_value: The maximum exchange rate value.
        """
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.min_value = min_value
        self.max_value = max_value
        self.api_url = "https://api.exchangerate.host/timeseries"

    def fetch_exchange_rates(self):
        """
        Fetches historical exchange rates from the API for the specified date range.

        :return: A dictionary containing the exchange rates.
        :raises Exception: If the API request fails or returns an error.
        """
        params = {
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'base': 'USD',
            'symbols': 'EUR'
        }
        
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            if 'error' in data:
                raise Exception(data['error'])
            return data['rates']
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def filter_rates(self, rates):
        """
        Filters the exchange rates based on the specified minimum and maximum values.

        :param rates: A dictionary of exchange rates.
        :return: A dictionary of filtered exchange rates.
        """
        filtered_rates = {}
        for date, rate in rates.items():
            if self.min_value <= rate['EUR'] <= self.max_value:
                filtered_rates[date] = rate['EUR']
        return filtered_rates

    def convert(self):
        """
        Main method to fetch, filter, and display the exchange rates.

        :return: A dictionary of filtered exchange rates.
        """
        rates = self.fetch_exchange_rates()
        filtered_rates = self.filter_rates(rates)
        return filtered_rates

if __name__ == "__main__":
    # Example usage
    start_date = '2023-01-01'
    end_date = '2023-01-31'
    min_value = 0.85
    max_value = 0.95

    converter = ExchangeRateConverter(start_date, end_date, min_value, max_value)
    try:
        result = converter.convert()
        print("Filtered Exchange Rates (USD to EUR):")
        for date, rate in result.items():
            print(f"{date}: {rate}")
    except Exception as e:
        print(f"Error: {e}")
```
