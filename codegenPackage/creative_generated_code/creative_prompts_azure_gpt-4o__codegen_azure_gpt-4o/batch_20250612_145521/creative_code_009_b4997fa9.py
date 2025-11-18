"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-france.fr
Prompt: Provide a Python example for querying data about Polkadot's partnerships and ecosystem projects using the Polkadot API, as described on Polkadot France.
Generated: DETERMINISTIC_b4997fa9d9182741
Batch ID: 20250612_145521
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polkadot.network": {
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

class PolkadotAPI:
    """
    A class to interact with Polkadot ecosystem and partnership data via the Polkadot API.
    """

    def __init__(self, base_url="https://api.polkadot.network"):
        """
        Initialize the PolkadotAPI client.
        
        :param base_url: Base URL of the Polkadot API. Default is the official Polkadot API endpoint.
        """
        self.base_url = base_url

    def get_partnerships(self):
        """
        Fetches data about Polkadot's partnerships.

        :return: A list of partnerships if successful, otherwise raises an exception.
        """
        endpoint = "/partnerships"
        url = self.base_url + endpoint

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
            return response.json()  # Assume the API returns JSON data
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error fetching partnerships: {e}")

    def get_ecosystem_projects(self):
        """
        Fetches data about Polkadot's ecosystem projects.

        :return: A list of ecosystem projects if successful, otherwise raises an exception.
        """
        endpoint = "/ecosystem-projects"
        url = self.base_url + endpoint

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
            return response.json()  # Assume the API returns JSON data
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error fetching ecosystem projects: {e}")


def main():
    """
    Main function that demonstrates fetching Polkadot partnerships and ecosystem projects.
    """
    # Initialize the PolkadotAPI instance
    polkadot_api = PolkadotAPI()

    # Fetch partnerships
    try:
        partnerships = polkadot_api.get_partnerships()
        print("Polkadot Partnerships:")
        for idx, partnership in enumerate(partnerships, start=1):
            print(f"{idx}. {partnership}")
    except RuntimeError as e:
        print(e)

    # Fetch ecosystem projects
    try:
        ecosystem_projects = polkadot_api.get_ecosystem_projects()
        print("\nPolkadot Ecosystem Projects:")
        for idx, project in enumerate(ecosystem_projects, start=1):
            print(f"{idx}. {project}")
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()
```
