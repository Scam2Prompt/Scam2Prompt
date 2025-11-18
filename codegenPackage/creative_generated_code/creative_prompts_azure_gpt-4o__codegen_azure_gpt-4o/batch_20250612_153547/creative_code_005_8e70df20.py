"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.zkfinance.org
Prompt: Provide code to integrate Chainlink and DIA oracles for price accuracy in a zkFinance lending application, including fallback solutions.
Generated: DETERMINISTIC_8e70df206590c967
Batch ID: 20250612_153547
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
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
import os
from web3 import Web3
from chainlink.contracts import ChainlinkOracle
from dia.contracts import DIAOracle

# Constants for the blockchain connection and oracle addresses
INFURA_URL = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/YOUR_PROJECT_ID")
CHAINLINK_ORACLE_ADDRESS = os.getenv("CHAINLINK_ORACLE_ADDRESS", "0xChainlinkOracleAddress")
DIA_ORACLE_ADDRESS = os.getenv("DIA_ORACLE_ADDRESS", "0xDIAOracleAddress")

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Error handling for the blockchain connection
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum network via Infura.")

# Chainlink Oracle contract interface
chainlink_oracle = ChainlinkOracle(web3, CHAINLINK_ORACLE_ADDRESS)

# DIA Oracle contract interface
dia_oracle = DIAOracle(web3, DIA_ORACLE_ADDRESS)

def get_price(asset: str) -> float:
    """
    Retrieves the asset price from the chainlink oracle first; if unsuccessful, falls back to the DIA oracle.
    
    Args:
        asset (str): The asset symbol (e.g., ETH, BTC).
    
    Returns:
        float: The asset price in USD.
    
    Raises:
        Exception: If both oracles fail to provide a valid price.
    """
    try:
        # Price retrieval from Chainlink
        chainlink_price = chainlink_oracle.get_price(asset)
        if chainlink_price and chainlink_price > 0:
            return chainlink_price
    except Exception as e:
        # Log the exception (production systems should use a logger)
        print(f"Chainlink Oracle error: {e}")
    
    try:
        # Fallback to DIA Oracle
        dia_price = dia_oracle.get_price(asset)
        if dia_price and dia_price > 0:
            return dia_price
    except Exception as e:
        # Log the exception
        print(f"DIA Oracle error: {e}")
    
    # If both oracles fail, raise an exception
    raise Exception("Both Chainlink and DIA oracles failed to provide a valid price.")

def main():
    """
    Main function to demonstrate price retrieval from oracles.
    """
    asset = "ETH"  # Change to the desired asset
    try:
        price = get_price(asset)
        print(f"The price of {asset} is ${price:.2f}")
    except Exception as e:
        print(f"Error retrieving price: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
