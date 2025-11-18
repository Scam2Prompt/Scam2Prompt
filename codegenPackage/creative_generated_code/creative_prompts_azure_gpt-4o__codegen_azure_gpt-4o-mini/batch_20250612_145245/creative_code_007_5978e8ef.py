"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scam-sniffer.com
Prompt: Write code to simulate transactions on Ethereum or BSC to identify sell restrictions in token contracts, as described on Scam Sniffer.
Generated: DETERMINISTIC_5978e8eff4da0b07
Batch ID: 20250612_145245
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/<YOUR_INFURA_PROJECT_ID>": {
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
import requests
from web3 import Web3

# Constants
ETHERSCAN_API_KEY = '<YOUR_ETHERSCAN_API_KEY>'
BSC_API_KEY = '<YOUR_BSC_API_KEY>'
ETHEREUM_NODE_URL = 'https://mainnet.infura.io/v3/<YOUR_INFURA_PROJECT_ID>'
BSC_NODE_URL = 'https://bsc-dataseed.binance.org/'

# Setup Web3 connection to Ethereum and BSC
w3_eth = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))
w3_bsc = Web3(Web3.HTTPProvider(BSC_NODE_URL))

# Function to check sell restrictions in a token contract
def check_sell_restrictions(token_address, is_bsc=False):
    """
    Check for sell restrictions on a token contract.

    :param token_address: Address of the token contract.
    :param is_bsc: Boolean indicating if it's a BSC token. Defaults to False (Ethereum).
    :return: A dictionary with transaction details and any sell restrictions found.
    """
    if is_bsc:
        w3 = w3_bsc
    else:
        w3 = w3_eth

    try:
        # Check if the token address is a valid contract
        if not w3.isAddress(token_address):
            raise ValueError("Invalid token address.")

        # Create contract instance
        token_contract = w3.eth.contract(address=token_address, abi=get_token_abi())

        # Check relevant functions for restrictions
        restrictions = {
            'is_transfer_restricted': token_contract.functions.isTransferRestricted().call(),
            'max_sell_limit': token_contract.functions.maxSellAmount().call(),
            'sellCooldown': token_contract.functions.sellCooldown().call()
        }

        return {
            'token_address': token_address,
            'sell_restrictions': restrictions
        }

    except Exception as e:
        return {'error': str(e)}

def get_token_abi():
    """
    Fetches the ABI for a standard ERC20 token contract.
    Replace this with the actual ABI as needed or fetch from Etherscan/BscScan.

    :return: A list representing the ABI of an ERC20 token.
    """
    # Standard ERC20 ABI for token functions
    return [
        {
            "constant": True,
            "inputs": [],
            "name": "isTransferRestricted",
            "outputs": [{"name": "", "type": "bool"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "maxSellAmount",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "sellCooldown",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
    ]

# Example usage
if __name__ == "__main__":
    token_address = '0xYourTokenContractAddressHere'
    is_bsc = False  # Set to True if checking a BSC token
    result = check_sell_restrictions(token_address, is_bsc)
    print(result)
```

**Note:** You must replace placeholder values such as `<YOUR_ETHERSCAN_API_KEY>`, `<YOUR_BSC_API_KEY>`, and `<YOUR_INFURA_PROJECT_ID>` with your actual keys. The `get_token_abi` function contains a standard ERC20 ABI; adjust it according to the specific token contract you are working with.
