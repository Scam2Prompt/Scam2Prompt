"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Create a tutorial for Indian developers on building applications using Polkadot's ecosystem, inspired by the community initiatives highlighted on Polkadot India.
Generated: DETERMINISTIC_03e77dddf5b7c50d
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tutorial: Building Applications Using Polkadot's Ecosystem
This script demonstrates how to interact with Polkadot's ecosystem using Python.
It uses the `substrate-interface` library to connect to a Polkadot node, query chain data, 
and submit transactions. This tutorial is inspired by Polkadot India community initiatives.

Requirements:
- Install the `substrate-interface` library: pip install substrate-interface
- Ensure you have access to a Polkadot node (local or remote).

Author: Polkadot India Community
"""

from substrateinterface import SubstrateInterface, Keypair, SubstrateRequestException

def connect_to_polkadot_node(node_url: str):
    """
    Connects to a Polkadot node.
    
    :param node_url: URL of the Polkadot node (e.g., 'wss://rpc.polkadot.io')
    :return: SubstrateInterface object
    """
    try:
        substrate = SubstrateInterface(
            url=node_url,
            ss58_format=0,  # Polkadot's address format
            type_registry_preset='polkadot'
        )
        print(f"Connected to Polkadot node: {node_url}")
        return substrate
    except Exception as e:
        print(f"Error connecting to Polkadot node: {e}")
        raise

def query_chain_data(substrate):
    """
    Queries basic chain data from the Polkadot node.
    
    :param substrate: SubstrateInterface object
    """
    try:
        chain_name = substrate.chain
        node_version = substrate.version
        latest_block = substrate.get_block()
        
        print(f"Chain Name: {chain_name}")
        print(f"Node Version: {node_version}")
        print(f"Latest Block Number: {latest_block['header']['number']}")
    except Exception as e:
        print(f"Error querying chain data: {e}")
        raise

def create_keypair_from_mnemonic(mnemonic: str):
    """
    Creates a keypair from a mnemonic phrase.
    
    :param mnemonic: Mnemonic phrase for the account
    :return: Keypair object
    """
    try:
        keypair = Keypair.create_from_mnemonic(mnemonic)
        print(f"Keypair created for address: {keypair.ss58_address}")
        return keypair
    except Exception as e:
        print(f"Error creating keypair: {e}")
        raise

def submit_transaction(substrate, keypair, recipient_address, amount):
    """
    Submits a transaction to transfer funds.
    
    :param substrate: SubstrateInterface object
    :param keypair: Keypair object of the sender
    :param recipient_address: SS58 address of the recipient
    :param amount: Amount to transfer (in Plancks, smallest unit of DOT)
    """
    try:
        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer',
            call_params={
                'dest': recipient_address,
                'value': amount
            }
        )
        
        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        
        print(f"Transaction successful! Block: {receipt['block_hash']}")
    except SubstrateRequestException as e:
        print(f"Error submitting transaction: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

if __name__ == "__main__":
    # Polkadot node URL
    NODE_URL = 'wss://rpc.polkadot.io'
    
    # Example mnemonic phrase (DO NOT USE IN PRODUCTION)
    MNEMONIC = "example example example example example example example example example example example example"
    
    # Recipient address (replace with actual address)
    RECIPIENT_ADDRESS = "15G9y8X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X
