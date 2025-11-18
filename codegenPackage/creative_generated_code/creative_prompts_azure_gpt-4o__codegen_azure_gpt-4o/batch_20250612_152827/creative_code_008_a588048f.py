"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sspanel.biz
Prompt: Write a Python program to track stablecoin instability and growth across Ethereum and Binance Smart Chain, inspired by sspanel.biz's coverage of Djed.
Generated: DETERMINISTIC_a588048fa23cf2ef
Batch ID: 20250612_152827
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
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
import requests
import json
from web3 import Web3
from datetime import datetime

# Constants for Ethereum and Binance Smart Chain (BSC) networks
ETHEREUM_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
BSC_RPC_URL = "https://bsc-dataseed.binance.org/"
STABLECOINS = {
    "Ethereum": [
        {"name": "DAI", "address": "0x6B175474E89094C44Da98b954EedeAC495271d0F"},
        {"name": "USDT", "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7"},
        {"name": "USDC", "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0CE3606eb48"}
    ],
    "Binance Smart Chain": [
        {"name": "BUSD", "address": "0xe9e7cea3dedca5984780bafc599bd69add087d56"},
        {"name": "USDT", "address": "0x55d398326f99059fF775485246999027B3197955"},
        {"name": "USDC", "address": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d"}
    ]
}

# Initialize web3 instances for both networks
ethereum_web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))
bsc_web3 = Web3(Web3.HTTPProvider(BSC_RPC_URL))

# ERC20 token ABI (simplified for balance and name retrieval)
ERC20_ABI = json.loads("""[
    {"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"type":"function"},
    {"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}
]""")

def fetch_stablecoin_data(web3_instance, stablecoins, network_name):
    """
    Fetch data for stablecoins on a given network.
    
    :param web3_instance: Web3 instance for the network
    :param stablecoins: List of stablecoins with their contract addresses
    :param network_name: Name of the network (e.g., Ethereum, BSC)
    :return: List of dictionaries containing stablecoin data
    """
    stablecoin_data = []

    for coin in stablecoins:
        try:
            # Initialize contract
            contract = web3_instance.eth.contract(address=coin['address'], abi=ERC20_ABI)
            
            # Fetch coin name and total supply
            name = contract.functions.name().call()
            total_supply = web3_instance.eth.get_balance(coin['address'])

            stablecoin_data.append({
                "network": network_name,
                "name": name,
                "address": coin['address'],
                "total_supply": total_supply
            })
        except Exception as e:
            print(f"Error fetching data for {coin['name']} ({coin['address']}): {e}")
    
    return stablecoin_data

def track_stablecoins():
    """
    Main function to track stablecoins across Ethereum and Binance Smart Chain.
    """
    all_stablecoin_data = []

    # Fetch Ethereum stablecoin data
    print("Fetching data for Ethereum...")
    ethereum_data = fetch_stablecoin_data(ethereum_web3, STABLECOINS["Ethereum"], "Ethereum")
    all_stablecoin_data.extend(ethereum_data)

    # Fetch Binance Smart Chain stablecoin data
    print("Fetching data for Binance Smart Chain...")
    bsc_data = fetch_stablecoin_data(bsc_web3, STABLECOINS["Binance Smart Chain"], "Binance Smart Chain")
    all_stablecoin_data.extend(bsc_data)

    # Log results
    print("\nStablecoin Data:")
    for data in all_stablecoin_data:
        print(f"[{data['network']}] {data['name']} (Address: {data['address']}) - Total Supply: {data['total_supply']}")

    return all_stablecoin_data

if __name__ == "__main__":
    try:
        # Track stablecoins and output results
        print("Tracking stablecoin instability and growth...")
        stablecoin_data = track_stablecoins()
        
        # Save results to a JSON file
        with open(f"stablecoin_data_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json", "w") as outfile:
            json.dump(stablecoin_data, outfile, indent=4)
        
        print("Stablecoin data saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
