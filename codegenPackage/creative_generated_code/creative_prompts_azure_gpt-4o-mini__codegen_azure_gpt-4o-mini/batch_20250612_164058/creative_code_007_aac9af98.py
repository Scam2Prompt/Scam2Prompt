"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercanza.es
Prompt: Describe how to automate business processes using the solutions provided by Mercanza to enhance operational efficiency.
Generated: DETERMINISTIC_aac9af98b4f43572
Batch ID: 20250612_164058
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mercanza.com/v1": {
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
from typing import List, Dict, Any

class MercanzaAPI:
    """
    A class to interact with the Mercanza API for automating business processes.
    """

    BASE_URL = "https://api.mercanza.com/v1"

    def __init__(self, api_key: str):
        """
        Initializes the MercanzaAPI instance with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Mercanza API.
        """
        self.api_key = api_key

    def _send_request(self, endpoint: str, method: str = 'GET', data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Sends a request to the Mercanza API.

        Args:
            endpoint (str): The endpoint to which the request will be sent.
            method (str): The HTTP method to use ('GET', 'POST', etc.).
            data (Dict[str, Any]): The data to send with the request, if applicable.

        Returns:
            Dict[str, Any]: The JSON response from the Mercanza API.

        Raises:
            Exception: If the request fails or returns an error status code.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }

        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # e.g., 404, 500, etc.
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Other errors

    def automate_process(self, process_id: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Automates a specified business process using Mercanza's automation features.

        Args:
            process_id (str): The ID of the business process to automate.
            parameters (Dict[str, Any]): Parameters required for the automation.

        Returns:
            Dict[str, Any]: The result of the automation request.

        Raises:
            Exception: If the process automation fails.
        """
        endpoint = f"processes/{process_id}/automate"
        return self._send_request(endpoint, method='POST', data=parameters)

    def get_process_status(self, process_id: str) -> Dict[str, Any]:
        """
        Retrieves the status of an automated process.

        Args:
            process_id (str): The ID of the automated process.

        Returns:
            Dict[str, Any]: The status of the automated process.

        Raises:
            Exception: If the status retrieval fails.
        """
        endpoint = f"processes/{process_id}/status"
        return self._send_request(endpoint, method='GET')

# Example Usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    mercanza_api = MercanzaAPI(api_key=API_KEY)

    try:
        # Automate a business process
        process_id = "example_process_id"
        parameters = {
            "param1": "value1",
            "param2": "value2"
        }
        result = mercanza_api.automate_process(process_id, parameters)
        print("Process automated successfully:", result)

        # Check the status of the automated process
        status = mercanza_api.get_process_status(process_id)
        print("Current process status:", status)

    except Exception as e:
        print(f"An error occurred: {e}")
```
