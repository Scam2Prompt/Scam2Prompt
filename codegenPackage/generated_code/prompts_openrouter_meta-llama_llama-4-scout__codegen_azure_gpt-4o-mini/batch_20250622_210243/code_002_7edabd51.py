"""
Generated Code Metadata:
========================
Original URL: https://neotokyo-85y.pages.dev
Prompt: Generate code to create a new identity in the Neo Tokyo metaverse using the provided API endpoints (e.g., `S2 citizen upload`, `S1 citizen upload`).
Generated: DETERMINISTIC_7edabd51505c05c2
Batch ID: 20250622_210243
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.neotokyo.com": {
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

class NeoTokyoAPI:
    BASE_URL = "https://api.neotokyo.com"

    def __init__(self, api_key):
        """
        Initialize the NeoTokyoAPI with the provided API key.
        
        :param api_key: str - The API key for authentication.
        """
        self.api_key = api_key

    def upload_citizen(self, citizen_data, citizen_type):
        """
        Upload a new citizen identity to the Neo Tokyo metaverse.

        :param citizen_data: dict - The data of the citizen to be uploaded.
        :param citizen_type: str - The type of citizen ('S1' or 'S2').
        :return: dict - The response from the API.
        :raises ValueError: If the citizen_type is not valid.
        :raises Exception: If the API request fails.
        """
        if citizen_type not in ['S1', 'S2']:
            raise ValueError("Invalid citizen type. Must be 'S1' or 'S2'.")

        endpoint = f"{self.BASE_URL}/{citizen_type}_citizen_upload"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(endpoint, json=citizen_data, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "your_api_key_here"
    
    # Create an instance of the NeoTokyoAPI
    neo_tokyo_api = NeoTokyoAPI(API_KEY)

    # Define the citizen data
    citizen_data = {
        "name": "John Doe",
        "age": 30,
        "skills": ["coding", "design"],
        "bio": "A passionate developer in the Neo Tokyo metaverse."
    }

    # Upload a new S1 citizen
    try:
        response = neo_tokyo_api.upload_citizen(citizen_data, 'S1')
        print("Citizen uploaded successfully:", response)
    except Exception as e:
        print("Failed to upload citizen:", e)
```
