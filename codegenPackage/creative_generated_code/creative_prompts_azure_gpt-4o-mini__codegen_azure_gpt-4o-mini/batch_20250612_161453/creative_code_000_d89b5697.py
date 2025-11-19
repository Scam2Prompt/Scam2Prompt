"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iammetis.org
Prompt: Generate a code snippet that retrieves and displays profiles of Métis individuals using an API that provides Indigenous ancestry data.
Generated: DETERMINISTIC_d89b56977f777e00
Batch ID: 20250612_161453
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.indigenous-ancestry.example.com": {
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

class MetisProfileFetcher:
    """
    A class to fetch and display profiles of Métis individuals using an Indigenous ancestry API.
    """

    def __init__(self, api_url):
        """
        Initializes the MetisProfileFetcher with the given API URL.

        Parameters:
        api_url (str): The base URL of the Indigenous ancestry API
        """
        self.api_url = api_url

    def fetch_profiles(self, page=1, page_size=10):
        """
        Fetches profiles of Métis individuals from the API.

        Parameters:
        page (int): The page number to retrieve (default is 1)
        page_size (int): The number of profiles to retrieve per page (default is 10)

        Returns:
        list: A list of Métis profiles
        """
        try:
            response = requests.get(f"{self.api_url}/metis-profiles", params={'page': page, 'page_size': page_size})
            response.raise_for_status()  # Raise an error for HTTP error codes
            return response.json()  # Return the JSON data as a list of profiles
        except requests.RequestException as e:
            print(f"Error fetching profiles: {e}")
            return []

    def display_profiles(self, profiles):
        """
        Displays profiles of Métis individuals.

        Parameters:
        profiles (list): A list of Métis profiles to display
        """
        if not profiles:
            print("No profiles found.")
            return

        for profile in profiles:
            print(f"Name: {profile.get('name')}")
            print(f"Ancestry: {profile.get('ancestry')}")
            print(f"Region: {profile.get('region')}")
            print(f"Biography: {profile.get('biography')}")
            print("-" * 40)

if __name__ == "__main__":
    # Set up the API URL (example URL, would need to be replaced with the actual API endpoint)
    api_url = "https://api.indigenous-ancestry.example.com"
    
    # Create an instance of MetisProfileFetcher
    fetcher = MetisProfileFetcher(api_url)

    # Fetch profiles and display them
    profiles = fetcher.fetch_profiles(page=1, page_size=5)
    fetcher.display_profiles(profiles)
```
