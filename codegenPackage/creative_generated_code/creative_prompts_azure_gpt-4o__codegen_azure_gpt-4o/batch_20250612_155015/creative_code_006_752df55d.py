"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pytheth.com
Prompt: How can I use Pytheth's price feed oracles to ensure accurate and secure market data in blockchain applications?
Generated: DETERMINISTIC_752df55dba412f81
Batch ID: 20250612_155015
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/<YOUR_INFURA_PROJECT_ID>": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/": {
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
# Import required modules
from web3 import Web3
import json

# Initialize connection to Ethereum blockchain
INFURA_URL = "https://mainnet.infura.io/v3/<YOUR_INFURA_PROJECT_ID>"  # Replace with your Infura Project ID
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the blockchain
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Contract address for Chainlink's price feed oracle (e.g., ETH/USD on Ethereum Mainnet)
ORACLE_CONTRACT_ADDRESS = "0xF79D6aFBb6dA890132F9D7c355e3015f15F3406F"

# ABI for the Chainlink price feed contract (truncated for brevity; use the official ABI)
ORACLE_ABI = json.loads('[{"inputs":[],"stateMutability":"view","type":"function","name":"latestRoundData","outputs":[{"name":"roundId","type":"uint80"},{"name":"answer","type":"int256"},{"name":"startedAt","type":"uint256"},{"name":"updatedAt","type":"uint256"},{"name":"answeredInRound","type":"uint80"}]}]')

# Initialize the contract
price_feed_contract = web3.eth.contract(address=ORACLE_CONTRACT_ADDRESS, abi=ORACLE_ABI)

try:
    # Fetch the latest price data from the oracle
    price_data = price_feed_contract.functions.latestRoundData().call()

    # Extract required fields from the returned data
    round_id = price_data[0]
    price = price_data[1] / (10 ** 8)  # Adjust for the 8 decimal places used by Chainlink
    started_at = price_data[2]
    updated_at = price_data[3]
    answered_in_round = price_data[4]

    # Print the formatted price data
    print(f"Round ID: {round_id}")
    print(f"Price (ETH/USD): ${price}")
    print(f"Started At: {started_at}")
    print(f"Updated At: {updated_at}")
    print(f"Answered In Round: {answered_in_round}")
except Exception as e:
    # Handle errors in fetching the price data
    print(f"Error fetching price data: {e}")
```
