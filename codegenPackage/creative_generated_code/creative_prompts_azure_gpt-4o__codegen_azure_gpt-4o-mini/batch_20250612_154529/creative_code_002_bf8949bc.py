"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.in
Prompt: Generate Python code using the etherscan-python library to query Ethereum transaction details by Txhash.
Generated: DETERMINISTIC_bf8949bc5723f727
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from etherscan import Etherscan
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the Etherscan client with your API key
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
if not ETHERSCAN_API_KEY:
    raise ValueError("ETHERSCAN_API_KEY is not set in the environment variables.")

etherscan_client = Etherscan(ETHERSCAN_API_KEY)

def get_transaction_details(tx_hash):
    """
    Fetch transaction details from Etherscan by transaction hash.

    :param tx_hash: str - The transaction hash to query.
    :return: dict - A dictionary containing transaction details or raises an exception on error.
    """
    try:
        # Query transaction details using the transaction hash
        transaction_details = etherscan_client.get_tx_by_txid(tx_hash)

        # Check if the transaction details were retrieved successfully
        if transaction_details is None:
            raise ValueError(f"No transaction found for hash: {tx_hash}")

        return transaction_details

    except Exception as e:
        # Log the error and raise it for further handling
        print(f"An error occurred while fetching transaction details: {e}")
        raise

def main():
    # Example transaction hash (replace with a valid one)
    tx_hash = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
    
    try:
        # Get and print transaction details
        details = get_transaction_details(tx_hash)
        print(details)

    except Exception as e:
        print(f"Failed to retrieve transaction details: {e}")

if __name__ == "__main__":
    main()
```

Make sure to install the required packages:
```bash
pip install etherscan-python python-dotenv
```

Create a `.env` file in the same directory with your Etherscan API key:
```
ETHERSCAN_API_KEY=your_api_key_here
```
