"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeielizhnh2kfpdv2iivhqh4ttf4kqfecv2qyislghqacr6n5gzcfzm.ipfs.dweb.link
Prompt: Provide code examples for developers to interact with the Vana network and query decentralized AI models.
Generated: DETERMINISTIC_3b4568440f517ec1
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vananetwork.com": {
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
# File: vana_network_client.py

import requests

class VanaNetworkClient:
    """
    A client to interact with the Vana network's decentralized AI models.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initialize the VanaNetworkClient.

        Args:
            base_url (str): The base URL of the Vana network API.
            api_key (str): Your API key for authentication.
        """
        if not base_url or not api_key:
            raise ValueError("Base URL and API key must be provided.")
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def query_model(self, model_id: str, payload: dict) -> dict:
        """
        Query a decentralized AI model on the Vana network.

        Args:
            model_id (str): The unique identifier of the AI model to query.
            payload (dict): Input data to send to the model.

        Returns:
            dict: The result returned by the model.

        Raises:
            RuntimeError: Raised if the request fails or the API responds with an error.
        """
        if not model_id or not payload:
            raise ValueError("Model ID and payload must be provided.")

        url = f"{self.base_url}/models/{model_id}/query"
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP failure codes
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to query model: {e}")

    def list_models(self) -> dict:
        """
        List all available AI models on the Vana network.

        Returns:
            dict: A list of models with their details.

        Raises:
            RuntimeError: Raised if the request fails or the API responds with an error.
        """
        url = f"{self.base_url}/models"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP failure codes
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to retrieve model list: {e}")


if __name__ == "__main__":
    # Example usage of VanaNetworkClient
    import os

    # Replace these with your actual Vana network base URL and API key
    BASE_URL = os.getenv("VANA_BASE_URL", "https://api.vananetwork.com")
    API_KEY = os.getenv("VANA_API_KEY", "your_api_key_here")

    try:
        vana_client = VanaNetworkClient(BASE_URL, API_KEY)

        # List available models
        print("Fetching available models...")
        models = vana_client.list_models()
        print(models)

        # Query a specific model
        model_id = "example_model_id"
        payload = {"input": "example query data"}
        print(f"Querying model {model_id}...")
        result = vana_client.query_model(model_id, payload)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
```
