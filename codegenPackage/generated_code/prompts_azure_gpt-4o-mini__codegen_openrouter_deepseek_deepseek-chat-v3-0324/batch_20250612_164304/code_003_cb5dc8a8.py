"""
Generated Code Metadata:
========================
Original URL: https://jm4-dapp.pages.dev
Prompt: Generate a function that verifies withdrawals from a DApp to an external crypto wallet based on the provided content.
Generated: DETERMINISTIC_cb5dc8a89f229342
Batch ID: 20250612_164304
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
from web3 import Web3
from typing import Dict, Optional

class WithdrawalVerifier:
    """
    A class to verify withdrawals from a DApp to an external crypto wallet.
    Handles validation of addresses, transaction verification, and balance checks.
    """

    def __init__(self, provider_url: str, contract_address: str, contract_abi: Dict):
        """
        Initialize the WithdrawalVerifier with blockchain provider and contract details.

        Args:
            provider_url: URL of the Ethereum node provider (e.g., Infura, Alchemy)
            contract_address: Address of the DApp's smart contract
            contract_abi: ABI of the DApp's smart contract
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node")

        self.contract_address = self.web3.to_checksum_address(contract_address)
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=contract_abi
        )

    def is_valid_address(self, address: str) -> bool:
        """
        Check if a given address is a valid Ethereum address.

        Args:
            address: Ethereum address to validate

        Returns:
            bool: True if address is valid, False otherwise
        """
        try:
            return self.web3.is_address(address)
        except ValueError:
            return False

    def verify_withdrawal(
        self,
        user_address: str,
        recipient_address: str,
        amount: int,
        transaction_hash: str
    ) -> Dict:
        """
        Verify a withdrawal transaction from the DApp to an external wallet.

        Args:
            user_address: Address of the user initiating the withdrawal
            recipient_address: Destination wallet address
            amount: Amount withdrawn in wei
            transaction_hash: Hash of the withdrawal transaction

        Returns:
            Dict: Dictionary containing verification status and details
        """
        result = {
            "status": "error",
            "message": "",
            "transaction_verified": False,
            "balance_verified": False
        }

        try:
            # Validate addresses
            if not all([
                self.is_valid_address(user_address),
                self.is_valid_address(recipient_address)
            ]):
                result["message"] = "Invalid address provided"
                return result

            # Get transaction details
            tx = self.web3.eth.get_transaction(transaction_hash)
            if not tx:
                result["message"] = "Transaction not found"
                return result

            # Verify transaction details
            if tx["to"] != self.contract_address:
                result["message"] = "Transaction not sent to contract"
                return result

            # Decode transaction input
            tx_data = self.contract.decode_function_input(tx["input"])
            function_name = tx_data[0].fn_name

            if function_name != "withdraw":
                result["message"] = "Not a withdrawal transaction"
                return result

            # Verify transaction parameters
            if tx["from"].lower() != user_address.lower():
                result["message"] = "User address mismatch"
                return result

            if tx_data[1]["_to"].lower() != recipient_address.lower():
                result["message"] = "Recipient address mismatch"
                return result

            if tx_data[1]["_amount"] != amount:
                result["message"] = "Amount mismatch"
                return result

            # Verify transaction receipt (successful execution)
            tx_receipt = self.web3.eth.get_transaction_receipt(transaction_hash)
            if not tx_receipt or tx_receipt["status"] != 1:
                result["message"] = "Transaction failed"
                return result

            result["transaction_verified"] = True

            # Verify recipient balance change (optional)
            balance_before = self._get_balance_before_transfer(
                recipient_address,
                tx["blockNumber"]
            )
            balance_after = self.web3.eth.get_balance(recipient_address)

            if balance_after - balance_before == amount:
                result["balance_verified"] = True

            result["status"] = "success"
            result["message"] = "Withdrawal verified successfully"

        except Exception as e:
            result["message"] = f"Verification error: {str(e)}"

        return result

    def _get_balance_before_transfer(self, address: str, block_number: int) -> int:
        """
        Get the balance of an address before a specific block number.

        Args:
            address: Address to check balance for
            block_number: Block number to check balance before

        Returns:
            int: Balance in wei at the previous block
        """
        return self.web3.eth.get_balance(address, block_number - 1)

    def get_contract_balance(self, address: str) -> Optional[int]:
        """
        Get the current balance of a user in the DApp's contract.

        Args:
            address: User's address to check balance for

        Returns:
            Optional[int]: Balance in wei, or None if failed
        """
        try:
            return self.contract.functions.balanceOf(
                self.web3.to_checksum_address(address)
            ).call()
        except Exception:
            return None
```
