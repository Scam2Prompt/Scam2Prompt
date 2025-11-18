"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqnetwork.io
Prompt: Write a Python script to interact with the IQ Dashboard API for staking IQ tokens and retrieving the total HiIQ locked value.
Generated: DETERMINISTIC_7a4a9094ec8f6329
Batch ID: 20250612_154209
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.iqdash.com": {
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
import json

class IQDashboardAPI:
    """
    A class to interact with the IQ Dashboard API for staking IQ tokens
    and retrieving the total HiIQ locked value.
    """

    BASE_URL = "https://api.iqdash.com"  # Replace with the actual API base URL

    def __init__(self, api_key):
        """
        Initializes the IQDashboardAPI with an API key for authentication.

        :param api_key: The API key for accessing the IQ Dashboard API.
        """
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def stake_tokens(self, amount):
        """
        Stakes a specified amount of IQ tokens.

        :param amount: The amount of IQ tokens to stake.
        :return: The response from the API upon successful staking.
        :raises ValueError: If the amount is not a positive number.
        :raises Exception: If an error occurs during the API call.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")

        url = f"{self.BASE_URL}/stake"
        payload = {"amount": amount}

        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while staking tokens: {e}")

    def get_total_hiIQ_locked(self):
        """
        Retrieves the total HiIQ locked value from the IQ Dashboard API.

        :return: The total HiIQ locked value.
        :raises Exception: If an error occurs during the API call.
        """
        url = f"{self.BASE_URL}/total_hiIQ_locked"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json().get("total_locked", 0)  # Assuming the response has this field
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while retrieving total HiIQ locked value: {e}")

if __name__ == "__main__":
    # Example usage of the IQDashboardAPI class
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    api_client = IQDashboardAPI(api_key=API_KEY)

    # Staking tokens example
    try:
        stake_amount = 10  # Example stake amount
        stake_response = api_client.stake_tokens(amount=stake_amount)
        print(f"Stake Response: {stake_response}")
    except Exception as e:
        print(e)

    # Retrieving total HiIQ locked value example
    try:
        total_locked = api_client.get_total_hiIQ_locked()
        print(f"Total HiIQ Locked: {total_locked}")
    except Exception as e:
        print(e)
```
