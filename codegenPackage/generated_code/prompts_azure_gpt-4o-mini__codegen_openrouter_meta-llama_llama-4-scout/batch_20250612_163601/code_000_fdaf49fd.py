"""
Generated Code Metadata:
========================
Original URL: https://networkitcnetworkmo.com
Prompt: Write a Python script that integrates with an email marketing service like VertiStream to manage subscription lists and handle unsubscribe requests.
Generated: DETERMINISTIC_fdaf49fd4f0d6c05
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import requests
from typing import Dict, List

class VertiStreamClient:
    """
    A client for interacting with the VertiStream email marketing service.
    """

    def __init__(self, api_key: str, api_url: str):
        """
        Initializes a new VertiStream client.

        Args:
        - api_key (str): The API key for authenticating with VertiStream.
        - api_url (str): The base URL for the VertiStream API.
        """
        self.api_key = api_key
        self.api_url = api_url

    def _make_request(self, method: str, endpoint: str, data: Dict = None):
        """
        Makes a request to the VertiStream API.

        Args:
        - method (str): The HTTP method to use (e.g. "GET", "POST", etc.).
        - endpoint (str): The endpoint to request (e.g. "/lists", "/subscribe", etc.).
        - data (Dict): The data to send with the request.

        Returns:
        - The response from the API.

        Raises:
        - Exception: If the request fails.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        url = f"{self.api_url}{endpoint}"

        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Request failed: {e}")

    def get_lists(self) -> List[Dict]:
        """
        Retrieves a list of all subscription lists.

        Returns:
        - A list of dictionaries, each representing a subscription list.
        """
        return self._make_request("GET", "/lists")

    def subscribe(self, list_id: str, email: str, data: Dict = None) -> Dict:
        """
        Subscribes an email address to a list.

        Args:
        - list_id (str): The ID of the list to subscribe to.
        - email (str): The email address to subscribe.
        - data (Dict): Additional data to store with the subscription.

        Returns:
        - The subscription response from the API.
        """
        endpoint = f"/lists/{list_id}/subscribe"
        return self._make_request("POST", endpoint, {"email": email, **(data or {})})

    def unsubscribe(self, list_id: str, email: str) -> Dict:
        """
        Unsubscribes an email address from a list.

        Args:
        - list_id (str): The ID of the list to unsubscribe from.
        - email (str): The email address to unsubscribe.

        Returns:
        - The unsubscribe response from the API.
        """
        endpoint = f"/lists/{list_id}/unsubscribe"
        return self._make_request("POST", endpoint, {"email": email})

def main():
    api_key = os.environ.get("VERTISTREAM_API_KEY")
    api_url = os.environ.get("VERTISTREAM_API_URL")

    if not api_key or not api_url:
        raise Exception("VertiStream API key and URL are required")

    client = VertiStreamClient(api_key, api_url)

    # Example usage:
    lists = client.get_lists()
    print(json.dumps(lists, indent=4))

    list_id = lists[0]["id"]
    email = "example@example.com"
    subscribe_response = client.subscribe(list_id, email, {"name": "Example Name"})
    print(json.dumps(subscribe_response, indent=4))

    unsubscribe_response = client.unsubscribe(list_id, email)
    print(json.dumps(unsubscribe_response, indent=4))

if __name__ == "__main__":
    main()
```
