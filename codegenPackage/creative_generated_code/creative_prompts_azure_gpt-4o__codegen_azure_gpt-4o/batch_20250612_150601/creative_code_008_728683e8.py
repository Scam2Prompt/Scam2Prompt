"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-box.web.app
Prompt: Develop a script to implement dynamic royalties for NFTs minted using the Open Creator Protocol, as highlighted in the Magic Box section.
Generated: DETERMINISTIC_728683e85a51cfee
Batch ID: 20250612_150601
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
import json
from web3 import Web3
from web3.exceptions import ContractLogicError

# Constants
RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your RPC URL
CONTRACT_ADDRESS = "0xYourNFTContractAddress"  # Replace with your NFT contract address
ABI = json.loads("""[YOUR_CONTRACT_ABI_HERE]""")  # Replace with your contract ABI
PRIVATE_KEY = "0xYourPrivateKey"  # Replace with your private key
WALLET_ADDRESS = "0xYourWalletAddress"  # Replace with your wallet address

# Initialize web3 connection
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Load NFT contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def set_dynamic_royalty(token_id: int, royalty_percentage: float):
    """
    Updates the royalty percentage for a specific NFT token.
    
    Args:
        token_id (int): The ID of the NFT token to set royalties for.
        royalty_percentage (float): The royalty percentage as a decimal (e.g., 0.05 for 5%).
    
    Returns:
        str: Transaction hash.
    """
    if not (0 <= royalty_percentage <= 1):
        raise ValueError("Royalty percentage must be between 0 and 1.")

    try:
        # Build the transaction
        transaction = contract.functions.setRoyalty(token_id, int(royalty_percentage * 10000)).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': 200000,  # Adjust gas limit as necessary
            'gasPrice': web3.toWei('20', 'gwei'),  # Adjust gas price as necessary
            'nonce': web3.eth.get_transaction_count(WALLET_ADDRESS),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return web3.toHex(tx_hash)

    except ContractLogicError as e:
        raise RuntimeError(f"Contract execution error: {e}")
    except Exception as e:
        raise RuntimeError(f"Error setting dynamic royalty: {e}")

def get_royalty_info(token_id: int):
    """
    Retrieves the current royalty info for a specific NFT token.
    
    Args:
        token_id (int): The ID of the NFT token to retrieve royalties for.
    
    Returns:
        dict: Dictionary containing royalty info.
    """
    try:
        royalty_info = contract.functions.royaltyInfo(token_id).call()
        return {
            "recipient": royalty_info[0],
            "royalty_percentage": royalty_info[1] / 10000
        }
    except ContractLogicError as e:
        raise RuntimeError(f"Contract execution error: {e}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving royalty info: {e}")

if __name__ == "__main__":
    # Example Usage
    try:
        token_id = 1
        new_royalty_percentage = 0.075  # 7.5%

        # Set dynamic royalty
        tx_hash = set_dynamic_royalty(token_id, new_royalty_percentage)
        print(f"Royalty updated successfully. Transaction hash: {tx_hash}")

        # Get updated royalty info
        royalty_info = get_royalty_info(token_id)
        print(f"Updated Royalty Info: {royalty_info}")

    except Exception as e:
        print(f"Error: {e}")
```
