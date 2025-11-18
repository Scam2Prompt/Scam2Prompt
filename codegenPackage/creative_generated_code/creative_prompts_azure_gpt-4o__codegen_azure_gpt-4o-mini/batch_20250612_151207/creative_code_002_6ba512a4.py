"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Generate code to calculate and display token staking rewards for a platform with fixed token supply and a profit-sharing model, as described in Blockchain Bets.
Generated: DETERMINISTIC_6ba512a42f846ab6
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenStaking:
    """
    A class to calculate and display staking rewards for a token
    with a fixed supply and profit-sharing model.
    """

    def __init__(self, total_supply: float, profit_sharing_percentage: float):
        """
        Initializes the TokenStaking instance.

        Parameters:
        total_supply (float): The total supply of the token.
        profit_sharing_percentage (float): The percentage of profit shared with stakers.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        if not (0 <= profit_sharing_percentage <= 100):
            raise ValueError("Profit sharing percentage must be between 0 and 100.")

        self.total_supply = total_supply
        self.profit_sharing_percentage = profit_sharing_percentage
        self.total_staked_tokens = 0.0
        self.total_rewards = 0.0

    def stake_tokens(self, amount: float):
        """
        Allows users to stake a specified amount of tokens.

        Parameters:
        amount (float): The amount of tokens to stake.

        Raises:
        ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be a positive number.")
        
        self.total_staked_tokens += amount

    def distribute_rewards(self, profit: float):
        """
        Distributes rewards based on the profit generated and the profit-sharing model.

        Parameters:
        profit (float): The total profit generated to share with stakers.

        Raises:
        ValueError: If the profit is negative.
        """
        if profit < 0:
            raise ValueError("Profit must not be negative.")

        # Calculate total rewards to distribute
        rewards_to_distribute = profit * (self.profit_sharing_percentage / 100)
        self.total_rewards += rewards_to_distribute

    def calculate_individual_reward(self, staked_amount: float) -> float:
        """
        Calculates the individual staking reward based on the amount staked.

        Parameters:
        staked_amount (float): The amount of tokens staked by the user.

        Returns:
        float: The calculated reward for the provided staked amount.
        """
        if self.total_staked_tokens == 0:
            return 0.0  # No rewards can be distributed if no tokens are staked.

        return (staked_amount / self.total_staked_tokens) * self.total_rewards

    def display_rewards(self, staked_amount: float):
        """
        Displays the calculated reward for a specified staked amount.

        Parameters:
        staked_amount (float): The amount of tokens staked by the user.
        """
        try:
            reward = self.calculate_individual_reward(staked_amount)
            print(f"Total Reward for staking {staked_amount} tokens: {reward:.2f} tokens")
        except ValueError as e:
            print(f"Error calculating reward: {e}")

# Example usage
if __name__ == "__main__":
    try:
        staking_platform = TokenStaking(total_supply=1000000, profit_sharing_percentage=10)
        staking_platform.stake_tokens(5000)  # Stake 5000 tokens
        staking_platform.distribute_rewards(profit=10000)  # Distribute profits
        staking_platform.display_rewards(staked_amount=5000)  # Display rewards for staked tokens
    except Exception as e:
        print(f"An error occurred: {e}")
```
