"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeissuesfix.com
Prompt: How can I implement a self-custodial wallet for decentralized Dapps using multichain support?
Generated: DETERMINISTIC_919409aef05a990b
Batch ID: 20250612_160232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from web3 import Web3
from eth_account import Account

class SelfCustodialWallet:
    """
    A self-custodial wallet for interacting with decentralized applications (DApps)
    across multiple blockchain networks.
    """

    def __init__(self, provider_url, private_key=None):
        """
        Initializes the wallet with a specified provider URL and an optional private key.

        :param provider_url: URL of the Ethereum provider (e.g., Infura or Alchemy)
        :param private_key: Optional private key for wallet access
        """
        self.provider_url = provider_url
        self.web3 = Web3(Web3.HTTPProvider(provider_url))

        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum provider.")

        if private_key:
            self.account = self.load_account(private_key)
        else:
            self.account = None

    def load_account(self, private_key):
        """
        Loads an Ethereum account from a private key.

        :param private_key: The private key of the account
        :return: An Account object
        """
        try:
            account = Account.from_key(private_key)
            return account
        except ValueError as e:
            raise ValueError("Invalid private key.") from e

    def create_account(self):
        """
        Creates a new Ethereum account and returns the private key and address.

        :return: Tuple containing the private key and address
        """
        account = Account.create()
        return account.privateKey.hex(), account.address

    def send_transaction(self, to_address, amount, gas_price=None):
        """
        Sends Ether from this wallet to another address.

        :param to_address: The recipient's Ethereum address
        :param amount: Amount of Ether to send (in Wei)
        :param gas_price: Optional gas price (in Gwei)
        :return: Transaction hash
        """
        if self.account is None:
            raise PermissionError("No account loaded. Use a private key to load an account.")

        if gas_price is None:
            gas_price = self.web3.eth.gas_price

        transaction = {
            'to': to_address,
            'value': amount,
            'gas': 2000000,  # Set a default gas limit
            'gasPrice': self.web3.toWei(gas_price, 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(self.account.address),
            'chainId': self.web3.eth.chain_id,
        }

        signed_txn = self.web3.eth.account.signTransaction(transaction, self.account.privateKey)

        try:
            txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return txn_hash.hex()
        except Exception as e:
            raise RuntimeError("Transaction failed.") from e

    def get_balance(self):
        """
        Retrieves the Ether balance of the wallet.

        :return: Balance in Wei
        """
        if self.account is None:
            raise PermissionError("No account loaded. Use a private key to load an account.")

        balance = self.web3.eth.get_balance(self.account.address)
        return balance

if __name__ == "__main__":
    # Example usage
    provider_url = os.getenv("ETH_PROVIDER_URL")  # Set your provider URL in an environment variable
    private_key = os.getenv("PRIVATE_KEY")  # Optionally set your private key in an environment variable

    wallet = SelfCustodialWallet(provider_url, private_key)

    # Creating a new account
    new_private_key, new_address = wallet.create_account()
    print(f"New account created. Address: {new_address}, Private Key: {new_private_key}")

    # Check balance
    balance = wallet.get_balance()
    print(f"Current balance: {balance} Wei")

    # Example sending transaction
    try:
        txn_hash = wallet.send_transaction("0xRecipientAddressHere", 1000000000000000000)  # Sending 1 Ether
        print(f"Transaction sent with hash: {txn_hash}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
