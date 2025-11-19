"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chhatrapatitimes.com
Prompt: Develop a code snippet that could automate the process of gathering data on public welfare schemes like the "Mukhyamantri Kanyadaan Yojana" mentioned in the news.
Generated: DETERMINISTIC_8996d1f284ac3d79
Batch ID: 20250612_162508
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/welfare-schemes": {
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
from bs4 import BeautifulSoup
from datetime import datetime

class WelfareSchemeScraper:
    """
    A class to scrape data on public welfare schemes from a specified website.
    """

    def __init__(self, url):
        """
        Initialize the scraper with the base URL of the welfare scheme data.

        :param url: str - The URL to scrape data from
        """
        self.url = url

    def fetch_data(self):
        """
        Fetch data from the URL and return the HTML content.

        :return: str - HTML content of the page
        :raises Exception: If the request to the URL fails
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from {self.url}: {e}")

    def parse_data(self, html_content):
        """
        Parse the HTML content to extract relevant data.

        :param html_content: str - HTML content of the page
        :return: list - List of dictionaries containing scheme data
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        schemes_data = []

        # Assuming the schemes are in a table format
        table = soup.find('table', {'id': 'schemes_table'})
        rows = table.find_all('tr')[1:]  # Skip header row

        for row in rows:
            columns = row.find_all('td')
            scheme_info = {
                'Scheme Name': columns[0].text.strip(),
                'Start Date': columns[1].text.strip(),
                'Eligibility': columns[2].text.strip(),
                'Benefits': columns[3].text.strip(),
            }
            schemes_data.append(scheme_info)

        return schemes_data

    def save_data_to_csv(self, data, filename):
        """
        Save the extracted data to a CSV file.

        :param data: list - List of dictionaries containing scheme data
        :param filename: str - The name of the file to save the data
        """
        try:
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"Data saved to {filename}")
        except Exception as e:
            raise Exception(f"Error saving data to {filename}: {e}")

    def run(self):
        """
        Execute the scraping and data saving process.
        """
        html_content = self.fetch_data()
        schemes_data = self.parse_data(html_content)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.save_data_to_csv(schemes_data, f'welfare_schemes_{timestamp}.csv')

if __name__ == "__main__":
    # URL to the page containing welfare schemes data
    url = 'https://example.com/welfare-schemes'  # Replace with the actual URL
    scraper = WelfareSchemeScraper(url)
    scraper.run()
```
