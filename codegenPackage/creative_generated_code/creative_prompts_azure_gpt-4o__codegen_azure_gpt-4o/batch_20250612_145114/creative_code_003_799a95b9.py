"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Develop a script to automate the connection to the Habbo server, verify account credentials, and load account data, as outlined in the webpage content.
Generated: DETERMINISTIC_799a95b95473b176
Batch ID: 20250612_145114
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.habbo.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.habbo.com`": {
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

class HabboAccountLoader:
    """
    Class to handle connection to the Habbo server, authentication of account credentials, 
    and loading of account data.
    """

    def __init__(self, base_url):
        """
        Initialize the HabboAccountLoader with the server base URL.

        :param base_url: The base URL of the Habbo API.
        """
        self.base_url = base_url

    def authenticate_credentials(self, username, password):
        """
        Authenticate user credentials with the Habbo server.

        :param username: Habbo account username.
        :param password: Habbo account password.
        :return: Authentication token if successful, None otherwise.
        """
        auth_endpoint = f"{self.base_url}/auth"
        payload = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(auth_endpoint, json=payload)
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()
            
            if 'token' in data:
                return data['token']
            else:
                print("Authentication failed. Please check your credentials.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error during authentication: {e}")
            return None

    def load_account_data(self, auth_token):
        """
        Load account data from the Habbo server using the authentication token.

        :param auth_token: The authentication token obtained after successful login.
        :return: Dictionary containing account data, or None if failed.
        """
        account_data_endpoint = f"{self.base_url}/account"
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }

        try:
            response = requests.get(account_data_endpoint, headers=headers)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error loading account data: {e}")
            return None

if __name__ == "__main__":
    # Base URL for the Habbo server API
    HABBO_API_BASE_URL = "https://api.habbo.com"

    # Prompt user for credentials
    username = input("Enter your Habbo username: ")
    password = input("Enter your Habbo password: ")

    # Create an instance of HabboAccountLoader
    loader = HabboAccountLoader(HABBO_API_BASE_URL)

    # Authenticate and retrieve account details
    auth_token = loader.authenticate_credentials(username, password)

    if auth_token:
        account_data = loader.load_account_data(auth_token)
        if account_data:
            print("Account Data Loaded Successfully:")
            print(json.dumps(account_data, indent=4))
        else:
            print("Failed to load account data.")
    else:
        print("Authentication failed.")
```

### Notes:
1. Replace `https://api.habbo.com` with the actual Habbo server's API base URL if it's different.
2. Ensure API endpoints `/auth` and `/account` exist and correctly handle authentication and account data retrieval.
3. This script uses `requests` library; ensure it's installed (`pip install requests`) before executing the code.
