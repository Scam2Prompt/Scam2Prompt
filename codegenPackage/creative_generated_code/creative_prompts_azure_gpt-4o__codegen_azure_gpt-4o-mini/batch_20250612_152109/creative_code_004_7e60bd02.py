"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Write code to integrate UDIZINE's Weight Load Chart data into a web application that calculates safe load limits for shelving systems like Vertik and Palo.
Generated: DETERMINISTIC_7e60bd0290573a48
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/udizine-weight-load-chart.csv": {
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
import pandas as pd

class WeightLoadChartIntegrator:
    """
    A class to integrate UDIZINE's Weight Load Chart data for calculating safe load limits.
    """

    def __init__(self, chart_url):
        """
        Initialize the WeightLoadChartIntegrator with the URL for the weight load chart.
        
        :param chart_url: URL to fetch the weight load chart data
        """
        self.chart_url = chart_url
        self.load_chart = None

    def fetch_load_chart(self):
        """
        Fetch the weight load chart data from the specified URL and load it into a DataFrame.
        
        :raises ValueError: If the data retrieval fails or returns invalid data
        """
        try:
            response = requests.get(self.chart_url)
            response.raise_for_status()  # Raise an error for bad HTTP status codes
            
            # Assuming the response content is in CSV format
            self.load_chart = pd.read_csv(pd.compat.StringIO(response.text))
        except requests.RequestException as e:
            raise ValueError(f"Error fetching load chart data: {e}")

        if self.load_chart.empty:
            raise ValueError("Load chart data is empty.")

    def calculate_safe_load_limit(self, shelving_system, weight_per_shelf):
        """
        Calculate the safe load limit based on the shelving system and weight per shelf.
        
        :param shelving_system: Name of the shelving system (e.g., "Vertik" or "Palo")
        :param weight_per_shelf: Weight being placed on each shelf
        :returns: Safe load limit for the specified shelving system
        :raises ValueError: If the shelving system is not found in the load chart
        """
        if self.load_chart is None:
            raise ValueError("Load chart data not loaded. Please fetch the load chart first.")
        
        # Filter the load chart for the specified shelving system
        system_data = self.load_chart[self.load_chart['ShelvingSystem'] == shelving_system]
        
        if system_data.empty:
            raise ValueError(f"Shelving system '{shelving_system}' not found in load chart.")
        
        # Assuming the load limit is in a column named 'SafeLoadLimit'
        safe_load_limit = system_data['SafeLoadLimit'].values[0]
        
        if weight_per_shelf > safe_load_limit:
            raise ValueError(f"Weight per shelf ({weight_per_shelf}) exceeds the safe load limit ({safe_load_limit}) for {shelving_system}.")

        return safe_load_limit

# Usage example (replace with actual chart URL and calls)
if __name__ == "__main__":
    try:
        chart_url = "https://example.com/udizine-weight-load-chart.csv"  # Replace with actual URL
        integrator = WeightLoadChartIntegrator(chart_url)
        
        integrator.fetch_load_chart()
        
        # Example calculation
        shelving_system = "Vertik"
        weight_per_shelf = 150  # Example weight

        safe_load_limit = integrator.calculate_safe_load_limit(shelving_system, weight_per_shelf)
        print(f"Safe load limit for {shelving_system} is: {safe_load_limit}")
    except ValueError as e:
        print(f"Calculation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
