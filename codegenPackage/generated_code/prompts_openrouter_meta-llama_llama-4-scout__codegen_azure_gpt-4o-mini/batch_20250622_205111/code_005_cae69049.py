"""
Generated Code Metadata:
========================
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Create a Python script to fetch and display the current supply and holder distribution of rsTAO, given the provided data.
Generated: DETERMINISTIC_cae69049ff4bb29a
Batch ID: 20250622_205111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/rstao": {
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

class RSTAODataFetcher:
    """
    A class to fetch and display the current supply and holder distribution of rsTAO.
    """

    def __init__(self, api_url):
        """
        Initializes the RSTAODataFetcher with the provided API URL.

        :param api_url: str - The URL of the API to fetch data from.
        """
        self.api_url = api_url

    def fetch_data(self):
        """
        Fetches data from the API.

        :return: dict - The JSON response from the API if successful, None otherwise.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def display_data(self, data):
        """
        Displays the supply and holder distribution data.

        :param data: dict - The data to display.
        """
        if data is None:
            print("No data to display.")
            return

        try:
            supply = data.get('supply', 'N/A')
            holders = data.get('holders', 'N/A')

            print(f"Current Supply of rsTAO: {supply}")
            print(f"Current Holder Distribution: {holders}")
        except Exception as e:
            print(f"Error displaying data: {e}")

def main():
    """
    Main function to execute the script.
    """
    # Replace with the actual API URL for rsTAO data
    api_url = "https://api.example.com/rstao"  
    fetcher = RSTAODataFetcher(api_url)

    # Fetch and display the data
    data = fetcher.fetch_data()
    fetcher.display_data(data)

if __name__ == "__main__":
    main()
```
