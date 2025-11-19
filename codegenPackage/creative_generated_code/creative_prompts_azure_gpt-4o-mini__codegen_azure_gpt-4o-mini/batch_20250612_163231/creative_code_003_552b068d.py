"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amldetect.app
Prompt: Generate a Python script that utilizes the AMLBot services for KYC and AML compliance checks.
Generated: DETERMINISTIC_552b068d00a31f5e
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.amlbot.com/v1": {
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

class AMLBotClient:
    """
    A client to interact with the AMLBot service for KYC and AML compliance checks.
    """

    BASE_URL = "https://api.amlbot.com/v1"

    def __init__(self, api_key):
        """
        Initializes the AMLBotClient with an API key.

        Args:
            api_key (str): The API key for authenticating with AMLBot.
        """
        self.api_key = api_key

    def _request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the AMLBot API.

        Args:
            endpoint (str): The API endpoint to call.
            method (str): The HTTP method to use (GET or POST).
            data (dict): The data to send with the request (for POST).

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the request fails or returns an error.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                response = requests.get(url, headers=headers)

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error while calling AMLBot API: {str(e)}")

    def check_kyc(self, user_data):
        """
        Checks the KYC compliance for a given user.

        Args:
            user_data (dict): A dictionary containing user information.

        Returns:
            dict: The response from the KYC check API.
        """
        return self._request('kyc/check', method='POST', data=user_data)

    def check_aml(self, user_data):
        """
        Checks the AML compliance for a given user.

        Args:
            user_data (dict): A dictionary containing user information.

        Returns:
            dict: The response from the AML check API.
        """
        return self._request('aml/check', method='POST', data=user_data)

if __name__ == "__main__":
    # Example usage of the AMLBotClient
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    aml_bot = AMLBotClient(API_KEY)

    # Sample user data for KYC/AML checks
    user_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "country": "US",
        "birthdate": "1980-01-01"
    }

    try:
        kyc_response = aml_bot.check_kyc(user_data)
        print("KYC Response:", json.dumps(kyc_response, indent=2))

        aml_response = aml_bot.check_aml(user_data)
        print("AML Response:", json.dumps(aml_response, indent=2))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
