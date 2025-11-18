"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helio-thedoghouse.web.app
Prompt: Create a script to implement a minting process for NFTs on Polygon, referencing Helio's announcement about their launch partner @kometverse and the mint date.
Generated: DETERMINISTIC_cad3d38e47088c9a
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from web3 import Web3
from eth_account import Account
import json
import os

# Load environment variables (e.g., from a .env file)
from dotenv import load_dotenv
load_dotenv()

# Constants
POLYGON_RPC_URL = os.getenv("POLYGON_RPC_URL")  # Polygon RPC endpoint
PRIVATE_KEY = os.getenv("PRIVATE_KEY")         # Wallet's private key for signing transactions
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # NFT contract address
ABI_PATH = "./contract_abi.json"               # Path to the NFT contract's ABI file

# Configuration
GAS_LIMIT = 300000                             # Gas limit for minting
GAS_PRICE = Web3.to_wei(50, "gwei")            # Gas price in GWei

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(POLYGON_RPC_URL))

# Check connection to the blockchain
if not web3.is_connected():
    raise ConnectionError("Failed to connect to the Polygon network.")

# Load NFT contract ABI
try:
    with open(ABI_PATH, "r") as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError(f"Contract ABI file not found: {ABI_PATH}")

# Initialize contract instance
nft_contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=contract_abi)

# Mint function
def mint_nft(to_address: str, token_id: int):
    """
    Mints an NFT to the specified address.

    Args:
        to_address (str): The recipient's wallet address.
        token_id (int): The unique ID of the NFT to mint.

    Returns:
        str: Transaction hash of the minting transaction.
    """
    # Validate recipient address
    if not Web3.is_address(to_address):
        raise ValueError("Invalid recipient address.")

    # Prepare the mint transaction
    nonce = web3.eth.get_transaction_count(Account.from_key(PRIVATE_KEY).address)
    mint_txn = nft_contract.functions.mint(
        Web3.to_checksum_address(to_address), token_id
    ).build_transaction({
        "chainId": 137,  # Polygon mainnet chain ID
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": nonce
    })

    # Sign the transaction
    signed_txn = web3.eth.account.sign_transaction(mint_txn, private_key=PRIVATE_KEY)

    # Send transaction
    try:
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return txn_hash.hex()
    except Exception as e:
        raise RuntimeError(f"An error occurred while sending the transaction: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace with actual recipient address and token ID
    recipient_address = "0xRecipientWalletAddressHere"
    token_id = 1  # Example token ID
    try:
        tx_hash = mint_nft(recipient_address, token_id)
        print(f"Successfully sent mint transaction. Tx hash: {tx_hash}")
    except Exception as e:
        print(f"Failed to mint NFT: {str(e)}")
```

### Notes:
- Replace `POLYGON_RPC_URL`, `PRIVATE_KEY`, and `CONTRACT_ADDRESS` with appropriate values (or use a `.env` file).
- The `contract_abi.json` file should contain the ABI of your NFT smart contract.
- The `mint` function in the contract must match the `mint(to, tokenId)` signature used in the code.
- This example assumes the NFT contract has a `mint(address to, uint256 tokenId)` function. Adjust accordingly if your contract differs.
