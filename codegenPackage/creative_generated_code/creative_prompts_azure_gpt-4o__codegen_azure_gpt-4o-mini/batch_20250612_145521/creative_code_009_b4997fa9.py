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
    A class to interact with the Polkadot API to fetch data about partnerships
    and ecosystem projects.
    """

    BASE_URL = "https://api.polkadot.network"  # Base URL for Polkadot API

    def __init__(self):
        """
        Initialize the PolkadotAPI class.
        """
        pass

    def get_partnerships(self):
        """
        Fetches data about Polkadot's partnerships.

        Returns:
            dict: A dictionary containing partnership data.
            
        Raises:
            Exception: If the API request fails.
        """
        endpoint = "/partnerships"
        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response data as JSON
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching partnerships: {e}")
            raise Exception("Failed to fetch partnerships data.")

    def get_ecosystem_projects(self):
        """
        Fetches data about Polkadot's ecosystem projects.

        Returns:
            dict: A dictionary containing ecosystem project data.
            
        Raises:
            Exception: If the API request fails.
        """
        endpoint = "/ecosystem-projects"
        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response data as JSON
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching ecosystem projects: {e}")
            raise Exception("Failed to fetch ecosystem projects data.")

if __name__ == "__main__":
    # Main execution block
    polkadot_api = PolkadotAPI()

    try:
        partnerships = polkadot_api.get_partnerships()
        print("Partnerships Data:")
        print(partnerships)

        ecosystem_projects = polkadot_api.get_ecosystem_projects()
        print("\nEcosystem Projects Data:")
        print(ecosystem_projects)
    except Exception as e:
        print(f"Error: {e}")
```
