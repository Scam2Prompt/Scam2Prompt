"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: Write code to interact with the Aethir dashboard API for tracking GPU earnings and node performance, as described in the Aethir documentation.
Generated: DETERMINISTIC_010ebf526f27e85d
Batch ID: 20250612_154142
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class AethirAPI:
    """
    A class to interact with the Aethir dashboard API for tracking GPU earnings and node performance.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.aethir.com"):
        """
        Initializes the AethirAPI client with an API key and base URL.

        Args:
            api_key (str): The API key for authentication.
            base_url (str): The base URL for the Aethir API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _get_headers(self) -> dict:
        """
        Builds the headers for the API request, including authentication.

        Returns:
            dict: A dictionary containing the headers for the request.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_gpu_earnings(self) -> dict:
        """
        Fetches the GPU earnings from the Aethir dashboard.

        Returns:
            dict: A dictionary containing the GPU earnings data.

        Raises:
            Exception: Raises an exception if the request fails.
        """
        try:
            response = requests.get(f"{self.base_url}/gpu/earnings", headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Successfully fetched GPU earnings data.")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching GPU earnings data: {e}")
            raise

    def get_node_performance(self) -> dict:
        """
        Fetches the node performance metrics from the Aethir dashboard.

        Returns:
            dict: A dictionary containing the node performance data.

        Raises:
            Exception: Raises an exception if the request fails.
        """
        try:
            response = requests.get(f"{self.base_url}/node/performance", headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Successfully fetched node performance data.")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching node performance data: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the AethirAPI class
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    aethir_api = AethirAPI(api_key=API_KEY)

    try:
        gpu_earnings = aethir_api.get_gpu_earnings()
        print("GPU Earnings:", gpu_earnings)

        node_performance = aethir_api.get_node_performance()
        print("Node Performance:", node_performance)

    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
