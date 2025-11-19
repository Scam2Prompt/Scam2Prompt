"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smart-5wk.pages.dev
Prompt: How can I implement a dual-tier allocation system for an airdrop similar to the one described in the Smart Layer Airdrop documentation?
Generated: DETERMINISTIC_45e489143836b972
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class AirdropError(Exception):
    """Custom exception for handling airdrop errors."""
    pass

class Airdrop:
    def __init__(self, total_tokens: int):
        """
        Initialize the Airdrop with a total number of tokens.

        Args:
            total_tokens (int): Total tokens allocated for the airdrop.
        """
        if total_tokens <= 0:
            raise AirdropError("Total tokens must be greater than zero.")
        self.total_tokens = total_tokens
        self.participants = []
        self.tier_allocation: Dict[str, float] = {
            "Tier 1": 0.7,  # 70% for Tier 1
            "Tier 2": 0.3   # 30% for Tier 2
        }
        self.allocations: Dict[str, int] = {
            "Tier 1": 0,
            "Tier 2": 0
        }

    def add_participant(self, address: str, tier: str) -> None:
        """
        Add a participant to the airdrop.

        Args:
            address (str): The address of the participant.
            tier (str): The tier of the participant ('Tier 1' or 'Tier 2').
        
        Raises:
            AirdropError: If the tier is invalid or the address is already registered.
        """
        if tier not in self.tier_allocation:
            raise AirdropError("Invalid tier. Must be 'Tier 1' or 'Tier 2'.")
        if address in [p['address'] for p in self.participants]:
            raise AirdropError("Participant already registered.")
        
        self.participants.append({
            'address': address,
            'tier': tier
        })

    def allocate_tokens(self) -> Dict[str, Any]:
        """
        Allocate tokens to participants based on their tier.

        Returns:
            dict: Allocation results including total allocated tokens.
        
        Raises:
            AirdropError: If no participants are registered.
        """
        if not self.participants:
            raise AirdropError("No participants registered for the airdrop.")

        # Calculate total allocations based on the tiers
        tier_1_count = len([p for p in self.participants if p['tier'] == 'Tier 1'])
        tier_2_count = len([p for p in self.participants if p['tier'] == 'Tier 2'])

        if tier_1_count == 0 and tier_2_count == 0:
            raise AirdropError("No valid participants to allocate tokens.")

        # Allocate tokens to each tier
        tier_1_tokens = int(self.total_tokens * self.tier_allocation["Tier 1"]) if tier_1_count > 0 else 0
        tier_2_tokens = int(self.total_tokens * self.tier_allocation["Tier 2"]) if tier_2_count > 0 else 0
        
        # Distributing tokens randomly among participants in each tier
        for p in self.participants:
            if p['tier'] == 'Tier 1':
                allocated_tokens = random.randint(1, tier_1_tokens // tier_1_count) if tier_1_count > 0 else 0
                self.allocations["Tier 1"] += allocated_tokens
                tier_1_tokens -= allocated_tokens
            elif p['tier'] == 'Tier 2':
                allocated_tokens = random.randint(1, tier_2_tokens // tier_2_count) if tier_2_count > 0 else 0
                self.allocations["Tier 2"] += allocated_tokens
                tier_2_tokens -= allocated_tokens
        
        return {
            "total_allocated": self.allocations,
            "remaining_tokens": self.total_tokens - sum(self.allocations.values())
        }

# Example usage (uncomment to run):
# airdrop = Airdrop(total_tokens=1000)
# airdrop.add_participant(address='0xABC123', tier='Tier 1')
# airdrop.add_participant(address='0xDEF456', tier='Tier 2')
# results = airdrop.allocate_tokens()
# print(results)
```
