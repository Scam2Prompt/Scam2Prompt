"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogstoken.web.app
Prompt: Write a script to calculate rewards for early $SMOG token holders and stakers, incorporating the website's emphasis on privileges for "early dragon slayers."
Generated: DETERMINISTIC_bb7af374a3127d77
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class TokenHolder:
    def __init__(self, address: str, amount: float, staked: bool, join_date: datetime.datetime):
        """
        Initialize a TokenHolder instance.
        
        :param address: The wallet address of the token holder.
        :param amount: Amount of $SMOG tokens held.
        :param staked: Indicates whether the tokens are staked.
        :param join_date: The date when the holder joined (or purchased) the tokens.
        """
        self.address = address
        self.amount = amount
        self.staked = staked
        self.join_date = join_date

class RewardCalculator:
    EARLY_ADOPTER_BONUS = 0.1  # 10% bonus for early dragon slayers
    STAKING_BONUS = 0.05       # 5% bonus for stakers
    BASE_REWARD_PER_TOKEN = 1  # Base reward per token

    def __init__(self, early_cutoff: datetime.datetime):
        """
        Initialize a RewardCalculator instance.
        
        :param early_cutoff: The cutoff date for early adopters.
        """
        self.early_cutoff = early_cutoff

    def calculate_rewards(self, holders: List[TokenHolder]) -> Dict[str, float]:
        """
        Calculate rewards for a list of token holders.
        
        :param holders: A list of TokenHolder objects.
        :return: A dictionary mapping wallet addresses to their calculated rewards.
        """
        rewards = {}
        for holder in holders:
            try:
                reward = self.BASE_REWARD_PER_TOKEN * holder.amount

                # Check if the holder is an early dragon slayer
                if holder.join_date < self.early_cutoff:
                    reward += reward * self.EARLY_ADOPTER_BONUS
                
                # Check if the holder is a staker
                if holder.staked:
                    reward += reward * self.STAKING_BONUS

                rewards[holder.address] = round(reward, 2)

            except Exception as e:
                # Handle any errors during reward calculation
                print(f"Error calculating reward for address {holder.address}: {e}")
                rewards[holder.address] = 0.0  # Default to zero if an error occurs

        return rewards

def main():
    # Example usage
    early_cutoff_date = datetime.datetime(2023, 1, 1)  # Define the cutoff date for early adopters
    reward_calculator = RewardCalculator(early_cutoff=early_cutoff_date)

    # Sample token holders
    holders = [
        TokenHolder(address="0x123", amount=100, staked=True, join_date=datetime.datetime(2022, 12, 15)),
        TokenHolder(address="0x456", amount=200, staked=False, join_date=datetime.datetime(2023, 2, 10)),
        TokenHolder(address="0x789", amount=150, staked=True, join_date=datetime.datetime(2022, 11, 30)),
    ]

    # Calculate rewards
    rewards = reward_calculator.calculate_rewards(holders)

    # Display rewards
    for address, reward in rewards.items():
        print(f"Address: {address}, Reward: ${reward}")

if __name__ == "__main__":
    main()
```
