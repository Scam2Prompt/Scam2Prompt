"""
Generated Code Metadata:
========================
Original URL: https://jupiterdigitalasset.com
Prompt: How does Bitcoin function as a disintermediator of banks, and what implications does this have for financial transactions?
Generated: DETERMINISTIC_2dc566fff36ea39c
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simplified Bitcoin transaction system to illustrate
# how Bitcoin can disintermediate banks in financial transactions.

import hashlib
import json
from time import time
from typing import Dict, List, Optional, Tuple

class Blockchain:
    """
    A simple blockchain implementation to demonstrate Bitcoin's disintermediation.
    """
    
    def __init__(self):
        self.chain: List[Dict] = []
        self.current_transactions: List[Dict] = []
        self.nodes = set()  # Simplified network of nodes (no banks)
        
        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)
    
    def new_block(self, proof: int, previous_hash: Optional[str] = None) -> Dict:
        """
        Create a new block in the blockchain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        # Reset the current list of transactions
        self.current_transactions = []
        
        self.chain.append(block)
        return block
    
    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Create a new transaction to go into the next mined block.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block: Dict) -> str:
        """
        Create a SHA-256 hash of a block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    @property
    def last_block(self) -> Dict:
        """
        Returns the last block in the chain.
        """
        return self.chain[-1]
    
    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work algorithm for demonstration.
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
    
    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the Proof of Work.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

class BitcoinTransactionSystem:
    """
    Simulates how Bitcoin enables peer-to-peer transactions without banks.
    """
    
    def __init__(self):
        self.blockchain = Blockchain()
        self.wallets: Dict[str, float] = {}  # Simplified wallet balances
    
    def create_wallet(self, user_id: str, initial_balance: float = 0.0) -> None:
        """
        Create a new wallet with an initial balance.
        """
        if user_id in self.wallets:
            raise ValueError("Wallet already exists")
        self.wallets[user_id] = initial_balance
    
    def send_bitcoin(self, sender: str, recipient: str, amount: float) -> Tuple[bool, str]:
        """
        Send bitcoin from one wallet to another without bank intermediation.
        """
        if sender not in self.wallets:
            return False, "Sender wallet not found"
        if recipient not in self.wallets:
            return False, "Recipient wallet not found"
        if self.wallets[sender] < amount:
            return False, "Insufficient balance"
        
        # Create transaction (no bank involved)
        self.blockchain.new_transaction(sender, recipient, amount)
        
        # Mine a new block to confirm the transaction
        last_block = self.blockchain.last_block
        last_proof = last_block['proof']
        proof = self.blockchain.proof_of_work(last_proof)
        
        # Forge the new block by adding it to the chain
        previous_hash = self.blockchain.hash(last_block)
        self.blockchain.new_block(proof, previous_hash)
        
        # Update balances (simplified - in reality, balances are derived from blockchain)
        self.wallets[sender] -= amount
        self.wallets[recipient] += amount
        
        return True, "Transaction successful"

# Example usage demonstrating bank disintermediation
if __name__ == "__main__":
    # Initialize the system
    btc_system = BitcoinTransactionSystem()
    
    # Create user wallets (no bank accounts needed)
    btc_system.create_wallet("alice", 10.0)
    btc_system.create_wallet("bob", 5.0)
    
    # Alice sends Bob 3 BTC directly (no bank involved)
    success, message = btc_system.send_bitcoin("alice", "bob", 3.0)
    print(f"Transaction status: {success}, Message: {message}")
    
    # Check balances (derived from blockchain, not bank records)
    print(f"Alice's balance: {btc_system.wallets['alice']} BTC")
    print(f"Bob's balance: {btc_system.wallets['bob']} BTC")
    
    # Transaction is recorded on the blockchain (not in a bank's ledger)
    print("Blockchain record of transaction:")
    print(json.dumps(btc_system.blockchain.chain, indent=2))
```
