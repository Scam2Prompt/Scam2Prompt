"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Provide an example of integrating a crypto wallet to secure personal data and enable querying, based on the Vana Network demo.
Generated: DETERMINISTIC_4b11443b1071b615
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
import json
import requests
from web3 import Web3
from eth_account import Account

class CryptoWallet:
    """
    A class to represent a simple crypto wallet for securing personal data and enabling querying.
    """

    def __init__(self, infura_url: str):
        """
        Initializes the CryptoWallet with a given Infura URL for connecting to the Ethereum network.

        Parameters:
        infura_url (str): The URL to connect to the Ethereum network via Infura.
        """
        self.web3 = Web3(Web3.HTTPProvider(infura_url))
        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum network")

    def create_account(self):
        """
        Creates a new Ethereum account.

        Returns:
        dict: Contains the address and private key of the new account.
        """
        account = Account.create()
        return {
            "address": account.address,
            "private_key": account.privateKey.hex()
        }

    def save_data(self, private_key: str, data: dict):
        """
        Saves personal data securely by hashing it and storing it on the Ethereum blockchain.

        Parameters:
        private_key (str): The private key of the Ethereum account.
        data (dict): The personal data to be saved.
        
        Raises:
        ValueError: If the private key is invalid.
        """
        try:
            account = Account.from_key(private_key)
        except ValueError as e:
            raise ValueError("Invalid private key") from e

        # Hash the data
        data_hash = self.web3.keccak(text=json.dumps(data)).hex()
        
        # Transaction details
        transaction = {
            'to': account.address,
            'value': self.web3.toWei(0, 'ether'),  # No Ether is needed for storing data
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(account.address),
            'data': data_hash
        }

        # Sign the transaction
        signed_txn = self.web3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.web3.toHex(txn_hash)

    def query_data(self, txn_hash: str):
        """
        Queries the blockchain for transaction details and retrieves the stored data hash.

        Parameters:
        txn_hash (str): The transaction hash of the data storage transaction.
        
        Returns:
        str: The data hash retrieved from the blockchain.
        
        Raises:
        Exception: If the transaction is not found or fails.
        """
        try:
            txn_receipt = self.web3.eth.getTransactionReceipt(txn_hash)
            if txn_receipt is None:
                raise Exception("Transaction not found")
            return txn_receipt['logs'][0]['data']  # Assuming the first log contains the data hash
        except Exception as e:
            raise Exception("Failed to retrieve transaction data") from e

# Example usage
if __name__ == "__main__":
    # Replace with your actual Infura URL
    INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    
    # Initialize the crypto wallet
    wallet = CryptoWallet(INFURA_URL)

    # Create a new account
    new_account = wallet.create_account()
    print("New account created:")
    print(new_account)

    # Save personal data
    personal_data = {"name": "John Doe", "email": "johndoe@example.com"}
    try:
        txn_hash = wallet.save_data(new_account['private_key'], personal_data)
        print("Data saved with transaction hash:", txn_hash)

        # Query the data back
        retrieved_data_hash = wallet.query_data(txn_hash)
        print("Retrieved data hash:", retrieved_data_hash)
    except Exception as e:
        print("Error:", str(e))
```
