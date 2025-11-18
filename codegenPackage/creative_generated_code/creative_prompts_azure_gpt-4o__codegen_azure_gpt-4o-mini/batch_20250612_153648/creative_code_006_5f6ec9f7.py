"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9ias90dia90sdi9asidasdk.pages.dev
Prompt: Write a tutorial for developers on how to use THORChain's synthetic assets and lending features to build a decentralized finance (DeFi) application.
Generated: DETERMINISTIC_5f6ec9f7f0b8ae5e
Batch ID: 20250612_153648
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.thorchain.info/v1/assets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.thorchain.info": {
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
# Import necessary libraries for web3 interaction and THORChain API
import requests
from web3 import Web3

# Constants for THORChain
THORCHAIN_RPC_URL = "https://rpc.thorchain.info"  # Sample RPC URL
THORCHAIN_ASSET_API_URL = "https://api.thorchain.info/v1/assets"  # THORChain Asset API

# Initialize a Web3 instance
w3 = Web3(Web3.HTTPProvider(THORCHAIN_RPC_URL))

def check_network():
    """
    Check if connected to the THORChain network.
    
    Returns:
        bool: True if connected, False otherwise.
    """
    return w3.isConnected()

def fetch_synthetic_assets():
    """
    Fetch the list of synthetic assets available on THORChain.
    
    Returns:
        list: A list of synthetic assets data.
    """
    try:
        response = requests.get(THORCHAIN_ASSET_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching synthetic assets: {e}")
        return []

def lend_asset(asset, amount, recipient):
    """
    Lend a specified amount of a synthetic asset to a recipient.
    
    Parameters:
        asset (str): The symbol of the synthetic asset to lend.
        amount (float): The amount of the asset to lend.
        recipient (str): The address of the recipient.
    
    Returns:
        str: Transaction hash if successful, otherwise None.
    """
    # Placeholder for lending logic
    try:
        # In a real application, you would construct and send a transaction here.
        # This is a mock transaction for demonstration purposes.
        transaction = {
            'to': recipient,
            'value': w3.toWei(amount, 'ether'),  # Convert amount to wei
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(w3.eth.defaultAccount),
        }
        
        # Sign and send transaction (mocked)
        # signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        # tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        
        # For demonstration, we will return a mock transaction hash
        return "0xMockTransactionHash"
    except Exception as e:
        print(f"Error lending asset: {e}")
        return None

def main():
    """
    Main function to run the tutorial example.
    """
    if not check_network():
        print("Unable to connect to THORChain network.")
        return
    
    # Fetch available synthetic assets
    assets = fetch_synthetic_assets()
    print("Available Synthetic Assets:")
    for asset in assets:
        print(f"- {asset['symbol']}")

    # Example of lending an asset (these values are placeholders)
    asset_to_lend = 'BTC'  # Sample synthetic asset
    amount_to_lend = 0.1    # Amount to lend
    recipient_address = "0xRecipientAddress"  # Sample recipient address

    tx_hash = lend_asset(asset_to_lend, amount_to_lend, recipient_address)
    if tx_hash:
        print(f"Asset lent successfully! Transaction hash: {tx_hash}")
    else:
        print("Lending asset failed.")

if __name__ == "__main__":
    main()
```
