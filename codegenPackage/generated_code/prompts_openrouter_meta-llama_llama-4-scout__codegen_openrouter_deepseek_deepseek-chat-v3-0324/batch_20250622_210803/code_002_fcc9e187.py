"""
Generated Code Metadata:
========================
Original URL: https://eternallaunch.pages.dev
Prompt: What are the different tiers for the $EAI public sale, and how do they affect the boost and hard cap for participants?
Generated: DETERMINISTIC_fcc9e18735ecec73
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EAITokenSale:
    """
    Represents the EAI token sale with different tiers and their respective benefits.
    """
    
    def __init__(self):
        self.tiers = {
            'Tier 1': {
                'min_contribution': 1000,  # USD
                'max_contribution': 5000,  # USD
                'boost_multiplier': 1.5,
                'hard_cap': 1000000  # USD
            },
            'Tier 2': {
                'min_contribution': 5001,  # USD
                'max_contribution': 20000,  # USD
                'boost_multiplier': 2.0,
                'hard_cap': 500000  # USD
            },
            'Tier 3': {
                'min_contribution': 20001,  # USD
                'max_contribution': 50000,  # USD
                'boost_multiplier': 2.5,
                'hard_cap': 250000  # USD
            },
            'Tier 4': {
                'min_contribution': 50001,  # USD
                'max_contribution': 100000,  # USD
                'boost_multiplier': 3.0,
                'hard_cap': 100000  # USD
            }
        }
    
    def get_tier_details(self, tier_name):
        """
        Returns details for a specific tier.
        
        Args:
            tier_name (str): Name of the tier (e.g., 'Tier 1')
            
        Returns:
            dict: Tier details or None if tier doesn't exist
        """
        return self.tiers.get(tier_name)
    
    def get_all_tiers(self):
        """
        Returns all available tiers and their details.
        
        Returns:
            dict: All tiers and their details
        """
        return self.tiers
    
    def calculate_boosted_allocation(self, tier_name, contribution_amount):
        """
        Calculates the boosted token allocation based on tier and contribution.
        
        Args:
            tier_name (str): Name of the tier
            contribution_amount (float): Contribution amount in USD
            
        Returns:
            float: Boosted allocation amount
            None: If tier doesn't exist or contribution is out of bounds
        """
        tier = self.get_tier_details(tier_name)
        if not tier:
            return None
            
        if contribution_amount < tier['min_contribution'] or contribution_amount > tier['max_contribution']:
            return None
            
        return contribution_amount * tier['boost_multiplier']
    
    def check_hard_cap(self, tier_name, current_total):
        """
        Checks if current total contributions exceed the tier's hard cap.
        
        Args:
            tier_name (str): Name of the tier
            current_total (float): Current total contributions in USD
            
        Returns:
            bool: True if under hard cap, False if exceeded
            None: If tier doesn't exist
        """
        tier = self.get_tier_details(tier_name)
        if not tier:
            return None
            
        return current_total <= tier['hard_cap']
```
