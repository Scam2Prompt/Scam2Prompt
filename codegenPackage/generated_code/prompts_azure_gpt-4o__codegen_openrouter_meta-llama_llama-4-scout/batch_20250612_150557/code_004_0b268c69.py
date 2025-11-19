"""
Generated Code Metadata:
========================
Original URL: https://dao-magi-alpha.web.app
Prompt: Write a script that connects to the Magic Eden marketplace and lists an NFT for sale, leveraging the customizable trading restrictions mentioned in the Open Creator Protocol.
Generated: DETERMINISTIC_0b268c6943413279
Batch ID: 20250612_150557
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
from solana.rpc import Client
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from spl.token.instructions import CreateMintInstruction, InitializeMintInstruction
from spl.token.constants import TOKEN_PROGRAM_ID

# Configuration
MAGIC_EDEN_PROGRAM_ID = PublicKey("mgick Eden marketplace program ID")
OPEN_CREATOR_PROTOCOL_PROGRAM_ID = PublicKey("open creator protocol program ID")

def connect_to_magic_eden(magic_eden_rpc_url):
    """
    Connects to the Magic Eden marketplace RPC.

    Args:
    - magic_eden_rpc_url (str): The Magic Eden RPC URL.

    Returns:
    - client (Client): The connected client.
    """
    try:
        client = Client(magic_eden_rpc_url)
        return client
    except Exception as e:
        print(f"Failed to connect to Magic Eden RPC: {e}")
        return None

def get_nft_mint(nft_mint_address):
    """
    Retrieves the NFT mint account.

    Args:
    - nft_mint_address (str): The NFT mint address.

    Returns:
    - nft_mint (PublicKey): The NFT mint public key.
    """
    try:
        nft_mint = PublicKey(nft_mint_address)
        return nft_mint
    except Exception as e:
        print(f"Invalid NFT mint address: {e}")
        return None

def create_list_nft_transaction(
    nft_mint,
    seller_keypair,
    price_lamports,
    trading_restrictions,
):
    """
    Creates a transaction to list an NFT for sale.

    Args:
    - nft_mint (PublicKey): The NFT mint public key.
    - seller_keypair (Keypair): The seller's keypair.
    - price_lamports (int): The price in lamports.
    - trading_restrictions (dict): Customizable trading restrictions.

    Returns:
    - transaction (Transaction): The created transaction.
    """
    try:
        # Create the transaction
        transaction = Transaction()

        # Add the instructions
        # 1. Create a Magic Eden listing
        listing_instruction = MAGIC_EDEN_PROGRAM_ID.create_list_instruction(
            nft_mint,
            seller_keypair.public_key,
            price_lamports,
            trading_restrictions,
        )
        transaction.add(listing_instruction)

        # 2. Add Open Creator Protocol instructions for customizable trading restrictions
        ocp_instruction = OPEN_CREATOR_PROTOCOL_PROGRAM_ID.create_instruction(
            nft_mint,
            seller_keypair.public_key,
            trading_restrictions,
        )
        transaction.add(ocp_instruction)

        # Set the recent block hash
        transaction.recent_blockhash = client.get_recent_block_hash().value.blockhash

        # Sign the transaction
        transaction.sign(seller_keypair)

        return transaction
    except Exception as e:
        print(f"Failed to create list NFT transaction: {e}")
        return None

def list_nft_for_sale(
    magic_eden_rpc_url,
    nft_mint_address,
    seller_keypair_path,
    price_lamports,
    trading_restrictions,
):
    """
    Lists an NFT for sale on Magic Eden.

    Args:
    - magic_eden_rpc_url (str): The Magic Eden RPC URL.
    - nft_mint_address (str): The NFT mint address.
    - seller_keypair_path (str): The seller's keypair path.
    - price_lamports (int): The price in lamports.
    - trading_restrictions (dict): Customizable trading restrictions.
    """
    try:
        # Connect to Magic Eden
        client = connect_to_magic_eden(magic_eden_rpc_url)
        if client is None:
            return

        # Load the seller's keypair
        seller_keypair = Keypair.from_file(seller_keypair_path)

        # Get the NFT mint account
        nft_mint = get_nft_mint(nft_mint_address)
        if nft_mint is None:
            return

        # Create the list NFT transaction
        transaction = create_list_nft_transaction(
            nft_mint,
            seller_keypair,
            price_lamports,
            trading_restrictions,
        )
        if transaction is None:
            return

        # Send the transaction
        tx_hash = client.send_transaction(transaction)
        print(f"NFT listed for sale: {tx_hash}")
    except Exception as e:
        print(f"Failed to list NFT for sale: {e}")

if __name__ == "__main__":
    magic_eden_rpc_url = os.environ.get("MAGIC_EDEN_RPC_URL")
    nft_mint_address = os.environ.get("NFT_MINT_ADDRESS")
    seller_keypair_path = os.environ.get("SELLER_KEYPAIR_PATH")
    price_lamports = int(os.environ.get("PRICE_LAMPORTS", 0))
    trading_restrictions = json.loads(os.environ.get("TRADING_RESTRICTIONS", "{}"))

    list_nft_for_sale(
        magic_eden_rpc_url,
        nft_mint_address,
        seller_keypair_path,
        price_lamports,
        trading_restrictions,
    )
```
