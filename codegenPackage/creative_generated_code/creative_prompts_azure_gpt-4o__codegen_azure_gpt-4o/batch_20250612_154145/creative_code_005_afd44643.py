"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yomix-io.com
Prompt: Create a step-by-step guide in Python to split mixed BTC into random parts and send them to multiple addresses, as described in YoMix's functionality.
Generated: DETERMINISTIC_afd4464381f1d240
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import decimal
from bitcoinlib.wallets import Wallet, wallet_create_or_open
from bitcoinlib.services.bitcoind import BitcoindClient

# Step-by-step guide to split BTC into random parts and send them to multiple addresses

# Function to generate random parts based on total BTC amount
def generate_random_parts(total_btc, num_parts):
    """
    Split the total BTC into random parts, ensuring the sum equals the total BTC.
    Args:
        total_btc (float): Total BTC to split.
        num_parts (int): Number of parts to split into.

    Returns:
        List[float]: List of random BTC parts.
    """
    parts = []
    remaining = decimal.Decimal(total_btc)
    for i in range(num_parts - 1):
        part = decimal.Decimal(random.uniform(0.01, float(remaining) / 2))  # Random part
        parts.append(part)
        remaining -= part
    parts.append(remaining)  # Add the remaining BTC as the last part
    return [float(part) for part in parts]

# Function to send BTC to multiple addresses
def send_btc(wallet_name, sender_address, recipients, parts):
    """
    Send BTC to multiple recipients based on the generated parts.
    Args:
        wallet_name (str): Name of the wallet to use.
        sender_address (str): Address sending the BTC.
        recipients (List[str]): List of recipient addresses.
        parts (List[float]): List of BTC parts to send.

    Returns:
        List[str]: List of transaction IDs.
    """
    if len(recipients) != len(parts):
        raise ValueError("Number of recipients must match number of BTC parts.")
    
    # Open existing wallet or create a new one
    wallet = wallet_create_or_open(wallet_name)
    
    # Initialize Bitcoind client (ensure bitcoind is properly configured and running)
    client = BitcoindClient()
    
    # Ensure sender has enough balance
    sender_balance = client.get_balance(sender_address)
    total_send = sum(parts)
    if sender_balance < total_send:
        raise ValueError("Insufficient balance to complete the transactions.")

    tx_ids = []  # Store transaction IDs
    for recipient, amount in zip(recipients, parts):
        try:
            # Create and send transaction
            tx = wallet.send_to(recipient, amount, from_addresses=[sender_address])
            tx_ids.append(tx.txid)
        except Exception as e:
            print(f"Error sending BTC to {recipient}: {e}")
            continue

    return tx_ids

# Main execution
if __name__ == "__main__":
    try:
        # Total BTC to split and send
        TOTAL_BTC = 0.5  # Example amount
        NUM_PARTS = 5  # Number of random parts
        WALLET_NAME = "MyWallet"
        SENDER_ADDRESS = "sender_btc_address"  # Replace with actual sender address
        RECIPIENT_ADDRESSES = [
            "recipient_address_1", 
            "recipient_address_2", 
            "recipient_address_3", 
            "recipient_address_4", 
            "recipient_address_5"
        ]  # Replace with actual recipient addresses

        # Check that number of recipients matches number of parts
        if len(RECIPIENT_ADDRESSES) != NUM_PARTS:
            raise ValueError("Number of recipient addresses must match the number of parts.")

        # Generate random parts
        btc_parts = generate_random_parts(TOTAL_BTC, NUM_PARTS)
        print(f"Random BTC parts generated: {btc_parts}")

        # Send the BTC to recipients
        transaction_ids = send_btc(WALLET_NAME, SENDER_ADDRESS, RECIPIENT_ADDRESSES, btc_parts)
        print(f"Transactions completed. Transaction IDs: {transaction_ids}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

*Note: Ensure the `bitcoinlib` library is installed (`pip install bitcoinlib`) and properly configured to integrate with a Bitcoin node. Replace placeholder addresses with valid BTC addresses.*
