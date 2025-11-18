"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koi-finance.pages.dev
Prompt: Create a function to lock KOI tokens into a vote-escrow NFT for DAO governance participation, including calculating vote shares based on lock duration.
Generated: DETERMINISTIC_96b9c1520889b144
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import math

class VoteEscrowNFT:
    def __init__(self, token_id, owner, lock_amount, lock_end):
        """
        Initializes a Vote Escrow NFT object.
        :param token_id: Unique identifier for the NFT.
        :param owner: Owner of the NFT.
        :param lock_amount: Amount of KOI tokens locked.
        :param lock_end: Timestamp when the lock period ends.
        """
        self.token_id = token_id
        self.owner = owner
        self.lock_amount = lock_amount
        self.lock_end = lock_end

class GovernanceSystem:
    def __init__(self):
        """
        Initializes the governance system.
        """
        self.nfts = {}
        self.token_id_counter = 1  # Unique token ID generator

    def lock_tokens(self, owner, lock_amount, lock_duration_days):
        """
        Locks KOI tokens into a vote-escrow NFT for DAO governance participation.
        :param owner: Address of the user locking tokens.
        :param lock_amount: Amount of KOI tokens to lock.
        :param lock_duration_days: Duration for the token lock in days.
        :return: The created Vote Escrow NFT object.
        """
        if lock_amount <= 0:
            raise ValueError("Lock amount must be greater than zero.")
        if lock_duration_days <= 0:
            raise ValueError("Lock duration must be greater than zero.")
        
        # Calculate the lock end date
        lock_end = datetime.now() + timedelta(days=lock_duration_days)
        
        # Generate the NFT object
        nft = VoteEscrowNFT(
            token_id=self.token_id_counter,
            owner=owner,
            lock_amount=lock_amount,
            lock_end=lock_end
        )
        
        # Store the NFT in the governance system
        self.nfts[self.token_id_counter] = nft
        
        # Increment token ID counter for future NFTs
        self.token_id_counter += 1
        
        return nft

    def calculate_vote_shares(self, token_id):
        """
        Calculates the vote shares based on the lock duration and lock amount.
        :param token_id: The ID of the NFT for which to calculate vote shares.
        :return: Calculated vote share as a numeric value.
        """
        if token_id not in self.nfts:
            raise ValueError("Invalid NFT token ID.")
        
        nft = self.nfts[token_id]
        current_time = datetime.now()
        
        # Ensure lock period is still active
        if current_time > nft.lock_end:
            raise ValueError("Lock period has expired.")
        
        # Calculate lock duration in days
        lock_duration_days = (nft.lock_end - current_time).days
        
        # Calculate vote shares
        vote_shares = nft.lock_amount * math.sqrt(lock_duration_days)
        
        return vote_shares

# Example usage:
# governance = GovernanceSystem()
# nft = governance.lock_tokens(owner="user1", lock_amount=1000, lock_duration_days=30)
# vote_shares = governance.calculate_vote_shares(nft.token_id)
# print(f"Vote shares: {vote_shares}")
```
