"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumauthenticationswallets.pages.dev
Prompt: Create a script to integrate NFT (Non-Fungible Token) functionality with Ethereum Wallets, focusing on secure asset management.
Generated: DETERMINISTIC_2ab7e17081c06187
Batch ID: 20250612_150122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3, exceptions
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Infura URL for Ethereum node connection
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Wallet private key for signing transactions
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet address for ownership validation
NFT_CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")  # NFT smart contract address
NFT_ABI_PATH = os.getenv("NFT_ABI_PATH")  # Path to the NFT contract ABI file

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check Ethereum node connection
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node. Check your INFURA_URL.")

# Load NFT Contract ABI
try:
    with open(NFT_ABI_PATH, "r") as abi_file:
        nft_contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError(f"ABI file not found at {NFT_ABI_PATH}.")
except json.JSONDecodeError:
    raise ValueError("Failed to decode ABI. Ensure the file is a valid JSON.")

# Initialize NFT Contract instance
nft_contract = web3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=nft_contract_abi)

# Function to fetch NFT balance of a wallet
def get_nft_balance(wallet_address):
    """
    Get the number of NFTs owned by a specific wallet.
    :param wallet_address: Ethereum wallet address (string)
    :return: Number of NFTs owned by the wallet (integer)
    """
    try:
        balance = nft_contract.functions.balanceOf(wallet_address).call()
        return balance
    except exceptions.ContractLogicError as e:
        raise RuntimeError(f"Error interacting with the contract: {e}")

# Function to transfer an NFT from one wallet to another
def transfer_nft(token_id, to_address):
    """
    Transfer an NFT to another wallet securely.
    :param token_id: Token ID of the NFT to transfer (integer)
    :param to_address: Ethereum address to transfer the NFT to (string)
    :return: Transaction hash (string)
    """
    try:
        # Validate recipient address
        if not web3.isAddress(to_address):
            raise ValueError(f"Invalid recipient address: {to_address}")

        # Create transaction payload
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
        transaction = nft_contract.functions.safeTransferFrom(
            WALLET_ADDRESS, to_address, token_id
        ).buildTransaction({
            "chainId": 1,  # Mainnet chain ID
            "gas": 300000,  # Gas limit
            "gasPrice": web3.eth.gas_price,  # Current gas price
            "nonce": nonce,
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Return the transaction hash
        return web3.toHex(tx_hash)
    except ValueError as e:
        raise ValueError(f"Transaction error: {e}")
    except exceptions.TransactionNotFound as e:
        raise RuntimeError(f"Transaction failed: {e}")
    except exceptions.ContractLogicError as e:
        raise RuntimeError(f"Error interacting with the contract: {e}")

# Function to check ownership of a specific NFT
def is_nft_owner(wallet_address, token_id):
    """
    Check if a wallet is the owner of a specific NFT.
    :param wallet_address: Ethereum wallet address (string)
    :param token_id: Token ID of the NFT (integer)
    :return: Boolean indicating ownership
    """
    try:
        owner = nft_contract.functions.ownerOf(token_id).call()
        return owner.lower() == wallet_address.lower()
    except exceptions.ContractLogicError as e:
        raise RuntimeError(f"Error interacting with the contract: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Replace with actual token ID and recipient wallet address
        token_id = 1
        recipient_address = "0xRecipientWalletAddressHere"

        # Check NFT balance
        print(f"NFT Balance: {get_nft_balance(WALLET_ADDRESS)}")

        # Check ownership
        if is_nft_owner(WALLET_ADDRESS, token_id):
            print(f"Wallet {WALLET_ADDRESS} owns NFT with Token ID: {token_id}.")
        else:
            print(f"Wallet {WALLET_ADDRESS} does not own NFT with Token ID: {token_id}.")

        # Transfer NFT
        tx_hash = transfer_nft(token_id, recipient_address)
        print(f"NFT transferred successfully. Transaction hash: {tx_hash}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
