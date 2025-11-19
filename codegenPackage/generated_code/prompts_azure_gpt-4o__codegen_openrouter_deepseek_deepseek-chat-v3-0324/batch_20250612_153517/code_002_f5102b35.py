"""
Generated Code Metadata:
========================
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Create a program that tracks referral statistics, including total referrals, claimed bonuses, and ready-to-claim bonuses, based on the referral program details provided on ScapesMania.
Generated: DETERMINISTIC_f5102b354b96070d
Batch ID: 20250612_153517
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
from typing import Dict, List, Optional
from datetime import datetime

@dataclass
class ReferralBonus:
    """Represents a referral bonus with its status and timestamp."""
    bonus_amount: float
    is_claimed: bool
    timestamp: datetime

class ReferralTracker:
    """Tracks referral statistics for users in a referral program."""
    
    def __init__(self):
        """Initializes the referral tracker with empty data structures."""
        self.referrals: Dict[str, List[ReferralBonus]] = {}
    
    def add_referral(self, referrer_id: str, bonus_amount: float) -> None:
        """Adds a new referral bonus for the given referrer.
        
        Args:
            referrer_id: The ID of the referrer.
            bonus_amount: The amount of the bonus to be added.
        """
        if not referrer_id:
            raise ValueError("Referrer ID cannot be empty.")
        if bonus_amount <= 0:
            raise ValueError("Bonus amount must be positive.")
        
        bonus = ReferralBonus(
            bonus_amount=bonus_amount,
            is_claimed=False,
            timestamp=datetime.now()
        )
        
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(bonus)
    
    def claim_bonus(self, referrer_id: str, bonus_index: int) -> float:
        """Claims a specific bonus for the given referrer.
        
        Args:
            referrer_id: The ID of the referrer.
            bonus_index: The index of the bonus to claim.
        
        Returns:
            The amount of the claimed bonus.
        
        Raises:
            ValueError: If referrer_id is not found or bonus_index is invalid.
        """
        if referrer_id not in self.referrals:
            raise ValueError("Referrer ID not found.")
        if bonus_index < 0 or bonus_index >= len(self.referrals[referrer_id]):
            raise ValueError("Invalid bonus index.")
        if self.referrals[referrer_id][bonus_index].is_claimed:
            raise ValueError("Bonus already claimed.")
        
        self.referrals[referrer_id][bonus_index].is_claimed = True
        return self.referrals[referrer_id][bonus_index].bonus_amount
    
    def get_total_referrals(self, referrer_id: str) -> int:
        """Returns the total number of referrals for a referrer.
        
        Args:
            referrer_id: The ID of the referrer.
        
        Returns:
            The total number of referrals.
        """
        return len(self.referrals.get(referrer_id, []))
    
    def get_claimed_bonuses(self, referrer_id: str) -> List[ReferralBonus]:
        """Returns all claimed bonuses for a referrer.
        
        Args:
            referrer_id: The ID of the referrer.
        
        Returns:
            A list of claimed ReferralBonus objects.
        """
        if referrer_id not in self.referrals:
            return []
        return [bonus for bonus in self.referrals[referrer_id] if bonus.is_claimed]
    
    def get_ready_to_claim_bonuses(self, referrer_id: str) -> List[ReferralBonus]:
        """Returns all unclaimed bonuses for a referrer.
        
        Args:
            referrer_id: The ID of the referrer.
        
        Returns:
            A list of unclaimed ReferralBonus objects.
        """
        if referrer_id not in self.referrals:
            return []
        return [bonus for bonus in self.referrals[referrer_id] if not bonus.is_claimed]
    
    def get_total_claimed_amount(self, referrer_id: str) -> float:
        """Returns the total amount of claimed bonuses for a referrer.
        
        Args:
            referrer_id: The ID of the referrer.
        
        Returns:
            The total claimed amount.
        """
        claimed_bonuses = self.get_claimed_bonuses(referrer_id)
        return sum(bonus.bonus_amount for bonus in claimed_bonuses)
    
    def get_total_ready_to_claim_amount(self, referrer_id: str) -> float:
        """Returns the total amount of unclaimed bonuses for a referrer.
        
        Args:
            referrer_id: The ID of the referrer.
        
        Returns:
            The total unclaimed amount.
        """
        ready_bonuses = self.get_ready_to_claim_bonuses(referrer_id)
        return sum(bonus.bonus_amount for bonus in ready_bonuses)
    
    def save_to_file(self, file_path: str) -> None:
        """Saves the referral data to a JSON file.
        
        Args:
            file_path: The path to the file where data will be saved.
        
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            serializable_data = {
                referrer_id: [
                    {
                        "bonus_amount": bonus.bonus_amount,
                        "is_claimed": bonus.is_claimed,
                        "timestamp": bonus.timestamp.isoformat()
                    }
                    for bonus in bonuses
                ]
                for referrer_id, bonuses in self.referrals.items()
            }
            with open(file_path, 'w') as f:
                json.dump(serializable_data, f, indent=2)
        except Exception as e:
            raise IOError(f"Failed to save data to file: {e}")
    
    def load_from_file(self, file_path: str) -> None:
        """Loads referral data from a JSON file.
        
        Args:
            file_path: The path to the file from which data will be loaded.
        
        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            self.referrals = {}
            for referrer_id, bonuses in data.items():
                self.referrals[referrer_id] = [
                    ReferralBonus(
                        bonus_amount=bonus["bonus_amount"],
                        is_claimed=bonus["is_claimed"],
                        timestamp=datetime.fromisoformat(bonus["timestamp"])
                    )
                    for bonus in bonuses
                ]
        except Exception as e:
            raise IOError(f"Failed to load data from file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = ReferralTracker()
    
    # Add some referrals
    tracker.add_referral("user1", 10.0)
    tracker.add_referral("user1", 15.0)
    tracker.add_referral("user2", 20.0)
    
    # Claim a bonus
    claimed_amount = tracker.claim_bonus("user1", 0)
    print(f"Claimed amount: {claimed_amount}")
    
    # Get statistics
    print(f"Total referrals for user1: {tracker.get_total_referrals('user1')}")
    print(f"Total claimed for user1: {tracker.get_total_claimed_amount('user1')}")
    print(f"Total ready to claim for user1: {tracker.get_total_ready_to_claim_amount('user1')}")
    
    # Save and load data
    tracker.save_to_file("referrals.json")
    new_tracker = ReferralTracker()
    new_tracker.load_from_file("referrals.json")
```
