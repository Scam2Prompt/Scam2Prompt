"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hokkaidokeneth.vip
Prompt: Generate a Python script using Web3.py to query the total supply and contract details of an Ethereum token, referencing Hokkaido-ken's tokenomics.
Generated: DETERMINISTIC_9b744d602849056c
Batch ID: 20250612_151024
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
from web3 import Web3
from web3.exceptions import ContractLogicError

# Configuration
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID
CONTRACT_ADDRESS = "0xC1f4Eea110cAf4FfC715d2eaB6F8F957a42A1C3b"  # Replace with the Hokkaido-ken token contract address
ABI_PATH = "hokkaido_ken_abi.json"  # Path to the ABI JSON file

def load_abi(file_path):
    """
    Load contract ABI from a JSON file.

    :param file_path: Path to the ABI JSON file
    :return: ABI as a dictionary
    """
    try:
        with open(file_path, 'r') as file:
            abi = json.load(file)
        return abi
    except FileNotFoundError:
        raise FileNotFoundError(f"ABI file not found at {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Failed to decode JSON from ABI file")


def query_token_details(web3, contract):
    """
    Query token details such as total supply and token metadata.

    :param web3: Instance of Web3
    :param contract: Web3 contract instance
    :return: Dictionary containing token details
    """
    try:
        # Fetch total supply
        total_supply = contract.functions.totalSupply().call()
        
        # Fetch token name
        token_name = contract.functions.name().call()
        
        # Fetch token symbol
        token_symbol = contract.functions.symbol().call()
        
        # Fetch decimal places
        decimals = contract.functions.decimals().call()

        # Return token details
        return {
            "name": token_name,
            "symbol": token_symbol,
            "total_supply": total_supply / (10 ** decimals),  # Adjust for decimals
            "decimals": decimals
        }
    except ContractLogicError as e:
        raise RuntimeError("Failed to execute contract function") from e
    except Exception as e:
        raise RuntimeError("An unknown error occurred while querying token details") from e


def main():
    """
    Main function to query Ethereum token details.
    """
    try:
        # Connect to Ethereum network via Infura
        web3 = Web3(Web3.HTTPProvider(INFURA_URL))

        # Validate connection
        if not web3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum network")

        # Load ABI from file
        abi = load_abi(ABI_PATH)

        # Create contract instance
        contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

        # Query token details
        token_details = query_token_details(web3, contract)

        # Display token details
        print("Token Details:")
        print(f"Name: {token_details['name']}")
        print(f"Symbol: {token_details['symbol']}")
        print(f"Total Supply: {token_details['total_supply']}")
        print(f"Decimals: {token_details['decimals']}")

    except Exception as e:
        # Handle exceptions gracefully
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```

**Instructions for Usage:**
1. Replace `YOUR_INFURA_PROJECT_ID` with your Infura Project ID.
2. Replace `0xC1f4Eea110cAf4FfC715d2eaB6F8F957a42A1C3b` with the correct contract address for the Hokkaido-ken token.
3. Ensure the ABI JSON file (`hokkaido_ken_abi.json`) is correctly formatted and accessible at the specified path. You can obtain the ABI from Etherscan or the token project's documentation.
4. Install dependencies: `pip install web3`
