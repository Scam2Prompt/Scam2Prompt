"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerf-cjl.pages.dev
Prompt: Write a Python script to connect to the $Slerf token smart contract on Ethereum and retrieve the total supply and ownership details.
Generated: DETERMINISTIC_20e79c156e6c4b39
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Constants / Configuration
INFURA_URL = os.getenv("INFURA_URL")  # Infura URL for Ethereum Node
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Address of the $Slerf token smart contract
ABI_PATH = os.getenv("ABI_PATH")  # Path to the ABI file of the $Slerf token smart contract

# Initialize Web3
try:
    web3 = Web3(HTTPProvider(INFURA_URL))
    if not web3.isConnected():
        raise ConnectionError("Unable to connect to Ethereum network.")
except Exception as e:
    print(f"Error initializing Web3: {e}")
    exit(1)

# Load Contract ABI
try:
    with open(ABI_PATH, 'r') as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    print("ABI file not found. Please check the path provided in ABI_PATH.")
    exit(1)
except json.JSONDecodeError:
    print("Failed to decode ABI file. Ensure it is a valid JSON.")
    exit(1)

# Instantiate the smart contract
try:
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)
except ValueError as e:
    print(f"Error instantiating the contract: {e}")
    exit(1)

# Function to retrieve total supply
def get_total_supply():
    try:
        total_supply = contract.functions.totalSupply().call()
        return total_supply
    except Exception as e:
        print(f"Error retrieving total supply: {e}")
        return None

# Function to retrieve ownership details (owner address)
def get_owner():
    try:
        owner = contract.functions.owner().call()
        return owner
    except Exception as e:
        print(f"Error retrieving owner details: {e}")
        return None

# Main execution
if __name__ == "__main__":
    print("Connecting to the $Slerf token smart contract...\n")

    # Retrieve total supply
    total_supply = get_total_supply()
    if total_supply is not None:
        print(f"Total Supply of $Slerf Token: {total_supply}")
    else:
        print("Failed to retrieve total supply.")

    # Retrieve ownership details
    owner = get_owner()
    if owner is not None:
        print(f"Owner Address of $Slerf Token: {owner}")
    else:
        print("Failed to retrieve owner details.")
```

Make sure to configure your `.env` file with the following keys:
```
INFURA_URL=<Your Infura Project URL>
CONTRACT_ADDRESS=<Address of the $Slerf token smart contract>
ABI_PATH=<Path to the ABI JSON file>
```
