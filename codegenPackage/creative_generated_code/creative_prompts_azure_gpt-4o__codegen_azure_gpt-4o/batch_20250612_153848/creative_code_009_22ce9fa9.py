"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-connect.com
Prompt: Create a tutorial for developers on how to use Flare's blockchain to build decentralized applications that integrate data from multiple blockchains and Web2 APIs.
Generated: DETERMINISTIC_22ce9fa9e41ac5d7
Batch ID: 20250612_153848
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.blockcypher.com/v1/btc/main": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://flare-api.flare.network/ext/bc/C/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/your_infura_project_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.openweathermap.org/data/2.5/weather": {
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
"""
Tutorial: Building a Decentralized Application on Flare's Blockchain
This script serves as a foundational example for interacting with Flare's blockchain and integrating 
data from multiple blockchains and Web2 APIs. It demonstrates how to:
1. Connect and interact with Flare's blockchain.
2. Fetch data from Ethereum and Bitcoin blockchains using Infura and a public Bitcoin API.
3. Pull external Web2 data from an example API.
4. Integrate the gathered data into a simple smart contract.
"""

from web3 import Web3, HTTPProvider
import requests

# Constants for Flare's Network
FLARE_RPC_URL = "https://flare-api.flare.network/ext/bc/C/rpc"  # RPC URL for Flare's blockchain
PRIVATE_KEY = "your_private_key_here"  # Replace with your private key (ensure this is stored securely)
CONTRACT_ADDRESS = "0xYourContractAddressHere"  # Replace with your deployed smart contract address
ABI = [...]  # Replace with your smart contract ABI

# Constants for Ethereum and Bitcoin APIs
INFURA_ETH_URL = "https://mainnet.infura.io/v3/your_infura_project_id"  # Ethereum RPC URL
BITCOIN_API_URL = "https://api.blockcypher.com/v1/btc/main"  # Public Bitcoin API

# Constants for a Web2 API (example: OpenWeatherMap API for weather data)
WEB2_API_URL = "https://api.openweathermap.org/data/2.5/weather"
WEB2_API_KEY = "your_openweathermap_api_key_here"

# Function to initialize a connection to Flare's blockchain
def connect_to_flare():
    try:
        web3 = Web3(HTTPProvider(FLARE_RPC_URL))
        if web3.isConnected():
            print("Successfully connected to Flare's blockchain.")
            return web3
        else:
            raise ConnectionError("Failed to connect to Flare's blockchain.")
    except Exception as e:
        print(f"Error connecting to Flare: {e}")
        raise

# Function to fetch Ethereum blockchain data
def fetch_ethereum_data():
    try:
        eth_web3 = Web3(HTTPProvider(INFURA_ETH_URL))
        if eth_web3.isConnected():
            latest_block = eth_web3.eth.get_block('latest')
            print("Fetched latest Ethereum block data.")
            return latest_block
        else:
            raise ConnectionError("Failed to connect to Ethereum blockchain.")
    except Exception as e:
        print(f"Error fetching Ethereum data: {e}")
        raise

# Function to fetch Bitcoin blockchain data
def fetch_bitcoin_data():
    try:
        response = requests.get(BITCOIN_API_URL)
        response.raise_for_status()
        bitcoin_data = response.json()
        print("Fetched Bitcoin data successfully.")
        return bitcoin_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin data: {e}")
        raise

# Function to fetch data from a Web2 API
def fetch_web2_data(location="London"):
    try:
        params = {"q": location, "appid": WEB2_API_KEY}
        response = requests.get(WEB2_API_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        print("Fetched Web2 API data successfully.")
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Web2 API data: {e}")
        raise

# Function to interact with a deployed smart contract on Flare's blockchain
def interact_with_contract(web3, ethereum_data, bitcoin_data, web2_data):
    try:
        contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
        account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)
        nonce = web3.eth.getTransactionCount(account.address)

        # Example function call: store aggregated data in the smart contract
        tx = contract.functions.storeData(
            ethereum_data['number'],  # Ethereum block number
            bitcoin_data['height'],   # Bitcoin block height
            web2_data['main']['temp']  # Weather temperature from Web2 API
        ).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce
        })

        # Sign and send the transaction
        signed_tx = web3.eth.account.signTransaction(tx, PRIVATE_KEY)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Transaction sent! Tx hash: {web3.toHex(tx_hash)}")
    except Exception as e:
        print(f"Error interacting with contract: {e}")
        raise

# Main function to orchestrate the tutorial's steps
def main():
    try:
        # Step 1: Connect to Flare's blockchain
        web3 = connect_to_flare()

        # Step 2: Fetch data from Ethereum blockchain
        ethereum_data = fetch_ethereum_data()

        # Step 3: Fetch data from Bitcoin blockchain
        bitcoin_data = fetch_bitcoin_data()

        # Step 4: Fetch data from Web2 API
        web2_data = fetch_web2_data()

        # Step 5: Interact with the smart contract on Flare
        interact_with_contract(web3, ethereum_data, bitcoin_data, web2_data)

    except Exception as e:
        print(f"Error in main execution: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```

**Notes:**
- Replace placeholders such as `your_private_key_here`, `your_infura_project_id`, `your_openweathermap_api_key_here`, and `[...]` (ABI array) with actual values.
- Ensure sensitive data (e.g., private keys) is stored securely, such as in environment variables or secure vaults, and avoid hardcoding them in production.
- Add unit tests to cover each function for robust code validation.
