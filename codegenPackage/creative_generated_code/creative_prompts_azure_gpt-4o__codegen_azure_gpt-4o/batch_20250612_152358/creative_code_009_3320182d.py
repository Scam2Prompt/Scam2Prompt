"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cactus-network.net
Prompt: Generate code to calculate and display the decentralization metrics of the Cactus Blockchain, based on worldwide farmer participation.
Generated: DETERMINISTIC_3320182d18d46d3a
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cactus-blockchain.com/farmer_data": {
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
import json
import requests
from collections import Counter

class DecentralizationMetrics:
    """
    Class to calculate and display decentralization metrics for the Cactus Blockchain
    based on worldwide farmer participation.
    """

    def __init__(self):
        self.farmer_data_url = "https://api.cactus-blockchain.com/farmer_data"  # Example API Endpoint
        self.farmer_data = []
    
    def fetch_farmer_data(self):
        """
        Fetch farmer data from the API. This data should include the location (country)
        of each farmer participating in the Cactus Blockchain.
        """
        try:
            response = requests.get(self.farmer_data_url)
            response.raise_for_status()  # Raise an error for HTTP error codes
            self.farmer_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching farmer data: {e}")
            self.farmer_data = []

    def calculate_metrics(self):
        """
        Calculate decentralization metrics based on farmer participation.
        Returns a dictionary containing metrics.
        """
        if not self.farmer_data:
            return {
                "total_farmers": 0,
                "unique_countries": 0,
                "country_distribution": {},
                "most_represented_country": None
            }

        # Extract countries from farmer data
        countries = [farmer.get("country") for farmer in self.farmer_data if farmer.get("country")]

        # Count occurrences of each country
        country_distribution = Counter(countries)

        # Determine the most represented country
        most_represented_country = country_distribution.most_common(1)[0] if country_distribution else None

        return {
            "total_farmers": len(self.farmer_data),
            "unique_countries": len(country_distribution),
            "country_distribution": dict(country_distribution),
            "most_represented_country": most_represented_country
        }

    def display_metrics(self, metrics):
        """
        Display decentralization metrics in a user-friendly format.
        """
        print("Decentralization Metrics for Cactus Blockchain:")
        print(f"Total Farmers: {metrics['total_farmers']}")
        print(f"Unique Countries: {metrics['unique_countries']}")
        if metrics['most_represented_country']:
            print(f"Most Represented Country: {metrics['most_represented_country'][0]} "
                  f"({metrics['most_represented_country'][1]} farmers)")
        print("Country Distribution:")
        for country, count in metrics['country_distribution'].items():
            print(f"  {country}: {count} farmers")

def main():
    """
    Main function to execute the decentralization metrics calculation and display.
    """
    metrics_calculator = DecentralizationMetrics()
    metrics_calculator.fetch_farmer_data()
    metrics = metrics_calculator.calculate_metrics()
    metrics_calculator.display_metrics(metrics)

if __name__ == "__main__":
    main()
```
