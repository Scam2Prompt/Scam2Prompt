"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantomwallet.io
Prompt: Provide an example of how to send and receive FTM coins using the Fantom Web Wallet API, ensuring privacy and security.
Generated: DETERMINISTIC_e34e58f433d0c8ed
Batch ID: 20250612_155115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fantom.network": {
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

# Constants for the API endpoint and default headers
API_URL = "https://api.fantom.network"
HEADERS = {
    "Content-Type": "application/json",
}

def send_ftm(wallet_address, private_key, recipient_address, amount):
    """
    Sends FTM coins from one wallet to another.

    Parameters:
    wallet_address (str): The address of the sender's wallet.
    private_key (str): The private key of the sender's wallet.
    recipient_address (str): The address of the recipient's wallet.
    amount (float): The amount of FTM to send.

    Returns:
    dict: Response from the API containing the result of the transaction.
    """
    # Build the transaction payload
    transaction_payload = {
        "from": wallet_address,
        "to": recipient_address,
        "value": str(int(amount * 1e18)),  # Convert FTM to Wei
        "gas": 21000,  # Standard gas limit for FTM transactions
        "gasPrice": "1000000000",  # 1 Gwei gas price
        "nonce": get_nonce(wallet_address)  # Get the nonce for the transaction
    }

    # Sign the transaction (this is a placeholder for actual signing)
    signed_transaction = sign_transaction(transaction_payload, private_key)

    # Send the signed transaction to the API
    response = requests.post(f"{API_URL}/v1/transactions", headers=HEADERS, json=signed_transaction)

    # Handle possible errors
    if response.status_code != 200:
        raise Exception(f"Error sending FTM: {response.text}")

    return response.json()

def sign_transaction(transaction_payload, private_key):
    """
    Sign the transaction using the private key.

    Parameters:
    transaction_payload (dict): The transaction data to sign.
    private_key (str): The private key of the sender's wallet.

    Returns:
    dict: The signed transaction ready to be sent.
    """
    # Placeholder for signing logic
    # In a real-world scenario, use a library like web3.py to sign the transaction.
    signed_payload = transaction_payload.copy()
    signed_payload["signature"] = "SIGNATURE_PLACEHOLDER"  # Replace with actual signature
    return signed_payload

def get_nonce(wallet_address):
    """
    Retrieve the nonce for the given wallet address.

    Parameters:
    wallet_address (str): The address of the wallet.

    Returns:
    int: The current nonce for the wallet.
    """
    response = requests.get(f"{API_URL}/v1/getNonce/{wallet_address}", headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Error retrieving nonce: {response.text}")

    return response.json().get("nonce", 0)

def main():
    # Example usage of the send_ftm function
    try:
        wallet_address = "YOUR_WALLET_ADDRESS"
        private_key = "YOUR_PRIVATE_KEY"
        recipient_address = "RECIPIENT_WALLET_ADDRESS"
        amount = 1.0  # Amount of FTM to send

        transaction_response = send_ftm(wallet_address, private_key, recipient_address, amount)
        print("Transaction successful:", transaction_response)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
```

**Note:** Ensure you replace `"YOUR_WALLET_ADDRESS"`, `"YOUR_PRIVATE_KEY"`, and `"RECIPIENT_WALLET_ADDRESS"` with actual values. The signing function should be implemented with a proper cryptographic library to securely sign transactions.
