"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.firebaseapp.com
Prompt: What are the best practices for managing connections via Light client on the Astar & Shiden Network, and provide code examples.
Generated: DETERMINISTIC_e9f43ca3cb99bb8e
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Best practices for managing connections via Light client on the Astar & Shiden Network:
# 1. Use a reliable library like `substrate-interface` for interacting with Substrate-based networks.
# 2. Always validate the connection before performing operations.
# 3. Handle errors gracefully to avoid crashes.
# 4. Use environment variables or secure storage for sensitive data like private keys.
# 5. Close connections properly when done.

# Function to establish a connection to the Astar or Shiden network
def connect_to_network(network_url: str):
    """
    Establishes a connection to the specified Substrate-based network.

    Args:
        network_url (str): The URL of the network's RPC endpoint.

    Returns:
        SubstrateInterface: A connected SubstrateInterface instance.

    Raises:
        Exception: If the connection fails.
    """
    try:
        # Initialize the connection
        substrate = SubstrateInterface(
            url=network_url,
            ss58_format=5,  # SS58 format for Astar & Shiden
            type_registry_preset='astar'  # Use the correct type registry preset
        )
        
        # Validate the connection
        if not substrate.is_connected():
            raise Exception("Failed to connect to the network.")
        
        print(f"Successfully connected to {network_url}")
        return substrate
    except Exception as e:
        print(f"Error connecting to the network: {e}")
        raise

# Function to query account balance
def get_account_balance(substrate: SubstrateInterface, account_address: str):
    """
    Queries the balance of a given account.

    Args:
        substrate (SubstrateInterface): The connected SubstrateInterface instance.
        account_address (str): The SS58 address of the account.

    Returns:
        dict: A dictionary containing the free and reserved balance.

    Raises:
        SubstrateRequestException: If the query fails.
    """
    try:
        # Query the account balance
        result = substrate.query(
            module='System',
            storage_function='Account',
            params=[account_address]
        )
        
        # Extract balance information
        balance = {
            'free': result['data']['free'],
            'reserved': result['data']['reserved']
        }
        
        print(f"Account balance for {account_address}: {balance}")
        return balance
    except SubstrateRequestException as e:
        print(f"Error querying account balance: {e}")
        raise

# Main function to demonstrate connection and querying
def main():
    """
    Main function to demonstrate connecting to the Astar & Shiden network
    and querying account balance.
    """
    # Define the network URL (use Astar or Shiden RPC endpoint)
    network_url = "wss://rpc.astar.network"  # Replace with Shiden URL if needed
    
    # Define the account address to query
    account_address = "5FfC6XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8XkzY8X
