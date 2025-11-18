"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.news
Prompt: Suggest an approach for integrating Starknet with an existing Ethereum-based dApp. Provide code examples for bridging assets between Ethereum and Starknet.
Generated: DETERMINISTIC_8ab2d164c5d75b91
Batch ID: 20250612_153809
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
"""
This script demonstrates an approach to bridging assets between Ethereum and Starknet 
using Python. It integrates Web3.py for Ethereum and Starknet.py for Starknet.

Before running the script:
1. Install dependencies:
   pip install web3 starknet.py
2. Configure the required parameters such as private keys, RPC URLs, and contract addresses.
3. Ensure that the bridging contracts are deployed on Ethereum and Starknet.

NOTE: Replace placeholders with actual values for production use.
"""

from web3 import Web3, exceptions
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.contract import Contract
from starknet_py.net.networks import MAINNET
from starknet_py.transaction_exceptions import TransactionRejectedError

# Ethereum Configuration
ETH_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
ETH_BRIDGE_CONTRACT_ADDRESS = "0xYourEthereumBridgeContractAddress"  # Replace with actual Ethereum bridge address
ETH_PRIVATE_KEY = "YourEthereumPrivateKey"  # Replace with your private key

# Starknet Configuration
STARKNET_GATEWAY_URL = MAINNET.gateway_url
STARKNET_BRIDGE_CONTRACT_ADDRESS = "0xYourStarknetBridgeContractAddress"  # Replace with actual Starknet bridge address
STARKNET_PRIVATE_KEY = "YourStarknetPrivateKey"  # Replace with your Starknet private key
STARKNET_ACCOUNT_ADDRESS = "YourStarknetAccountAddress"  # Replace with your Starknet account address

# Initialize Web3 for Ethereum
eth_web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))
if not eth_web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum RPC.")

# Ethereum bridge contract ABI (Replace with actual ABI)
eth_bridge_abi = [
    {
        "constant": False,
        "inputs": [{"name": "recipient", "type": "address"}, {"name": "amount", "type": "uint256"}],
        "name": "lockTokens",
        "outputs": [],
        "payable": True,
        "stateMutability": "nonpayable",
        "type": "function",
    }
]

# Initialize Starknet GatewayClient
starknet_client = GatewayClient(STARKNET_GATEWAY_URL)

async def bridge_eth_to_starknet(eth_recipient_address: str, amount: int):
    """
    Function to bridge assets from Ethereum to Starknet.
    
    :param eth_recipient_address: Ethereum address of the recipient.
    :param amount: Amount to be bridged.
    """
    # Ethereum Bridge: Lock tokens
    eth_account = eth_web3.eth.account.privateKeyToAccount(ETH_PRIVATE_KEY)
    eth_bridge_contract = eth_web3.eth.contract(address=ETH_BRIDGE_CONTRACT_ADDRESS, abi=eth_bridge_abi)

    try:
        # Build transaction
        lock_txn = eth_bridge_contract.functions.lockTokens(
            eth_recipient_address, amount
        ).buildTransaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 200000,  # Adjust gas limit as needed
            'gasPrice': eth_web3.eth.gas_price,
            'nonce': eth_web3.eth.getTransactionCount(eth_account.address),
        })

        # Sign transaction
        signed_txn = eth_web3.eth.account.sign_transaction(lock_txn, ETH_PRIVATE_KEY)

        # Send transaction
        tx_hash = eth_web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Ethereum transaction sent: {tx_hash.hex()}")

        # Wait for receipt
        receipt = eth_web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Ethereum transaction confirmed: {receipt}")

    except exceptions.Web3Exception as e:
        print(f"Ethereum transaction failed: {e}")
        return

    # Starknet Bridge: Mint tokens
    try:
        starknet_bridge_contract = await Contract.from_address(
            STARKNET_BRIDGE_CONTRACT_ADDRESS, starknet_client
        )

        tx = await starknet_bridge_contract.functions["mint_tokens"].invoke(
            recipient=STARKNET_ACCOUNT_ADDRESS, amount=amount
        )
        await tx.wait_for_acceptance()
        print(f"Starknet transaction confirmed: {tx.transaction_hash}")
    except TransactionRejectedError as e:
        print(f"Starknet transaction failed: {e}")


# Example usage
import asyncio

if __name__ == "__main__":
    # The actual recipient address and amount should be provided
    ETH_RECIPIENT = "0xRecipientEthereumAddress"
    AMOUNT = 1000000000000000000  # Example amount (1 ETH in wei)
    
    asyncio.run(bridge_eth_to_starknet(ETH_RECIPIENT, AMOUNT))
```
