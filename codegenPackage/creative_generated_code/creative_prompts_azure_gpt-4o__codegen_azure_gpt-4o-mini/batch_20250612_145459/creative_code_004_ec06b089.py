"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-explorer.pages.dev
Prompt: Write a Python script using web3.py to interact with multiple blockchain networks, ensuring interoperability as described in the Dapp Protocol's multichain-friendly features.
Generated: DETERMINISTIC_ec06b0890a568ea7
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from web3.exceptions import ContractLogicError

# Configuration: Define the blockchain networks to connect to
NETWORKS = {
    "ethereum": {
        "url": os.getenv("ETHEREUM_RPC_URL"),
        "chain_id": 1
    },
    "polygon": {
        "url": os.getenv("POLYGON_RPC_URL"),
        "chain_id": 137
    },
    "bsc": {
        "url": os.getenv("BSC_RPC_URL"),
        "chain_id": 56
    }
}

class MultiChainDApp:
    def __init__(self):
        """
        Initialize the MultiChainDApp with connections to various blockchain networks.
        """
        self.web3_instances = {}
        for name, config in NETWORKS.items():
            self.web3_instances[name] = self.connect_to_network(config)

    def connect_to_network(self, config):
        """
        Connect to a blockchain network using the provided configuration.

        :param config: Dictionary containing the RPC URL and chain ID
        :return: Web3 instance
        """
        try:
            web3 = Web3(Web3.HTTPProvider(config["url"]))
            if web3.isConnected():
                print(f"Connected to {config['url']}")
                return web3
            else:
                raise ConnectionError(f"Could not connect to {config['url']}")
        except Exception as e:
            print(f"Error connecting to {config['url']}: {e}")
            return None

    def get_balance(self, network_name, address):
        """
        Retrieve the balance of a specified address on the given network.

        :param network_name: Name of the network (e.g., 'ethereum', 'polygon', 'bsc')
        :param address: Address to check the balance for
        :return: Balance in Wei
        """
        web3 = self.web3_instances.get(network_name)
        if web3 is None:
            raise ValueError(f"Network '{network_name}' is not connected.")
        
        try:
            balance = web3.eth.get_balance(address)
            return balance
        except Exception as e:
            print(f"Error retrieving balance for {address} on {network_name}: {e}")
            return None

    def send_transaction(self, network_name, from_address, private_key, to_address, value):
        """
        Send a transaction from one address to another on the specified network.

        :param network_name: Name of the network
        :param from_address: Address sending the transaction
        :param private_key: Private key of the sender
        :param to_address: Address receiving the transaction
        :param value: Amount to send in Wei
        :return: Transaction hash
        """
        web3 = self.web3_instances.get(network_name)
        if web3 is None:
            raise ValueError(f"Network '{network_name}' is not connected.")

        try:
            # Build the transaction
            transaction = {
                'to': to_address,
                'value': value,
                'gas': 2000000,
                'gasPrice': web3.toWei('50', 'gwei'),
                'nonce': web3.eth.getTransactionCount(from_address),
                'chainId': NETWORKS[network_name]["chain_id"]
            }
            
            # Sign the transaction
            signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
            
            # Send the signed transaction
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            return web3.toHex(tx_hash)
        except ContractLogicError as cle:
            print(f"Contract logic error: {cle}")
            return None
        except Exception as e:
            print(f"Error sending transaction: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    dapp = MultiChainDApp()
    
    # Replace with actual addresses and private keys for testing
    ethereum_address = "0xYourEthereumAddress"
    private_key = "YourPrivateKey"
    polygon_address = "0xYourPolygonAddress"
    
    # Get Ethereum balance
    eth_balance = dapp.get_balance("ethereum", ethereum_address)
    print(f"Ethereum Balance: {eth_balance}")

    # Send a transaction on Ethereum
    tx_hash = dapp.send_transaction("ethereum", ethereum_address, private_key, polygon_address, eth_balance // 10)
    print(f"Transaction Hash: {tx_hash}")
```
