"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: How can I use the Polkadot Live desktop client to interact with Polkadot's blockchain features programmatically?
Generated: DETERMINISTIC_86f7521463764012
Batch ID: 20250612_162744
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

# Connect to the Polkadot node
def connect_to_node(node_url: str) -> SubstrateInterface:
    """
    Connects to the specified Polkadot node.

    :param node_url: The URL of the Polkadot node to connect to.
    :return: An instance of SubstrateInterface connected to the node.
    """
    try:
        substrate = SubstrateInterface(
            url=node_url,
            ss58_format=0,  # Default for Polkadot
            type_registry_preset='polkadot'  # Use the Polkadot type registry
        )
        print("Connected to Polkadot node:", node_url)
        return substrate
    except Exception as e:
        print("Error connecting to node:", e)
        raise


# Fetch the balance of an account
async def fetch_balance(substrate: SubstrateInterface, address: str) -> float:
    """
    Fetches the balance of a given account.

    :param substrate: The SubstrateInterface instance for interaction.
    :param address: The SS58 address of the account to check.
    :return: The balance of the account in DOT.
    """
    try:
        # Retrieve the account's balance
        balance = await substrate.query('System', 'Account', [address])
        return balance['data']['free'] / 10**10  # Convert from Plancks to DOT
    except Exception as e:
        print("Error fetching balance:", e)
        return None

# Main function to execute the program
async def main():
    # Define the Polkadot node URL
    node_url = "wss://rpc.polkadot.io"  # Public Polkadot node
    # Connect to the node
    substrate = connect_to_node(node_url)
    
    # Define the address to check
    address = "YOUR_ACCOUNT_ADDRESS_HERE"  # Replace with a valid SS58 address
    
    # Fetch and print the account balance
    balance = await fetch_balance(substrate, address)
    if balance is not None:
        print(f"Balance of {address}: {balance} DOT")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```
