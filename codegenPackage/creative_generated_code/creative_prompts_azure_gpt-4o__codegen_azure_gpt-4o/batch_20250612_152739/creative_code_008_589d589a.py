"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://planetserfi.pages.dev
Prompt: Create a blockchain-based voting system to allow users to prioritize sustainability projects, leveraging the principles of Planet ReFi.
Generated: DETERMINISTIC_589d589aa7ed89ec
Batch ID: 20250612_152739
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

Below is the clean, well-documented, and production-ready code for a blockchain-based voting system using Python and the Ethereum blockchain via the `web3.py` library. This code assumes that you have a blockchain node (e.g., Infura) and a smart contract already deployed for voting. Make sure to replace placeholder values with actual data.

```python
from web3 import Web3, exceptions
import json

# Configuration
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura endpoint
CONTRACT_ADDRESS = "0xYourContractAddress"  # Replace with your deployed smart contract address
ABI_PATH = "contract_abi.json"  # Path to your smart contract ABI file
PRIVATE_KEY = "0xYourPrivateKey"  # Replace with your private key
ACCOUNT_ADDRESS = "0xYourAccountAddress"  # Replace with your Ethereum wallet address

# Connect to Ethereum blockchain
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum blockchain.")

# Load contract ABI
try:
    with open(ABI_PATH, "r") as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError(f"ABI file not found at path: {ABI_PATH}")

# Get contract instance
try:
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)
except exceptions.ContractLogicError as e:
    raise ValueError(f"Error initializing contract instance: {e}")

# Function to submit a vote for a sustainability project
def submit_vote(project_id: int):
    """
    Submit a vote for a given sustainability project.

    Args:
        project_id (int): ID of the sustainability project to vote for.

    Returns:
        str: Transaction hash of the vote submission.
    """
    try:
        # Build the transaction
        nonce = web3.eth.getTransactionCount(ACCOUNT_ADDRESS)
        txn = contract.functions.vote(project_id).buildTransaction({
            "chainId": 1,  # Ethereum Mainnet chain ID
            "gas": 200000,  # Estimated gas
            "gasPrice": web3.toWei("30", "gwei"),  # Set gas price
            "nonce": nonce
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Return transaction hash
        return web3.toHex(tx_hash)
    except ValueError as e:
        raise ValueError(f"Error during vote submission: {e}")
    except exceptions.TransactionNotFound as e:
        raise RuntimeError(f"Transaction could not be found: {e}")

# Function to get the current vote count for a project
def get_vote_count(project_id: int) -> int:
    """
    Get the current vote count for a given sustainability project.

    Args:
        project_id (int): ID of the sustainability project.

    Returns:
        int: Current vote count.
    """
    try:
        return contract.functions.getVoteCount(project_id).call()
    except ValueError as e:
        raise ValueError(f"Error retrieving vote count: {e}")

# Function to fetch all available projects
def get_projects() -> list:
    """
    Fetch all sustainability projects available for voting.

    Returns:
        list: List of project IDs and their details.
    """
    try:
        return contract.functions.getAllProjects().call()
    except ValueError as e:
        raise ValueError(f"Error retrieving projects list: {e}")

# Example usage
if __name__ == "__main__":
    try:
        print("Fetching sustainability projects...")
        projects = get_projects()
        for project in projects:
            print(f"Project ID: {project[0]}, Name: {project[1]}, Votes: {get_vote_count(project[0])}")

        # Submit a vote
        print("Submitting vote for Project ID 1...")
        tx_hash = submit_vote(1)
        print(f"Vote submitted successfully! Transaction hash: {tx_hash}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
1. Replace `YOUR_INFURA_PROJECT_ID`, `0xYourContractAddress`, `contract_abi.json`, `0xYourPrivateKey`, and `0xYourAccountAddress` with your actual Infura project ID, contract address, ABI file path, private key, and wallet address.
2. The smart contract requires functions like `vote`, `getVoteCount`, and `getAllProjects` defined in its ABI for this code to work.
3. Add proper logging and monitoring for production use.
