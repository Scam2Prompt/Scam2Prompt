"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Provide a Python script to parse and display institutional symbols and historical data, referencing the "Símbolos de la Institución" and "Reseña Histórica" sections on the IEBCA website.
Generated: DETERMINISTIC_c09a3c3a0473643d
Batch ID: 20250612_152527
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.iebca.com": {
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
from bs4 import BeautifulSoup
import pandas as pd

class InstitutionalDataParser:
    """
    A class to parse institutional symbols and historical data from the IEBCA website.
    """

    BASE_URL = "https://www.iebca.com"  # Base URL of the IEBCA website

    def __init__(self):
        """
        Initialize the InstitutionalDataParser class.
        """
        self.symbols = []
        self.history = ""

    def fetch_webpage(self, endpoint):
        """
        Fetch the webpage content from the specified endpoint.

        Parameters:
            endpoint (str): The specific endpoint to fetch data from.

        Returns:
            BeautifulSoup: Parsed HTML of the webpage.

        Raises:
            Exception: If the request to the webpage fails.
        """
        try:
            response = requests.get(f"{self.BASE_URL}{endpoint}")
            response.raise_for_status()  # Raise an error for bad responses
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            raise Exception(f"Error fetching webpage: {e}")

    def parse_symbols(self):
        """
        Parse the institutional symbols from the "Símbolos de la Institución" section.
        """
        try:
            soup = self.fetch_webpage("/simbolos")  # Update with the actual endpoint
            symbol_section = soup.find('div', {'id': 'symbols'})
            self.symbols = [symbol.get_text().strip() for symbol in symbol_section.find_all('li')]
        except Exception as e:
            print(f"Error parsing symbols: {e}")

    def parse_history(self):
        """
        Parse the historical data from the "Reseña Histórica" section.
        """
        try:
            soup = self.fetch_webpage("/historia")  # Update with the actual endpoint
            history_section = soup.find('div', {'id': 'history'})
            self.history = history_section.get_text().strip()
        except Exception as e:
            print(f"Error parsing history: {e}")

    def display_data(self):
        """
        Display the parsed institutional symbols and historical data.
        """
        print("Institutional Symbols:")
        for symbol in self.symbols:
            print(f" - {symbol}")
        print("\nHistorical Overview:")
        print(self.history)

    def run(self):
        """
        Execute the parsing and display process.
        """
        self.parse_symbols()
        self.parse_history()
        self.display_data()


if __name__ == "__main__":
    parser = InstitutionalDataParser()
    parser.run()
```
