"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Develop a tool to simulate the impact of early access participation on token rewards in Manta CeDeFi, using the APR and TVL data provided.
Generated: DETERMINISTIC_65968f6be60f54b4
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class TokenRewardSimulator:
    """
    A class to simulate the impact of early access participation on token rewards in Manta CeDeFi using APR and TVL data.
    """

    def __init__(self, apr: float, tvl: float, early_access_bonus: float):
        """
        Initialize the TokenRewardSimulator with APR, TVL, and early access bonus.

        :param apr: Annual Percentage Rate (APR) as a percentage (e.g., 12.5 for 12.5%)
        :param tvl: Total Value Locked (TVL) in the platform, in tokens
        :param early_access_bonus: Bonus multiplier for early access participants (e.g., 1.1 for 10% bonus)
        """
        if apr < 0 or tvl < 0 or early_access_bonus <= 0:
            raise ValueError("APR, TVL, and early access bonus values must be positive.")
        
        self.apr = apr
        self.tvl = tvl
        self.early_access_bonus = early_access_bonus

    def simulate_rewards(self, user_stake: float, days_staked: int, early_access: bool = False) -> float:
        """
        Simulate the rewards for a user based on their stake, duration, and early access participation.

        :param user_stake: User's stake in the platform, in tokens
        :param days_staked: Number of days the stake is held
        :param early_access: True if the user participates in early access, False otherwise
        :return: Simulated rewards in tokens
        """
        if user_stake <= 0 or days_staked <= 0:
            raise ValueError("User stake and days staked must be positive.")
        
        # Convert APR from percentage to decimal and calculate daily rewards rate
        daily_rate = self.apr / 100 / 365
        
        # Calculate base rewards
        base_rewards = user_stake * daily_rate * days_staked
        
        # Apply early access bonus if applicable
        if early_access:
            return base_rewards * self.early_access_bonus
        return base_rewards

def main():
    """
    Main function to demonstrate the TokenRewardSimulator usage.
    """
    try:
        # Example APR, TVL, and early access bonus values
        apr = 12.0  # 12% APR
        tvl = 1_000_000  # Total Value Locked is 1,000,000 tokens
        early_access_bonus = 1.2  # 20% bonus for early access participants

        # Initialize the simulator
        simulator = TokenRewardSimulator(apr, tvl, early_access_bonus)
        
        # Example user input
        user_stake = 1000  # User stakes 1,000 tokens
        days_staked = 30  # User stakes for 30 days
        early_access = True  # User participates in early access
        
        # Simulate rewards
        rewards = simulator.simulate_rewards(user_stake, days_staked, early_access)
        
        print(f"Simulated rewards for {days_staked} days: {rewards:.2f} tokens")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
