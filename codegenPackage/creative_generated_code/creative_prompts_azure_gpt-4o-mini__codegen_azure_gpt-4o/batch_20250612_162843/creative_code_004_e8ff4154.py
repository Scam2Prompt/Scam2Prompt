"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbrowser.ru
Prompt: Provide an example of a mini app that utilizes the TON ecosystem features.
Generated: DETERMINISTIC_e8ff4154089afb3f
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Mini TON Ecosystem App: Fetch Account Balance and Send a Transaction

This app demonstrates interacting with the TON blockchain using the TonLib library.
It fetches the balance of a TON wallet and sends a transaction to another account.

Dependencies:
1. Install `ton` library: pip install ton
2. You need a TON wallet and API key for testing purposes.

Ensure your TON Wallet and API keys are secure and never hardcode sensitive data.
"""

import os
from ton import TonClient, Wallet, TonException

# Configuration variables
TON_API_KEY = os.getenv("TON_API_KEY")  # Set your TON API key as an environment variable
TON_WALLET_SECRET = os.getenv("TON_WALLET_SECRET")  # Set your wallet secret as an environment variable
RECIPIENT_ADDRESS = "EQD5XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with recipient wallet address
AMOUNT_TO_SEND = 0.1  # Amount to send in TON

# Initialize the TON client
try:
    client = TonClient(api_key=TON_API_KEY)
except Exception as e:
    print(f"Failed to initialize TON client: {e}")
    exit(1)

def fetch_balance(wallet_address: str):
    """
    Fetch the balance of a TON wallet.

    :param wallet_address: TON wallet address
    :return: Balance in TON
    """
    try:
        balance = client.get_balance(wallet_address)
        return balance
    except TonException as e:
        print(f"Error fetching balance: {e}")
        return None

def send_transaction(wallet: Wallet, recipient_address: str, amount: float):
    """
    Send TONs to another wallet.

    :param wallet: Wallet instance for sending
    :param recipient_address: Recipient wallet address
    :param amount: Amount to send in TON
    :return: Transaction result
    """
    try:
        result = wallet.send_transaction(recipient_address, amount)
        return result
    except TonException as e:
        print(f"Error sending transaction: {e}")
        return None

def main():
    """
    Main function to demonstrate TON wallet operations.
    """
    # Create a wallet instance
    try:
        wallet = Wallet(client, TON_WALLET_SECRET)
        wallet_address = wallet.get_address()
        print(f"Wallet Address: {wallet_address}")
    except TonException as e:
        print(f"Error initializing wallet: {e}")
        return

    # Fetch wallet balance
    balance = fetch_balance(wallet_address)
    if balance is not None:
        print(f"Wallet Balance: {balance} TON")

    # Send a transaction
    if balance and balance > AMOUNT_TO_SEND:
        print(f"Sending {AMOUNT_TO_SEND} TON to {RECIPIENT_ADDRESS}...")
        transaction_result = send_transaction(wallet, RECIPIENT_ADDRESS, AMOUNT_TO_SEND)
        if transaction_result:
            print(f"Transaction successful! ID: {transaction_result['id']}")
        else:
            print("Transaction failed.")
    else:
        print("Insufficient balance to send transaction.")

if __name__ == "__main__":
    main()
```

**Note:**
- Replace `RECIPIENT_ADDRESS` and environment variables (`TON_API_KEY`, `TON_WALLET_SECRET`) with valid data.
- Ensure you have the correct permissions and sufficient balance for transactions during testing.
- Use a secure method to store wallet secrets and API keys, such as environment variables or secure vault services.
