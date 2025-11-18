"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penpie.io
Prompt: Write a script to convert PENDLE tokens into mPENDLE using the Pendle Converter on Arbitrum and calculate potential bonus rewards based on market conditions.
Generated: DETERMINISTIC_f83a2d4c9092cd77
Batch ID: 20250612_150604
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://arb1.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/bonus_rewards": {
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
import requests
from web3 import Web3, exceptions
from decimal import Decimal

# Constants
RPC_URL = "https://arb1.arbitrum.io/rpc"  # Arbitrum RPC Endpoint
CONVERTER_CONTRACT_ADDRESS = "0xYourConverterContractAddress"  # Replace with actual Pendle Converter contract address
PENDLE_TOKEN_ADDRESS = "0xYourPendleTokenAddress"  # Replace with actual PENDLE token address
CONVERTER_ABI_PATH = "converter_abi.json"  # Path to ABI file for converter contract
PENDLE_ABI_PATH = "pendle_abi.json"  # Path to ABI file for PENDLE token contract
BONUS_REWARD_API = "https://api.example.com/bonus_rewards"  # Replace with actual API for bonus rewards

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Ensure connection to blockchain
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Arbitrum blockchain.")

# Load contract ABIs
try:
    with open(CONVERTER_ABI_PATH, "r") as file:
        converter_abi = json.load(file)
    with open(PENDLE_ABI_PATH, "r") as file:
        pendle_abi = json.load(file)
except FileNotFoundError as e:
    raise FileNotFoundError(f"ABI file not found: {e}")

# Initialize contracts
pendle_contract = web3.eth.contract(address=PENDLE_TOKEN_ADDRESS, abi=pendle_abi)
converter_contract = web3.eth.contract(address=CONVERTER_CONTRACT_ADDRESS, abi=converter_abi)

# Helper function to fetch current bonus rewards
def fetch_bonus_rewards():
    try:
        response = requests.get(BONUS_REWARD_API)
        response.raise_for_status()
        return Decimal(response.json().get("bonus_percentage", 0))
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch bonus rewards: {e}")
        return Decimal(0)  # Return 0 if API call fails

# Function to convert PENDLE to mPENDLE
def convert_pendle_to_mpendle(sender_address, private_key, amount_in_wei):
    try:
        # Check allowance
        allowance = pendle_contract.functions.allowance(sender_address, CONVERTER_CONTRACT_ADDRESS).call()
        if allowance < amount_in_wei:
            # Approve tokens for conversion
            nonce = web3.eth.getTransactionCount(sender_address)
            approve_tx = pendle_contract.functions.approve(CONVERTER_CONTRACT_ADDRESS, amount_in_wei).buildTransaction({
                'nonce': nonce,
                'gas': 100000,
                'gasPrice': web3.toWei('1', 'gwei'),
            })
            signed_approve_tx = web3.eth.account.sign_transaction(approve_tx, private_key)
            web3.eth.sendRawTransaction(signed_approve_tx.rawTransaction)
            print("Tokens approved successfully.")

        # Convert tokens
        nonce = web3.eth.getTransactionCount(sender_address)
        convert_tx = converter_contract.functions.convert(amount_in_wei).buildTransaction({
            'nonce': nonce,
            'gas': 150000,
            'gasPrice': web3.toWei('1', 'gwei'),
        })
        signed_convert_tx = web3.eth.account.sign_transaction(convert_tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_convert_tx.rawTransaction)
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Conversion successful. Transaction hash: {tx_hash.hex()}")
        return receipt
    except exceptions.ContractLogicError as e:
        print(f"Contract logic error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return None

# Main function to execute the script
def main():
    sender_address = input("Enter your wallet address: ").strip()
    private_key = input("Enter your private key (keep this secure): ").strip()
    amount_in_ether = input("Enter amount of PENDLE to convert (in Ether): ").strip()

    try:
        amount_in_wei = web3.toWei(Decimal(amount_in_ether), 'ether')
        bonus_percentage = fetch_bonus_rewards()
        print(f"Current bonus rewards percentage: {bonus_percentage}%")

        # Perform conversion
        receipt = convert_pendle_to_mpendle(sender_address, private_key, amount_in_wei)
        if receipt:
            print("Conversion completed successfully.")
            print(f"Potential bonus rewards based on {bonus_percentage}%: {Decimal(amount_in_ether) * bonus_percentage / 100}")
        else:
            print("Conversion failed.")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
```
