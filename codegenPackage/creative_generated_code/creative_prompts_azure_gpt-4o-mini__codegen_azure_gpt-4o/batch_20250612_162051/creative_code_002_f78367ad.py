"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onedivepb.com
Prompt: Create a code snippet that integrates with the One Dive API to list all available diving specialties and their descriptions.
Generated: DETERMINISTIC_f78367ad4ac05cab
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.onedive.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a clean, well-documented, production-ready Python code snippet that integrates with a hypothetical "One Dive" API to list all available diving specialties and their descriptions:

```python
import requests

class OneDiveAPIClient:
    """
    A client to interact with the One Dive API.
    """

    BASE_URL = "https://api.onedive.com/v1"  # Replace with the actual API endpoint

    def __init__(self, api_key):
        """
        Initializes the One Dive API client.

        :param api_key: API key for authenticating requests.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get_diving_specialties(self):
        """
        Fetches a list of diving specialties and their descriptions.

        :return: A dictionary containing diving specialties and their descriptions.
        :raises: RuntimeError if the API request fails or returns an error.
        """
        endpoint = f"{self.BASE_URL}/diving-specialties"

        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

            # Parse the response JSON
            data = response.json()
            specialties = data.get("specialties", [])

            # Ensure the response contains valid data
            if not specialties:
                raise ValueError("No diving specialties found in the API response.")

            return specialties

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch diving specialties: {e}")
        except ValueError as ve:
            raise RuntimeError(f"Invalid data received from the API: {ve}")


def main():
    """
    Main function to fetch and display diving specialties and their descriptions.
    """
    # Replace with your actual API key
    api_key = "your_api_key_here"
    client = OneDiveAPIClient(api_key)

    try:
        specialties = client.get_diving_specialties()

        print("Available Diving Specialties:")
        for specialty in specialties:
            name = specialty.get("name", "Unknown Specialty")
            description = specialty.get("description", "No description available.")
            print(f"- {name}: {description}")

    except RuntimeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
```

**Key Points:**
- Replace `"your_api_key_here"` with your actual One Dive API key.
- Replace `"https://api.onedive.com/v1"` with the actual base URL of the One Dive API if it's different.
- The code includes comprehensive error handling for network issues and invalid API data.
