"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omantel.net
Prompt: Write code to integrate with Omantel's API for checking postpaid plan details, including Baqati and roaming options.
Generated: DETERMINISTIC_a445195a5f0bcb11
Batch ID: 20250612_151519
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.omantel.om/v1/": {
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

class OmantelAPI:
    """
    A class to interact with Omantel's API for checking postpaid plan details.
    """

    BASE_URL = "https://api.omantel.om/v1/"

    def __init__(self, api_key):
        """
        Initializes the OmantelAPI class with the provided API key.

        Args:
            api_key (str): Your API key for authenticating requests.
        """
        self.api_key = api_key

    def _get_headers(self):
        """
        Constructs the headers for the API request.

        Returns:
            dict: The headers including the authorization token.
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_postpaid_plan_details(self, plan_id):
        """
        Fetches postpaid plan details by plan ID.

        Args:
            plan_id (str): The ID of the postpaid plan to retrieve.

        Returns:
            dict: The details of the postpaid plan.

        Raises:
            ValueError: If the plan ID is not provided.
            Exception: If the API request fails.
        """
        if not plan_id:
            raise ValueError("Plan ID must be provided.")

        url = f"{self.BASE_URL}postpaid/plans/{plan_id}"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            # Handle other requests exceptions
            raise Exception(f"Error occurred while requesting data: {req_err}")

    def get_baqati_options(self):
        """
        Fetches available Baqati options.

        Returns:
            dict: The available Baqati options.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.BASE_URL}postpaid/baqati"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            # Handle other requests exceptions
            raise Exception(f"Error occurred while requesting Baqati options: {req_err}")

    def get_roaming_options(self):
        """
        Fetches roaming options available for postpaid plans.

        Returns:
            dict: The available roaming options.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.BASE_URL}postpaid/roaming"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            # Handle other requests exceptions
            raise Exception(f"Error occurred while requesting roaming options: {req_err}")

# Example usage:
# if __name__ == "__main__":
#     api_key = "YOUR_API_KEY_HERE"
#     omantel_api = OmantelAPI(api_key)
#     try:
#         plan_details = omantel_api.get_postpaid_plan_details("12345")
#         baqati_options = omantel_api.get_baqati_options()
#         roaming_options = omantel_api.get_roaming_options()
#         print(plan_details, baqati_options, roaming_options)
#     except Exception as e:
#         print(f"An error occurred: {e}")
```
