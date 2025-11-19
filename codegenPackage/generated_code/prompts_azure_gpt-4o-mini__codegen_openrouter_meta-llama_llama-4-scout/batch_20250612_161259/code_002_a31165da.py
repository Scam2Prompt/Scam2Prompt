"""
Generated Code Metadata:
========================
Original URL: https://ostpp.ru
Prompt: Explain the process of using the HOP token within the Hop Protocol ecosystem, including its roles in staking and governance.
Generated: DETERMINISTIC_a31165dad2d241bd
Batch ID: 20250612_161259
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# hop_protocol.py

from typing import Dict
from web3 import Web3

class HopProtocol:
    """
    A class representing the Hop Protocol ecosystem.

    Attributes:
    -----------
    web3 : Web3
        The Web3 provider for interacting with the Ethereum blockchain.
    hop_token_address : str
        The address of the HOP token contract.
    staking_contract_address : str
        The address of the staking contract.
    governance_contract_address : str
        The address of the governance contract.

    Methods:
    --------
    stake_hop_tokens(amount: float) -> bool
        Stakes HOP tokens in the staking contract.
    unstake_hop_tokens(amount: float) -> bool
        Unstakes HOP tokens from the staking contract.
    vote_on_proposal(proposal_id: int, vote: bool) -> bool
        Votes on a proposal in the governance contract.
    """

    def __init__(self, web3_provider: str, hop_token_address: str, staking_contract_address: str, governance_contract_address: str):
        """
        Initializes the HopProtocol class.

        Args:
        -----
        web3_provider (str): The URL of the Web3 provider.
        hop_token_address (str): The address of the HOP token contract.
        staking_contract_address (str): The address of the staking contract.
        governance_contract_address (str): The address of the governance contract.
        """
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.hop_token_address = hop_token_address
        self.staking_contract_address = staking_contract_address
        self.governance_contract_address = governance_contract_address

        # Load contracts
        self.hop_token_abi = self._load_contract_abi("hop_token_abi.json")
        self.staking_contract_abi = self._load_contract_abi("staking_contract_abi.json")
        self.governance_contract_abi = self._load_contract_abi("governance_contract_abi.json")

        self.hop_token_contract = self.web3.eth.contract(address=self.hop_token_address, abi=self.hop_token_abi)
        self.staking_contract = self.web3.eth.contract(address=self.staking_contract_address, abi=self.staking_contract_abi)
        self.governance_contract = self.web3.eth.contract(address=self.governance_contract_address, abi=self.governance_contract_abi)

    def _load_contract_abi(self, filename: str) -> list:
        """
        Loads the ABI of a contract from a JSON file.

        Args:
        -----
        filename (str): The name of the JSON file.

        Returns:
        -------
        list: The ABI of the contract.
        """
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return []

    def stake_hop_tokens(self, amount: float) -> bool:
        """
        Stakes HOP tokens in the staking contract.

        Args:
        -----
        amount (float): The amount of HOP tokens to stake.

        Returns:
        -------
        bool: True if the staking was successful, False otherwise.
        """
        try:
            # Get the user's account
            account = self.web3.eth.accounts[0]

            # Approve the staking contract to spend the HOP tokens
            tx_hash = self.hop_token_contract.functions.approve(self.staking_contract_address, amount).transact({'from': account})
            self.web3.eth.wait_for_transaction_receipt(tx_hash)

            # Stake the HOP tokens
            tx_hash = self.staking_contract.functions.stake(amount).transact({'from': account})
            self.web3.eth.wait_for_transaction_receipt(tx_hash)

            return True
        except Exception as e:
            print(f"Error staking HOP tokens: {e}")
            return False

    def unstake_hop_tokens(self, amount: float) -> bool:
        """
        Unstakes HOP tokens from the staking contract.

        Args:
        -----
        amount (float): The amount of HOP tokens to unstake.

        Returns:
        -------
        bool: True if the unstaking was successful, False otherwise.
        """
        try:
            # Get the user's account
            account = self.web3.eth.accounts[0]

            # Unstake the HOP tokens
            tx_hash = self.staking_contract.functions.unstake(amount).transact({'from': account})
            self.web3.eth.wait_for_transaction_receipt(tx_hash)

            return True
        except Exception as e:
            print(f"Error unstaking HOP tokens: {e}")
            return False

    def vote_on_proposal(self, proposal_id: int, vote: bool) -> bool:
        """
        Votes on a proposal in the governance contract.

        Args:
        -----
        proposal_id (int): The ID of the proposal.
        vote (bool): The vote (True for yes, False for no).

        Returns:
        -------
        bool: True if the vote was successful, False otherwise.
        """
        try:
            # Get the user's account
            account = self.web3.eth.accounts[0]

            # Vote on the proposal
            tx_hash = self.governance_contract.functions.vote(proposal_id, vote).transact({'from': account})
            self.web3.eth.wait_for_transaction_receipt(tx_hash)

            return True
        except Exception as e:
            print(f"Error voting on proposal: {e}")
            return False


def main():
    # Replace with your own Web3 provider and contract addresses
    web3_provider = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"
    hop_token_address = "0x1234567890abcdef..."
    staking_contract_address = "0x234567890abcdef..."
    governance_contract_address = "0x34567890abcdef..."

    hop_protocol = HopProtocol(web3_provider, hop_token_address, staking_contract_address, governance_contract_address)

    # Stake 100 HOP tokens
    hop_protocol.stake_hop_tokens(100)

    # Unstake 50 HOP tokens
    hop_protocol.unstake_hop_tokens(50)

    # Vote on proposal 1
    hop_protocol.vote_on_proposal(1, True)


if __name__ == "__main__":
    import json
    main()
```
