"""
Generated Code Metadata:
========================
Original URL: https://app-explorer.pages.dev
Prompt: Write a Python script using web3.py to interact with multiple blockchain networks, ensuring interoperability as described in the Dapp Protocol's multichain-friendly features.
Generated: DETERMINISTIC_ec06b0890a568ea7
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from web3 import Web3
from web3.exceptions import ContractLogicError, InvalidAddress

# Define a class to handle interactions with multiple blockchain networks
class MultiChainDApp:
    def __init__(self, networks):
        """
        Initialize the MultiChainDApp with a list of network configurations.

        :param networks: A dictionary where keys are network names and values are dictionaries containing
                         'url' for the RPC URL and 'chain_id' for the blockchain's chain ID.
        """
        self.networks = networks
        self.web3_instances = self._initialize_web3_instances()

    def _initialize_web3_instances(self):
        """
        Initialize Web3 instances for each network.

        :return: A dictionary of Web3 instances keyed by network name.
        """
        web3_instances = {}
        for name, config in self.networks.items():
            try:
                web3 = Web3(Web3.HTTPProvider(config['url']))
                if not web3.isConnected():
                    raise ConnectionError(f"Failed to connect to {name} at {config['url']}")
                web3_instances[name] = web3
            except Exception as e:
                print(f"Error initializing {name}: {e}")
        return web3_instances

    def get_balance(self, network_name, address):
        """
        Get the balance of an address on a specified network.

        :param network_name: The name of the network to query.
        :param address: The address to check the balance of.
        :return: The balance in Wei, or None if an error occurs.
        """
        try:
            web3 = self.web3_instances[network_name]
            if not web3.isAddress(address):
                raise InvalidAddress(f"Invalid address: {address}")
            balance = web3.eth.get_balance(address)
            return balance
        except KeyError:
            print(f"Network {network_name} is not configured.")
        except InvalidAddress as e:
            print(e)
        except Exception as e:
            print(f"Error getting balance for {address} on {network_name}: {e}")
        return None

    def send_transaction(self, network_name, from_address, to_address, value, private_key):
        """
        Send a transaction from one address to another on a specified network.

        :param network_name: The name of the network to send the transaction on.
        :param from_address: The address sending the transaction.
        :param to_address: The address receiving the transaction.
        :param value: The amount of Wei to send.
        :param private_key: The private key of the sender's address.
        :return: The transaction hash, or None if an error occurs.
        """
        try:
            web3 = self.web3_instances[network_name]
            if not web3.isAddress(from_address) or not web3.isAddress(to_address):
                raise InvalidAddress("Invalid sender or receiver address.")
            
            # Create the transaction
            transaction = {
                'to': to_address,
                'value': web3.toWei(value, 'ether'),
                'gas': 2000000,
                'gasPrice': web3.toWei('50', 'gwei'),
                'nonce': web3.eth.getTransactionCount(from_address),
                'chainId': web3.eth.chain_id
            }

            # Sign the transaction
            signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

            # Send the transaction
            txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return txn_hash.hex()
        except KeyError:
            print(f"Network {network_name} is not configured.")
        except InvalidAddress as e:
            print(e)
        except ContractLogicError as e:
            print(f"Transaction failed: {e}")
        except Exception as e:
            print(f"Error sending transaction from {from_address} to {to_address} on {network_name}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Define network configurations
    networks = {
        'Ethereum': {
            'url': os.getenv('ETHEREUM_RPC_URL'),
            'chain_id': 1
        },
        'Binance Smart Chain': {
            'url': os.getenv('BSC_RPC_URL'),
            'chain_id': 56
        },
        'Polygon': {
            'url': os.getenv('POLYGON_RPC_URL'),
            'chain_id': 137
        }
    }

    # Initialize the DApp
    dapp = MultiChainDApp(networks)

    # Example: Get balance
    address = '0xYourAddressHere'
    balance = dapp.get_balance('Ethereum', address)
    print(f"Balance of {address} on Ethereum: {balance} Wei")

    # Example: Send transaction
    txn_hash = dapp.send_transaction('Binance Smart Chain', '0xYourFromAddress', '0xYourToAddress', 0.01, 'YourPrivateKey')
    print(f"Transaction hash: {txn_hash}")
```
