"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-coin-mixer.com
Prompt: Write code to implement a refund mechanism for TONCOIN transactions sent to the TONCOIN Mixer from an exchange wallet or contract wallet.
Generated: DETERMINISTIC_58e2cd9e30b8e2a7
Batch ID: 20250612_152906
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{TON_NETWORK}.toncenter.com/api/v2": {
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
import os
from tonclient.client import TonClient, ClientConfig
from tonclient.types import KeyPair, Abi, ParamsOfQuery, ParamsOfEncodeMessage, ParamsOfSendMessage, ParamsOfWaitForTransaction

# TONCOIN Mixer Refund Mechanism

# Configuration Constants
TON_NETWORK = "mainnet"  # Change to "testnet" for testing
TON_API_URL = f"https://{TON_NETWORK}.toncenter.com/api/v2"
TON_API_KEY = os.getenv("TON_API_KEY")  # Store your TON API key securely
MIXER_CONTRACT_ADDRESS = "EQ***********************"  # Replace with the mixer contract address
MIXER_ABI_PATH = "./mixer.abi.json"  # Path to the mixer contract ABI file

# Initialize TON client
client = TonClient(config=ClientConfig(network=TON_API_URL, api_key=TON_API_KEY))

def load_mixer_abi():
    """
    Load the mixer contract ABI.

    Returns:
        dict: ABI dictionary.
    """
    if not os.path.exists(MIXER_ABI_PATH):
        raise FileNotFoundError(f"Mixer ABI file not found at {MIXER_ABI_PATH}")
    with open(MIXER_ABI_PATH, 'r') as abi_file:
        return Abi.Contract(value=abi_file.read())

def validate_transaction(sender_address: str) -> bool:
    """
    Validate if the transaction is eligible for a refund.

    Args:
        sender_address (str): The sender's wallet address.

    Returns:
        bool: True if eligible, False otherwise.
    """
    # Fetch transaction details (replace with actual validation logic)
    # Example: Check if sender_address matches specific rules
    return sender_address.startswith("0:") or sender_address.startswith("1:")

def process_refund(sender_address: str, amount: int, keypair: KeyPair):
    """
    Process refund to the sender.

    Args:
        sender_address (str): The sender's wallet address.
        amount (int): Amount to refund in nanotons.
        keypair (KeyPair): KeyPair for signing the transaction.
    
    Raises:
        Exception: If refund fails.
    """
    try:
        # Load mixer ABI
        mixer_abi = load_mixer_abi()

        # Encode refund message
        encoded_message = client.abi.encode_message(
            ParamsOfEncodeMessage(
                abi=mixer_abi,
                signer=KeyPair(secret=keypair.secret, public=keypair.public),
                address=MIXER_CONTRACT_ADDRESS,
                call_set={"function_name": "refund", "input": {"recipient": sender_address, "amount": amount}},
                is_internal=True
            )
        )

        # Send the refund transaction
        send_result = client.processing.send_message(
            ParamsOfSendMessage(
                message=encoded_message.message,
                abi=mixer_abi
            )
        )

        # Wait for transaction to finalize
        transaction_result = client.processing.wait_for_transaction(
            ParamsOfWaitForTransaction(
                abi=mixer_abi,
                message=encoded_message.message,
                send_events=False
            )
        )

        print(f"Refund successful. Transaction ID: {transaction_result.transaction.id}")
    except Exception as e:
        print(f"Refund failed: {e}")
        raise

def handle_incoming_transactions():
    """
    Handle incoming transactions to the TONCOIN mixer.

    This function scans the mixer contract for incoming transactions and processes refunds when required.
    """
    try:
        # Query incoming transactions (replace with actual query logic)
        query_result = client.net.query(
            ParamsOfQuery(
                query="transactions",
                result="id, sender, value",
                limit=100,  # Limit number of transactions to process
                filter={"account_addr": {"eq": MIXER_CONTRACT_ADDRESS}}
            )
        )

        for transaction in query_result.result:
            sender_address = transaction['sender']
            amount = int(transaction['value'])

            # Validate transaction for refund
            if validate_transaction(sender_address):
                keypair = KeyPair(public=os.getenv("TON_MIXER_PUBLIC_KEY"), secret=os.getenv("TON_MIXER_SECRET_KEY"))
                process_refund(sender_address, amount, keypair)
            else:
                print(f"Transaction {transaction['id']} from {sender_address} ignored (not eligible for refund).")

    except Exception as e:
        print(f"Error handling transactions: {e}")
        raise

if __name__ == "__main__":
    print("Starting TONCOIN Mixer Refund Mechanism...")
    handle_incoming_transactions()
```
