"""
Generated Code Metadata:
========================
Original URL: https://bafybeielizhnh2kfpdv2iivhqh4ttf4kqfecv2qyislghqacr6n5gzcfzm.ipfs.dweb.link
Prompt: Provide code examples for developers to interact with the Vana network and query decentralized AI models.
Generated: DETERMINISTIC_3b4568440f517ec1
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vana.network": {
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
# vana_network_client.py

import requests
import json

class VanaNetworkClient:
    """
    Client for interacting with the Vana network and querying decentralized AI models.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the VanaNetworkClient.

        Args:
        - base_url (str): The base URL of the Vana network API.
        - api_key (str): The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, method: str, endpoint: str, data: dict = None):
        """
        Makes a request to the Vana network API.

        Args:
        - method (str): The HTTP method (e.g., GET, POST, PUT, DELETE).
        - endpoint (str): The API endpoint.
        - data (dict): The request data.

        Returns:
        - response (requests.Response): The API response.

        Raises:
        - requests.RequestException: If the request fails.
        """
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            raise Exception(f"Request failed: {e}")

    def get_models(self):
        """
        Retrieves a list of available decentralized AI models.

        Returns:
        - models (list): A list of model metadata.
        """
        response = self._make_request("GET", "/models")
        return response.json()

    def get_model(self, model_id: str):
        """
        Retrieves metadata for a specific decentralized AI model.

        Args:
        - model_id (str): The ID of the model.

        Returns:
        - model (dict): The model metadata.

        Raises:
        - Exception: If the model is not found.
        """
        response = self._make_request("GET", f"/models/{model_id}")
        if response.status_code == 404:
            raise Exception(f"Model not found: {model_id}")
        return response.json()

    def query_model(self, model_id: str, input_data: dict):
        """
        Queries a decentralized AI model with input data.

        Args:
        - model_id (str): The ID of the model.
        - input_data (dict): The input data for the model.

        Returns:
        - output (dict): The model output.

        Raises:
        - Exception: If the model is not found or the query fails.
        """
        response = self._make_request("POST", f"/models/{model_id}/query", input_data)
        if response.status_code == 404:
            raise Exception(f"Model not found: {model_id}")
        return response.json()

def main():
    base_url = "https://api.vana.network"
    api_key = "your_api_key_here"

    client = VanaNetworkClient(base_url, api_key)

    try:
        models = client.get_models()
        print("Available models:")
        for model in models:
            print(model["id"])

        model_id = models[0]["id"]
        model = client.get_model(model_id)
        print(f"Model metadata: {model}")

        input_data = {"input": "example input"}
        output = client.query_model(model_id, input_data)
        print(f"Model output: {output}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
