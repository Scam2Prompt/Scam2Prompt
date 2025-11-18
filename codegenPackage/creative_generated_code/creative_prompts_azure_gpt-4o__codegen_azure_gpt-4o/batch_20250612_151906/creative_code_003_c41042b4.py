"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ens.gifts
Prompt: Provide an example of using ENS to resolve a domain name to an Ethereum address in a gifting use case.
Generated: DETERMINISTIC_c41042b43825dc92
Batch ID: 20250612_151906
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
# Import the necessary libraries
from web3 import Web3
from ens import ENS

# Configuration: Ethereum node and ENS domain
ETHEREUM_NODE_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
ENS_DOMAIN = "example.eth"  # Replace with the ENS domain name
GIFT_AMOUNT_ETH = 0.01  # Specify the gift amount in ETH

def main():
    try:
        # Connect to Ethereum node
        web3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))
        
        # Check if connection to Ethereum node is successful
        if not web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum node.")
        
        # Initialize ENS resolver
        ns = ENS.fromWeb3(web3)
        
        # Resolve the ENS domain to an Ethereum address
        recipient_address = ns.address(ENS_DOMAIN)
        if not recipient_address:
            raise ValueError(f"Unable to resolve ENS domain: {ENS_DOMAIN}")
        
        print(f"Resolved ENS domain '{ENS_DOMAIN}' to address: {recipient_address}")
        
        # Prepare transaction for sending the gift
        sender_address = web3.eth.accounts[0]  # Assuming the first account in the wallet
        private_key = "YOUR_PRIVATE_KEY"  # Replace with the private key of the sender account

        # Ensure sender address and private key are properly set
        if not sender_address or not private_key:
            raise ValueError("Sender address or private key is not configured.")
        
        # Convert the gift amount to Wei (smallest unit of ETH)
        gift_amount_wei = web3.toWei(GIFT_AMOUNT_ETH, 'ether')
        
        # Build transaction
        transaction = {
            "to": recipient_address,
            "value": gift_amount_wei,
            "gas": 21000,
            "gasPrice": web3.toWei("50", "gwei"),
            "nonce": web3.eth.getTransactionCount(sender_address),
        }
        
        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
        
        # Send the transaction to the Ethereum network
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        
        print(f"Transaction sent! Transaction hash: {web3.toHex(tx_hash)}")
        
    except Exception as e:
        # Handle and log errors
        print(f"Error occurred: {str(e)}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
