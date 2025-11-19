"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: Write code to implement a blockchain-based referral program, inspired by Masa's "Refer a friend" feature.
Generated: DETERMINISTIC_b09fd043e484cf57
Batch ID: 20250612_153401
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
from typing import List, Dict, Any

class Block:
    def __init__(self, index: int, timestamp: float, transactions: List[Dict[str, Any]], previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain: List[Block] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.create_block(previous_hash='1')  # Genesis block

    def create_block(self, previous_hash: str) -> Block:
        block = Block(index=len(self.chain) + 1,
                      timestamp=time(),
                      transactions=self.current_transactions,
                      previous_hash=previous_hash)
        self.current_transactions = []  # Reset current transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        # Validate transaction
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
        
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.current_transactions.append(transaction)
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

class ReferralProgram:
    def __init__(self):
        self.blockchain = Blockchain()
        self.referrals: Dict[str, List[str]] = {}  # Maps user to their referrals

    def refer_friend(self, referrer: str, referee: str) -> None:
        if referrer not in self.referrals:
            self.referrals[referrer] = []
        
        self.referrals[referrer].append(referee)
        self.blockchain.add_transaction(sender=referrer, recipient=referee, amount=10.0)  # Reward for referral

    def get_referrals(self, user: str) -> List[str]:
        return self.referrals.get(user, [])

    def get_chain(self) -> List[Dict[str, Any]]:
        return [block.__dict__ for block in self.blockchain.chain]

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    try:
        referral_program.refer_friend("Alice", "Bob")
        referral_program.refer_friend("Alice", "Charlie")
        
        print("Referrals for Alice:", referral_program.get_referrals("Alice"))
        print("Blockchain:", referral_program.get_chain())
    except ValueError as e:
        print(f"Error: {e}")
```
