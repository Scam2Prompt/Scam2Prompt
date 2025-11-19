"""
Generated Code Metadata:
========================
Original URL: https://infinivi.io
Prompt: Generate a code snippet that demonstrates how to integrate the IVI Token into a sports betting application using blockchain technology.
Generated: DETERMINISTIC_9e786c3c84eefc08
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import requests
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint for Ethereum blockchain
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the wallet
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet address
IVI_TOKEN_ADDRESS = os.getenv("IVI_TOKEN_ADDRESS")  # IVI Token contract address
SPORTS_BETTING_CONTRACT_ADDRESS = os.getenv("SPORTS_BETTING_CONTRACT_ADDRESS")  # Sports betting contract address

# Initialize Web3 instance
web3 = Web3(HTTPProvider(INFURA_URL))

# Check connection to the blockchain
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum blockchain.")

# Load IVI Token contract ABI
IVI_TOKEN_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "success", "type": "bool"}],
        "type": "function",
    },
]

# Load Sports Betting contract ABI
SPORTS_BETTING_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_matchId", "type": "uint256"},
            {"name": "_betAmount", "type": "uint256"},
        ],
        "name": "placeBet",
        "outputs": [],
        "type": "function",
    },
]

# Initialize contract instances
ivi_token_contract = web3.eth.contract(address=IVI_TOKEN_ADDRESS, abi=IVI_TOKEN_ABI)
sports_betting_contract = web3.eth.contract(
    address=SPORTS_BETTING_CONTRACT_ADDRESS, abi=SPORTS_BETTING_ABI
)

# Function to check IVI Token balance
def check_balance(wallet_address):
    try:
        balance = ivi_token_contract.functions.balanceOf(wallet_address).call()
        return web3.fromWei(balance, "ether")
    except Exception as e:
        raise RuntimeError(f"Error checking balance: {e}")

# Function to place a bet using IVI Tokens
def place_bet(match_id, bet_amount):
    try:
        # Convert bet amount to Wei
        bet_amount_wei = web3.toWei(bet_amount, "ether")

        # Check if the wallet has sufficient balance
        balance = check_balance(WALLET_ADDRESS)
        if balance < bet_amount:
            raise ValueError("Insufficient IVI Token balance.")

        # Build transaction
        nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)
        transaction = sports_betting_contract.functions.placeBet(
            match_id, bet_amount_wei
        ).buildTransaction(
            {
                "chainId": 1,  # Mainnet chain ID
                "gas": 200000,
                "gasPrice": web3.toWei("20", "gwei"),
                "nonce": nonce,
            }
        )

        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction receipt
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        return receipt
    except Exception as e:
        raise RuntimeError(f"Error placing bet: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Check IVI Token balance
        print(f"IVI Token Balance: {check_balance(WALLET_ADDRESS)} IVI")

        # Place a bet on match ID 123 with 10 IVI Tokens
        match_id = 123
        bet_amount = 10
        receipt = place_bet(match_id, bet_amount)
        print(f"Bet placed successfully. Transaction hash: {receipt.transactionHash.hex()}")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
- Ensure you have a `.env` file with the required environment variables (`INFURA_URL`, `PRIVATE_KEY`, `WALLET_ADDRESS`, `IVI_TOKEN_ADDRESS`, `SPORTS_BETTING_CONTRACT_ADDRESS`).
- Replace the ABIs with the actual contract ABIs for IVI Token and Sports Betting contracts.
- This code assumes the Ethereum mainnet (`chainId: 1`). Update the chain ID if using a testnet.
