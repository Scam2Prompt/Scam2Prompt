"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-stockfinancemarket.com
Prompt: Generate a script to automate the process of creating a trading account, adding funds, and requesting withdrawals as described on the Multi-stock Finance Market website.
Generated: DETERMINISTIC_a138dd663929b61e
Batch ID: 20250612_150116
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multistockfinance.com": {
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

class TradingAccountManager:
    """
    A class to manage a trading account, allowing for account creation,
    fund deposits, and withdrawal requests.
    """

    BASE_URL = 'https://api.multistockfinance.com'

    def __init__(self, username, password):
        """
        Initializes the TradingAccountManager with credentials.

        Args:
            username (str): The username for the trading account.
            password (str): The password for the trading account.
        """
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.account_id = None

    def create_account(self):
        """
        Creates a trading account by sending a POST request to the API.

        Raises:
            Exception: If account creation fails.
        """
        try:
            response = self.session.post(f'{self.BASE_URL}/create_account', json={
                'username': self.username,
                'password': self.password
            })
            response.raise_for_status()  # Raise an error for bad responses
            self.account_id = response.json().get('account_id')
            print(f"Account created successfully with ID: {self.account_id}")
        except requests.RequestException as e:
            raise Exception(f"Failed to create account: {e}")

    def add_funds(self, amount):
        """
        Adds funds to the trading account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            Exception: If fund addition fails.
        """
        try:
            response = self.session.post(f'{self.BASE_URL}/add_funds', json={
                'account_id': self.account_id,
                'amount': amount
            })
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Successfully added ${amount:.2f} to account ID: {self.account_id}")
        except requests.RequestException as e:
            raise Exception(f"Failed to add funds: {e}")

    def request_withdrawal(self, amount):
        """
        Requests a withdrawal from the trading account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            Exception: If withdrawal request fails.
        """
        try:
            response = self.session.post(f'{self.BASE_URL}/request_withdrawal', json={
                'account_id': self.account_id,
                'amount': amount
            })
            response.raise_for_status()  # Raise an error for bad responses
            print(f"Withdrawal of ${amount:.2f} requested successfully from account ID: {self.account_id}")
        except requests.RequestException as e:
            raise Exception(f"Failed to request withdrawal: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Initialize the TradingAccountManager with user credentials
        account_manager = TradingAccountManager(username='your_username', password='your_password')
        
        # Create a new trading account
        account_manager.create_account()
        
        # Add funds to the trading account
        account_manager.add_funds(1000.00)
        
        # Request a withdrawal from the trading account
        account_manager.request_withdrawal(200.00)
    except Exception as e:
        print(f"An error occurred: {e}")
```
