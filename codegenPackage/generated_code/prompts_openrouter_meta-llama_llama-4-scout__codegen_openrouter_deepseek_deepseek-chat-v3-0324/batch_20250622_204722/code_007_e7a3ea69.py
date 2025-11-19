"""
Generated Code Metadata:
========================
Original URL: https://expulserevs.pages.dev
Prompt: Develop a library to interact with the PulseChain Mainnet Populator, allowing users to add tokens and view their balances.
Generated: DETERMINISTIC_e7a3ea69300b3d4b
Batch ID: 20250622_204722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import Dict, List, Optional
from web3 import Web3
from web3.exceptions import ContractLogicError, InvalidAddress
from eth_utils import to_checksum_address

class PulseChainPopulator:
    """
    A library to interact with the PulseChain Mainnet Populator.
    Allows users to add tokens and view their balances.
    """

    def __init__(self, rpc_url: str, contract_address: str):
        """
        Initialize the PulseChainPopulator.

        Args:
            rpc_url: The RPC URL for PulseChain Mainnet.
            contract_address: The address of the Populator contract.
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to PulseChain RPC")

        self.contract_address = to_checksum_address(contract_address)
        self.contract_abi = self._load_contract_abi()
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )

    def _load_contract_abi(self) -> List[Dict]:
        """
        Load the contract ABI from a predefined source.
        In production, this should be fetched from a verified source.

        Returns:
            The contract ABI as a list of dictionaries.
        """
        # Simplified ABI for demonstration. In production, use the full ABI.
        return [
            {
                "inputs": [
                    {"internalType": "address", "name": "token", "type": "address"},
                    {"internalType": "address", "name": "account", "type": "address"}
                ],
                "name": "addToken",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "inputs": [
                    {"internalType": "address", "name": "account", "type": "address"}
                ],
                "name": "getBalances",
                "outputs": [
                    {
                        "components": [
                            {"internalType": "address", "name": "token", "type": "address"},
                            {"internalType": "uint256", "name": "balance", "type": "uint256"}
                        ],
                        "internalType": "struct Populator.TokenBalance[]",
                        "name": "",
                        "type": "tuple[]"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            }
        ]

    def add_token(self, token_address: str, account_address: str, private_key: str) -> str:
        """
        Add a token to the populator for a specific account.

        Args:
            token_address: The address of the token to add.
            account_address: The account address to associate with the token.
            private_key: The private key to sign the transaction.

        Returns:
            The transaction hash.

        Raises:
            ValueError: If addresses are invalid.
            ContractLogicError: If contract call fails.
        """
        try:
            token_address = to_checksum_address(token_address)
            account_address = to_checksum_address(account_address)
        except (ValueError, InvalidAddress) as e:
            raise ValueError(f"Invalid address: {e}")

        nonce = self.web3.eth.get_transaction_count(account_address)
        tx = self.contract.functions.addToken(
            token_address,
            account_address
        ).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': 200000,
            'gasPrice': self.web3.eth.gas_price,
            'nonce': nonce,
        })

        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()

    def get_balances(self, account_address: str) -> List[Dict[str, str]]:
        """
        Get token balances for a specific account.

        Args:
            account_address: The account address to query.

        Returns:
            A list of dictionaries containing token addresses and balances.

        Raises:
            ValueError: If address is invalid.
            ContractLogicError: If contract call fails.
        """
        try:
            account_address = to_checksum_address(account_address)
        except (ValueError, InvalidAddress) as e:
            raise ValueError(f"Invalid address: {e}")

        balances = self.contract.functions.getBalances(account_address).call()
        return [
            {
                'token': balance[0],
                'balance': str(balance[1])
            }
            for balance in balances
        ]

    def get_token_balance(self, account_address: str, token_address: str) -> Optional[str]:
        """
        Get balance of a specific token for an account.

        Args:
            account_address: The account address to query.
            token_address: The token address to query.

        Returns:
            The balance as a string, or None if not found.

        Raises:
            ValueError: If addresses are invalid.
        """
        try:
            balances = self.get_balances(account_address)
            token_address = to_checksum_address(token_address)
            for balance in balances:
                if balance['token'].lower() == token_address.lower():
                    return balance['balance']
            return None
        except (ValueError, ContractLogicError) as e:
            raise ValueError(f"Error getting balance: {e}")
```
