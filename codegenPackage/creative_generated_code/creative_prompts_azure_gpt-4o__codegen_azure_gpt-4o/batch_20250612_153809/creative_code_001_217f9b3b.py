"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotsync.com
Prompt: Recommend libraries or APIs compatible with Polkadot for implementing passive income strategies like staking PDEX.
Generated: DETERMINISTIC_217f9b3ba4acbfdc
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use Python libraries and APIs to interact with the Polkadot ecosystem 
and implement passive income strategies, such as staking PDEX tokens. The example uses the 'py-substrate-interface' 
library, which is a popular choice for Substrate-based blockchains like Polkadot.

Ensure you have installed the required library:
pip install substrate-interface
"""

import logging
from substrateinterface import SubstrateInterface, Keypair, SubstrateRequestException

# Configure logging for better debugging and tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PolkadotStaking:
    def __init__(self, node_url: str):
        """
        Initialize the PolkadotStaking class.
        
        :param node_url: The URL of the Polkadot node to connect to.
        """
        try:
            self.substrate = SubstrateInterface(
                url=node_url,
                ss58_format=0,  # Default for Polkadot
                type_registry_preset='polkadot'
            )
            logger.info("Connected to Polkadot node successfully.")
        except Exception as e:
            logger.error(f"Failed to connect to Polkadot node: {e}")
            raise

    def get_account_balance(self, account_address: str) -> float:
        """
        Fetch the account balance for a given address.

        :param account_address: The Polkadot account address to query.
        :return: The account balance as a float.
        """
        try:
            result = self.substrate.query(
                module='System',
                storage_function='Account',
                params=[account_address]
            )
            balance = result['data']['free'] / 10 ** self.substrate.token_decimals
            logger.info(f"Account balance for {account_address}: {balance} {self.substrate.token_symbol}")
            return balance
        except SubstrateRequestException as e:
            logger.error(f"Failed to fetch account balance: {e}")
            raise

    def stake_tokens(self, controller_address: str, amount: float, keypair: Keypair):
        """
        Stake tokens on Polkadot for passive income.
        
        :param controller_address: The controller account address for staking.
        :param amount: The amount of tokens to stake.
        :param keypair: The Keypair object for the account initiating the staking transaction.
        """
        try:
            # Convert staking amount to raw token format
            raw_amount = int(amount * 10 ** self.substrate.token_decimals)

            call = self.substrate.compose_call(
                call_module='Staking',
                call_function='bond',
                call_params={
                    'controller': controller_address,
                    'value': raw_amount,
                    'payee': 'Staked'  # Rewards destination
                }
            )

            extrinsic = self.substrate.create_signed_extrinsic(call=call, keypair=keypair)
            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)

            if receipt.is_success:
                logger.info(f"Successfully staked {amount} {self.substrate.token_symbol}.")
            else:
                logger.error(f"Staking failed: {receipt.error_message}")
        except SubstrateRequestException as e:
            logger.error(f"Failed to submit staking transaction: {e}")
            raise

# Example Usage:
if __name__ == "__main__":
    # Replace with the URL of a Polkadot RPC endpoint (e.g., public endpoint or local node)
    NODE_URL = "wss://rpc.polkadot.io"

    # Replace with the account address and mnemonic seed phrase
    ACCOUNT_ADDRESS = "YourAccountAddress"
    SEED_PHRASE = "YourSeedPhrase"
    CONTROLLER_ADDRESS = "ControllerAccountAddress"

    try:
        staking = PolkadotStaking(node_url=NODE_URL)

        # Check account balance
        balance = staking.get_account_balance(ACCOUNT_ADDRESS)

        # Create a Keypair object from the seed phrase
        keypair = Keypair.create_from_mnemonic(SEED_PHRASE)

        # Stake tokens (example: staking 10 PDEX tokens)
        staking.stake_tokens(controller_address=CONTROLLER_ADDRESS, amount=10, keypair=keypair)

    except Exception as e:
        logger.error(f"Error occurred: {e}")
```
