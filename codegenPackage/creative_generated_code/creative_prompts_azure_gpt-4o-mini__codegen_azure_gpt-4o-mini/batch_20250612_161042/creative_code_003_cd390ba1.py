"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wemix-shoebill.pages.dev
Prompt: Generate a script to calculate the net APY and borrow limit for a user on the Shoebill Finance platform.
Generated: DETERMINISTIC_cd390ba1261babe8
Batch ID: 20250612_161042
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.shoebill.finance": {
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
import json
import requests

class ShoebillFinance:
    def __init__(self, api_url):
        """
        Initialize the ShoebillFinance class with the API URL.
        
        :param api_url: The base URL of the Shoebill Finance API.
        """
        self.api_url = api_url

    def get_user_data(self, user_id):
        """
        Fetch user data from the Shoebill Finance API.

        :param user_id: The unique identifier of the user.
        :return: A dictionary containing user data.
        :raises ValueError: If the user ID is invalid or not found.
        """
        response = requests.get(f"{self.api_url}/users/{user_id}")

        if response.status_code != 200:
            raise ValueError(f"Error fetching user data: {response.text}")

        return response.json()

    def calculate_net_apy(self, user_data):
        """
        Calculate the net Annual Percentage Yield (APY) for a user.

        :param user_data: A dictionary containing user data.
        :return: The net APY as a float.
        """
        try:
            apy = user_data['apy']
            fees = user_data['fees']
            net_apy = apy - fees
            return round(net_apy, 2)
        except KeyError as e:
            raise ValueError(f"Missing data in user data: {e}")

    def calculate_borrow_limit(self, user_data):
        """
        Calculate the borrow limit for a user based on their balance and leverage.

        :param user_data: A dictionary containing user data.
        :return: The borrow limit as a float.
        """
        try:
            balance = user_data['balance']
            leverage = user_data['leverage']
            borrow_limit = balance * leverage
            return round(borrow_limit, 2)
        except KeyError as e:
            raise ValueError(f"Missing data in user data: {e}")

    def get_financial_metrics(self, user_id):
        """
        Get the financial metrics (net APY and borrow limit) for a user.

        :param user_id: The unique identifier of the user.
        :return: A dictionary with net APY and borrow limit.
        """
        try:
            user_data = self.get_user_data(user_id)
            net_apy = self.calculate_net_apy(user_data)
            borrow_limit = self.calculate_borrow_limit(user_data)

            return {
                "net_apy": net_apy,
                "borrow_limit": borrow_limit
            }
        except ValueError as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    API_URL = "https://api.shoebill.finance"  # Update with the actual API URL
    user_id = "12345"  # Example user ID

    shoebill = ShoebillFinance(API_URL)
    metrics = shoebill.get_financial_metrics(user_id)

    if metrics:
        print(json.dumps(metrics, indent=4))
```
