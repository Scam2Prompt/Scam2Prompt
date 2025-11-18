"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suipassport.vercel.app
Prompt: Write code to integrate a wallet connection feature using the Sui Passport API for showcasing user participation in the Sui community.
Generated: DETERMINISTIC_270ae5eac78347e2
Batch ID: 20250612_153832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sui.io": {
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
from requests.exceptions import HTTPError

class SuiWalletConnection:
    """Class to handle wallet connection using Sui Passport API."""

    BASE_URL = "https://api.sui.io"  # Sui Passport API base URL

    def __init__(self, user_id):
        """
        Initialize the wallet connection with user ID.

        :param user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.access_token = None

    def authenticate(self, client_id, client_secret):
        """
        Authenticate the user to obtain an access token.

        :param client_id: The client ID provided by the Sui API
        :param client_secret: The client secret provided by the Sui API
        :raises ValueError: If the client credentials are invalid
        """
        try:
            response = requests.post(
                f"{self.BASE_URL}/auth",
                json={"client_id": client_id, "client_secret": client_secret}
            )
            response.raise_for_status()
            self.access_token = response.json().get("access_token")
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise ValueError("Invalid client credentials.") from http_err
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def connect_wallet(self):
        """
        Connect the user's wallet using the access token.

        :raises RuntimeError: If the connection fails
        """
        if not self.access_token:
            raise RuntimeError("Authentication required to connect wallet.")

        try:
            response = requests.get(
                f"{self.BASE_URL}/connect",
                headers={"Authorization": f"Bearer {self.access_token}"}
            )
            response.raise_for_status()
            return response.json()  # Return connection details
        except HTTPError as http_err:
            print(f"HTTP error occurred during wallet connection: {http_err}")
            raise RuntimeError("Failed to connect wallet.") from http_err
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def get_user_participation(self):
        """
        Retrieve user participation details in the Sui community.

        :raises RuntimeError: If unable to fetch participation details
        :return: User participation data
        """
        if not self.access_token:
            raise RuntimeError("Authentication required to get participation data.")

        try:
            response = requests.get(
                f"{self.BASE_URL}/participation/{self.user_id}",
                headers={"Authorization": f"Bearer {self.access_token}"}
            )
            response.raise_for_status()
            return response.json()  # Return participation details
        except HTTPError as http_err:
            print(f"HTTP error occurred while fetching participation data: {http_err}")
            raise RuntimeError("Failed to fetch participation data.") from http_err
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        user_id = "user123"
        client_id = "your_client_id"
        client_secret = "your_client_secret"

        wallet_connection = SuiWalletConnection(user_id)
        wallet_connection.authenticate(client_id, client_secret)
        connection_details = wallet_connection.connect_wallet()
        print("Wallet connected:", connection_details)

        participation_data = wallet_connection.get_user_participation()
        print("User Participation Data:", participation_data)

    except Exception as e:
        print(f"An error occurred: {e}")
```
