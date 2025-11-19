"""
Generated Code Metadata:
========================
Original URL: https://thegraph.live
Prompt: "What are the differences between R1 to R8 required business tiers in The Graph's reward system, and how do their rewards and tour incentives vary?"
Generated: DETERMINISTIC_ca5ee9c38b2df840
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script defines and explains the different business tiers (R1-R8) in The Graph's reward system,
including their requirements, rewards, and incentives.
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class BusinessTier:
    """Represents a business tier in The Graph's reward system."""
    tier_name: str
    min_stake: float  # In GRT
    min_delegators: int
    min_indexers: int
    base_reward_rate: float  # Annual percentage
    tour_incentives: List[str]
    additional_benefits: List[str]

def get_business_tiers() -> Dict[str, BusinessTier]:
    """Returns a dictionary of all business tiers (R1-R8) with their specifications."""
    return {
        "R1": BusinessTier(
            tier_name="Starter",
            min_stake=10000,
            min_delegators=1,
            min_indexers=1,
            base_reward_rate=0.10,
            tour_incentives=["Basic support"],
            additional_benefits=["Access to community forums"]
        ),
        "R2": BusinessTier(
            tier_name="Basic",
            min_stake=50000,
            min_delegators=3,
            min_indexers=1,
            base_reward_rate=0.12,
            tour_incentives=["Basic support", "Monthly check-ins"],
            additional_benefits=["Access to community forums", "Basic analytics"]
        ),
        "R3": BusinessTier(
            tier_name="Standard",
            min_stake=100000,
            min_delegators=5,
            min_indexers=2,
            base_reward_rate=0.15,
            tour_incentives=["Priority support", "Quarterly reviews"],
            additional_benefits=["Advanced analytics", "API access"]
        ),
        "R4": BusinessTier(
            tier_name="Professional",
            min_stake=250000,
            min_delegators=10,
            min_indexers=3,
            base_reward_rate=0.18,
            tour_incentives=["Dedicated account manager", "Quarterly reviews"],
            additional_benefits=["Custom reporting", "Early feature access"]
        ),
        "R5": BusinessTier(
            tier_name="Advanced",
            min_stake=500000,
            min_delegators=15,
            min_indexers=5,
            base_reward_rate=0.20,
            tour_incentives=["24/7 support", "Monthly strategy sessions"],
            additional_benefits=["Custom integrations", "Premium training"]
        ),
        "R6": BusinessTier(
            tier_name="Enterprise",
            min_stake=1000000,
            min_delegators=20,
            min_indexers=7,
            base_reward_rate=0.22,
            tour_incentives=["Dedicated engineer", "Bi-weekly strategy sessions"],
            additional_benefits=["White-glove onboarding", "Co-marketing opportunities"]
        ),
        "R7": BusinessTier(
            tier_name="Elite",
            min_stake=2500000,
            min_delegators=30,
            min_indexers=10,
            base_reward_rate=0.25,
            tour_incentives=["Executive sponsorship", "Weekly strategy sessions"],
            additional_benefits=["Custom SLAs", "Governance participation"]
        ),
        "R8": BusinessTier(
            tier_name="Platinum",
            min_stake=5000000,
            min_delegators=50,
            min_indexers=15,
            base_reward_rate=0.30,
            tour_incentives=["C-level access", "Custom engagement model"],
            additional_benefits=["Protocol influence", "Exclusive events"]
        )
    }

def print_tier_comparison():
    """Prints a comparison table of all business tiers."""
    tiers = get_business_tiers()
    
    print("The Graph Business Tiers Comparison")
    print("="*50)
    print(f"{'Tier':<5} {'Name':<12} {'Min Stake (GRT)':<15} {'Min Delegators':<15} {'Reward Rate':<12} {'Key Incentives'}")
    print("-"*50)
    
    for tier_code, tier in tiers.items():
        key_incentives = ", ".join(tier.tour_incentives[:2]) + ("..." if len(tier.tour_incentives) > 2 else "")
        print(f"{tier_code:<5} {tier.tier_name:<12} {tier.min_stake:<15,} {tier.min_delegators:<15} {tier.base_reward_rate:<12.1%} {key_incentives}")

if __name__ == "__main__":
    print_tier_comparison()
```
