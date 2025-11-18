"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lyvely-claim.pages.dev
Prompt: Generate code for setting up a tiered tipping system on a platform, inspired by Lyvely's "Grateful" feature, with customizable tip amounts.
Generated: DETERMINISTIC_bccc891688c4ba8f
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TieredTipSystem:
    """
    A class to implement a tiered tipping system inspired by Lyvely's "Grateful" feature.
    
    Attributes:
        tiers (dict): A dictionary that holds the tier names and their corresponding tip amounts.
    """

    def __init__(self):
        """
        Initializes the TieredTipSystem with default tiers and tip amounts.
        """
        self.tiers = {
            "Bronze": 5.00,  # Minimum tip amount
            "Silver": 10.00,  # Mid-tier tip amount
            "Gold": 20.00,  # High-tier tip amount
            "Platinum": 50.00  # Premium tier tip amount
        }

    def set_tier(self, tier_name, tip_amount):
        """
        Set a custom tip amount for a specific tier.
        
        Args:
            tier_name (str): The name of the tier to be updated.
            tip_amount (float): The custom tip amount to set for the tier.
        
        Raises:
            ValueError: If the tip amount is less than or equal to zero.
            KeyError: If the tier name does not exist.
        """
        if tip_amount <= 0:
            raise ValueError("Tip amount must be greater than zero.")
        
        if tier_name not in self.tiers:
            raise KeyError(f"Tier '{tier_name}' does not exist.")
        
        self.tiers[tier_name] = tip_amount

    def get_tip_amount(self, tier_name):
        """
        Get the tip amount for a specific tier.
        
        Args:
            tier_name (str): The name of the tier.
        
        Returns:
            float: The tip amount for the specified tier.
        
        Raises:
            KeyError: If the tier name does not exist.
        """
        if tier_name not in self.tiers:
            raise KeyError(f"Tier '{tier_name}' does not exist.")
        
        return self.tiers[tier_name]

    def display_tiers(self):
        """
        Display the available tiers and their corresponding tip amounts.
        
        Returns:
            dict: A dictionary of the tiers and their respective tip amounts.
        """
        return self.tiers

def main():
    """
    Main function to demonstrate the TieredTipSystem functionality.
    """
    try:
        tip_system = TieredTipSystem()
        
        # Display initial tiers and tip amounts
        print("Initial Tiers and Tip Amounts:")
        print(tip_system.display_tiers())
        
        # Update a tier with a custom tip amount
        tip_system.set_tier("Gold", 25.00)
        
        # Display updated tiers
        print("\nUpdated Tiers:")
        print(tip_system.display_tiers())
        
        # Retrieve a specific tip amount
        gold_tip = tip_system.get_tip_amount("Gold")
        print(f"\nThe tip amount for the Gold tier is: ${gold_tip:.2f}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
