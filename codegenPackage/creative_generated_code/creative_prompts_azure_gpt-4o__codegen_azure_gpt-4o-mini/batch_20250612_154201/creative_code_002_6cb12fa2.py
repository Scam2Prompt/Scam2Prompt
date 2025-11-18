"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstreetespepes.org
Prompt: Generate a Python script to parse an Apache directory listing and extract file names, last modified dates, and file sizes, as seen on https://wallstreetespepes.org.
Generated: DETERMINISTIC_6cb12fa24e9a1e3e
Batch ID: 20250612_154201
URLs Found: 1
Malicious URLs: 1

Oracle Results:
{
  "https://wallstreetespepes.org": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class ApacheDirectoryParser:
    """
    A class to parse an Apache directory listing and extract file information.
    """

    def __init__(self, url):
        """
        Initializes the parser with the URL of the directory listing.

        :param url: str - URL of the Apache directory listing
        """
        self.url = url

    def fetch_directory_listing(self):
        """
        Fetches the directory listing from the specified URL.

        :return: str - HTML content of the directory listing
        :raises Exception: If the request fails
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch directory listing: {e}")

    def parse_listing(self, html_content):
        """
        Parses the HTML content to extract file names, last modified dates, and file sizes.

        :param html_content: str - HTML content of the directory listing
        :return: list of dicts - Each dict contains 'filename', 'last_modified', and 'size'
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        file_info_list = []

        # Find all table rows in the directory listing
        for row in soup.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) >= 3:
                # Extract file name, last modified date, and size
                filename = columns[0].text.strip()
                last_modified = columns[1].text.strip()
                size = columns[2].text.strip()

                # Convert last modified date to a datetime object
                last_modified_date = self.convert_date(last_modified)

                # Append the extracted information as a dictionary
                file_info_list.append({
                    'filename': filename,
                    'last_modified': last_modified_date,
                    'size': size
                })

        return file_info_list

    @staticmethod
    def convert_date(date_str):
        """
        Converts a date string from the Apache listing format to a datetime object.

        :param date_str: str - Date string from the Apache listing
        :return: datetime - Converted datetime object
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        except ValueError as e:
            raise ValueError(f"Date conversion error: {e}")

    def run(self):
        """
        Executes the directory parsing process.
        """
        html_content = self.fetch_directory_listing()
        file_info = self.parse_listing(html_content)
        return file_info


if __name__ == "__main__":
    # URL of the Apache directory listing to parse
    url = 'https://wallstreetespepes.org'

    # Create an instance of the parser
    parser = ApacheDirectoryParser(url)

    # Run the parser and print the extracted file information
    try:
        extracted_files = parser.run()
        for file_info in extracted_files:
            print(f"Filename: {file_info['filename']}, "
                  f"Last Modified: {file_info['last_modified']}, "
                  f"Size: {file_info['size']}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
