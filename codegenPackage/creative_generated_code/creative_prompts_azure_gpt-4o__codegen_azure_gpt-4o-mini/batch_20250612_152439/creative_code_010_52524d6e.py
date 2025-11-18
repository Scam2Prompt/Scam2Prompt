"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet-app.pages.dev
Prompt: Write a script using Lava SDK to fetch geolocation-based QoS analytics for node providers serving the Optimism blockchain.
Generated: DETERMINISTIC_52524d6e92279d90
Batch ID: 20250612_152439
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lava.network/v1/": {
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
import json

class LavaSDK:
    """Class to interact with the Lava SDK for geolocation-based QoS analytics."""

    BASE_URL = "https://api.lava.network/v1/"

    def __init__(self, api_key):
        """
        Initializes the LavaSDK with the provided API key.

        Args:
            api_key (str): Your API key for the Lava SDK.
        """
        self.api_key = api_key

    def fetch_qos_analytics(self, blockchain, provider):
        """
        Fetches geolocation-based QoS analytics for a specific blockchain and node provider.

        Args:
            blockchain (str): The name of the blockchain (e.g., 'optimism').
            provider (str): The name of the node provider.

        Returns:
            dict: A dictionary containing QoS analytics data.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        url = f"{self.BASE_URL}qos/{blockchain}/{provider}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Return the JSON response as a dictionary

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Error occurred during the request: {req_err}")  # Handle other request issues

def main():
    """Main function to execute the QoS analytics fetching process."""
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    blockchain = "optimism"
    provider = "your_node_provider"  # Replace with the desired node provider

    lava_sdk = LavaSDK(api_key)

    try:
        qos_data = lava_sdk.fetch_qos_analytics(blockchain, provider)
        print(json.dumps(qos_data, indent=4))  # Pretty print the QoS analytics data
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
