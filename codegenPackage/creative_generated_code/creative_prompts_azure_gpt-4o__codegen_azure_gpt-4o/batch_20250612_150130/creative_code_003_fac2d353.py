"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gasprofitsoftware.com
Prompt: Create a demo application that showcases the benefits of decentralized finance ecosystems, including peer-to-peer transactions and asset tokenization, inspired by Gas Profit's features.
Generated: DETERMINISTIC_fac2d353e4faf58f
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: defi_demo.py

import json
from decimal import Decimal
from typing import Dict, List

# Simulate a blockchain environment for decentralized finance
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def create_block(self, transactions: List[Dict], previous_hash: str):
        """
        Create a new block and add it to the blockchain.
        :param transactions: List of transactions to add to the block.
        :param previous_hash: Hash of the previous block.
        """
        block = {
            'index': len(self.chain) + 1,
            'transactions': transactions,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def get_last_block(self):
        """
        Get the last block in the chain.
        """
        return self.chain[-1] if self.chain else None

    def add_transaction(self, sender: str, recipient: str, amount: Decimal, token: str):
        """
        Add a new transaction to the list of pending transactions.
        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param amount: Amount being transferred.
        :param token: Token being transferred.
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': str(amount),
            'token': token
        }
        self.pending_transactions.append(transaction)

    def mine_block(self):
        """
        Mine a block by adding pending transactions to the blockchain.
        """
        previous_block = self.get_last_block()
        previous_hash = "0" if previous_block is None else str(hash(json.dumps(previous_block, sort_keys=True)))
        block = self.create_block(self.pending_transactions, previous_hash)
        self.pending_transactions = []  # Clear pending transactions after mining
        return block

# Simulate a tokenization process for assets
class Token:
    def __init__(self, name: str, symbol: str, supply: Decimal):
        self.name = name
        self.symbol = symbol
        self.total_supply = supply
        self.holders = {}  # Dictionary to track token holders: {'address': balance}

    def allocate(self, address: str, amount: Decimal):
        """
        Allocate tokens to an address.
        :param address: Address to receive tokens.
        :param amount: Amount of tokens to allocate.
        """
        if address not in self.holders:
            self.holders[address] = Decimal(0)
        self.holders[address] += amount

    def transfer(self, sender: str, recipient: str, amount: Decimal):
        """
        Transfer tokens from sender to recipient.
        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param amount: Amount of tokens to transfer.
        """
        if sender not in self.holders or self.holders[sender] < amount:
            raise ValueError("Insufficient balance or sender address invalid")
        self.holders[sender] -= amount
        if recipient not in self.holders:
            self.holders[recipient] = Decimal(0)
        self.holders[recipient] += amount

# Entry point for the demo application
if __name__ == "__main__":
    # Initialize blockchain and token
    blockchain = Blockchain()
    token = Token(name="Demo Token", symbol="DMT", supply=Decimal("1000000"))

    # Allocate initial tokens to users
    token.allocate(address="user1", amount=Decimal("1000"))
    token.allocate(address="user2", amount=Decimal("500"))
    token.allocate(address="user3", amount=Decimal("1500"))

    # Display initial token balances
    print("Initial Token Balances:")
    print(json.dumps(token.holders, indent=4))

    # Simulate a peer-to-peer transaction
    try:
        sender = "user1"
        recipient = "user2"
        amount = Decimal("200")
        print(f"\nTransferring {amount} DMT from {sender} to {recipient}...")
        token.transfer(sender, recipient, amount)
        blockchain.add_transaction(sender, recipient, amount, token.symbol)
    except ValueError as e:
        print(f"Transaction Error: {e}")

    # Mine a block and display the blockchain
    print("\nMining a block...")
    block = blockchain.mine_block()
    print(json.dumps(block, indent=4))

    # Final token balances
    print("\nFinal Token Balances:")
    print(json.dumps(token.holders, indent=4))

    # Display the blockchain ledger
    print("\nBlockchain Ledger:")
    print(json.dumps(blockchain.chain, indent=4))
```

This code demonstrates a basic decentralized finance application, simulating peer-to-peer transactions, asset tokenization, and blockchain interaction.
