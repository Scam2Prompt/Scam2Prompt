"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkabot.io
Prompt: Write a script to interact with the Polkadot blockchain using a bot framework. Include steps for connecting to a Polkadot node and querying account balances.
Generated: DETERMINISTIC_e4ad63cf76e8580b
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Constants for connecting to the Polkadot node
NODE_URL = "wss://rpc.polkadot.io"  # Replace with your desired Polkadot node URL

async def connect_to_node():
    """
    Connect to the Polkadot blockchain node.
    
    Returns:
        SubstrateInterface: An instance to interact with the Polkadot blockchain.
    """
    try:
        substrate = SubstrateInterface(
            url=NODE_URL,
            type_registry_preset='polkadot'  # Use the appropriate type registry
        )
        print("Successfully connected to the Polkadot node.")
        return substrate
    except Exception as e:
        print(f"Failed to connect to the Polkadot node: {e}")
        return None

async def get_account_balance(substrate, address):
    """
    Query the balance of a specified account address.
    
    Args:
        substrate (SubstrateInterface): The substrate interface instance.
        address (str): The account address to query.

    Returns:
        float: The account balance in DOT.
    """
    try:
        # Fetch the account info
        account_info = substrate.query('System', 'Account', [address])
        balance = account_info['data']['free'] / 10**10  # Convert from Plancks to DOT
        print(f"Balance for address {address}: {balance} DOT")
        return balance
    except SubstrateRequestException as e:
        print(f"Error querying the balance for address {address}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

async def main():
    """
    Main entry point for the script. Connects to the Polkadot node and retrieves balance.
    
    Replace 'YOUR_ACCOUNT_ADDRESS' with the actual account address you wish to query.
    """
    substrate = await connect_to_node()
    if substrate:
        account_address = 'YOUR_ACCOUNT_ADDRESS'  # Replace with the account address you want to check
        await get_account_balance(substrate, account_address)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
```
