"""
Generated Code Metadata:
========================
Original URL: https://pythusdc.com
Prompt: Write a tutorial-style prompt for integrating Pyth price feed oracles into a blockchain-based application for real-time market data.
Generated: DETERMINISTIC_aa78d36d325a11f7
Batch ID: 20250612_155024
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

# Generated Code:
# ===============

```python
# Import required libraries
import requests
from web3 import Web3
import json
from typing import Dict

# Define a class for Pyth Price Feed Oracle
class PythPriceFeedOracle:
    def __init__(self, 
                 pyth_contract_address: str, 
                 pyth_abi: list, 
                 web3_provider_url: str):
        """
        Initialize Pyth Price Feed Oracle.

        Args:
        - pyth_contract_address (str): The address of the Pyth contract.
        - pyth_abi (list): The ABI of the Pyth contract.
        - web3_provider_url (str): The URL of the Web3 provider.
        """
        self.pyth_contract_address = pyth_contract_address
        self.pyth_abi = pyth_abi
        self.web3 = Web3(Web3.HTTPProvider(web3_provider_url))

        # Check if Web3 provider is connected
        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to Web3 provider")

    def get_price(self, symbol: str) -> float:
        """
        Get the current price of a symbol.

        Args:
        - symbol (str): The symbol of the price to get.

        Returns:
        - float: The current price of the symbol.

        Raises:
        - ValueError: If the symbol is not found.
        """
        try:
            # Get the Pyth contract instance
            pyth_contract = self.web3.eth.contract(address=self.pyth_contract_address, abi=self.pyth_abi)

            # Get the price of the symbol
            price_feed = pyth_contract.functions.getPrice(symbol.encode()).call()
            price = price_feed[0] / (10 ** 8)  # Pyth price feed returns price with 8 decimal places

            return price

        except Exception as e:
            raise ValueError(f"Failed to get price for symbol {symbol}: {str(e)}")

    def get_multiple_prices(self, symbols: list) -> Dict[str, float]:
        """
        Get the current prices of multiple symbols.

        Args:
        - symbols (list): A list of symbols to get prices for.

        Returns:
        - Dict[str, float]: A dictionary of symbol-price pairs.

        Raises:
        - ValueError: If any symbol is not found.
        """
        try:
            # Get the Pyth contract instance
            pyth_contract = self.web3.eth.contract(address=self.pyth_contract_address, abi=self.pyth_abi)

            # Get the prices of the symbols
            prices = {}
            for symbol in symbols:
                price_feed = pyth_contract.functions.getPrice(symbol.encode()).call()
                price = price_feed[0] / (10 ** 8)  # Pyth price feed returns price with 8 decimal places
                prices[symbol] = price

            return prices

        except Exception as e:
            raise ValueError(f"Failed to get prices for symbols {symbols}: {str(e)}")


# Example usage:
if __name__ == "__main__":
    # Replace with your own values
    pyth_contract_address = "0x..."
    pyth_abi = [...]  # ABI of the Pyth contract
    web3_provider_url = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"

    oracle = PythPriceFeedOracle(pyth_contract_address, pyth_abi, web3_provider_url)

    symbol = "BTC/USD"
    price = oracle.get_price(symbol)
    print(f"The current price of {symbol} is: {price}")

    symbols = ["BTC/USD", "ETH/USD"]
    prices = oracle.get_multiple_prices(symbols)
    print(f"The current prices are: {prices}")
```
