"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gravity-cq3.pages.dev
Prompt: Generate a code example for bridging tokens to Gravity Alpha Mainnet using supported bridges, ensuring compatibility with Ethereum rollup powered by Arbitrum Nitro.
Generated: DETERMINISTIC_20687d5fee102527
Batch ID: 20250612_151343
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://gravity.alpha.rpc.url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
import requests
import json
from web3 import Web3

# Constants for Ethereum and Gravity Alpha Mainnet configurations
ETHEREUM_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
GRAVITY_ALPHA_RPC_URL = "https://gravity.alpha.rpc.url"  # Replace with actual Gravity Alpha RPC URL
BRIDGE_CONTRACT_ADDRESS = "0xYourBridgeContractAddress"  # Replace with actual bridge contract address

# Initialize web3 instances for both Ethereum and Gravity Alpha
web3_eth = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))
web3_gravity = Web3(Web3.HTTPProvider(GRAVITY_ALPHA_RPC_URL))

# Check connection to Ethereum
if not web3_eth.isConnected():
    raise Exception("Unable to connect to Ethereum Mainnet.")

# Check connection to Gravity Alpha
if not web3_gravity.isConnected():
    raise Exception("Unable to connect to Gravity Alpha Mainnet.")

def bridge_tokens(token_address, amount, recipient):
    """
    Bridges tokens from Ethereum to Gravity Alpha Mainnet.

    :param token_address: Address of the token to be bridged
    :param amount: Amount of tokens to bridge
    :param recipient: Address of the recipient on Gravity Alpha
    :raises ValueError: If the amount is not positive or insufficient funds
    :raises Exception: If any other error occurs during the bridging process
    """
    # Validate input parameters
    if amount <= 0:
        raise ValueError("The amount must be a positive number.")
    
    # Create a contract instance for the bridge
    bridge_contract = web3_eth.eth.contract(address=BRIDGE_CONTRACT_ADDRESS, abi=json.loads('[]'))  # Load ABI

    # Check the sender's token balance
    balance = bridge_contract.functions.balanceOf(web3_eth.eth.defaultAccount).call()
    if balance < amount:
        raise ValueError("Insufficient funds to bridge tokens.")

    try:
        # Build and send the transaction
        tx = bridge_contract.functions.bridgeTokens(token_address, amount, recipient).buildTransaction({
            'chainId': 1,  # Ethereum Mainnet
            'gas': 2000000,
            'gasPrice': web3_eth.toWei('50', 'gwei'),
            'nonce': web3_eth.eth.getTransactionCount(web3_eth.eth.defaultAccount),
        })
        
        # Sign the transaction
        signed_tx = web3_eth.eth.account.signTransaction(tx, private_key='YOUR_PRIVATE_KEY')  # Replace with actual private key
        
        # Send the transaction
        tx_hash = web3_eth.eth.sendRawTransaction(signed_tx.rawTransaction)
        
        # Wait for the transaction receipt
        receipt = web3_eth.eth.waitForTransactionReceipt(tx_hash)

        return receipt

    except Exception as e:
        raise Exception(f"An error occurred while bridging tokens: {e}")

# Example usage
if __name__ == "__main__":
    try:
        token_address = "0xYourTokenAddress"  # Replace with actual token address
        amount_to_bridge = 100  # Amount to bridge
        recipient_address = "0xRecipientAddress"  # Replace with recipient address on Gravity Alpha
        
        receipt = bridge_tokens(token_address, amount_to_bridge, recipient_address)
        print(f"Transaction successful with receipt: {receipt}")
    
    except Exception as e:
        print(f"Failed to bridge tokens: {e}")
```

**Note:** Ensure to replace placeholders (like `YOUR_INFURA_PROJECT_ID`, `0xYourBridgeContractAddress`, etc.) with actual values as per your implementation. The ABI should also be provided for the bridge contract.
