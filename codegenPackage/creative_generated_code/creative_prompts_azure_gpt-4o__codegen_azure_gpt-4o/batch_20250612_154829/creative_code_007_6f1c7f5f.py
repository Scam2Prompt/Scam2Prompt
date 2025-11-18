"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hovrachev.ru
Prompt: Create a tutorial for integrating Yield Yak's API into a DeFi application to enable auto-compounding and token swapping functionalities.
Generated: DETERMINISTIC_6f1c7f5f1ac16ef9
Batch ID: 20250612_154829
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.yieldyak.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a production-ready, well-documented Python code example for integrating Yield Yak's API into a DeFi application for auto-compounding and token swapping functionalities. Note that you may need to install required dependencies with `pip install requests web3 dotenv` before running this code.

```python
import requests
from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants for Yield Yak API and Ethereum RPC
YIELD_YAK_API_BASE_URL = "https://api.yieldyak.com/v1"
ETHEREUM_RPC_URL = os.getenv("ETHEREUM_RPC_URL")  # Ethereum RPC URL from .env
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Wallet private key from .env
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")  # Wallet public address from .env

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))

# Verify Web3 connection
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum RPC endpoint.")

# Function to fetch available Yak strategies
def fetch_strategies():
    try:
        response = requests.get(f"{YIELD_YAK_API_BASE_URL}/strategies")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch strategies from Yield Yak API: {e}")

# Function to auto-compound funds using a specific strategy
def auto_compound(strategy_address, amount):
    try:
        # Load contract ABI dynamically via Yield Yak
        response = requests.get(f"{YIELD_YAK_API_BASE_URL}/strategies/{strategy_address}/abi")
        response.raise_for_status()
        abi = response.json()

        # Set up the contract
        contract = web3.eth.contract(address=Web3.toChecksumAddress(strategy_address), abi=abi)

        # Build the transaction for auto-compounding
        tx = contract.functions.deposit().buildTransaction({
            "from": PUBLIC_ADDRESS,
            "value": web3.toWei(amount, "ether"),  # Deposit amount in Ether
            "gas": 2000000,  # Gas limit
            "gasPrice": web3.toWei("30", "gwei"),  # Gas price
            "nonce": web3.eth.getTransactionCount(PUBLIC_ADDRESS),
        })

        # Sign and send the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Wait for the transaction receipt
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        return receipt
    except Exception as e:
        raise RuntimeError(f"Error during auto-compounding: {e}")

# Function to swap tokens using Yield Yak API
def swap_tokens(input_token, output_token, amount):
    try:
        # Fetch swap quote from Yield Yak API
        response = requests.get(
            f"{YIELD_YAK_API_BASE_URL}/swap/quote",
            params={
                "fromToken": input_token,
                "toToken": output_token,
                "amountIn": str(amount),
            },
        )
        response.raise_for_status()
        quote = response.json()

        # Perform the token swap on-chain using the quote data
        tx = {
            "to": Web3.toChecksumAddress(quote["routerAddress"]),
            "from": PUBLIC_ADDRESS,
            "value": web3.toWei(amount, "ether"),  # Swap amount in Ether
            "data": quote["data"],  # Encoded data for the swap
            "gas": 2000000,
            "gasPrice": web3.toWei("30", "gwei"),
            "nonce": web3.eth.getTransactionCount(PUBLIC_ADDRESS),
        }

        # Sign and send the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Wait for the transaction receipt
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        return receipt
    except Exception as e:
        raise RuntimeError(f"Error during token swap: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Fetch available strategies
        strategies = fetch_strategies()
        print("Available strategies:", strategies)

        # Auto-compound funds using a strategy (replace with real strategy address and amount)
        strategy_address = "0x1234567890abcdef1234567890abcdef12345678"
        auto_compound_receipt = auto_compound(strategy_address, 0.1)
        print("Auto-compound transaction receipt:", auto_compound_receipt)

        # Swap tokens (replace with real token addresses and amount)
        input_token = "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"  # Native ETH token
        output_token = "0x1234567890abcdef1234567890abcdef12345678"  # Example token address
        swap_receipt = swap_tokens(input_token, output_token, 0.05)
        print("Swap transaction receipt:", swap_receipt)

    except Exception as e:
        print(f"An error occurred: {e}")
```

**Important Notes:**
- Replace placeholder addresses and token details with real values from your environment.
- Ensure the `.env` file contains `ETHEREUM_RPC_URL`, `PRIVATE_KEY`, and `PUBLIC_ADDRESS`.
- Double-check the strategy and token details using the Yield Yak documentation.
