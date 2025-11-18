"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.pages.dev
Prompt: Write code to calculate rewards from the 5% sell tax pool for $QUBE token staking, following InQubeta's tokenomics.
Generated: DETERMINISTIC_0c67d725b7f6f80b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class QubeTokenStaking:
    """
    A class to represent the staking of QUBE tokens and the calculation of rewards
    based on a 5% sell tax pool.
    """

    def __init__(self, total_supply: float, sell_tax_percentage: float = 0.05):
        """
        Initializes the QubeTokenStaking class.

        Args:
            total_supply (float): Total supply of QUBE tokens.
            sell_tax_percentage (float): Percentage of tokens allocated to the sell tax pool.
        """
        self.total_supply = total_supply
        self.sell_tax_percentage = sell_tax_percentage
        self.sell_tax_pool = 0.0  # Initialize the sell tax pool

    def update_sell_tax_pool(self, sell_amount: float):
        """
        Updates the sell tax pool based on the amount of tokens sold.

        Args:
            sell_amount (float): The amount of tokens that were sold.

        Raises:
            ValueError: If the sell_amount is negative or exceeds total supply.
        """
        if sell_amount < 0:
            raise ValueError("Sell amount must be a non-negative value.")
        if sell_amount > self.total_supply:
            raise ValueError("Sell amount cannot exceed total supply.")

        # Calculate the tax from the sell amount
        tax_amount = sell_amount * self.sell_tax_percentage
        self.sell_tax_pool += tax_amount

    def calculate_rewards(self, staked_amount: float) -> float:
        """
        Calculates rewards from the sell tax pool based on staked amount.

        Args:
            staked_amount (float): The amount of QUBE tokens staked.

        Returns:
            float: The calculated rewards based on the sell tax pool.

        Raises:
            ValueError: If the staked_amount is negative or exceeds total supply.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be a non-negative value.")
        if staked_amount > self.total_supply:
            raise ValueError("Staked amount cannot exceed total supply.")

        # Handle case where staked amount is zero to prevent division by zero
        if self.total_supply == 0:
            return 0.0

        # Calculate rewards based on the proportion of staked amount to total supply
        rewards = (staked_amount / self.total_supply) * self.sell_tax_pool
        return rewards

    def reset_sell_tax_pool(self):
        """
        Resets the sell tax pool to zero. This could be used at the end of a reward distribution cycle.
        """
        self.sell_tax_pool = 0.0

# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000.0  # Example total supply of QUBE tokens
        staking = QubeTokenStaking(total_supply)

        # Update the sell tax pool with a sell transaction of 1000 tokens
        staking.update_sell_tax_pool(1000)

        # Calculate rewards for a staked amount of 20000 tokens
        rewards = staking.calculate_rewards(20000)
        print(f"Calculated rewards: {rewards:.2f} QUBE tokens")

        # Reset the sell tax pool for a new cycle
        staking.reset_sell_tax_pool()

    except ValueError as e:
        print(f"Error: {e}")
```
