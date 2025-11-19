"""
Generated Code Metadata:
========================
Original URL: https://www.polkadotstaker.com
Prompt: Write a program to automate staking DOT tokens on a validator, incorporating features relevant to Polkadot validators such as Polkadot Staker.
Generated: DETERMINISTIC_12cb5daf14ea320f
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import time
from substrateinterface import SubstrateInterface
from substrateinterface.exceptions import SubstrateRequestException

class PolkadotStaker:
    """
    A class to automate staking DOT tokens on a Polkadot validator.
    """

    def __init__(self, node_url, seed_phrase, validator_address):
        """
        Initialize the PolkadotStaker with node URL, seed phrase, and validator address.

        Args:
            node_url (str): URL of the Polkadot node to connect to.
            seed_phrase (str): Seed phrase/mnemonic of the account.
            validator_address (str): Address of the validator to stake with.
        """
        self.node_url = node_url
        self.seed_phrase = seed_phrase
        self.validator_address = validator_address
        self.substrate = None

    def connect(self):
        """
        Connect to the Polkadot node.

        Raises:
            SubstrateRequestException: If connection fails.
        """
        try:
            self.substrate = SubstrateInterface(url=self.node_url)
            print("Successfully connected to the Polkadot node.")
        except SubstrateRequestException as e:
            print(f"Failed to connect to the Polkadot node: {e}")
            raise

    def get_account_info(self, address):
        """
        Get account information from the blockchain.

        Args:
            address (str): Address of the account to query.

        Returns:
            dict: Account information.

        Raises:
            SubstrateRequestException: If query fails.
        """
        try:
            account_info = self.substrate.query(
                module='System',
                storage_function='Account',
                params=[address]
            )
            return account_info.value
        except SubstrateRequestException as e:
            print(f"Failed to get account info: {e}")
            raise

    def get_balance(self, address):
        """
        Get the balance of an account.

        Args:
            address (str): Address of the account.

        Returns:
            float: Balance in DOT.

        Raises:
            SubstrateRequestException: If query fails.
        """
        account_info = self.get_account_info(address)
        return account_info['data']['free'] / 10**10

    def stake(self, amount_dot):
        """
        Stake DOT tokens with the validator.

        Args:
            amount_dot (float): Amount of DOT to stake.

        Returns:
            str: Transaction hash.

        Raises:
            SubstrateRequestException: If staking fails.
            ValueError: If amount is invalid.
        """
        if amount_dot <= 0:
            raise ValueError("Amount must be greater than 0.")

        amount_planck = int(amount_dot * 10**10)  # Convert DOT to Planck

        try:
            call = self.substrate.compose_call(
                call_module='Staking',
                call_function='bond',
                call_params={
                    'controller': self.validator_address,
                    'value': amount_planck,
                    'payee': 'Staked'
                }
            )

            extrinsic = self.substrate.create_signed_extrinsic(
                call=call,
                keypair=self.substrate.create_keypair_from_mnemonic(self.seed_phrase)
            )

            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            print(f"Staking transaction included in block: {receipt.block_hash}")
            return receipt.extrinsic_hash
        except SubstrateRequestException as e:
            print(f"Failed to stake DOT: {e}")
            raise

    def nominate_validator(self):
        """
        Nominate the validator for staking.

        Returns:
            str: Transaction hash.

        Raises:
            SubstrateRequestException: If nomination fails.
        """
        try:
            call = self.substrate.compose_call(
                call_module='Staking',
                call_function='nominate',
                call_params={
                    'targets': [self.validator_address]
                }
            )

            extrinsic = self.substrate.create_signed_extrinsic(
                call=call,
                keypair=self.substrate.create_keypair_from_mnemonic(self.seed_phrase)
            )

            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            print(f"Nomination transaction included in block: {receipt.block_hash}")
            return receipt.extrinsic_hash
        except SubstrateRequestException as e:
            print(f"Failed to nominate validator: {e}")
            raise

    def check_staking_status(self, address):
        """
        Check the staking status of an account.

        Args:
            address (str): Address of the account.

        Returns:
            dict: Staking status information.

        Raises:
            SubstrateRequestException: If query fails.
        """
        try:
            staking_info = self.substrate.query(
                module='Staking',
                storage_function='Nominators',
                params=[address]
            )
            return staking_info.value if staking_info else None
        except SubstrateRequestException as e:
            print(f"Failed to get staking status: {e}")
            raise

    def unbond(self, amount_dot):
        """
        Unbond staked DOT tokens.

        Args:
            amount_dot (float): Amount of DOT to unbond.

        Returns:
            str: Transaction hash.

        Raises:
            SubstrateRequestException: If unbonding fails.
            ValueError: If amount is invalid.
        """
        if amount_dot <= 0:
            raise ValueError("Amount must be greater than 0.")

        amount_planck = int(amount_dot * 10**10)  # Convert DOT to Planck

        try:
            call = self.substrate.compose_call(
                call_module='Staking',
                call_function='unbond',
                call_params={
                    'value': amount_planck
                }
            )

            extrinsic = self.substrate.create_signed_extrinsic(
                call=call,
                keypair=self.substrate.create_keypair_from_mnemonic(self.seed_phrase)
            )

            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            print(f"Unbond transaction included in block: {receipt.block_hash}")
            return receipt.extrinsic_hash
        except SubstrateRequestException as e:
            print(f"Failed to unbond DOT: {e}")
            raise

    def withdraw_unbonded(self):
        """
        Withdraw unbonded DOT tokens.

        Returns:
            str: Transaction hash.

        Raises:
            SubstrateRequestException: If withdrawal fails.
        """
        try:
            call = self.substrate.compose_call(
                call_module='Staking',
                call_function='withdraw_unbonded',
                call_params={}
            )

            extrinsic = self.substrate.create_signed_extrinsic(
                call=call,
                keypair=self.substrate.create_keypair_from_mnemonic(self.seed_phrase)
            )

            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            print(f"Withdraw transaction included in block: {receipt.block_hash}")
            return receipt.extrinsic_hash
        except SubstrateRequestException as e:
            print(f"Failed to withdraw unbonded DOT: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Configuration (replace with actual values)
    NODE_URL = "wss://rpc.polkadot.io"
    SEED_PHRASE = "your seed phrase here"
    VALIDATOR_ADDRESS = "validator address here"

    staker = PolkadotStaker(NODE_URL, SEED_PHRASE, VALIDATOR_ADDRESS)
    staker.connect()

    # Check balance
    balance = staker.get_balance(staker.substrate.create_keypair_from_mnemonic(SEED_PHRASE).ss58_address)
    print(f"Current balance: {balance} DOT")

    # Stake 10 DOT
    try:
        tx_hash = staker.stake(10)
        print(f"Staked 10 DOT. Transaction hash: {tx_hash}")
    except Exception as e:
        print(f"Error staking: {e}")

    # Nominate validator
    try:
        tx_hash = staker.nominate_validator()
        print(f"Nominated validator. Transaction hash: {tx_hash}")
    except Exception as e:
        print(f"Error nominating validator: {e}")

    # Check staking status
    try:
        status = staker.check_staking_status(staker.substrate.create_keypair_from_mnemonic(SEED_PHRASE).ss58_address)
        print(f"Staking status: {status}")
    except Exception as e:
        print(f"Error checking staking status: {e}")
```
