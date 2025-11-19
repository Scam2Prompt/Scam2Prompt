"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapala.tc
Prompt: Develop an API integration that fetches travel destinations and activities, focusing on unique experiences as highlighted by Rapala Travel Concierge.
Generated: DETERMINISTIC_0016664e464cf9be
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.rapalatravel.com/v1": {
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

class RapalaTravelAPI:
    """
    A client for interacting with the Rapala Travel Concierge API to fetch travel destinations and activities.
    """

    BASE_URL = "https://api.rapalatravel.com/v1"  # Replace with the actual Rapala API base URL
    TIMEOUT = 10  # Timeout for API requests in seconds

    def __init__(self, api_key: str):
        """
        Initializes the RapalaTravelAPI client.

        :param api_key: API key for authenticating requests
        """
        self.api_key = api_key

    def get_unique_experiences(self, destination: str) -> List[Dict]:
        """
        Fetches unique travel experiences for a given destination.

        :param destination: Name of the destination (e.g., "Paris", "Tokyo")
        :return: List of unique experiences (e.g., activities, locations of interest)
        """
        url = f"{self.BASE_URL}/unique-experiences"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"destination": destination}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=self.TIMEOUT)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            data = response.json()
            return data.get("experiences", [])
        except requests.exceptions.RequestException as e:
            # Log the error and return an empty list in case of an error
            print(f"Error fetching unique experiences: {e}")
            return []

    def get_all_destinations(self) -> List[str]:
        """
        Fetches all available travel destinations.

        :return: List of destination names
        """
        url = f"{self.BASE_URL}/destinations"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers, timeout=self.TIMEOUT)
            response.raise_for_status()
            data = response.json()
            return data.get("destinations", [])
        except requests.exceptions.RequestException as e:
            # Log the error and return an empty list in case of an error
            print(f"Error fetching destinations: {e}")
            return []


def main():
    """
    Main function to demonstrate API usage.
    """
    # Replace 'your_api_key_here' with a valid API key for the Rapala Travel Concierge API.
    api_key = "your_api_key_here"
    rapala_api = RapalaTravelAPI(api_key)

    # Fetch all destinations
    destinations = rapala_api.get_all_destinations()
    print("Available destinations:")
    print(destinations)

    # Fetch unique experiences for each destination
    for destination in destinations:
        print(f"\nUnique experiences for {destination}:")
        experiences = rapala_api.get_unique_experiences(destination)
        for experience in experiences:
            print(f"- {experience['name']}: {experience['description']}")


if __name__ == "__main__":
    main()
```

**Notes:**
- Replace `your_api_key_here` with a valid API key.
- Update `BASE_URL` with the actual endpoint URL for the Rapala Travel Concierge API.
- Ensure the endpoint paths (e.g., `/unique-experiences`, `/destinations`) match the actual API documentation provided by Rapala Travel.
