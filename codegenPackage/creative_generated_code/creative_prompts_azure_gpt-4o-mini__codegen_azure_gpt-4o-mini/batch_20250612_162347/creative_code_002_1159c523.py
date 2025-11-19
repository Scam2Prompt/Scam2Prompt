"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.network
Prompt: How can I use the Polkadot library to create a decentralized application that interacts with multiple blockchains?
Generated: DETERMINISTIC_1159c523973428cc
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from Polkadot
from substrateinterface import Keypair, SubstrateInterface, KeypairType

# Constants for blockchain nodes (you can replace these with actual endpoints)
POLKADOT_NODE = 'wss://rpc.polkadot.io'
KUSAMA_NODE = 'wss://rpc.kusama.network'

# Function to create a connection to a blockchain node
def connect_to_blockchain(node_url):
    """
    Connect to a Substrate-based blockchain node.

    :param node_url: The WebSocket URL of the blockchain node.
    :return: A SubstrateInterface instance connected to the specified node.
    """
    try:
        substrate = SubstrateInterface(url=node_url)
        print(f"Connected to {node_url}")
        return substrate
    except Exception as e:
        print(f"Error connecting to node {node_url}: {e}")
        return None

# Function to create a new keypair
def create_keypair():
    """
    Create a new keypair for account management.

    :return: A Keypair instance containing the public and private keys.
    """
    keypair = Keypair.create_from_mnemonic(KeypairType.SR25519)
    print(f"Generated new keypair: {keypair.ss58_address}")
    return keypair

# Function to send a transaction
def send_transaction(substrate, keypair, dest_address, amount):
    """
    Send a transaction from the keypair's account to a destination address.

    :param substrate: The SubstrateInterface instance for the blockchain.
    :param keypair: The Keypair instance used to sign the transaction.
    :param dest_address: The recipient's address.
    :param amount: The amount to send (in the smallest unit).
    """
    try:
        # Prepare the transaction call
        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer',
            call_params={
                'dest': dest_address,
                'value': amount
            }
        )
        
        # Create and send the extrinsic
        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Transaction sent! Hash: {receipt['extrinsic_hash']}")
    except Exception as e:
        print(f"Error sending transaction: {e}")

# Main function to demonstrate the usage of the above functions
def main():
    # Connect to Polkadot and Kusama nodes
    polkadot_substrate = connect_to_blockchain(POLKADOT_NODE)
    kusama_substrate = connect_to_blockchain(KUSAMA_NODE)

    # Create keypair for sending transactions
    keypair = create_keypair()

    # Example sending transaction (ensure the destination address and amount are valid)
    if polkadot_substrate:
        send_transaction(polkadot_substrate, keypair, '5FfJ…', 1000000000000)  # replace '5FfJ...' with a real address

    if kusama_substrate:
        send_transaction(kusama_substrate, keypair, 'D1uA…', 500000000000)  # replace 'D1uA...' with a real address

if __name__ == "__main__":
    main()
```

**Note**: Ensure you replace the placeholder addresses with actual valid addresses in the Polkadot and Kusama networks to test the transactions successfully. Additionally, install the required library using `pip install substrate-interface` if you haven't done so.
