"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Explain the concept of tokenomics in the context of the FreeDum Fighters project, highlighting the allocation of tokens for liquidity pools, staking, and rewards.
Generated: DETERMINISTIC_11dc00e0f7a9467f
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    """
    A class to represent the tokenomics of the FreeDum Fighters project.
    
    Attributes:
        total_supply (int): Total number of tokens available.
        liquidity_pool (float): Percentage of tokens allocated to liquidity pools.
        staking (float): Percentage of tokens allocated for staking rewards.
        rewards (float): Percentage of tokens allocated for user rewards.
    """

    def __init__(self, total_supply: int, liquidity_pool: float, staking: float, rewards: float):
        """
        Initializes the Tokenomics class with the specified allocations.

        Args:
            total_supply (int): Total number of tokens available.
            liquidity_pool (float): Percentage of tokens allocated to liquidity pools.
            staking (float): Percentage of tokens allocated for staking rewards.
            rewards (float): Percentage of tokens allocated for user rewards.

        Raises:
            ValueError: If any allocation percentage is negative or exceeds 100.
        """
        if not (0 <= liquidity_pool <= 100):
            raise ValueError("Liquidity pool allocation must be between 0 and 100.")
        if not (0 <= staking <= 100):
            raise ValueError("Staking allocation must be between 0 and 100.")
        if not (0 <= rewards <= 100):
            raise ValueError("Rewards allocation must be between 0 and 100.")
        
        if liquidity_pool + staking + rewards > 100:
            raise ValueError("Total allocation cannot exceed 100%.")

        self.total_supply = total_supply
        self.liquidity_pool = liquidity_pool
        self.staking = staking
        self.rewards = rewards

    def calculate_allocations(self):
        """
        Calculates the number of tokens allocated to each category.

        Returns:
            dict: A dictionary containing the allocations for liquidity pools, staking, and rewards.
        """
        allocations = {
            "liquidity_pool": self.total_supply * (self.liquidity_pool / 100),
            "staking": self.total_supply * (self.staking / 100),
            "rewards": self.total_supply * (self.rewards / 100),
        }
        return allocations

    def __str__(self):
        """
        Returns a string representation of the tokenomics allocations.

        Returns:
            str: A formatted string showing the total supply and allocations.
        """
        allocations = self.calculate_allocations()
        return (f"Total Supply: {self.total_supply}\n"
                f"Liquidity Pool Allocation: {allocations['liquidity_pool']}\n"
                f"Staking Allocation: {allocations['staking']}\n"
                f"Rewards Allocation: {allocations['rewards']}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Tokenomics for FreeDum Fighters
        tokenomics = Tokenomics(total_supply=1000000, liquidity_pool=30, staking=50, rewards=20)
        
        # Print the allocations
        print(tokenomics)
    except ValueError as e:
        print(f"Error: {e}")
```
