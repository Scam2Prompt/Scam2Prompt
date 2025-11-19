"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubles.sellpass.io
Prompt: Describe how to create a referral program for digital product sales using Sellpass's built-in features.
Generated: DETERMINISTIC_3a2c37e309236196
Batch ID: 20250612_163625
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sellpass.com/v1/referrals": {
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
# referral_program.py

class ReferralProgram:
    """
    A class to create and manage a referral program for digital product sales using Sellpass API.
    """

    def __init__(self, api_key):
        """
        Initialize the ReferralProgram with the necessary API key.

        Args:
            api_key (str): The API key for authenticating with Sellpass.
        """
        self.api_key = api_key
        self.base_url = "https://api.sellpass.com/v1/referrals"

    def create_referral_link(self, product_id, referrer_email):
        """
        Create a referral link for the given product and referrer.

        Args:
            product_id (str): The ID of the product to be referred.
            referrer_email (str): The email of the referrer.

        Returns:
            str: The generated referral link.

        Raises:
            Exception: If the API call fails.
        """
        try:
            response = self._make_api_call("POST", {"product_id": product_id, "referrer_email": referrer_email})
            return response.get("referral_link")
        except Exception as e:
            raise Exception(f"Failed to create referral link: {str(e)}")

    def _make_api_call(self, method, data):
        """
        Make an API call to the Sellpass API.

        Args:
            method (str): The HTTP method (GET, POST, etc.).
            data (dict): The payload for the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: If the API call fails.
        """
        import requests

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        url = self.base_url
        try:
            response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def track_referral(self, referral_code):
        """
        Track a referral using its unique code.

        Args:
            referral_code (str): The unique code for the referral.

        Returns:
            dict: The details of the referral.

        Raises:
            Exception: If the API call fails.
        """
        try:
            response = self._make_api_call("GET", {"referral_code": referral_code})
            return response
        except Exception as e:
            raise Exception(f"Failed to track referral: {str(e)}")

# Example usage (to be used in a separate script):
if __name__ == "__main__":
    API_KEY = "your_sellpass_api_key"
    referral_program = ReferralProgram(API_KEY)

    # Create a referral link
    try:
        link = referral_program.create_referral_link("product_id_123", "referrer@example.com")
        print(f"Referral link created: {link}")
    except Exception as e:
        print(e)

    # Track a referral
    try:
        referral_details = referral_program.track_referral("unique_referral_code")
        print(f"Referral details: {referral_details}")
    except Exception as e:
        print(e)
```
