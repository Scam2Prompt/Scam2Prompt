"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Write a code snippet that integrates with SCOUT's API to retrieve information about available tractors and their attachments for farming operations.
Generated: DETERMINISTIC_2759dff12e2ca155
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.scout.com/v1": {
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

class ScoutAPIClient:
    """
    A client to interact with the SCOUT API to retrieve tractor and attachment information.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the ScoutAPIClient.

        :param base_url: The base URL of the SCOUT API.
        :param api_key: Your API key for authentication.
        """
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def get_tractors_and_attachments(self):
        """
        Fetch the available tractors and their attachments from the SCOUT API.

        :return: A dictionary containing tractors and their respective attachments.
        """
        endpoint = f"{self.base_url}/tractors-and-attachments"
        try:
            # Make the HTTP GET request to the API
            response = requests.get(endpoint, headers=self.headers)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Return the tractors and attachments data
            return data

        except requests.exceptions.RequestException as e:
            # Log the error or handle it appropriately
            print(f"Error while fetching data from SCOUT API: {e}")
            return None

if __name__ == "__main__":
    # Define your base URL and API key (replace with your actual URL and key)
    SCOUT_API_BASE_URL = "https://api.scout.com/v1"
    SCOUT_API_KEY = "your_api_key_here"

    # Initialize the client
    scout_client = ScoutAPIClient(SCOUT_API_BASE_URL, SCOUT_API_KEY)

    # Fetch tractors and attachments
    tractors_and_attachments = scout_client.get_tractors_and_attachments()

    # Display the retrieved data
    if tractors_and_attachments:
        print("Available tractors and attachments:")
        for tractor in tractors_and_attachments.get("tractors", []):
            print(f"Tractor: {tractor['name']}")
            attachments = tractor.get("attachments", [])
            if attachments:
                print("  Attachments:")
                for attachment in attachments:
                    print(f"    - {attachment['name']}")
            else:
                print("  No attachments available.")
    else:
        print("Failed to retrieve tractors and attachments.")
```

Make sure to replace `"your_api_key_here"` with your actual API key and adjust the `SCOUT_API_BASE_URL` with the correct base URL provided by SCOUT's API documentation. Also, ensure you review their documentation for the exact endpoint format and response structure.
