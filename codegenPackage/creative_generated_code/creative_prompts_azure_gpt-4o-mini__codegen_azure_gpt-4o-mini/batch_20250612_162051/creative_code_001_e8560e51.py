"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superdar.com
Prompt: Write a function that retrieves and displays pricing information for various kitchen tables, including specific models such as "Кръгла маса разтегателна Перла" and "Дизайнерска правоъгълна маса Алана."
Generated: DETERMINISTIC_e8560e51cd8d673f
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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
from typing import List, Dict

class TablePricingService:
    """
    A service to retrieve pricing information for various kitchen tables.
    """

    def __init__(self, api_url: str):
        """
        Initialize the pricing service with the API URL.

        :param api_url: The base URL for the product pricing API.
        """
        self.api_url = api_url

    def fetch_table_prices(self, models: List[str]) -> Dict[str, float]:
        """
        Fetch prices for the specified table models from the API.

        :param models: A list of table model names to fetch prices for.
        :return: A dictionary with model names as keys and their prices as values.
        """
        prices = {}
        for model in models:
            try:
                response = requests.get(f"{self.api_url}/tables", params={"model": model})
                response.raise_for_status()  # Raise an error for bad responses
                data = response.json()

                # Assuming the API response contains 'model' and 'price' fields
                if 'model' in data and 'price' in data:
                    prices[data['model']] = data['price']
                else:
                    print(f"Invalid response structure for model: {model}")

            except requests.exceptions.RequestException as e:
                print(f"Error fetching price for {model}: {e}")

        return prices

    def display_prices(self, prices: Dict[str, float]) -> None:
        """
        Display the pricing information in a formatted way.

        :param prices: A dictionary of table models and their prices.
        """
        if not prices:
            print("No pricing information available.")
            return

        print("Pricing Information for Kitchen Tables:")
        for model, price in prices.items():
            print(f"{model}: ${price:.2f}")


if __name__ == "__main__":
    # Example usage
    API_URL = "https://api.example.com"  # Replace with actual API URL
    table_models = [
        "Кръгла маса разтегателна Перла",
        "Дизайнерска правоъгълна маса Алана"
    ]

    service = TablePricingService(API_URL)
    table_prices = service.fetch_table_prices(table_models)
    service.display_prices(table_prices)
```
