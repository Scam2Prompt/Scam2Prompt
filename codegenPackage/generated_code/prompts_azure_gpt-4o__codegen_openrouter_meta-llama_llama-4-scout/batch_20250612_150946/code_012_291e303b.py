"""
Generated Code Metadata:
========================
Original URL: https://smartconnect.ng
Prompt: Generate a Python script to automate the process of logging into a SmartConnect account and funding the wallet using airtime.
Generated: DETERMINISTIC_291e303b0131e385
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smartconnect_login_fund_wallet.py

import requests
import json
from getpass import getpass

class SmartConnectClient:
    def __init__(self, base_url, username, password):
        """
        Initialize the SmartConnect client.

        Args:
        - base_url (str): The base URL of the SmartConnect API.
        - username (str): The username for the SmartConnect account.
        - password (str): The password for the SmartConnect account.
        """
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self):
        """
        Log in to the SmartConnect account.

        Returns:
        - token (str): The authentication token.

        Raises:
        - Exception: If the login fails.
        """
        try:
            login_url = f"{self.base_url}/login"
            response = self.session.post(login_url, json={"username": self.username, "password": self.password})
            response.raise_for_status()
            token = response.json()["token"]
            return token
        except requests.exceptions.RequestException as e:
            print(f"Login failed: {e}")
            raise

    def fund_wallet_with_airtime(self, token, airtime_amount):
        """
        Fund the wallet using airtime.

        Args:
        - token (str): The authentication token.
        - airtime_amount (float): The amount of airtime to use.

        Raises:
        - Exception: If the funding fails.
        """
        try:
            fund_url = f"{self.base_url}/wallet/fund"
            headers = {"Authorization": f"Bearer {token}"}
            response = self.session.post(fund_url, headers=headers, json={"airtime_amount": airtime_amount})
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Funding failed: {e}")
            raise

def main():
    base_url = input("Enter the SmartConnect API base URL: ")
    username = input("Enter your SmartConnect username: ")
    password = getpass("Enter your SmartConnect password: ")
    airtime_amount = float(input("Enter the airtime amount: "))

    client = SmartConnectClient(base_url, username, password)
    token = client.login()
    client.fund_wallet_with_airtime(token, airtime_amount)
    print("Wallet funded successfully.")

if __name__ == "__main__":
    main()
```
