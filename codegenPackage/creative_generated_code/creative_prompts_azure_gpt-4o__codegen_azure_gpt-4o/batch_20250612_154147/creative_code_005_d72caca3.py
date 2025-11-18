"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0kn.vercel.app
Prompt: Write code to query the 0KN API for node operation status and retrieve network metrics for privacy analysis.
Generated: DETERMINISTIC_d72caca3527ed409
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class ZeroKNAPIClient:
    """
    A client to interact with the 0KN API for retrieving node operation status 
    and network metrics for privacy analysis.
    """

    def __init__(self, base_url, api_key):
        """
        Constructor to initialize the API client.

        :param base_url: Base URL of the 0KN API.
        :param api_key: API key for authentication.
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        """
        Internal method to make HTTP GET requests to the 0KN API.

        :param endpoint: Endpoint to call (relative to base URL).
        :param params: Query parameters for the request.
        :return: Parsed JSON response from the API.
        :raises Exception: Raises an exception for HTTP errors or request failures.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Accept': 'application/json'
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error making request to {url}: {e}")

    def get_node_operation_status(self):
        """
        Retrieve the operational status of nodes from the 0KN API.

        :return: A dictionary containing the status of nodes.
        """
        endpoint = 'nodes/status'
        try:
            return self._make_request(endpoint)
        except Exception as e:
            print(f"Failed to fetch node operation status: {e}")
            return None

    def get_network_metrics():
        """
        Retrieve network metrics for privacy analysis from the 0KN API.

        :return: A dictionary containing network metrics.
        """
        endpoint = 'network/metrics'
        try metrics=
