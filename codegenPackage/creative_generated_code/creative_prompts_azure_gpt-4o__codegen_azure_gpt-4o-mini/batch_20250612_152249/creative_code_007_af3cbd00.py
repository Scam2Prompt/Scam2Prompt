"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Write a tutorial explaining how to use CVEX's affiliate program API to track referrals and calculate rewards in USDC.
Generated: DETERMINISTIC_af3cbd00ec418351
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cvex.com": {
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

class CVEXAffiliateAPI:
    """
    A class to interact with CVEX's affiliate program API.
    This class provides methods to track referrals and calculate rewards in USDC.
    """

    def __init__(self, api_key, base_url='https://api.cvex.com'):
        """
        Initializes the CVEXAffiliateAPI with the API key and base URL.

        :param api_key: Your affiliate API key.
        :param base_url: Base URL for the CVEX API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _get_headers(self):
        """
        Constructs the headers for API requests.

        :return: A dictionary of headers.
        """
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def track_referral(self, referral_code):
        """
        Tracks a referral using the provided referral code.

        :param referral_code: The unique code for the referral.
        :return: Response from the API.
        """
        url = f'{self.base_url}/referrals/track'
        payload = {'referral_code': referral_code}
        
        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error tracking referral: {e}")
            return None

    def calculate_rewards(self, user_id):
        """
        Calculates the rewards for a specific user in USDC.

        :param user_id: The unique identifier for the user.
        :return: The reward amount in USDC or None if there was an error.
        """
        url = f'{self.base_url}/rewards/calculate'
        payload = {'user_id': user_id}

        try:
            response = requests.post(url, json=payload, headers=self._get_headers())
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json().get('reward_amount', 0)
        except requests.exceptions.RequestException as e:
            print(f"Error calculating rewards: {e}")
            return None

# Example usage of the CVEXAffiliateAPI class
if __name__ == "__main__":
    # Initialize with your actual API key
    api_key = 'YOUR_API_KEY_HERE'
    affiliate_api = CVEXAffiliateAPI(api_key)

    # Tracking a referral
    referral_code = 'EXAMPLE_REFERRAL_CODE'
    referral_response = affiliate_api.track_referral(referral_code)
    print(f"Referral tracking response: {referral_response}")

    # Calculating rewards for a user
    user_id = 'USER_ID_HERE'
    reward_amount = affiliate_api.calculate_rewards(user_id)
    print(f"User's reward amount in USDC: {reward_amount}")
```
