"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Create a script to calculate staking rewards for a blockchain token similar to Pushd, where interest rates range between 7% and 17% based on the number of tokens staked.
Generated: DETERMINISTIC_98ad09f88a2364e6
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for a blockchain token.
    The interest rates range from 7% to 17% based on the number of tokens staked.
    """
    
    def __init__(self, min_tokens: int = 1000, max_tokens: int = 10000):
        """
        Initializes the StakingRewardsCalculator with minimum and maximum staking tokens.
        
        :param min_tokens: Minimum number of tokens required to stake (default is 1000).
        :param max_tokens: Maximum number of tokens for the reward calculation (default is 10000).
        """
        self.min_tokens = min_tokens
        self.max_tokens = max_tokens

    def calculate_interest_rate(self, tokens_staked: int) -> float:
        """
        Calculates the interest rate based on the number of tokens staked.
        
        :param tokens_staked: The number of tokens staked by the user.
        :return: The applicable interest rate as a decimal.
        :raises ValueError: If the tokens_staked is less than the minimum or greater than the maximum.
        """
        if tokens_staked < self.min_tokens or tokens_staked > self.max_tokens:
            raise ValueError(f"Tokens staked must be between {self.min_tokens} and {self.max_tokens}.")

        # Determine interest rate based on staked tokens
        if tokens_staked < 5000:
            return 0.07  # 7%
        elif tokens_staked < 10000:
            return 0.12  # 12%
        else:
            return 0.17  # 17%

    def calculate_rewards(self, tokens_staked: int, duration_years: float) -> float:
        """
        Calculates the staking rewards for the given number of tokens and duration in years.
        
        :param tokens_staked: The number of tokens staked by the user.
        :param duration_years: The duration for which tokens are staked, in years.
        :return: The total rewards earned.
        """
        try:
            interest_rate = self.calculate_interest_rate(tokens_staked)
            # Calculate rewards using compound interest formula: A = P(1 + r/n)^(nt)
            rewards = tokens_staked * (1 + interest_rate) ** duration_years - tokens_staked
            return rewards
        except ValueError as e:
            print(f"Error calculating rewards: {e}")
            return 0.0  # Return 0 rewards in case of error

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of StakingRewardsCalculator
        calculator = StakingRewardsCalculator()
        
        # Define the number of tokens staked and the duration in years
        tokens_staked = 5000
        duration_years = 2
        
        # Calculate the rewards
        rewards = calculator.calculate_rewards(tokens_staked, duration_years)
        
        print(f"Staking rewards for {tokens_staked} tokens over {duration_years} years: {rewards:.2f} tokens")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
