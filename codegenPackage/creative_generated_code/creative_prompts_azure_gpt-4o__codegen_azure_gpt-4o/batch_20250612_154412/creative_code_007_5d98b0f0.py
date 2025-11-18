"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepecoin.blog
Prompt: Write code to compare transaction fees between $PEP and $PEPE ERC-20 tokens, emphasizing Pepecoin's accessibility for small daily transactions.
Generated: DETERMINISTIC_5d98b0f0c5f7f4c3
Batch ID: 20250612_154412
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
import web3
from web3 import Web3
from decimal import Decimal

# Configuration
INFURA_API_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
PEP_CONTRACT_ADDRESS = "0xPEP_CONTRACT_ADDRESS"  # Replace with actual $PEP contract address
PEPE_CONTRACT_ADDRESS = "0xPEPE_CONTRACT_ADDRESS"  # Replace with actual $PEPE contract address
ETHERSCAN_API_URL = "https://api.etherscan.io/api"  # Etherscan API URL
ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"  # Replace with your Etherscan API Key

# ERC-20 ABI for basic token interactions
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "decimals", "type": "uint8"}],
        "type": "function",
    },
]

# Initialize web3
web3 = Web3(Web3.HTTPProvider(INFURA_API_URL))

# Check connection to the Ethereum network
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum network. Check your Infura URL or internet connection.")

# Function to fetch gas price (in Gwei)
def fetch_gas_price():
    try:
        gas_price = web3.eth.gas_price  # Fetch current gas price
        return gas_price
    except Exception as e:
        raise Exception(f"Error fetching gas price: {str(e)}")

# Function to calculate transaction fee for a token transfer
def calculate_transaction_fee(contract_address):
    try:
        # Create contract instance
        contract = web3.eth.contract(address=web3.to_checksum_address(contract_address), abi=ERC20_ABI)
        
        # Example gas estimate for a token transfer (may vary based on blockchain conditions)
        gas_limit = 65000  # Average gas for ERC-20 transfer
        
        gas_price = fetch_gas_price()  # Fetch current gas price
        
        # Fee = gas_limit * gas_price
        fee_in_wei = gas_limit * gas_price
        fee_in_eth = web3.from_wei(fee_in_wei, "ether")  # Convert fee to Ether
        return fee_in_eth
    except Exception as e:
        raise Exception(f"Error calculating transaction fee: {str(e)}")

# Function to compare fees between $PEP and $PEPE
def compare_fees():
    try:
        pep_fee = calculate_transaction_fee(PEP_CONTRACT_ADDRESS)
        pepe_fee = calculate_transaction_fee(PEPE_CONTRACT_ADDRESS)

        print(f"Transaction Fee for $PEP Token: {pep_fee:.8f} ETH")
        print(f"Transaction Fee for $PEPE Token: {pepe_fee:.8f} ETH")

        if pep_fee < pepe_fee:
            print(f"$PEP is more accessible for small daily transactions due to lower transaction fees.")
        elif pepe_fee < pep_fee:
            print(f"$PEPE is more accessible for small daily transactions due to lower transaction fees.")
        else:
            print(f"Both tokens have similar transaction fees.")
    except Exception as e:
        raise Exception(f"Error comparing transaction fees: {str(e)}")

# Main entry point
if __name__ == "__main__":
    try:
        print("Comparing transaction fees between $PEP and $PEPE tokens...")
        compare_fees()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

Make sure to replace the placeholders (`YOUR_INFURA_PROJECT_ID`, `0xPEP_CONTRACT_ADDRESS`, `0xPEPE_CONTRACT_ADDRESS`, `YOUR_ETHERSCAN_API_KEY`) with actual values for the code to work. Additionally, adjust the `gas_limit` for token transfers based on the current conditions of the Ethereum network.
