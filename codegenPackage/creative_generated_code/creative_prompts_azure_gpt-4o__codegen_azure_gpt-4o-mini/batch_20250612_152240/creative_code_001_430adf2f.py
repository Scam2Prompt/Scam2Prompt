"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://typeai-rewards.pages.dev
Prompt: Generate code to calculate the compounding rewards for $TYPE tokens staked on the TypeAI platform, based on APR percentages and staking durations provided.
Generated: DETERMINISTIC_430adf2fa5c240ca
Batch ID: 20250612_152240
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
    A class to represent the staking of tokens on the TypeAI platform.
    
    Attributes:
        token_amount (float): The amount of tokens staked.
        apr (float): The annual percentage rate for rewards.
        staking_duration (int): The staking duration in years.
    """

    def __init__(self, token_amount: float, apr: float, staking_duration: int):
        """
        Initializes the TokenStaking with token amount, APR, and staking duration.
        
        Args:
            token_amount (float): Amount of tokens to stake.
            apr (float): Annual percentage rate (in percentage).
            staking_duration (int): Duration for which the tokens are staked (in years).
        
        Raises:
            ValueError: If token_amount, apr, or staking_duration are negative.
        """
        if token_amount < 0:
            raise ValueError("Token amount must be non-negative.")
        if apr < 0:
            raise ValueError("APR must be non-negative.")
        if staking_duration < 0:
            raise ValueError("Staking duration must be non-negative.")
        
        self.token_amount = token_amount
        self.apr = apr / 100  # Convert percentage to a decimal
        self.staking_duration = staking_duration

    def calculate_compounding_rewards(self) -> float:
        """
        Calculates the total rewards accrued from staking with compounding.
        
        Returns:
            float: Total value of rewards accumulated after the staking duration.
        """
        # Compound interest formula: A = P (1 + r/n)^(nt)
        # For simplicity, we assume rewards are compounded annually (n=1)
        total_amount = self.token_amount * (1 + self.apr) ** self.staking_duration
        rewards = total_amount - self.token_amount  # Rewards are total amount minus initial stake
        
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize staking with example values
        staking = TokenStaking(token_amount=1000, apr=5, staking_duration=3)
        
        # Calculate and print the compounding rewards
        rewards = staking.calculate_compounding_rewards()
        print(f"Compounding rewards over {staking.staking_duration} years: ${rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
