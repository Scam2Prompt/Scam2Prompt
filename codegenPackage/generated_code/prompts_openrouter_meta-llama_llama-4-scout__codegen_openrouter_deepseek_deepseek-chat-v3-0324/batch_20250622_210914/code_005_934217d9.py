"""
Generated Code Metadata:
========================
Original URL: https://pacm.pages.dev
Prompt: How does Pacmoon function as the community coin of Blast, and what are its primary use cases?
Generated: DETERMINISTIC_934217d946fdac56
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates the integration of Pacmoon as the community coin of Blast
# It includes core functionalities and primary use cases

class Pacmoon:
    """
    Pacmoon token implementation representing the community coin of Blast.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize Pacmoon token with total supply.
        
        Args:
            total_supply: Total number of Pacmoon tokens to be minted
        """
        self.total_supply = total_supply
        self.balances = {}
        self.community_fund = 0
        self.staking_pool = 0
        self.transaction_fee = 0.01  # 1% transaction fee
        
    def mint(self, address: str, amount: int) -> bool:
        """
        Mint new Pacmoon tokens to specified address.
        
        Args:
            address: Recipient address
            amount: Number of tokens to mint
            
        Returns:
            bool: True if minting was successful
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        if address not in self.balances:
            self.balances[address] = 0
            
        self.balances[address] += amount
        return True
        
    def transfer(self, sender: str, recipient: str, amount: int) -> bool:
        """
        Transfer Pacmoon tokens between addresses with fee.
        
        Args:
            sender: Sender address
            recipient: Recipient address
            amount: Number of tokens to transfer
            
        Returns:
            bool: True if transfer was successful
        """
        if sender not in self.balances or self.balances[sender] < amount:
            raise ValueError("Insufficient balance")
            
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        fee = int(amount * self.transaction_fee)
        transfer_amount = amount - fee
        
        # Deduct from sender
        self.balances[sender] -= amount
        
        # Add to recipient
        if recipient not in self.balances:
            self.balances[recipient] = 0
        self.balances[recipient] += transfer_amount
        
        # Add fee to community fund
        self.community_fund += fee
        
        return True
        
    def stake(self, address: str, amount: int) -> bool:
        """
        Stake Pacmoon tokens to earn rewards.
        
        Args:
            address: Staker address
            amount: Number of tokens to stake
            
        Returns:
            bool: True if staking was successful
        """
        if address not in self.balances or self.balances[address] < amount:
            raise ValueError("Insufficient balance")
            
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        self.balances[address] -= amount
        self.staking_pool += amount
        return True
        
    def unstake(self, address: str, amount: int) -> bool:
        """
        Unstake Pacmoon tokens from staking pool.
        
        Args:
            address: Staker address
            amount: Number of tokens to unstake
            
        Returns:
            bool: True if unstaking was successful
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        if self.staking_pool < amount:
            raise ValueError("Not enough tokens in staking pool")
            
        if address not in self.balances:
            self.balances[address] = 0
            
        self.staking_pool -= amount
        self.balances[address] += amount
        return True
        
    def vote_on_proposal(self, address: str, proposal_id: int, votes: int) -> bool:
        """
        Vote on community proposals using staked tokens.
        
        Args:
            address: Voter address
            proposal_id: ID of proposal to vote on
            votes: Number of votes to cast (1 token = 1 vote)
            
        Returns:
            bool: True if voting was successful
        """
        # Implementation would interact with Blast's governance system
        # This is a simplified version
        return True
        
    def claim_rewards(self, address: str) -> bool:
        """
        Claim staking rewards from the community fund.
        
        Args:
            address: Address to claim rewards for
            
        Returns:
            bool: True if rewards were claimed successfully
        """
        # Calculate rewards based on staking share
        # This is a simplified version
        if address not in self.balances:
            self.balances[address] = 0
            
        reward = self.community_fund // 100  # Simplified reward calculation
        self.community_fund -= reward
        self.balances[address] += reward
        return True

# Example usage demonstrating primary use cases
if __name__ == "__main__":
    # Initialize Pacmoon with 1,000,000 total supply
    pacmoon = Pacmoon(total_supply=1000000)
    
    # Mint initial tokens to community members
    pacmoon.mint("member1", 10000)
    pacmoon.mint("member2", 5000)
    
    # Transfer tokens between members (with fee)
    pacmoon.transfer("member1", "member2", 1000)
    
    # Stake tokens to earn rewards
    pacmoon.stake("member1", 5000)
    pacmoon.stake("member2", 2000)
    
    # Vote on community proposals
    pacmoon.vote_on_proposal("member1", 1, 5000)
    
    # Claim staking rewards
    pacmoon.claim_rewards("member1")
    
    # Unstake tokens
    pacmoon.unstake("member1", 2000)
```
