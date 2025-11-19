"""
Generated Code Metadata:
========================
Original URL: https://mainnet-eq3aby93s-venus-protocol.vercel.app
Prompt: Write a Python script using the Venus Protocol API to interact with the decentralized money market on the BNB Chain, specifically for borrowing assets.
Generated: DETERMINISTIC_7574e65d7e4be372
Batch ID: 20250612_151626
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.bscscan.com/api": {
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
  "https://api.venus.io/api": {
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
import requests
import json
from web3 import Web3
from eth_account import Account
from web3.middleware import geth_poa_middleware

# Configuration
VENUS_API_URL = "https://api.venus.io/api"
BNB_CHAIN_RPC = "https://bsc-dataseed.binance.org/"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your private key
GAS_LIMIT = 200000
GAS_PRICE = Web3.to_wei('5', 'gwei')

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(BNB_CHAIN_RPC))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load account
account = Account.from_key(PRIVATE_KEY)
w3.eth.default_account = account.address

class VenusProtocol:
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_markets(self):
        """Get all available markets from Venus Protocol"""
        try:
            response = requests.get(f"{VENUS_API_URL}/markets", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching markets: {e}")
            return None

    def get_market_details(self, asset_address):
        """Get details for a specific market"""
        try:
            response = requests.get(
                f"{VENUS_API_URL}/market?asset={asset_address}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching market details: {e}")
            return None

    def borrow_asset(self, asset_address, amount):
        """
        Borrow an asset from Venus Protocol
        :param asset_address: Address of the asset to borrow
        :param amount: Amount to borrow (in wei)
        :return: Transaction receipt
        """
        try:
            # Get Venus Comptroller contract ABI
            comptroller_abi = self._get_comptroller_abi()
            if not comptroller_abi:
                raise Exception("Failed to get Comptroller ABI")

            # Get Venus Unitroller address
            unitroller_address = self._get_unitroller_address()
            if not unitroller_address:
                raise Exception("Failed to get Unitroller address")

            # Create contract instance
            comptroller = w3.eth.contract(
                address=unitroller_address,
                abi=comptroller_abi
            )

            # Get vToken address for the asset
            vtoken_address = self._get_vtoken_address(asset_address)
            if not vtoken_address:
                raise Exception(f"Failed to get vToken address for asset {asset_address}")

            # Build transaction
            transaction = comptroller.functions.borrow(
                Web3.to_checksum_address(vtoken_address),
                amount
            ).build_transaction({
                'chainId': 56,  # BNB Chain ID
                'gas': GAS_LIMIT,
                'gasPrice': GAS_PRICE,
                'nonce': w3.eth.get_transaction_count(account.address),
            })

            # Sign and send transaction
            signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            
            # Wait for transaction receipt
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            return receipt

        except Exception as e:
            print(f"Error borrowing asset: {e}")
            return None

    def _get_comptroller_abi(self):
        """Get Venus Comptroller ABI"""
        try:
            response = requests.get(
                "https://api.bscscan.com/api",
                params={
                    "module": "contract",
                    "action": "getabi",
                    "address": "0xfD36E2c2a6789Db23113685031d7F16329158384",  # Venus Comptroller
                    "apikey": "YourApiKeyToken"  # Replace with your BscScan API key
                }
            )
            response.raise_for_status()
            data = response.json()
            if data["status"] == "1":
                return json.loads(data["result"])
            return None
        except Exception as e:
            print(f"Error getting Comptroller ABI: {e}")
            return None

    def _get_unitroller_address(self):
        """Get Venus Unitroller address"""
        try:
            response = requests.get(f"{VENUS_API_URL}/config", headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data.get("data", {}).get("unitroller")
        except Exception as e:
            print(f"Error getting Unitroller address: {e}")
            return None

    def _get_vtoken_address(self, asset_address):
        """Get vToken address for a given asset"""
        try:
            markets = self.get_markets()
            if not markets:
                return None

            for market in markets.get("data", {}).get("markets", []):
                if market.get("underlyingAddress", "").lower() == asset_address.lower():
                    return market.get("vTokenAddress")

            return None
        except Exception as e:
            print(f"Error getting vToken address: {e}")
            return None

# Example usage
if __name__ == "__main__":
    venus = VenusProtocol()
    
    # Example: Borrow 0.1 BNB (amount in wei)
    bnb_address = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
    amount_to_borrow = Web3.to_wei(0.1, 'ether')
    
    receipt = venus.borrow_asset(bnb_address, amount_to_borrow)
    if receipt:
        print(f"Borrow transaction successful. Tx hash: {receipt.transactionHash.hex()}")
    else:
        print("Failed to borrow asset")
```
