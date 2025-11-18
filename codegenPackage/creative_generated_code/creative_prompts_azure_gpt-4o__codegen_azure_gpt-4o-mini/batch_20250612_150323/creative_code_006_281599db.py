"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reown.com
Prompt: Explain how Reown's Developer Cloud can be used to streamline the integration of onchain UX features into a payments platform. Include code examples.
Generated: DETERMINISTIC_281599db8c56ce46
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.reown.com/v1": {
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

class ReownDeveloperCloud:
    """
    A class to interact with Reown's Developer Cloud for integrating on-chain UX features
    into a payments platform.
    """

    BASE_URL = "https://api.reown.com/v1"

    def __init__(self, api_key):
        """
        Initialize the ReownDeveloperCloud instance with the provided API key.

        :param api_key: str - The API key for authenticating with Reown's Developer Cloud.
        """
        self.api_key = api_key

    def get_onchain_features(self):
        """
        Retrieve available on-chain features from Reown's Developer Cloud.

        :return: dict - A dictionary containing available on-chain features.
        :raises Exception: Raises an exception if the request fails.
        """
        endpoint = f"{self.BASE_URL}/features"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(endpoint, headers=headers)

            # Check if the request was successful
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise

    def integrate_payment(self, payment_data):
        """
        Integrate an on-chain payment using Reown's Developer Cloud.

        :param payment_data: dict - The payment data containing necessary information.
        :return: dict - A dictionary with the response from the payment integration.
        :raises Exception: Raises an exception if the request fails.
        """
        endpoint = f"{self.BASE_URL}/payments"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        try:
            response = requests.post(endpoint, json=payment_data, headers=headers)

            # Check if the request was successful
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log other errors
            raise


# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with the actual API key from Reown Developer Cloud
    api_key = "your_api_key"
    reown = ReownDeveloperCloud(api_key)

    # Retrieve on-chain features
    try:
        features = reown.get_onchain_features()
        print("Available On-chain Features:", features)
    except Exception as e:
        print("Failed to retrieve features:", e)

    # Example payment data
    payment_data = {
        "amount": 100.00,
        "currency": "USD",
        "recipient": "recipient_address",
        "description": "Payment for services"
    }

    # Integrate a payment
    try:
        payment_response = reown.integrate_payment(payment_data)
        print("Payment Integration Response:", payment_response)
    except Exception as e:
        print("Failed to integrate payment:", e)
```
