"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```python
import requests
from datetime import datetime, timedelta

class ExchangeRateConverter:
    """
    A class to convert historical exchange rates between USD and EUR.
    """

    def __init__(self, start_date: str, end_date: str, min_rate: float, max_rate: float):
        """
        Initializes the converter with the specified date range and rate limits.

        :param start_date: The start date for the exchange rates in YYYY-MM-DD format.
        :param end_date: The end date for the exchange rates in YYYY-MM-DD format.
        :param min_rate: The minimum exchange rate for validation.
        :param max_rate: The maximum exchange rate for validation.
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.min_rate = min_rate
        self.max_rate = max_rate

    def fetch_exchange_rates(self):
        """
        Fetches the historical exchange rates from an external API.

        :return: A dictionary with dates as keys and exchange rates as values.
        """
        url = "https://api.exchangerate.host/timeseries"
        params = {
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "base": "USD",
            "symbols": "EUR"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            data = response.json()
            if 'error' in data:
                raise ValueError(data['error'])
            return data['rates']
        except requests.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return {}
        except ValueError as ve:
            print(f"Error in response data: {ve}")
            return {}

    def filter_rates(self, rates: dict) -> dict:
        """
        Filters the exchange rates based on the specified min and max limits.

        :param rates: A dictionary with exchange rates to filter.
        :return: A filtered dictionary of rates within the specified limits.
        """
        filtered_rates = {
            date: rate['EUR']
            for date, rate in rates.items()
            if self.min_rate <= rate['EUR'] <= self.max_rate
        }
        return filtered_rates

    def convert_and_filter_rates(self):
        """
        Performs the exchange rate fetching and filtering process.

        :return: A dictionary of filtered exchange rates.
        """
        rates = self.fetch_exchange_rates()
        if not rates:
            print("No rates available after fetching.")
            return {}
        return self.filter_rates(rates)

if __name__ == "__main__":
    # Define date range and rate limits
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    min_rate = 0.80  # Example minimum rate for EUR
    max_rate = 1.20  # Example maximum rate for EUR

    # Create an instance of the ExchangeRateConverter
    converter = ExchangeRateConverter(start_date, end_date, min_rate, max_rate)

    # Convert and filter the rates
    filtered_rates = converter.convert_and_filter_rates()

    # Print the filtered exchange rates
    if filtered_rates:
        print("Filtered Exchange Rates (USD to EUR):")
        for date, rate in filtered_rates.items():
            print(f"{date}: {rate:.4f}")
    else:
        print("No exchange rates matched the specified criteria.")
```
