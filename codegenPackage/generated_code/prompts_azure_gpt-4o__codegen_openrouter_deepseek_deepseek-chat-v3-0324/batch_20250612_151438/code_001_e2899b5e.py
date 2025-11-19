"""
Generated Code Metadata:
========================
Original URL: https://elon-crypto.online
Prompt: Generate a script that simulates the referral bonus system for OctaFx VIP plans, ensuring it adheres to the zero-level referral bonus structure mentioned on the webpage.
Generated: DETERMINISTIC_e2899b5ef169c58b
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional

class VIPPlan(Enum):
    """Enum representing the different VIP plans available."""
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"
    DIAMOND = "Diamond"

@dataclass
class ReferralBonus:
    """Data class representing referral bonus structure for a VIP plan."""
    plan: VIPPlan
    bonus_percentage: float

class ReferralSystem:
    """Class to simulate the OctaFx VIP referral bonus system."""
    
    def __init__(self):
        """Initialize the referral system with predefined bonus structures."""
        self._bonus_structure = self._load_bonus_structure()
    
    def _load_bonus_structure(self) -> Dict[VIPPlan, float]:
        """Load the predefined bonus structure for each VIP plan.
        
        Returns:
            Dict[VIPPlan, float]: Mapping of VIP plan to bonus percentage.
        """
        return {
            VIPPlan.BRONZE: 0.10,    # 10%
            VIPPlan.SILVER: 0.15,    # 15%
            VIPPlan.GOLD: 0.20,      # 20%
            VIPPlan.PLATINUM: 0.25,  # 25%
            VIPPlan.DIAMOND: 0.30    # 30%
        }
    
    def calculate_bonus(self, referrer_plan: VIPPlan, referred_amount: float) -> float:
        """Calculate the referral bonus based on the referrer's VIP plan and referred amount.
        
        Args:
            referrer_plan: VIPPlan of the referrer.
            referred_amount: Amount deposited by the referred client.
            
        Returns:
            float: Calculated bonus amount.
            
        Raises:
            ValueError: If referred_amount is negative.
        """
        if referred_amount < 0:
            raise ValueError("Referred amount cannot be negative.")
        
        bonus_percentage = self._bonus_structure.get(referrer_plan, 0.0)
        return referred_amount * bonus_percentage
    
    def get_bonus_structure(self) -> List[ReferralBonus]:
        """Get the current bonus structure for all VIP plans.
        
        Returns:
            List[ReferralBonus]: List of referral bonuses for each VIP plan.
        """
        return [
            ReferralBonus(plan=plan, bonus_percentage=percentage)
            for plan, percentage in self._bonus_structure.items()
        ]
    
    def to_json(self) -> str:
        """Serialize the bonus structure to JSON.
        
        Returns:
            str: JSON string representation of the bonus structure.
        """
        bonus_list = [
            {"plan": bonus.plan.value, "bonus_percentage": bonus.bonus_percentage}
            for bonus in self.get_bonus_structure()
        ]
        return json.dumps(bonus_list, indent=2)

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Calculate bonus for a Bronze VIP referrer with $1000 referred amount
    try:
        bonus = referral_system.calculate_bonus(VIPPlan.BRONZE, 1000)
        print(f"Referral bonus: ${bonus:.2f}")
    except ValueError as e:
        print(f"Error calculating bonus: {e}")
    
    # Display current bonus structure
    print("\nCurrent Bonus Structure:")
    print(referral_system.to_json())
```
