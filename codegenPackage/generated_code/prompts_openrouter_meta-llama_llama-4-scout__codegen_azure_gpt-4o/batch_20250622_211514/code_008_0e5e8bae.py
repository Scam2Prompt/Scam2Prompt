"""
Generated Code Metadata:
========================
Original URL: https://debridge-finance.org
Prompt: "Develop a code example for integrating deBridge Finance with a Layer 2 solution to reduce transaction costs and increase throughput."
Generated: DETERMINISTIC_0e5e8baec728af54
Batch ID: 20250622_211514
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-layer2-rpc-url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.debridge.finance/v1.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware

# Constants
DEBRIDGE_API_URL = "https://api.debridge.finance/v1.0"
LAYER2_RPC_URL = "https://your-layer2-rpc-url"  # Replace with your Layer 2 RPC URL
PRIVATE_KEY = "your-private-key"  # Replace with your private key
WALLET_ADDRESS = "your-wallet-address"  # Replace with your wallet address
DEBRIDGE_GATEWAY_CONTRACT = "0xYourDeBridgeGatewayContractAddress"  # Replace with the deBridge gateway contract address

# Initialize Web3 connection to Layer 2
web3 = Web3(Web3.HTTPProvider(LAYER2_RPC_URL))

# Add middleware for Layer 2 (if using a PoA chain like Polygon or BSC)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Ensure connection is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Layer 2 RPC")

# Load the deBridge Gateway contract ABI (replace with actual ABI)
DEBRIDGE_GATEWAY_ABI = [
    # Add the ABI of the deBridge Gateway contract here
]

# Initialize the deBridge Gateway contract
debridge_gateway = web3.eth.contract(
    address=web3.toChecksumAddress(DEBRIDGE_GATEWAY_CONTRACT),
    abi=DEBRIDGE_GATEWAY_ABI
)

def get_debridge_fee(asset_id, amount):
    """
    Fetches the estimated fee for a cross-chain transfer from the deBridge API.
    :param asset_id: The asset ID to transfer (e.g., token address on source chain).
    :param amount: The amount to transfer.
    :return: The estimated fee in the source chain's native currency.
    """
    try:
        response = requests.get(
            f"{DEBRIDGE_API_URL}/estimate-fee",
            params={"assetId": asset_id, "amount": amount}
        )
        response.raise_for_status()
        return response.json().get("fee")
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch fee from deBridge API: {e}")

def send_cross_chain_transfer(asset_id, amount, destination_chain_id, receiver_address):
    """
    Sends a cross-chain transfer using the deBridge Gateway contract.
    :param asset_id: The asset ID to transfer (e.g., token address on source chain).
    :param amount: The amount to transfer.
    :param destination_chain_id: The destination chain ID.
    :param receiver_address: The receiver's address on the destination chain.
    """
    try:
        # Fetch the estimated fee
        fee = get_debridge_fee(asset_id, amount)
        print(f"Estimated fee: {fee}")

        # Build the transaction
        transaction = debridge_gateway.functions.send(
            asset_id,
            amount,
            destination_chain_id,
            receiver_address,
            fee,
            False,  # Use fallback address (set to True if needed)
            "0x"  # Optional data (empty in this case)
        ).buildTransaction({
            "from": WALLET_ADDRESS,
            "value": web3.toWei(fee, "ether"),  # Include the fee in the transaction
            "gas": 2000000,  # Adjust gas limit as needed
            "gasPrice": web3.toWei("10", "gwei"),  # Adjust gas price as needed
            "nonce": web3.eth.getTransactionCount(WALLET_ADDRESS)
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction sent! Hash: {web3.toHex(tx_hash)}")

        # Wait for the transaction receipt
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Transaction confirmed! Block number: {receipt.blockNumber}")

    except Exception as e:
        raise RuntimeError(f"Failed to send cross-chain transfer: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace with actual values
        ASSET_ID = "0xYourTokenAddress"  # Token address on the source chain
        AMOUNT = 100  # Amount to transfer
        DESTINATION_CHAIN_ID = 137  # Destination chain ID (e.g., Polygon)
        RECEIVER_ADDRESS = "0xReceiverAddressOnDestinationChain"

        send_cross_chain_transfer(ASSET_ID, AMOUNT, DESTINATION_CHAIN_ID, RECEIVER_ADDRESS)
    except Exception as e:
        print(f"Error: {e}")
```
