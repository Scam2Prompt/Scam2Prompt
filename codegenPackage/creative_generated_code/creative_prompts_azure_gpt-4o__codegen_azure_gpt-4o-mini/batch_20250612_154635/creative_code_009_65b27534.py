"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elara-celestia.com
Prompt: Create a Python script to extract and display the connectivity details (e.g., proximity to IT hubs, airport, and metro) from the L&T Elara Celestia webpage.
Generated: DETERMINISTIC_65b275340cdb366f
Batch ID: 20250612_154635
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/lnt-elara-celestia": {
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

class ConnectivityExtractor:
    """
    A class to extract connectivity details from a given webpage.
    """

    def __init__(self, url):
        """
        Initializes the ConnectivityExtractor with the specified URL.

        Args:
            url (str): The URL of the webpage to extract information from.
        """
        self.url = url
        self.connectivity_details = {}

    def fetch_page(self):
        """
        Fetches the webpage content from the specified URL.

        Returns:
            str: The HTML content of the webpage.

        Raises:
            Exception: If the HTTP request fails or the URL is unreachable.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Error fetching the webpage: {e}")

    def parse_connectivity_details(self, html_content):
        """
        Parses the HTML content to extract connectivity details.

        Args:
            html_content (str): The HTML content of the webpage.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Example selectors; these need to be adjusted based on actual webpage structure
        try:
            # Extracting connectivity details with appropriate selectors
            self.connectivity_details['IT_hubs'] = soup.select_one('.it-hubs').get_text(strip=True)
            self.connectivity_details['airport'] = soup.select_one('.airport').get_text(strip=True)
            self.connectivity_details['metro'] = soup.select_one('.metro').get_text(strip=True)
        except AttributeError as e:
            raise Exception("Error parsing the connectivity details: Ensure the HTML structure has not changed.") from e

    def display_connectivity_details(self):
        """
        Displays the extracted connectivity details.
        """
        for key, value in self.connectivity_details.items():
            print(f"{key}: {value}")

    def run(self):
        """
        Executes the process to fetch, parse, and display connectivity details.
        """
        try:
            html_content = self.fetch_page()
            self.parse_connectivity_details(html_content)
            self.display_connectivity_details()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    # URL of the L&T Elara Celestia webpage
    url = "https://www.example.com/lnt-elara-celestia"  # Replace with the actual URL
    extractor = ConnectivityExtractor(url)
    extractor.run()
```
