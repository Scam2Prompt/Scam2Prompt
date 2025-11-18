"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimgift-x24.web.app
Prompt: Provide code to calculate the maximum supply of DUST tokens (33,300,000) and simulate the distribution of the 100,000 DUST airdrop pool among active Solana community members.
Generated: DETERMINISTIC_ee3ab30bc0440524
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class DustTokenDistribution:
    def __init__(self, max_supply: int, airdrop_pool: int):
        """
        Initializes the DustTokenDistribution instance.

        :param max_supply: The maximum supply of DUST tokens.
        :param airdrop_pool: The total amount of DUST tokens to distribute as an airdrop.
        """
        self.max_supply = max_supply
        self.airdrop_pool = airdrop_pool
        self.active_members = []

    def add_active_member(self, member_id: str):
        """
        Adds an active member to the distribution list.

        :param member_id: Unique identifier for the member.
        """
        if member_id not in self.active_members:
            self.active_members.append(member_id)

    def distribute_airdrop(self):
        """
        Distributes the airdrop pool among active members randomly.

        :return: A dictionary mapping member IDs to received DUST amounts.
        :raises ValueError: If there are no active members to distribute to.
        """
        if not self.active_members:
            raise ValueError("No active members to distribute DUST tokens to.")

        # Shuffle the list of active members to ensure random distribution
        random.shuffle(self.active_members)

        # Distribute the airdrop pool among active members
        distribution = {}
        remaining_airdrop = self.airdrop_pool
        
        for member in self.active_members:
            # Calculate random amount for this member, ensuring it does not exceed the remaining pool
            amount = random.randint(1, remaining_airdrop // len(self.active_members))
            distribution[member] = amount
            remaining_airdrop -= amount
            
            # If the remaining airdrop is depleted, break the loop
            if remaining_airdrop <= 0:
                break
        
        return distribution

    def get_active_members(self):
        """
        Returns the list of active members.

        :return: List of active member IDs.
        """
        return self.active_members


if __name__ == "__main__":
    # Constants for DUST token distribution
    MAX_SUPPLY = 33300000
    AIRDROP_POOL = 100000

    # Create a distribution instance
    distribution = DustTokenDistribution(MAX_SUPPLY, AIRDROP_POOL)

    # Simulate adding active members
    for i in range(1, 101):  # Simulating 100 active members
        distribution.add_active_member(f'member_{i}')

    try:
        # Perform the airdrop distribution
        result = distribution.distribute_airdrop()
        print("Airdrop Distribution Result:")
        for member, amount in result.items():
            print(f"{member}: {amount} DUST")
    except ValueError as e:
        print(f"Error: {e}")
```

This code simulates the distribution of 100,000 DUST tokens among a set of active Solana community members, ensuring proper error handling and documentation as requested.
