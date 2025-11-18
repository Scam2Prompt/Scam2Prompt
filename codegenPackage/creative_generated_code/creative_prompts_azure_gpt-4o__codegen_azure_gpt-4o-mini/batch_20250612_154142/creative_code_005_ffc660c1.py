"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: Write code to interact with the Aethir API for retrieving GPU node statistics, including location and earnings data, as described in the Aethir ecosystem documentation.
Generated: DETERMINISTIC_ffc660c1d19f5647
Batch ID: 20250612_154142
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aethir.com/v1": {
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
import logging
from typing import Any, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AethirAPIClient:
    """A client for interacting with the Aethir API to retrieve GPU node statistics."""

    BASE_URL = "https://api.aethir.com/v1"

    def __init__(self, api_key: str):
        """Initialize the Aethir API client with an API key.

        Args:
            api_key (str): The API key for authenticating requests to the Aethir API.
        """
        self.api_key = api_key

    def _request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Internal method to send a GET request to the Aethir API.

        Args:
            endpoint (str): The API endpoint to call.
            params (Optional[Dict[str, Any]]): Query parameters to include in the request.

        Returns:
            Dict[str, Any]: The JSON response from the API.

        Raises:
            Exception: If the request fails or returns an error.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for HTTP error codes
            return response.json()
        except requests.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise Exception("Failed to retrieve data from Aethir API") from e

    def get_gpu_node_statistics(self) -> Dict[str, Any]:
        """Retrieve GPU node statistics, including location and earnings data.

        Returns:
            Dict[str, Any]: A dictionary containing GPU node statistics.

        Raises:
            Exception: If the data retrieval fails.
        """
        logger.info("Retrieving GPU node statistics from Aethir API...")
        return self._request("gpu/nodes")

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual Aethir API key
    api_key = 'your_api_key_here'
    
    try:
        client = AethirAPIClient(api_key)
        statistics = client.get_gpu_node_statistics()
        print("GPU Node Statistics:", statistics)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
