"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptekaimed.ru
Prompt: Write a Python script that connects to the Beefy Finance smart contracts to monitor investment performance in real-time.
Generated: DETERMINISTIC_0222764f15f2bbe8
Batch ID: 20250612_161226
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

```python
import json
import requests
from web3 import Web3
from web3.exceptions import ContractLogicError

# Constants
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'  # Replace with your Infura project ID
BEEFY_VAULT_ADDRESS = '0xYourVaultAddressHere'  # Replace with the specific Beefy vault address
ABI_FILE = 'vault_abi.json'  # Path to the ABI JSON file for Beefy vault contracts

# Initialize Web3 connection
try:
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))
    if not web3.isConnected():
        raise ConnectionError("Could not connect to the Ethereum network.")
except Exception as e:
    print(f"Error initializing Web3: {e}")
    exit()

# Load ABI for Beefy vault contract
try:
    with open(ABI_FILE, 'r') as abi_file:
        vault_abi = json.load(abi_file)
except FileNotFoundError:
    print(f"Error: ABI file '{ABI_FILE}' was not found.")
    exit()
except json.JSONDecodeError:
    print("Error: Failed to parse ABI file.")
    exit()

# Connect to Beefy vault contract
try:
    vault_contract = web3.eth.contract(address=web3.toChecksumAddress(BEEFY_VAULT_ADDRESS), abi=vault_abi)
except ValueError as e:
    print(f"Error connecting to vault contract: {e}")
    exit()

# Function to fetch real-time performance metrics
def get_vault_info():
    try:
        # Example metrics: Total value locked (TVL) and price per full share (PPFS)
        total_balance = vault_contract.functions.balance().call()
        price_per_full_share = vault_contract.functions.getPricePerFullShare().call()

        # Convert raw values to human-readable format (assuming ETH-based vault)
        total_balance_eth = web3.fromWei(total_balance, 'ether')
        price_per_full_share_eth = web3.fromWei(price_per_full_share, 'ether')

        return {
            "total_balance_eth": total_balance_eth,
            "price_per_full_share_eth": price_per_full_share_eth
        }
    except ContractLogicError as e:
        print(f"Error fetching performance data from contract: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None

# Main monitoring loop
if __name__ == "__main__":
    print("Monitoring Beefy Finance vault performance in real-time...")
    try:
        while True:
            vault_info = get_vault_info()
            if vault_info:
                print("Vault Performance Metrics:")
                print(f"Total Value Locked (ETH): {vault_info['total_balance_eth']}")
                print(f"Price Per Full Share (ETH): {vault_info['price_per_full_share_eth']}")
            else:
                print("Failed to retrieve vault performance metrics.")

            # Fetch metrics at regular intervals (e.g., every 10 seconds)
            import time
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Unexpected error occurred during monitoring: {e}")
```

This script assumes you have access to the Beefy Finance vault address and its ABI. Replace placeholders such as `YOUR_INFURA_PROJECT_ID`, `0xYourVaultAddressHere`, and `vault_abi.json` with actual values. Install the required libraries (`web3`, `requests`) using `pip` before running the script.
