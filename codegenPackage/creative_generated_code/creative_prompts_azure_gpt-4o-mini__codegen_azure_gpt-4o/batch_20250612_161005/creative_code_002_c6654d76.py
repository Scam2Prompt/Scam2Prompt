"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Generate a code snippet that demonstrates how to trigger a smart contract on Flare using data from a Web2 API.
Generated: DETERMINISTIC_c6654d76ed4ddc4d
Batch ID: 20250612_161005
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.coindesk.com/v1/bpi/currentprice/BTC.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://flare-mainnet-rpc.flare.network": {
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
from web3.middleware import geth_poa_middleware

# Configuration variables
WEB2_API_URL = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"  # Example API
FLARE_RPC_URL = "https://flare-mainnet-rpc.flare.network"              # Flare network RPC endpoint
SMART_CONTRACT_ADDRESS = "0xYourSmartContractAddressHere"
PRIVATE_KEY = "0xYourPrivateKeyHere"                                   # Replace with your private key
ABI = [
    # Paste your contract's ABI here
]

def fetch_data_from_api(api_url):
    """
    Fetches data from a Web2 API.
    :param api_url: URL of the API to fetch data from
    :return: Parsed data from the response
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def trigger_smart_contract(web3, contract, data):
    """
    Triggers a smart contract function using data from a Web2 API.
    :param web3: Web3 instance connected to a Flare RPC
    :param contract: Contract instance
    :param data: Data to send to the contract
    :return: Transaction hash
    """
    try:
        # Prepare the transaction payload
        account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)
        nonce = web3.eth.get_transaction_count(account.address)
        gas_price = web3.eth.gas_price

        # Assume the contract has a method `updatePrice(uint256)`
        transaction = contract.functions.updatePrice(data).build_transaction({
            'chainId': 14,  # Flare's chain ID
            'gas': 2000000,  # Adjust gas limit as needed
            'gasPrice': gas_price,
            'nonce': nonce
        })

        # Sign and send the transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Return transaction hash
        return tx_hash.hex()
    except Exception as e:
        print(f"Error triggering smart contract: {e}")
        return None

def main():
    """
    Main function to fetch data from Web2 API and trigger Flare smart contract.
    """
    # Step 1: Connect to the Flare network
    web3 = Web3(Web3.HTTPProvider(FLARE_RPC_URL))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # Required for Flare's Proof of Authority

    # Step 2: Load the contract
    contract = web3.eth.contract(address=Web3.to_checksum_address(SMART_CONTRACT_ADDRESS), abi=ABI)

    # Step 3: Fetch data from Web2 API
    api_data = fetch_data_from_api(WEB2_API_URL)
    if not api_data:
        print("Failed to fetch API data. Exiting...")
        return

    # Extract relevant data (e.g., Bitcoin price in USD)
    try:
        btc_price = int(float(api_data['bpi']['USD']['rate'].replace(',', '')))  # Convert price to integer
    except KeyError as e:
        print(f"Error parsing API data: {e}")
        return

    # Step 4: Trigger the smart contract
    tx_hash = trigger_smart_contract(web3, contract, btc_price)
    if tx_hash:
        print(f"Smart contract triggered successfully. Transaction hash: {tx_hash}")
    else:
        print("Failed to trigger smart contract.")

if __name__ == "__main__":
    main()
```
