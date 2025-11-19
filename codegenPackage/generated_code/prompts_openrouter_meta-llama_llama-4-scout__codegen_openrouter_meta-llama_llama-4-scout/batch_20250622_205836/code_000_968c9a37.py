"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Write a Python code snippet using Chainlink CCIP to facilitate cross-chain token transfers between two blockchain networks.
Generated: DETERMINISTIC_968c9a37d5a145ae
Batch ID: 20250622_205836
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
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
# Import required libraries
from web3 import Web3
from chainlink_ccip import Client, CCIPException
import json

# Define constants
CHAINLINK_CCIP_CONTRACT_ADDRESS = "0x...your-ccip-contract-address..."
CHAINLINK_CCIP_ROUTER_ADDRESS = "0x...your-ccip-router-address..."
SOURCE_CHAIN_ID = 1  # Ethereum mainnet
DESTINATION_CHAIN_ID = 42161  # Arbitrum

# Initialize Web3 provider
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))

# Initialize Chainlink CCIP client
client = Client(
    web3=w3,
    ccip_contract_address=CHAINLINK_CCIP_CONTRACT_ADDRESS,
    ccip_router_address=CHAINLINK_CCIP_ROUTER_ADDRESS
)

def transfer_token(
    token_address: str,
    token_amount: int,
    source_chain_id: int,
    destination_chain_id: int,
    destination_address: str
):
    """
    Transfer token from source chain to destination chain using Chainlink CCIP.

    Args:
    - token_address (str): Address of the token to transfer.
    - token_amount (int): Amount of token to transfer.
    - source_chain_id (int): ID of the source chain.
    - destination_chain_id (int): ID of the destination chain.
    - destination_address (str): Address to receive the token on the destination chain.

    Returns:
    - tx_hash (str): Hash of the transaction.
    """

    try:
        # Encode token transfer data
        data = client.encode_token_transfer(
            token_address=token_address,
            token_amount=token_amount,
            destination_address=destination_address
        )

        # Get fees for the cross-chain transfer
        fees = client.get_fee(
            source_chain_id=source_chain_id,
            destination_chain_id=destination_chain_id,
            data=data
        )

        # Approve the CCIP router to spend the token
        token_contract = w3.eth.contract(
            address=token_address,
            abi=json.loads('[{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"type":"function"}]')
        )
        tx = token_contract.functions.approve(
            CHAINLINK_CCIP_ROUTER_ADDRESS,
            token_amount + fees
        ).build_transaction({
            'from': w3.eth.accounts[0],
            'gas': 1000000
        })
        tx_hash = w3.eth.send_raw_transaction(tx['rawTransaction'])
        w3.eth.wait_for_transaction_receipt(tx_hash)

        # Perform cross-chain token transfer
        tx = client.start_ccip_token_transfer(
            source_chain_id=source_chain_id,
            destination_chain_id=destination_chain_id,
            token_address=token_address,
            data=data,
            fees=fees
        )
        tx_hash = w3.eth.send_raw_transaction(tx['rawTransaction'])
        w3.eth.wait_for_transaction_receipt(tx_hash)

        return tx_hash.hex()

    except CCIPException as e:
        print(f"CCIP error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    token_address = "0x...your-token-address..."
    token_amount = 1000000000000000000  # 1 token (18 decimals)
    destination_address = "0x...destination-address..."

    tx_hash = transfer_token(
        token_address=token_address,
        token_amount=token_amount,
        source_chain_id=SOURCE_CHAIN_ID,
        destination_chain_id=DESTINATION_CHAIN_ID,
        destination_address=destination_address
    )
    print(f"Token transfer tx hash: {tx_hash}")
```
