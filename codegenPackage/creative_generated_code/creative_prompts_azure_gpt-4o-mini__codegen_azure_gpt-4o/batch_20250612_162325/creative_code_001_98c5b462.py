"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-thruster.pages.dev
Prompt: How can I implement a multi-chain airdrop system similar to the one described for Thruster on TrustPad?
Generated: DETERMINISTIC_98c5b462c6174c2f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code implementing a multi-chain airdrop system in Python utilizing the Web3 library for blockchain interaction.

```python
import json
import os
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables for private keys and RPC URLs
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_URLS = {
    "ethereum": os.getenv("ETH_RPC_URL"),
    "polygon": os.getenv("POLYGON_RPC_URL"),
    "binance_smart_chain": os.getenv("BSC_RPC_URL"),
}

# Configuration for token contracts (ERC20 tokens)
TOKEN_CONTRACT_ADDRESSES = {
    "ethereum": os.getenv("ETH_TOKEN_CONTRACT"),
    "polygon": os.getenv("POLYGON_TOKEN_CONTRACT"),
    "binance_smart_chain": os.getenv("BSC_TOKEN_CONTRACT"),
}

# ABI for ERC20 tokens (standard ABI for balance and transfer)
ERC20_ABI = json.loads('''[
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]''')

def connect_to_chain(rpc_url):
    """
    Connect to a blockchain via RPC URL.
    :param rpc_url: RPC URL of the blockchain node
    :return: Web3 instance connected to the chain
    """
    try:
        web3 = Web3(HTTPProvider(rpc_url))
        if not web3.isConnected():
            raise ConnectionError(f"Cannot connect to chain at {rpc_url}")
        return web3
    except Exception as e:
        raise RuntimeError(f"Error connecting to blockchain: {e}")

def send_airdrop(chain_name, recipients, amounts):
    """
    Send an airdrop on a specific blockchain.
    :param chain_name: Name of the blockchain (e.g., "ethereum", "polygon", "binance_smart_chain")
    :param recipients: List of recipient addresses
    :param amounts: List of token amounts to send to the recipients
    """
    try:
        if chain_name not in RPC_URLS or chain_name not in TOKEN_CONTRACT_ADDRESSES:
            raise ValueError(f"Unsupported chain: {chain_name}")
        
        # Connect to the chain
        web3 = connect_to_chain(RPC_URLS[chain_name])
        
        # Load token contract
        token_contract = web3.eth.contract(
            address=web3.toChecksumAddress(TOKEN_CONTRACT_ADDRESSES[chain_name]),
            abi=ERC20_ABI
        )
        
        # Get wallet address from private key
        wallet_address = web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address
        
        # Verify wallet balance
        wallet_balance = token_contract.functions.balanceOf(wallet_address).call()
        total_airdrop_amount = sum(amounts)
        if wallet_balance < total_airdrop_amount:
            raise ValueError(f"Insufficient balance to perform airdrop. Balance: {wallet_balance}, Required: {total_airdrop_amount}")
        
        # Prepare and send transactions
        for recipient, amount in zip(recipients, amounts):
            try:
                tx = token_contract.functions.transfer(
                    web3.toChecksumAddress(recipient),
                    amount
                ).buildTransaction({
                    'chainId': web3.eth.chain_id,
                    'gas': 200000,
                    'gasPrice': web3.eth.gas_price,
                    'nonce': web3.eth.getTransactionCount(wallet_address),
                })
                signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
                tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
                print(f"Airdrop sent to {recipient}: {amount} tokens. Transaction hash: {tx_hash.hex()}")
            except Exception as tx_error:
                print(f"Error sending airdrop to {recipient}: {tx_error}")
    except Exception as e:
        print(f"Failed to complete airdrop on {chain_name}: {e}")

if __name__ == "__main__":
    # Example usage
    recipients_ethereum = ["0xRecipientAddress1...", "0xRecipientAddress2..."]
    amounts_ethereum = [1000, 2000]  # Example token amounts
    
    recipients_polygon = ["0xRecipientAddress3...", "0xRecipientAddress4..."]
    amounts_polygon = [500, 1500]
    
    # Perform airdrops on Ethereum and Polygon
    send_airdrop("ethereum", recipients_ethereum, amounts_ethereum)
    send_airdrop("polygon", recipients_polygon, amounts_polygon)
```

### Notes:
1. Ensure you have a `.env` file set up with the appropriate environment variables for private keys, RPC URLs, and token contract addresses.
2. Install dependencies via `pip install web3 python-dotenv`.
3. Replace placeholder addresses and token amounts with actual values.
4. Proper error handling is included.
