"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: Write a script to integrate HatsFinance's bug bounty program into a Web3 application, ensuring that vulnerabilities can be reported securely.
Generated: DETERMINISTIC_d6c29e48aeca96a5
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to integrate HatsFinance's bug bounty program into a Web3 application.
This script allows users to securely report vulnerabilities via a smart contract.
"""

from web3 import Web3, HTTPProvider
from eth_account import Account
import json
import os
import sys

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configuration constants
INFURA_URL = os.getenv("INFURA_URL")  # Infura URL for Ethereum network connection
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the wallet used for transactions
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # HatsFinance smart contract address
ABI_PATH = os.getenv("ABI_PATH", "./HatsFinanceABI.json")  # Path to HatsFinance contract ABI

# Validate required configurations
if not INFURA_URL or not PRIVATE_KEY or not CONTRACT_ADDRESS or not os.path.exists(ABI_PATH):
    sys.exit("Missing required environment variables or ABI file.")

# Connect to Ethereum blockchain
web3 = Web3(HTTPProvider(INFURA_URL))

# Ensure connection is successful
if not web3.isConnected():
    sys.exit("Failed to connect to Ethereum network.")

# Load the HatsFinance contract ABI
try:
    with open(ABI_PATH, "r") as abi_file:
        contract_abi = json.load(abi_file)
except Exception as e:
    sys.exit(f"Failed to load contract ABI: {e}")

# Instantiate the HatsFinance contract
contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_abi)

# Define the wallet address
wallet_address = Account.from_key(PRIVATE_KEY).address

# Function to report a vulnerability
def report_vulnerability(description, severity_level):
    """
    Reports a vulnerability to the HatsFinance smart contract.

    Args:
        description (str): The description of the vulnerability.
        severity_level (int): The severity level of the vulnerability (e.g., 1=low, 5=critical).

    Returns:
        str: Transaction hash if successful, or error message.
    """
    try:
        # Validate inputs
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a non-empty string.")
        if not isinstance(severity_level, int) or not (1 <= severity_level <= 5):
            raise ValueError("Severity level must be an integer between 1 and 5.")
        
        # Build the transaction
        nonce = web3.eth.get_transaction_count(wallet_address)
        tx = contract.functions.reportVulnerability(description, severity_level).buildTransaction({
            'chainId': 1,  # Mainnet chain ID (adjust if using a testnet)
            'gas': 2000000,  # Estimated gas limit
            'gasPrice': web3.toWei('20', 'gwei'),  # Gas price
            'nonce': nonce
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Return transaction hash
        return f"Vulnerability reported successfully. Transaction hash: {web3.toHex(tx_hash)}"

    except Exception as e:
        return f"Failed to report vulnerability: {e}"

# Main entry point
if __name__ == "__main__":
    print("Welcome to the HatsFinance Bug Bounty Integration!")
    try:
        # Example input from user
        description = input("Enter the vulnerability description: ").strip()
        severity_level = int(input("Enter the severity level (1=low, 5=critical): "))

        # Report the vulnerability
        result = report_vulnerability(description, severity_level)
        print(result)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```

### Notes:
- Replace environment variables (`INFURA_URL`, `PRIVATE_KEY`, `CONTRACT_ADDRESS`, `ABI_PATH`) with valid values.
- Ensure the necessary dependencies (`web3`, `eth_account`, `dotenv`) are installed using `pip install web3 eth_account python-dotenv`.
- The `reportVulnerability` method assumes it exists in the HatsFinance contract. Update the ABI and method name as per the actual contract specification.
