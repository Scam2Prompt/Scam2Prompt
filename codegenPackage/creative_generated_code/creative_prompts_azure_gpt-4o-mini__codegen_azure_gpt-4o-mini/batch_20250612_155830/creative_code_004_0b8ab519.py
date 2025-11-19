"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: Generate a sample API call to retrieve statistics on the number of GPUs registered with Aethir.
Generated: DETERMINISTIC_0b8ab5196ce93ada
Batch ID: 20250612_155830
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aethir.com": {
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
from requests.exceptions import HTTPError, RequestException

class AethirAPI:
    """A class to interact with the Aethir API for GPU statistics."""

    BASE_URL = "https://api.aethir.com"  # Replace with the actual Aethir API base URL

    def __init__(self, api_key: str):
        """
        Initialize the AethirAPI client.

        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_gpu_statistics(self) -> dict:
        """
        Retrieve statistics on the number of GPUs registered with Aethir.

        Returns:
            dict: A dictionary containing GPU statistics.

        Raises:
            RuntimeError: If the API request fails or returns an error.
        """
        endpoint = f"{self.BASE_URL}/gpu/statistics"  # Replace with the actual endpoint
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            return response.json()  # Return the response JSON data

        except HTTPError as http_err:
            raise RuntimeError(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except RequestException as req_err:
            raise RuntimeError(f"Request error occurred: {req_err}")  # Handle other requests errors
        except ValueError as json_err:
            raise RuntimeError(f"Error parsing JSON response: {json_err}")  # Handle JSON parsing errors

if __name__ == "__main__":
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    aethir_api = AethirAPI(API_KEY)

    try:
        gpu_stats = aethir_api.get_gpu_statistics()
        print("GPU Statistics:", gpu_stats)
    except RuntimeError as e:
        print("Error retrieving GPU statistics:", e)
```
