"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enkrpt.com
Prompt: Generate a script to synchronize cryptocurrency portfolios across mobile and desktop using the Enkrpt Wallet's multicurrency wallet features.
Generated: DETERMINISTIC_355230d7acee8b44
Batch ID: 20250612_151504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.enkrptwallet.com": {
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
import os
from cryptography.fernet import Fernet

# Constants for Enkrpt Wallet API
ENKRPT_API_BASE_URL = "https://api.enkrptwallet.com"
SYNC_ENDPOINT = "/sync-portfolio"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Function to encrypt data for secure transmission
def encrypt_data(data, encryption_key):
    try:
        cipher = Fernet(encryption_key)
        encrypted_data = cipher.encrypt(json.dumps(data).encode())
        return encrypted_data
    except Exception as e:
        raise ValueError(f"Encryption failed: {e}")

# Function to decrypt data received from the API
def decrypt_data(encrypted_data, encryption_key):
    try:
        cipher = Fernet(encryption_key)
        decrypted_data = cipher.decrypt(encrypted_data).decode()
        return json.loads(decrypted_data)
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")

# Function to synchronize portfolios between mobile and desktop
def synchronize_portfolio(local_portfolio, device_type):
    """
    Synchronizes cryptocurrency portfolios between devices using the Enkrpt Wallet API.

    :param local_portfolio: A dictionary representing the local portfolio.
    :param device_type: The type of device (e.g., 'mobile' or 'desktop').
    :return: None
    """
    try:
        # Validate input
        if not isinstance(local_portfolio, dict):
            raise ValueError("local_portfolio must be a dictionary.")
        if device_type not in ["mobile", "desktop"]:
            raise ValueError("device_type must be 'mobile' or 'desktop'.")

        # Fetch encryption key from an environment variable
        encryption_key = os.getenv("ENCRYPTION_KEY")
        if not encryption_key:
            raise ValueError("Encryption key not set in environment variables.")
        encryption_key = encryption_key.encode()

        # Encrypt local portfolio data before sending
        encrypted_portfolio = encrypt_data(local_portfolio, encryption_key)

        # Prepare API request payload
        payload = {
            "api_key": API_KEY,
            "device_type": device_type,
            "encrypted_portfolio": encrypted_portfolio.decode()
        }

        # Send request to Enkrpt Wallet API
        response = requests.post(ENKRPT_API_BASE_URL + SYNC_ENDPOINT, json=payload)

        # Check for errors in the API response
        if response.status_code != 200:
            raise ValueError(f"API request failed with status code {response.status_code}: {response.text}")

        # Decrypt the response data from the API
        encrypted_response_data = response.json().get("encrypted_data")
        if not encrypted_response_data:
            raise ValueError("No encrypted data found in the API response.")

        synchronized_portfolio = decrypt_data(encrypted_response_data.encode(), encryption_key)

        # Output the synchronized portfolio
        print("Portfolio synchronized successfully:")
        print(json.dumps(synchronized_portfolio, indent=2))

    except Exception as e:
        print(f"Error during synchronization: {e}")

# Example usage
if __name__ == "__main__":
    # Sample local portfolio dictionary
    local_portfolio = {
        "BTC": 1.2345,
        "ETH": 10.9876,
        "USDT": 5000.00
    }

    # Device type: 'mobile' or 'desktop'
    device_type = "mobile"

    # Synchronize portfolio
    synchronize_portfolio(local_portfolio, device_type)
```
