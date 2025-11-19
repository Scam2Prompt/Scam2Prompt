"""
Generated Code Metadata:
========================
Original URL: https://mansorytoken.xyz
Prompt: Write a Python code snippet to create a simple blockchain-based system for tracking luxury car ownership, incorporating a token similar to Mansory Token (MN$RY).
Generated: DETERMINISTIC_bb53ed8f66535661
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from time import time
from typing import List, Dict, Any, Optional
from uuid import uuid4

class Blockchain:
    """
    A simple blockchain implementation for tracking luxury car ownership with MN$RY tokens.
    """
    
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.token_balances: Dict[str, float] = {}
        self.car_ownership: Dict[str, str] = {}  # car_id: owner_address
        self.nodes = set()
        
        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof: int, previous_hash: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new Block in the Blockchain
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

    def new_transaction(self, sender: str, recipient: str, amount: float, car_id: Optional[str] = None) -> int:
        """
        Creates a new transaction to go into the next mined Block
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'car_id': car_id,
        }
        
        self.current_transactions.append(transaction)
        
        # Update token balances immediately (simplification for demo)
        if sender != "0":  # Not a mining reward
            if sender not in self.token_balances or self.token_balances[sender] < amount:
                raise ValueError("Insufficient balance")
            self.token_balances[sender] -= amount
        
        if recipient not in self.token_balances:
            self.token_balances[recipient] = 0
        self.token_balances[recipient] += amount
        
        # Update car ownership if this is a car transfer
        if car_id:
            if car_id in self.car_ownership and self.car_ownership[car_id] != sender:
                raise ValueError("Sender does not own this car")
            self.car_ownership[car_id] = recipient
        
        return self.last_block['index'] + 1

    @property
    def last_block(self) -> Dict[str, Any]:
        return self.chain[-1]

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """
        Creates a SHA-256 hash of a Block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - p is the previous proof, p' is the new proof
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the Proof
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def register_node(self, address: str) -> None:
        """
        Add a new node to the list of nodes
        """
        self.nodes.add(address)

    def mine(self, miner_address: str) -> Dict[str, Any]:
        """
        Mine a new block and reward the miner with MN$RY tokens
        """
        # Reward the miner with 1 MN$RY token
        self.new_transaction(
            sender="0",
            recipient=miner_address,
            amount=1.0,
        )

        last_block = self.last_block
        last_proof = last_block['proof']
        proof = self.proof_of_work(last_proof)

        previous_hash = self.hash(last_block)
        block = self.new_block(proof, previous_hash)

        return block

    def get_balance(self, address: str) -> float:
        """
        Get the MN$RY token balance for an address
        """
        return self.token_balances.get(address, 0.0)

    def get_car_owner(self, car_id: str) -> Optional[str]:
        """
        Get the current owner of a car
        """
        return self.car_ownership.get(car_id)

    def register_car(self, car_id: str, owner_address: str) -> None:
        """
        Register a new car with initial owner
        """
        if car_id in self.car_ownership:
            raise ValueError("Car already registered")
        self.car_ownership[car_id] = owner_address

    def validate_chain(self, chain: List[Dict[str, Any]]) -> bool:
        """
        Determine if a given blockchain is valid
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

def generate_address() -> str:
    """
    Generate a new wallet address
    """
    return str(uuid4()).replace('-', '')

# Example usage
if __name__ == '__main__':
    blockchain = Blockchain()
    
    # Create some addresses
    alice = generate_address()
    bob = generate_address()
    dealer = generate_address()
    
    # Register a luxury car
    lambo_id = "LAMB12345"
    blockchain.register_car(lambo_id, dealer)
    
    # Dealer mines some tokens
    blockchain.mine(dealer)
    blockchain.mine(dealer)
    
    # Alice buys the car from dealer for 10 MN$RY
    blockchain.new_transaction(
        sender=alice,
        recipient=dealer,
        amount=10.0,
        car_id=lambo_id
    )
    
    # Print some info
    print(f"Alice balance: {blockchain.get_balance(alice)} MN$RY")
    print(f"Bob balance: {blockchain.get_balance(bob)} MN$RY")
    print(f"Dealer balance: {blockchain.get_balance(dealer)} MN$RY")
    print(f"Owner of {lambo_id}: {blockchain.get_car_owner(lambo_id)}")
    
    # Print the blockchain
    print("\nBlockchain:")
    for block in blockchain.chain:
        print(block)
```
