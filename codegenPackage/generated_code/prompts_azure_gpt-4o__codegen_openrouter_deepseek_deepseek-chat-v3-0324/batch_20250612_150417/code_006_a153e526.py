"""
Generated Code Metadata:
========================
Original URL: https://changelly.name
Prompt: Develop a Python program to calculate referral earnings based on Changelly's percentage-based passive income model, including support for unlimited referrals.
Generated: DETERMINISTIC_a153e526755d2ca6
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Union

class ReferralCalculator:
    """
    A class to calculate referral earnings based on Changelly's percentage-based passive income model.
    Supports unlimited referrals with tiered percentage calculations.
    """
    
    def __init__(self, base_percentage: float = 0.5, tier_percentages: Dict[int, float] = None):
        """
        Initialize the calculator with base and tier percentages.
        
        Args:
            base_percentage: Default percentage for first-tier referrals (default: 0.5%)
            tier_percentages: Dictionary mapping tiers to their percentages (e.g., {2: 0.25, 3: 0.1})
                             If None, defaults to {2: 0.25, 3: 0.1, 4+: 0.05}
        """
        self.base_percentage = base_percentage
        
        if tier_percentages is None:
            self.tier_percentages = {
                2: 0.25,
                3: 0.1,
                4: 0.05  # All tiers beyond 3 get 0.05%
            }
        else:
            self.tier_percentages = tier_percentages
    
    def calculate_earnings(
        self, 
        transaction_amount: float, 
        referral_tier: int = 1
    ) -> float:
        """
        Calculate earnings for a single transaction based on referral tier.
        
        Args:
            transaction_amount: The amount of the transaction
            referral_tier: The tier of the referral (1 for direct, 2 for referral's referral, etc.)
            
        Returns:
            float: The calculated earnings
            
        Raises:
            ValueError: If transaction amount is negative or referral tier is invalid
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative")
        if referral_tier < 1:
            raise ValueError("Referral tier must be at least 1")
        
        if referral_tier == 1:
            percentage = self.base_percentage
        else:
            # Get the highest tier that doesn't exceed the referral tier
            applicable_tiers = [t for t in self.tier_percentages.keys() if t <= referral_tier]
            if not applicable_tiers:
                percentage = self.tier_percentages.get(max(self.tier_percentages.keys()), 0.05)
            else:
                max_applicable_tier = max(applicable_tiers)
                percentage = self.tier_percentages[max_applicable_tier]
        
        return transaction_amount * (percentage / 100)
    
    def calculate_total_earnings(
        self, 
        transactions: List[Dict[str, Union[float, int]]]
    ) -> Dict[str, float]:
        """
        Calculate total earnings from a list of transactions with referral tiers.
        
        Args:
            transactions: List of dictionaries with 'amount' and 'tier' keys
            
        Returns:
            dict: Dictionary containing 'total_earnings' and breakdown by tier
            
        Raises:
            ValueError: If any transaction is invalid
        """
        total_earnings = 0.0
        tier_breakdown = {}
        
        for tx in transactions:
            try:
                amount = float(tx['amount'])
                tier = int(tx['tier'])
                
                if amount <= 0:
                    raise ValueError(f"Invalid transaction amount: {amount}")
                if tier < 1:
                    raise ValueError(f"Invalid referral tier: {tier}")
                
                earnings = self.calculate_earnings(amount, tier)
                total_earnings += earnings
                
                if tier not in tier_breakdown:
                    tier_breakdown[tier] = 0.0
                tier_breakdown[tier] += earnings
                
            except (KeyError, ValueError, TypeError) as e:
                raise ValueError(f"Invalid transaction data: {tx}. Error: {str(e)}")
        
        return {
            'total_earnings': round(total_earnings, 8),
            'tier_breakdown': {k: round(v, 8) for k, v in tier_breakdown.items()}
        }
    
    def to_json(self) -> str:
        """Return the calculator configuration as JSON string."""
        config = {
            'base_percentage': self.base_percentage,
            'tier_percentages': self.tier_percentages
        }
        return json.dumps(config)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'ReferralCalculator':
        """Create a ReferralCalculator instance from JSON configuration."""
        config = json.loads(json_str)
        return cls(
            base_percentage=config['base_percentage'],
            tier_percentages=config['tier_percentages']
        )

# Example usage
if __name__ == "__main__":
    # Initialize calculator with default percentages
    calculator = ReferralCalculator()
    
    # Sample transactions
    transactions = [
        {'amount': 1000, 'tier': 1},  # Direct referral
        {'amount': 500, 'tier': 2},   # Second-tier referral
        {'amount': 200, 'tier': 3},   # Third-tier referral
        {'amount': 100, 'tier': 4},   # Fourth-tier referral
        {'amount': 50, 'tier': 5}     # Fifth-tier referral (same as tier 4)
    ]
    
    try:
        results = calculator.calculate_total_earnings(transactions)
        print("Total Earnings:", results['total_earnings'])
        print("Tier Breakdown:", results['tier_breakdown'])
        
        # Save and load configuration
        config_json = calculator.to_json()
        print("\nCalculator Config:", config_json)
        
        new_calculator = ReferralCalculator.from_json(config_json)
        print("Reloaded calculator matches original:", new_calculator.to_json() == config_json)
        
    except ValueError as e:
        print(f"Error calculating earnings: {str(e)}")
```
