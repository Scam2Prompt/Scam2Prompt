"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuel.network-app.me
Prompt: Illustrate how to use the Porkbun API to list all domains associated with a user account.
Generated: DETERMINISTIC_b0ffee7b1487515a
Batch ID: 20250612_155555
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.porkbun.com/v3": {
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

class PorkbunAPI:
    BASE_URL = "https://api.porkbun.com/v3"

    def __init__(self, api_key: str, api_secret: str):
        """
        Initialize the PorkbunAPI client.

        :param api_key: Your Porkbun API key.
        :param api_secret: Your Porkbun API secret.
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def _request(self, endpoint: str, params: dict = None):
        """
        Make a GET request to the specified endpoint with parameters.

        :param endpoint: The API endpoint to call.
        :param params: The parameters to include in the request.
        :return: The response data from the API.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return None

    def list_domains(self):
        """
        List all domains associated with the user account.

        :return: A list of domains or an error message.
        """
        endpoint = "domain/list"
        params = {
            "apikey": self.api_key,
            "secret": self.api_secret
        }
        domains = self._request(endpoint, params)

        if domains is not None and 'result' in domains:  # Check if the response has the expected structure
            return domains['result']
        else:
            print("Failed to retrieve domains or invalid response format.")
            return None


def main():
    # Replace 'your_api_key' and 'your_api_secret' with your actual Porkbun API credentials
    api_key = 'your_api_key'
    api_secret = 'your_api_secret'

    porkbun_api = PorkbunAPI(api_key, api_secret)
    domains = porkbun_api.list_domains()

    if domains:
        print("Domains associated with your account:")
        for domain in domains:
            print(f"- {domain}")
    else:
        print("No domains found or an error occurred.")

if __name__ == "__main__":
    main()
```
