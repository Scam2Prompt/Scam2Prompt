"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-mdex.paypalreferralcode.com
Prompt: Provide an example of how to implement PayPal referral tracking in a blockchain-based application.
Generated: DETERMINISTIC_e966d38711f3fb00
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import time
from typing import Dict, List

# Blockchain-related classes and functions
class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index: int, timestamp: str, data: Dict, previous_hash: str):
        self.index = index  # Block index
        self.timestamp = timestamp  # Timestamp of block creation
        self.data = data  # Data contained in the block (e.g., referral transactions)
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calculate_hash()  # Hash of the current block

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using SHA-256.
        """
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain structure.
    """
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]  # Initialize blockchain with the genesis block

    def create_genesis_block(self) -> Block:
        """
        Creates the initial block in the blockchain.
        """
        return Block(0, time.strftime('%Y-%m-%d %H:%M:%S'), {"message": "Genesis Block"}, "0")

    def get_last_block(self) -> Block:
        """
        Retrieves the latest block on the chain.
        """
        return self.chain[-1]

    def add_block(self, data: Dict) -> None:
        """
        Adds a new block to the blockchain.
        """
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
            data=data,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Checks the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate current block hash
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate previous block hash reference
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Referral tracking system
class ReferralTracker:
    """
    Handles referral tracking and integrates it with the blockchain.
    """
    def __init__(self):
        self.blockchain = Blockchain()  # Blockchain instance
        self.referral_data: Dict[str, List[str]] = {}  # Maps referrer PayPal IDs to referred PayPal IDs

    def add_referral(self, referrer_id: str, referred_id: str) -> None:
        """
        Adds a referral to the system and records it on the blockchain.
        """
        # Error handling for invalid inputs
        if not referrer_id or not referred_id:
            raise ValueError("Referrer ID and Referred ID must be non-empty.")

        # Update referral data
        if referrer_id not in self.referral_data:
            self.referral_data[referrer_id] = []
        self.referral_data[referrer_id].append(referred_id)

        # Record the referral on the blockchain
        referral_record = {
            "referrer_id": referrer_id,
            "referred_id": referred_id,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        self.blockchain.add_block(referral_record)

    def get_referrals(self, referrer_id: str) -> List[str]:
        """
        Retrieves the list of referrals for a given referrer.
        """
        return self.referral_data.get(referrer_id, [])

    def validate_blockchain(self) -> bool:
        """
        Validates the integrity of the blockchain.
        """
        return self.blockchain.is_chain_valid()


# Example usage
if __name__ == "__main__":
    # Initialize the referral tracker
    tracker = ReferralTracker()

    # Add referrals
    try:
        tracker.add_referral("paypal_user_1", "paypal_user_2")
        tracker.add_referral("paypal_user_1", "paypal_user_3")
        tracker.add_referral("paypal_user_2", "paypal_user_4")
    except ValueError as e:
        print(f"Error adding referral: {e}")

    # Retrieve referrals
    print("Referrals for paypal_user_1:", tracker.get_referrals("paypal_user_1"))
    print("Referrals for paypal_user_2:", tracker.get_referrals("paypal_user_2"))

    # Validate blockchain integrity
    print("Is blockchain valid?", tracker.validate_blockchain())
```
