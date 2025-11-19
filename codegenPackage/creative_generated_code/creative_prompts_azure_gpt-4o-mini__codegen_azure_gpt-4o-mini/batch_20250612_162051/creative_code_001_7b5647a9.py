"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Write a code snippet that uses an API to fetch information about hiking trails in Bulgaria, focusing on the unique features of the Falakro mountain.
Generated: DETERMINISTIC_7b5647a9544259dc
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

class HikingTrailFetcher:
    """
    A class to fetch hiking trail information from an external API.

    Attributes
    ----------
    api_url : str
        The base URL for the hiking trails API.
    """

    def __init__(self, api_url):
        """
        Initializes the HikingTrailFetcher with the given API URL.

        Parameters
        ----------
        api_url : str
            The base URL for the hiking trails API.
        """
        self.api_url = api_url

    def fetch_trails(self, mountain_name):
        """
        Fetches hiking trails information for a specified mountain.

        Parameters
        ----------
        mountain_name : str
            The name of the mountain to fetch trails for.

        Returns
        -------
        dict
            A dictionary containing trail information if successful, 
            otherwise an error message.
        """
        try:
            response = requests.get(f"{self.api_url}/trails", params={"mountain": mountain_name})

            # Check if the request was successful
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}


def main():
    """
    The main function to execute the hiking trail fetching process.
    """
    # Base URL for the hiking trails API
    API_URL = "https://api.example.com"  # Replace with the actual API URL

    # Initialize the HikingTrailFetcher
    trail_fetcher = HikingTrailFetcher(API_URL)

    # Fetch trails for Falakro mountain
    mountain_name = "Falakro"
    trails_info = trail_fetcher.fetch_trails(mountain_name)

    # Print the trails information
    print(trails_info)


if __name__ == "__main__":
    main()
```
