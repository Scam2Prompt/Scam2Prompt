"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythshop.com
Prompt: Write a script to validate the accuracy of market data fetched from Pyth Network's price feed oracles in a decentralized finance application.
Generated: DETERMINISTIC_f655e2609f7515c0
Batch ID: 20250612_155024
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.pyth.network/api/v1/prices": {
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

# Constants and configurations
PYTH_PRICE_FEED_URL = "https://example.pyth.network/api/v1/prices"  # Replace with actual Pyth API URL
WEB3_PROVIDER_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with actual Web3 provider
VALIDATION_THRESHOLD = 0.01  # 1% price deviation threshold
TOKEN_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with the actual token address
CHAIN_ID = 1  # Ethereum mainnet

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

# Function to fetch market data from Pyth Network
def fetch_pyth_price(token_address):
    try:
        response = requests.get(PYTH_PRICE_FEED_URL, params={"token": token_address})
        response.raise_for_status()  # Raise HTTPError for bad responses
        price_data = response.json()
        return price_data.get("price"), price_data.get("confidence_interval")
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch data from Pyth Network: {e}")

# Function to fetch market data from on-chain oracle
def fetch_onchain_price(token_address):
    try:
        # Example contract ABI and method call. Replace with actual oracle details.
        contract_abi = [
            {
                "constant": True,
                "inputs": [],
                "name": "getPrice",
                "outputs": [{"name": "", "type": "uint256"}],
                "type": "function",
            }
        ]
        contract = web3.eth.contract(address=Web3.to_checksum_address(token_address), abi=contract_abi)
        price = contract.functions.getPrice().call()
        return Web3.from_wei(price, "ether")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data from on-chain oracle: {e}")

# Function to validate price data
def validate_prices(pyth_price, pyth_confidence, onchain_price):
    try:
        if pyth_price is None or onchain_price is None:
            raise ValueError("Price data cannot be None.")

        deviation = abs(pyth_price - onchain_price) / onchain_price
        if deviation > VALIDATION_THRESHOLD:
            return {"valid": False, "deviation": deviation}
        return {"valid": True, "deviation": deviation}
    except Exception as e:
        raise RuntimeError(f"Error during validation: {e}")

def main():
    try:
        # Fetch prices
        pyth_price, pyth_confidence = fetch_pyth_price(TOKEN_ADDRESS)
        onchain_price = fetch_onchain_price(TOKEN_ADDRESS)
        
        # Log fetched prices
        print(f"Pyth Price: {pyth_price}, Confidence Interval: {pyth_confidence}")
        print(f"On-chain Price: {onchain_price}")

        # Validate prices
        validation_result = validate_prices(pyth_price, pyth_confidence, onchain_price)
        if validation_result["valid"]:
            print("Prices are within acceptable range.")
        else:
            print(f"Price deviation too high! Deviation: {validation_result['deviation']:.2%}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
