"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinivi.io
Prompt: Generate a code snippet that demonstrates how to integrate the IVI Token into a sports betting application using blockchain technology.
Generated: DETERMINISTIC_9e786c3c84eefc08
Batch ID: 20250612_155349
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node": {
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

class IVIToken:
    """
    A class to interact with the IVI Token smart contract for a sports betting application.
    """

    def __init__(self, contract_address, web3_instance):
        """
        Initializes the IVIToken instance.

        :param contract_address: The address of the IVI Token smart contract.
        :param web3_instance: An instance of Web3 connected to the blockchain.
        """
        self.contract_address = contract_address
        self.web3 = web3_instance
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=self.get_contract_abi()
        )

    def get_contract_abi(self):
        """
        Fetches the ABI of the IVI Token contract.

        :return: The ABI of the contract.
        """
        # This should be replaced with the actual ABI of your contract
        return json.loads('''[
            // Replace this with the actual ABI
        ]''')

    def get_balance(self, address):
        """
        Retrieves the IVI token balance of a given wallet address.

        :param address: The wallet address of the user.
        :return: The balance of IVI tokens.
        """
        try:
            balance = self.contract.functions.balanceOf(address).call()
            return balance
        except Exception as e:
            print(f"Error getting balance: {e}")
            return None

    def transfer_tokens(self, to_address, amount, private_key):
        """
        Transfers IVI tokens from the sender's address to another address.

        :param to_address: The recipient's wallet address.
        :param amount: The amount of tokens to transfer.
        :param private_key: The private key of the sender's wallet.
        :return: Transaction hash if successful, None otherwise.
        """
        try:
            account = self.web3.eth.account.from_key(private_key)
            nonce = self.web3.eth.getTransactionCount(account.address)

            # Create the transaction
            txn = self.contract.functions.transfer(to_address, amount).buildTransaction({
                'chainId': 1,  # Mainnet ID, change accordingly
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'nonce': nonce,
            })

            # Sign the transaction
            signed_txn = self.web3.eth.account.signTransaction(txn, private_key)

            # Send the transaction
            txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return txn_hash.hex()
        except Exception as e:
            print(f"Error transferring tokens: {e}")
            return None

# Example usage
if __name__ == "__main__":
    from web3 import Web3

    # Initialize Web3 instance (connect to your preferred network)
    w3 = Web3(Web3.HTTPProvider('https://your.ethereum.node'))

    # Initialize IVI Token
    IVI_CONTRACT_ADDRESS = '0xYourIVIContractAddress'
    ivitoken = IVIToken(IVI_CONTRACT_ADDRESS, w3)

    # Replace with real user address and private key
    user_address = '0xYourUserAddress'
    user_private_key = 'your-private-key'

    # Get balance
    balance = ivitoken.get_balance(user_address)
    print(f"User balance: {balance}")

    # Transfer tokens example
    recipient_address = '0xRecipientAddress'
    amount_to_transfer = 100  # Amount to transfer
    txn_hash = ivitoken.transfer_tokens(recipient_address, amount_to_transfer, user_private_key)
    
    if txn_hash:
        print(f"Transaction successful with hash: {txn_hash}")
    else:
        print("Transaction failed.")
```
