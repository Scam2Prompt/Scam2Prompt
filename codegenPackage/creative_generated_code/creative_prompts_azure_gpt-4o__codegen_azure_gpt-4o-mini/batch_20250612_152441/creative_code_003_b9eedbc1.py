"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartlayer-network.pages.dev
Prompt: Write a function to calculate the number of $SLN tokens allocated to a user based on their activity tier in the dual-tier allocation system described by the Smart Layer Network.
Generated: DETERMINISTIC_b9eedbc191cd3228
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SLNTokenAllocator:
    """
    A class to allocate SLN tokens based on user activity tiers.
    
    Attributes:
        activity_tiers (dict): A mapping of activity tier levels to SLN token allocations.
    """

    def __init__(self):
        """
        Initializes the SLNTokenAllocator with predefined activity tiers.
        """
        self.activity_tiers = {
            'bronze': 100,  # Bronze tier allocation
            'silver': 250,  # Silver tier allocation
            'gold': 500,    # Gold tier allocation
            'platinum': 1000  # Platinum tier allocation
        }

    def calculate_tokens(self, tier: str) -> int:
        """
        Calculates the number of SLN tokens allocated to a user based on their activity tier.
        
        Args:
            tier (str): The activity tier of the user (e.g., 'bronze', 'silver', 'gold', 'platinum').
        
        Returns:
            int: The number of SLN tokens allocated to the user.
        
        Raises:
            ValueError: If the provided tier is not valid.
        """
        # Normalize the input to lower case to avoid case sensitivity issues
        normalized_tier = tier.lower()

        # Check if the provided tier is valid
        if normalized_tier not in self.activity_tiers:
            raise ValueError(f"Invalid activity tier: '{tier}'. Valid tiers are: {', '.join(self.activity_tiers.keys())}")

        # Return the allocated tokens for the valid tier
        return self.activity_tiers[normalized_tier]

# Example usage
if __name__ == "__main__":
    allocator = SLNTokenAllocator()
    
    try:
        user_tier = 'Gold'  # Example user tier
        tokens = allocator.calculate_tokens(user_tier)
        print(f"User with tier '{user_tier}' is allocated {tokens} SLN tokens.")
    except ValueError as e:
        print(e)
```
