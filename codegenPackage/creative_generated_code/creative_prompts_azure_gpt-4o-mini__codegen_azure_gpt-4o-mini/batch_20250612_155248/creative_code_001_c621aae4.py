"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-altvenusio-git-feat-optimism-venus-protocol.vercel.app
Prompt: Write a script that utilizes the Venus Protocol's algorithmic money market features for lending and borrowing.
Generated: DETERMINISTIC_c621aae4411c9f5a
Batch ID: 20250612_155248
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.venus.io": {
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

class VenusProtocolClient:
    """A client to interact with the Venus Protocol for lending and borrowing cryptocurrencies."""
    
    BASE_URL = "https://api.venus.io"  # Base URL for the Venus Protocol API

    def __init__(self, wallet_address):
        """
        Initialize the VenusProtocolClient.
        
        :param wallet_address: The address of the user's wallet.
        """
        self.wallet_address = wallet_address

    def get_market_data(self):
        """Fetch current market data for lending and borrowing."""
        try:
            response = requests.get(f"{self.BASE_URL}/markets")
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching market data: {e}")
            return None

    def lend(self, asset, amount):
        """
        Lend a specified amount of an asset in the Venus Protocol.
        
        :param asset: The asset to lend (e.g., 'USDC').
        :param amount: The amount to lend.
        :return: Response from the lending transaction.
        """
        try:
            payload = {
                "wallet": self.wallet_address,
                "asset": asset,
                "amount": amount
            }
            response = requests.post(f"{self.BASE_URL}/lend", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error lending asset: {e}")
            return None

    def borrow(self, asset, amount):
        """
        Borrow a specified amount of an asset from the Venus Protocol.
        
        :param asset: The asset to borrow (e.g., 'USDC').
        :param amount: The amount to borrow.
        :return: Response from the borrowing transaction.
        """
        try:
            payload = {
                "wallet": self.wallet_address,
                "asset": asset,
                "amount": amount
            }
            response = requests.post(f"{self.BASE_URL}/borrow", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error borrowing asset: {e}")
            return None

    def get_user_balance(self, asset):
        """
        Fetch the current balance of a specified asset in the user's wallet.
        
        :param asset: The asset to check the balance for (e.g., 'USDC').
        :return: The balance amount or None if an error occurs.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/balance/{self.wallet_address}/{asset}")
            response.raise_for_status()
            return response.json().get('balance', 0)
        except requests.RequestException as e:
            print(f"Error fetching balance for asset {asset}: {e}")
            return None


# Example usage
if __name__ == "__main__":
    USER_WALLET = "your_wallet_address_here"  # Replace with your actual wallet address
    client = VenusProtocolClient(USER_WALLET)

    # Fetch market data
    market_data = client.get_market_data()
    if market_data:
        print(json.dumps(market_data, indent=2))

    # Check balance of USDC
    usdc_balance = client.get_user_balance("USDC")
    print(f"USDC Balance: {usdc_balance}")

    # Lend USDC
    lend_response = client.lend("USDC", 100)
    print(f"Lend Response: {lend_response}")

    # Borrow USDC
    borrow_response = client.borrow("USDC", 50)
    print(f"Borrow Response: {borrow_response}")
```

Ensure to replace `"your_wallet_address_here"` with your actual wallet address when using the script. The code is designed to be clear, robust, and easy to understand, following best practices for readability and error handling.
