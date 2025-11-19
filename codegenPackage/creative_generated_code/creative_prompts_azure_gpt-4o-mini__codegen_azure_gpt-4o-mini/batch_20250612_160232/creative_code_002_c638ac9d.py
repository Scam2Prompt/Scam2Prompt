"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeissuesfix.com
Prompt: What are the best practices for developing multichain support in decentralized applications?
Generated: DETERMINISTIC_c638ac9dab74c7d4
Batch ID: 20250612_160232
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
import web3
from web3 import Web3
from typing import List, Dict

class MultiChainDApp:
    def __init__(self, chains: List[Dict[str, str]]):
        """
        Initializes the MultiChainDApp with a list of blockchain configurations.
        
        :param chains: List of dictionaries containing blockchain configurations, 
                       each with 'name', 'rpc_url', and 'chain_id'.
        """
        self.chains = {}
        for chain in chains:
            self.add_chain(chain['name'], chain['rpc_url'], chain['chain_id'])

    def add_chain(self, name: str, rpc_url: str, chain_id: str):
        """
        Adds a new blockchain to the application.

        :param name: The name of the blockchain.
        :param rpc_url: The RPC URL for the blockchain.
        :param chain_id: The chain ID of the blockchain.
        """
        try:
            # Create a Web3 instance
            w3 = Web3(Web3.HTTPProvider(rpc_url))
            if not w3.isConnected():
                raise ValueError(f"Could not connect to {name} at {rpc_url}")
            self.chains[name] = {
                'web3': w3,
                'chain_id': chain_id
            }
            print(f"Successfully added chain: {name}")
        except Exception as e:
            print(f"Error adding chain {name}: {str(e)}")

    def get_chain_balance(self, chain_name: str, address: str) -> float:
        """
        Retrieves the balance of a given address on a specified blockchain.

        :param chain_name: The name of the blockchain.
        :param address: The address whose balance is to be checked.
        :return: The balance of the address in Ether.
        """
        try:
            if chain_name not in self.chains:
                raise ValueError(f"Chain {chain_name} not found.")
            w3 = self.chains[chain_name]['web3']
            balance_wei = w3.eth.get_balance(address)
            balance_eth = w3.fromWei(balance_wei, 'ether')
            return balance_eth
        except Exception as e:
            print(f"Error getting balance for {address} on {chain_name}: {str(e)}")
            return 0.0

    def send_transaction(self, chain_name: str, from_address: str, to_address: str, amount: float, private_key: str):
        """
        Sends a transaction from one address to another on a specified blockchain.

        :param chain_name: The name of the blockchain.
        :param from_address: The sender's address.
        :param to_address: The recipient's address.
        :param amount: The amount of Ether to send.
        :param private_key: The private key of the sender's address.
        """
        try:
            if chain_name not in self.chains:
                raise ValueError(f"Chain {chain_name} not found.")
            w3 = self.chains[chain_name]['web3']

            # Prepare transaction details
            nonce = w3.eth.getTransactionCount(from_address)
            value = w3.toWei(amount, 'ether')

            transaction = {
                'to': to_address,
                'value': value,
                'gas': 2000000,
                'gasPrice': w3.toWei('50', 'gwei'),
                'nonce': nonce,
                'chainId': self.chains[chain_name]['chain_id']
            }

            # Sign the transaction
            signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

            # Send the transaction
            txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
            print(f"Transaction sent: {txn_hash.hex()}")
        except Exception as e:
            print(f"Error sending transaction from {from_address} to {to_address}: {str(e)}")


# Example usage
if __name__ == "__main__":
    chains_config = [
        {'name': 'Ethereum', 'rpc_url': 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID', 'chain_id': '1'},
        {'name': 'Binance Smart Chain', 'rpc_url': 'https://bsc-dataseed.binance.org/', 'chain_id': '56'}
    ]

    dapp = MultiChainDApp(chains_config)
    
    # Replace with actual addresses and private key
    address_to_check = '0xYourEthereumAddress'
    balance = dapp.get_chain_balance('Ethereum', address_to_check)
    print(f"Balance of {address_to_check}: {balance} ETH")
    
    # Uncomment to send transaction
    # dapp.send_transaction('Ethereum', '0xYourEthereumAddress', '0xRecipientAddress', 0.01, 'YourPrivateKey')
```
