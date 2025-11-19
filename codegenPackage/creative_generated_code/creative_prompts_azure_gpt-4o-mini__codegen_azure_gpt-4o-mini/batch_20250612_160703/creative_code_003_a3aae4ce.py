"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cm-coinmaster.home.blog
Prompt: Provide a code example for managing Coin Master subscriptions using a web API.
Generated: DETERMINISTIC_a3aae4ce8f42ab7b
Batch ID: 20250612_160703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coinmaster.com/v1": {
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

class CoinMasterAPI:
    """
    A class to manage Coin Master subscriptions via a web API.
    """

    BASE_URL = "https://api.coinmaster.com/v1"

    def __init__(self, api_key):
        """
        Initialize the CoinMasterAPI with an API key.

        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Make an HTTP request to the Coin Master API.

        Args:
            endpoint (str): The API endpoint to call.
            method (str): The HTTP method to use (GET, POST, etc.).
            data (dict, optional): The data to send with the request.

        Returns:
            dict: The response data from the API.

        Raises:
            Exception: If the request fails or returns an error.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            else:
                raise ValueError("Unsupported HTTP method.")

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise Exception("Failed to communicate with the API.")
        except Exception as err:
            print(f"An error occurred: {err}")
            raise Exception("An unknown error occurred.")

    def subscribe(self, user_id):
        """
        Subscribe a user to Coin Master.

        Args:
            user_id (str): The ID of the user to subscribe.

        Returns:
            dict: The API response confirming the subscription.
        """
        endpoint = 'subscriptions/subscribe'
        data = {'userId': user_id}

        return self._make_request(endpoint, method='POST', data=data)

    def unsubscribe(self, user_id):
        """
        Unsubscribe a user from Coin Master.

        Args:
            user_id (str): The ID of the user to unsubscribe.

        Returns:
            dict: The API response confirming the unsubscription.
        """
        endpoint = 'subscriptions/unsubscribe'
        data = {'userId': user_id}

        return self._make_request(endpoint, method='POST', data=data)

    def get_subscription_status(self, user_id):
        """
        Get the subscription status for a user.

        Args:
            user_id (str): The ID of the user to check.

        Returns:
            dict: The API response containing the subscription status.
        """
        endpoint = f'subscriptions/status/{user_id}'

        return self._make_request(endpoint, method='GET')


# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    coin_master_api = CoinMasterAPI(API_KEY)

    try:
        user_subscription = coin_master_api.subscribe("user123")
        print("Subscription Response:", user_subscription)

        status = coin_master_api.get_subscription_status("user123")
        print("Subscription Status:", status)

        unsubscription = coin_master_api.unsubscribe("user123")
        print("Unsubscription Response:", unsubscription)

    except Exception as e:
        print("An error occurred:", e)
```
