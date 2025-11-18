"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snailbrookwhitelist.pages.dev
Prompt: Create a Python program that uses web3.py to interact with the Base chain and verify the liquidity transfer of SNAIL tokens as described on the Snailbrook webpage.
Generated: DETERMINISTIC_045bf25c5ebc89f2
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from web3 import Web3
from web3.exceptions import ContractLogicError

# Load environment variables
INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
ACCOUNT_ADDRESS = os.getenv('ACCOUNT_ADDRESS')

# Initialize a Web3 connection
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Base chain
if not w3.isConnected():
    raise ConnectionError("Failed to connect to the Base chain.")

# Set the contract address and ABI for SNAIL token
SNAIL_CONTRACT_ADDRESS = '0xYourSNAILContractAddress'
with open('SNAIL_ABI.json', 'r') as abi_file:
    SNAIL_ABI = json.load(abi_file)

# Initialize the SNAIL contract
snail_contract = w3.eth.contract(address=SNAIL_CONTRACT_ADDRESS, abi=SNAIL_ABI)

def check_liquidity_transfer(tx_hash):
    """
    Check the liquidity transfer of SNAIL tokens using the transaction hash.

    Parameters:
        tx_hash (str): The transaction hash of the liquidity transfer.

    Returns:
        dict: Details of the transaction if successful, otherwise an error message.
    """
    try:
        # Get the transaction receipt
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)

        if tx_receipt is None:
            return {"error": "Transaction not found."}

        # Check if the transaction was successful
        if tx_receipt['status'] != 1:
            return {"error": "Transaction failed."}

        # Decode logs for liquidity transfer event
        event_filter = snail_contract.events.Transfer.createFilter(fromBlock=tx_receipt['blockNumber'])
        events = event_filter.get_all_entries()

        # Find the liquidity transfer event
        liquidity_transfers = [
            event for event in events if event['args']['from'] == ACCOUNT_ADDRESS
        ]

        if not liquidity_transfers:
            return {"error": "No liquidity transfers found for this account."}

        return {"success": "Liquidity transfer verified.", "transfers": liquidity_transfers}

    except ContractLogicError as e:
        return {"error": f"Contract logic error: {str(e)}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    # Example transaction hash for checking liquidity transfer
    transaction_hash = '0xYourTransactionHash'

    # Verify the liquidity transfer
    result = check_liquidity_transfer(transaction_hash)

    # Print the result
    print(json.dumps(result, indent=4))
```

**Note**: 
- Replace `'0xYourSNAILContractAddress'` with the actual SNAIL token contract address.
- The ABI file `SNAIL_ABI.json` must be in the same directory as the script.
- Make sure to set the environment variables `INFURA_URL`, `PRIVATE_KEY`, and `ACCOUNT_ADDRESS` appropriately in your environment before running the program.
