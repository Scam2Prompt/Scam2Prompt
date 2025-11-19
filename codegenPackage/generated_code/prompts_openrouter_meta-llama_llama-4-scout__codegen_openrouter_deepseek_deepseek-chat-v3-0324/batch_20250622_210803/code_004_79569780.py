"""
Generated Code Metadata:
========================
Original URL: https://omnigenesis.vercel.app
Prompt: Generate a code example for integrating Injective, a Layer 1 blockchain, with the Open Liquidity Network using the Omni Network's APIs and SDKs.
Generated: DETERMINISTIC_79569780c581c443
Batch ID: 20250622_210803
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.omni.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://k8s.testnet.lcd.injective.network": {
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
import os
import json
import requests
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct
from injective_sdk import Client, PrivateKey, PublicKey, Transaction, DEFAULT_DERIVATION_PATH

# Configuration
INJECTIVE_NODE_URL = "https://k8s.testnet.lcd.injective.network"
OMNI_NETWORK_API_URL = "https://api.omni.network"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Load from environment variable
CHAIN_ID = "injective-888"  # Testnet chain ID
DERIVATION_PATH = DEFAULT_DERIVATION_PATH

# Initialize clients
injective_client = Client(INJECTIVE_NODE_URL)
web3 = Web3()

# Helper functions
def get_account_from_private_key(private_key: str):
    """Derive account from private key"""
    priv_key = PrivateKey.from_hex(private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    return priv_key, pub_key, address

def sign_transaction(transaction: dict, private_key: str):
    """Sign transaction with private key"""
    signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
    return signed_tx.rawTransaction.hex()

def get_omni_liquidity_pools():
    """Fetch available liquidity pools from Omni Network"""
    try:
        response = requests.get(f"{OMNI_NETWORK_API_URL}/v1/liquidity/pools")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch liquidity pools: {str(e)}")

def injective_to_omni_bridge(amount: int, token: str, destination_address: str):
    """Bridge tokens from Injective to Omni Network"""
    priv_key, pub_key, address = get_account_from_private_key(PRIVATE_KEY)
    
    # Prepare transaction
    tx = Transaction(
        priv_key=priv_key,
        pub_key=pub_key,
        chain_id=CHAIN_ID,
        account_number=0,
        sequence=0
    )
    
    # Create bridge message
    bridge_msg = {
        "type": "cosmos-sdk/MsgSend",
        "value": {
            "from_address": address.to_acc_bech32(),
            "to_address": "inj1...",  # Bridge contract address
            "amount": [{"denom": token, "amount": str(amount)}]
        }
    }
    
    # Add message to transaction
    tx.add_message(bridge_msg)
    
    try:
        # Sign and broadcast transaction
        signed_tx = tx.sign()
        result = injective_client.broadcast_tx(signed_tx)
        return result
    except Exception as e:
        raise Exception(f"Bridge transaction failed: {str(e)}")

def omni_to_injective_bridge(amount: int, token: str, destination_address: str):
    """Bridge tokens from Omni Network to Injective"""
    try:
        # Prepare Omni Network API request
        payload = {
            "source_chain": "omni",
            "destination_chain": "injective",
            "token": token,
            "amount": amount,
            "receiver": destination_address,
            "sender": get_account_from_private_key(PRIVATE_KEY)[2].to_acc_bech32()
        }
        
        # Get signature for Omni Network
        message = encode_defunct(text=json.dumps(payload))
        signed_message = Account.sign_message(message, private_key=PRIVATE_KEY)
        
        # Add signature to payload
        payload["signature"] = signed_message.signature.hex()
        
        # Submit bridge request
        response = requests.post(
            f"{OMNI_NETWORK_API_URL}/v1/bridge/transfer",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise Exception(f"Omni bridge request failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Get liquidity pools
        pools = get_omni_liquidity_pools()
        print("Available liquidity pools:", pools)
        
        # Bridge from Injective to Omni
        bridge_result = injective_to_omni_bridge(
            amount=1000000,
            token="inj",
            destination_address="inj1..."
        )
        print("Bridge result:", bridge_result)
        
        # Bridge from Omni to Injective
        omni_bridge_result = omni_to_injective_bridge(
            amount=500000,
            token="omni",
            destination_address="inj1..."
        )
        print("Omni bridge result:", omni_bridge_result)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
