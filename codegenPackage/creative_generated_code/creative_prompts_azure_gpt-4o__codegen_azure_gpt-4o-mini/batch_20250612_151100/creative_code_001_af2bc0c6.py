"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverser.pages.dev
Prompt: Create a Python script that uses Wormhole or Portal Bridge technology to transfer $DOGEVERSE tokens between Ethereum and Solana blockchains.
Generated: DETERMINISTIC_af2bc0c6756fa02f
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import asyncio
from eth_account import Account
from web3 import Web3
from solana.rpc.api import Client as SolanaClient
from wormhole import Wormhole, Portal

# Configuration constants
ETHEREUM_RPC_URL = os.getenv('ETHEREUM_RPC_URL')
SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL')
WORMHOLE_CONTRACT_ADDRESS = os.getenv('WORMHOLE_CONTRACT_ADDRESS')
DOGEVERSE_TOKEN_ADDRESS = os.getenv('DOGEVERSE_TOKEN_ADDRESS')

# Initialize Ethereum and Solana clients
eth_web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))
solana_client = SolanaClient(SOLANA_RPC_URL)

# Ensure Web3 is connected to Ethereum
if not eth_web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Transfer $DOGEVERSE tokens from Ethereum to Solana
async def transfer_tokens_eth_to_solana(sender_private_key, amount, recipient_solana_address):
    """
    Transfers DOGEVERSE tokens from Ethereum to Solana using Wormhole or Portal Bridge.
    
    :param sender_private_key: Private key of the Ethereum sender
    :param amount: Amount of DOGEVERSE tokens to transfer
    :param recipient_solana_address: Solana address of the recipient
    """
    try:
        # Create Ethereum account from private key
        sender_account = Account.from_key(sender_private_key)

        # Check balance of DOGEVERSE tokens
        token_contract = eth_web3.eth.contract(address=DOGEVERSE_TOKEN_ADDRESS, abi=ERC20_ABI)
        balance = token_contract.functions.balanceOf(sender_account.address).call()
        
        if balance < amount:
            raise ValueError("Insufficient DOGEVERSE balance.")

        # Approve the Wormhole contract to spend tokens
        token_contract.functions.approve(WORMHOLE_CONTRACT_ADDRESS, amount).transact({'from': sender_account.address})

        # Create a Wormhole message to initiate the transfer
        wormhole = Wormhole(eth_web3, WORMHOLE_CONTRACT_ADDRESS)
        transfer_tx = await wormhole.transfer(
            token_address=DOGEVERSE_TOKEN_ADDRESS,
            amount=amount,
            recipient=recipient_solana_address,
            sender=sender_account.address
        )

        # Await confirmation of the transaction
        receipt = await eth_web3.eth.waitForTransactionReceipt(transfer_tx)
        return receipt

    except Exception as e:
        print(f"Error during Ethereum to Solana transfer: {e}")
        raise

# Transfer $DOGEVERSE tokens from Solana to Ethereum
async def transfer_tokens_solana_to_eth(sender_solana_address, amount, recipient_eth_address):
    """
    Transfers DOGEVERSE tokens from Solana to Ethereum using Wormhole or Portal Bridge.
    
    :param sender_solana_address: Solana address of the sender
    :param amount: Amount of DOGEVERSE tokens to transfer
    :param recipient_eth_address: Ethereum address of the recipient
    """
    try:
        # Check balance of DOGEVERSE tokens on Solana
        solana_balance = solana_client.get_token_account_balance(sender_solana_address)

        if solana_balance['result']['value']['amount'] < amount:
            raise ValueError("Insufficient DOGEVERSE balance on Solana.")

        # Create a transfer instruction to Wormhole
        portal = Portal(solana_client)
        transfer_tx = await portal.transfer(
            token_address=DOGEVERSE_TOKEN_ADDRESS,
            amount=amount,
            recipient=recipient_eth_address,
            sender=sender_solana_address
        )

        # Await confirmation of the transaction
        return transfer_tx

    except Exception as e:
        print(f"Error during Solana to Ethereum transfer: {e}")
        raise

# Main function to execute transfers
async def main():
    # Example usage
    eth_private_key = os.getenv('ETH_PRIVATE_KEY')
    solana_sender_address = os.getenv('SOLANA_SENDER_ADDRESS')
    recipient_solana_address = os.getenv('RECIPIENT_SOLANA_ADDRESS')
    recipient_eth_address = os.getenv('RECIPIENT_ETH_ADDRESS')
    amount_to_transfer = 100  # Example amount

    # Transfer from Ethereum to Solana
    eth_receipt = await transfer_tokens_eth_to_solana(eth_private_key, amount_to_transfer, recipient_solana_address)
    print(f"Ethereum to Solana transfer receipt: {eth_receipt}")

    # Transfer from Solana to Ethereum
    solana_receipt = await transfer_tokens_solana_to_eth(solana_sender_address, amount_to_transfer, recipient_eth_address)
    print(f"Solana to Ethereum transfer receipt: {solana_receipt}")

# Execute main function
if __name__ == "__main__":
    asyncio.run(main())
```
