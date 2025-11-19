"""
Generated Code Metadata:
========================
Original URL: https://singularity.pages.dev
Prompt: Generate a script to interact with SingularityNET's AGIX token for decentralized transactions and governance participation.
Generated: DETERMINISTIC_b5f9dd331ecf3a25
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agix_interactor.py

import os
import json
from web3 import Web3
from web3.exceptions import Web3Exception

class AGIXInteractor:
    """
    Interactor for SingularityNET's AGIX token.

    Provides functionality for decentralized transactions and governance participation.
    """

    def __init__(self, rpc_url, private_key, agix_contract_address, agix_abi):
        """
        Initialize the AGIX interactor.

        :param rpc_url: URL of the Ethereum RPC endpoint
        :param private_key: Private key of the Ethereum account
        :param agix_contract_address: Address of the AGIX contract
        :param agix_abi: ABI of the AGIX contract
        """
        self.rpc_url = rpc_url
        self.private_key = private_key
        self.agix_contract_address = agix_contract_address
        self.agix_abi = agix_abi

        # Initialize Web3 provider
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))

        # Check if Web3 provider is connected
        if not self.w3.isConnected():
            raise Web3Exception("Failed to connect to Web3 provider")

        # Initialize AGIX contract
        self.agix_contract = self.w3.eth.contract(address=self.agix_contract_address, abi=self.agix_abi)

    def get_balance(self, account_address):
        """
        Get the AGIX balance of an account.

        :param account_address: Address of the account
        :return: AGIX balance
        """
        try:
            balance = self.agix_contract.functions.balanceOf(account_address).call()
            return balance
        except Exception as e:
            print(f"Error getting balance: {e}")
            return None

    def transfer_agix(self, recipient_address, amount):
        """
        Transfer AGIX tokens to a recipient.

        :param recipient_address: Address of the recipient
        :param amount: Amount of AGIX to transfer
        """
        try:
            # Get the current account address
            account_address = self.w3.eth.account.fromKey(self.private_key).address

            # Get the current nonce
            nonce = self.w3.eth.getTransactionCount(account_address)

            # Create the transaction
            tx = self.agix_contract.functions.transfer(recipient_address, amount).buildTransaction({
                'from': account_address,
                'nonce': nonce,
                'gas': 200000,
                'gasPrice': self.w3.toWei('20', 'gwei')
            })

            # Sign the transaction
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)

            # Send the transaction
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            print(f"Error transferring AGIX: {e}")
            return None

    def participate_in_governance(self, proposal_id, vote):
        """
        Participate in governance by voting on a proposal.

        :param proposal_id: ID of the proposal
        :param vote: Vote (True for yes, False for no)
        """
        try:
            # Get the current account address
            account_address = self.w3.eth.account.fromKey(self.private_key).address

            # Get the current nonce
            nonce = self.w3.eth.getTransactionCount(account_address)

            # Create the transaction
            tx = self.agix_contract.functions.vote(proposal_id, vote).buildTransaction({
                'from': account_address,
                'nonce': nonce,
                'gas': 200000,
                'gasPrice': self.w3.toWei('20', 'gwei')
            })

            # Sign the transaction
            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)

            # Send the transaction
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return tx_hash.hex()
        except Exception as e:
            print(f"Error participating in governance: {e}")
            return None


def main():
    # Load configuration from environment variables
    rpc_url = os.environ.get('RPC_URL')
    private_key = os.environ.get('PRIVATE_KEY')
    agix_contract_address = os.environ.get('AGIX_CONTRACT_ADDRESS')
    agix_abi = json.loads(os.environ.get('AGIX_ABI'))

    # Create an AGIX interactor
    agix_interactor = AGIXInteractor(rpc_url, private_key, agix_contract_address, agix_abi)

    # Example usage
    account_address = '0x...'  # Replace with the account address
    balance = agix_interactor.get_balance(account_address)
    print(f"Balance: {balance}")

    recipient_address = '0x...'  # Replace with the recipient address
    amount = 100  # Replace with the amount
    tx_hash = agix_interactor.transfer_agix(recipient_address, amount)
    print(f"Transaction hash: {tx_hash}")

    proposal_id = 123  # Replace with the proposal ID
    vote = True  # Replace with the vote
    tx_hash = agix_interactor.participate_in_governance(proposal_id, vote)
    print(f"Transaction hash: {tx_hash}")


if __name__ == '__main__':
    main()
```
