"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaredrop.in
Prompt: Create a tutorial for building a decentralized application that leverages Flare's enshrined oracles for real-time data access.
Generated: DETERMINISTIC_7d4f5f32df1f92bf
Batch ID: 20250612_154631
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://flare-mainnet-rpc-url": {
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
"""
Tutorial: Building a Decentralized Application (dApp) that leverages Flare's enshrined oracles for real-time data access.

This example demonstrates how to interact with Flare's enshrined oracles to fetch real-time data 
and use it in a decentralized application (dApp) built with Python and web3.py.
"""

# Import necessary libraries
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Error handling for missing environment variables
try:
    FLARE_RPC_URL = os.getenv("FLARE_RPC_URL")  # Flare network RPC endpoint
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")      # Private key for transaction signing
    ORACLE_CONTRACT_ADDRESS = os.getenv("ORACLE_CONTRACT_ADDRESS")  # Oracle contract address
    assert FLARE_RPC_URL and PRIVATE_KEY and ORACLE_CONTRACT_ADDRESS, "Missing environment variables!"
except Exception as e:
    print(f"Error loading environment variables: {e}")
    exit(1)

# Connect to Flare Network
try:
    web3 = Web3(Web3.HTTPProvider(FLARE_RPC_URL))
    assert web3.isConnected(), "Failed to connect to Flare Network!"
except Exception as e:
    print(f"Error connecting to Flare Network: {e}")
    exit(1)

# Define the ABI (Application Binary Interface) for the oracle contract
# This ABI should match the deployed oracle contract on Flare Network
ORACLE_ABI = [
    {
        "inputs": [{"internalType": "string", "name": "key", "type": "string"}],
        "name": "getData",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    }
]

# Initialize the contract instance
try:
    oracle_contract = web3.eth.contract(address=ORACLE_CONTRACT_ADDRESS, abi=ORACLE_ABI)
except Exception as e:
    print(f"Error initializing oracle contract: {e}")
    exit(1)

# Function to fetch real-time data from the oracle
def fetch_oracle_data(key: str) -> str:
    """
    Fetches real-time data from Flare's enshrined oracle using the provided key.

    :param key: The key specifying the type of data to fetch (e.g., "ETH/USD").
    :return: The fetched data as a string.
    """
    try:
        # Call the oracle contract's getData function
        data = oracle_contract.functions.getData(key).call()
        return data
    except Exception as e:
        print(f"Error fetching data from oracle: {e}")
        return None


# Example usage of the function
if __name__ == "__main__":
    # Define the key for which data is being requested
    oracle_key = "ETH/USD"  # Example key for Ethereum to USD exchange rate

    print(f"Fetching real-time data for key: {oracle_key}")

    # Fetch the data
    real_time_data = fetch_oracle_data(oracle_key)

    if real_time_data:
        print(f"Real-time data from oracle ({oracle_key}): {real_time_data}")
    else:
        print("Failed to fetch data from oracle.")
```

### Notes:
1. Before running this code, ensure you have installed the required dependencies:
   - `pip install web3 python-dotenv`
2. Replace the placeholder values in the `.env` file with appropriate values:
   ```
   FLARE_RPC_URL=https://flare-mainnet-rpc-url
   PRIVATE_KEY=your-private-key
   ORACLE_CONTRACT_ADDRESS=oracle-contract-address
   ```
3. This example assumes that the Oracle contract exposes a `getData` method, which retrieves real-time data using a string key. Update the ABI if the contract structure differs.
