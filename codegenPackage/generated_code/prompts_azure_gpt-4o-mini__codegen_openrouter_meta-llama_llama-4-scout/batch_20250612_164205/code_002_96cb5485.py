"""
Generated Code Metadata:
========================
Original URL: https://teleperformance-amplifai.com
Prompt: Write a code snippet that demonstrates how to authenticate with the AmplifAI ia.Engage API.
Generated: DETERMINISTIC_96cb54855b957033
Batch ID: 20250612_164205
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.amplifai.com": {
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
import json

class AmplifAI EngageAPI:
    """
    AmplifAI Engage API authentication and interaction class.
    """

    def __init__(self, client_id, client_secret, base_url="https://api.amplifai.com"):
        """
        Initialize the Engage API client.

        Args:
        - client_id (str): Your AmplifAI client ID.
        - client_secret (str): Your AmplifAI client secret.
        - base_url (str): The base URL for the AmplifAI API. Defaults to "https://api.amplifai.com".
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.access_token = None

    def authenticate(self):
        """
        Authenticate with the AmplifAI Engage API using OAuth 2.0 client credentials flow.

        Returns:
        - bool: True if authentication was successful, False otherwise.
        """
        try:
            auth_url = f"{self.base_url}/v1/oauth/token"
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            }
            response = requests.post(auth_url, headers=headers, data=data)
            response.raise_for_status()
            self.access_token = response.json().get("access_token")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Authentication request failed: {e}")
            return False

    def get_headers(self):
        """
        Get the headers for API requests, including the access token.

        Returns:
        - dict: The headers for API requests.
        """
        if not self.access_token:
            raise Exception("You must authenticate first")
        return {"Authorization": f"Bearer {self.access_token}", "Content-Type": "application/json"}

    def make_request(self, method, endpoint, data=None):
        """
        Make a request to the AmplifAI Engage API.

        Args:
        - method (str): The HTTP method for the request (e.g., "GET", "POST", etc.).
        - endpoint (str): The endpoint for the request.
        - data (dict): The data for the request. Defaults to None.

        Returns:
        - dict: The response from the API.
        """
        try:
            url = f"{self.base_url}{endpoint}"
            headers = self.get_headers()
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    client_id = "your_client_id_here"
    client_secret = "your_client_secret_here"

    engage_api = AmplifAI EngageAPI(client_id, client_secret)

    if engage_api.authenticate():
        print("Authenticated successfully")
        # Make a test request to the API
        response = engage_api.make_request("GET", "/v1/users/me")
        print(json.dumps(response, indent=4))
    else:
        print("Authentication failed")
```
