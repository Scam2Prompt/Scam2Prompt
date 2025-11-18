"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ambassadors.org
Prompt: Create a tutorial for developers interested in contributing to the Starknet ecosystem, including examples of how to use Starknet libraries or APIs.
Generated: DETERMINISTIC_95f41565c591b327
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# starknet_tutorial.py
"""
This script is a tutorial for developers interested in contributing to the Starknet ecosystem.
It demonstrates how to interact with Starknet using Python and the `starknet_py` library.
Ensure you have Python 3.8+ and install the required dependencies:
    pip install starknet.py
"""

import asyncio
from starknet_py.net import AccountClient, GatewayClient
from starknet_py.net.models import StarknetChainId
from starknet_py.net.networks import TESTNET
from starknet_py.contract import Contract
from starknet_py.net.signer.stark_curve_signer import KeyPair

# Constants
PRIVATE_KEY = "YOUR_PRIVATE_KEY_HERE"  # Replace with your private key
PUBLIC_KEY = "YOUR_PUBLIC_KEY_HERE"    # Replace with your public key
DEFAULT_ACCOUNT_ADDRESS = "0xYOUR_ACCOUNT_CONTRACT_ADDRESS"  # Replace appropriately
CONTRACT_ADDRESS = "0xYOUR_DEPLOYED_CONTRACT_ADDRESS"        # Replace with a deployed contract address


async def main():
    """
    Main tutorial demonstrating how to:
    1. Set up an account client to interact with Starknet.
    2. Call a function on a deployed contract.
    3. Invoke a function to update contract state.
    """

    try:
        # STEP 1: Initialize AccountClient
        # GatewayClient connects to the Starknet testnet
        gateway_client = GatewayClient(net=TESTNET)

        # KeyPair allows signing transactions
        key_pair = KeyPair(private_key=int(PRIVATE_KEY, 16), public_key=int(PUBLIC_KEY, 16))

        # AccountClient handles account-specific transactions (e.g., invoking contracts)
        account_client = AccountClient(
            client=gateway_client,
            address=DEFAULT_ACCOUNT_ADDRESS,
            key_pair=key_pair,
            chain=StarknetChainId.TESTNET
        )

        print("AccountClient successfully initialized.")

        # STEP 2: Interact with a deployed contract
        # Load the contract using its address
        contract = await Contract.from_address(CONTRACT_ADDRESS, account_client)

        # Call a read-only method (e.g., get_balance)
        # Assuming the contract has a function `get_balance()`
        balance = await contract.functions["get_balance"].call()
        print(f"Current balance: {balance}")

        # STEP 3: Invoke a state-changing function
        # Assuming the contract has a function `increase_balance(uint256 amount)`
        amount_to_add = 100
        invocation = await contract.functions["increase_balance"].invoke(amount=amount_to_add)

        # Wait for transaction completion
        await invocation.wait_for_acceptance()
        print(f"Successfully increased balance by {amount_to_add}.")

    except Exception as e:
        # Proper error handling for debugging
        print(f"An error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    # Run the main function asynchronously
    asyncio.run(main())
```

### Notes:
- Replace placeholder values such as `YOUR_PRIVATE_KEY_HERE`, `YOUR_PUBLIC_KEY_HERE`, and contract addresses with actual values.
- Install the `starknet.py` library before running the script: `pip install starknet.py`.
- This script uses the Starknet Testnet (`TESTNET`) for safe experimentation.
- Ensure that your account and contract are properly configured on the Starknet Testnet.
