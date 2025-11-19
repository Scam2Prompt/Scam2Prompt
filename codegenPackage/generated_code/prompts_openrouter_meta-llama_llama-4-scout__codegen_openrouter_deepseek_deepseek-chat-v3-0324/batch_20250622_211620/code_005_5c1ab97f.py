"""
Generated Code Metadata:
========================
Original URL: https://jpegsfun.pages.dev
Prompt: What are the advantages of using jpegs.fun's fair launch process for NFT creators, and how does it differ from traditional presale models?
Generated: DETERMINISTIC_5c1ab97fab648fd8
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simplified simulation of jpegs.fun's fair launch process
# compared to traditional NFT presale models. It highlights key advantages like:
# - Equal opportunity for all participants
# - No preferential treatment for whales
# - Transparent and verifiable randomness
# - Reduced gas wars

import random
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Participant:
    wallet_address: str
    amount_committed: float  # In ETH
    is_whale: bool = False

class FairLaunch:
    def __init__(self, total_supply: int):
        self.total_supply = total_supply
        self.participants: List[Participant] = []
        self.winners: List[Participant] = []
    
    def add_participant(self, participant: Participant):
        """Add a participant to the fair launch pool"""
        self.participants.append(participant)
    
    def conduct_fair_launch(self):
        """Conduct a fair random drawing for NFT allocation"""
        if len(self.participants) == 0:
            raise ValueError("No participants in the launch")
        
        if self.total_supply <= 0:
            raise ValueError("Invalid total supply")
        
        # Equal chance for all participants regardless of contribution size
        self.winners = random.sample(
            self.participants,
            min(self.total_supply, len(self.participants))
        )
        return self.winners

class TraditionalPresale:
    def __init__(self, total_supply: int):
        self.total_supply = total_supply
        self.allocations: Dict[str, int] = {}  # wallet -> allocation
    
    def add_participant(self, participant: Participant):
        """Add participant with allocation based on contribution size"""
        if participant.amount_committed <= 0:
            raise ValueError("Invalid commitment amount")
        
        # Traditional model favors whales with larger allocations
        allocation = int(participant.amount_committed * 10)  # Simplified formula
        if participant.is_whale:
            allocation *= 2  # Additional bonus for whales
        
        self.allocations[participant.wallet_address] = min(
            allocation, 
            self.total_supply
        )
        self.total_supply -= allocation
    
    def get_allocations(self):
        """Return the allocation distribution"""
        return self.allocations

# Example usage
if __name__ == "__main__":
    # Fair Launch Example
    print("=== Fair Launch Simulation ===")
    fair_launch = FairLaunch(total_supply=100)
    
    # Add participants (small and large contributors)
    for i in range(200):
        is_whale = i % 10 == 0  # 10% whales
        amount = 10.0 if is_whale else 0.1
        fair_launch.add_participant(
            Participant(wallet_address=f"0x{i}", amount_committed=amount, is_whale=is_whale)
        )
    
    winners = fair_launch.conduct_fair_launch()
    whale_winners = sum(1 for p in winners if p.is_whale)
    print(f"Winners: {len(winners)}, Whale winners: {whale_winners} ({whale_winners/len(winners):.1%})")
    
    # Traditional Presale Example
    print("\n=== Traditional Presale Simulation ===")
    presale = TraditionalPresale(total_supply=100)
    
    for i in range(200):
        is_whale = i % 10 == 0  # 10% whales
        amount = 10.0 if is_whale else 0.1
        presale.add_participant(
            Participant(wallet_address=f"0x{i}", amount_committed=amount, is_whale=is_whale)
        )
    
    allocations = presale.get_allocations()
    whale_allocation = sum(v for k, v in allocations.items() if k.startswith("0x0") or k.startswith("0x10"))
    print(f"Total allocations: {sum(allocations.values())}, Whale allocation: {whale_allocation} ({whale_allocation/sum(allocations.values()):.1%})")
```
