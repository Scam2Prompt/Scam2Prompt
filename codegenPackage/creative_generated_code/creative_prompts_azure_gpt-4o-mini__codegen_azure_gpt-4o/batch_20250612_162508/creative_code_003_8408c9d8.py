"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pingu-buy.pages.dev
Prompt: Explain how to implement the "Ice Chest Airdrops" reward mechanism for Pingu token holders, including the types of rewards that can be distributed.
Generated: DETERMINISTIC_8408c9d84e04a167
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Union

class IceChestAirdrop:
    """
    Class to implement the 'Ice Chest Airdrops' reward mechanism for Pingu token holders.
    """

    def __init__(self, token_holders: Dict[str, int]):
        """
        Initialize with a dictionary of token holders and their token balances.

        :param token_holders: Dictionary where keys are wallet addresses (str) and values are token balances (int).
        """
        self.token_holders = token_holders
        self.rewards_pool = ['Rare NFT', 'Common NFT', 'Exclusive Merchandise', 'Discount Token', 'Bonus Tokens']
    
    def validate_token_holders(self):
        """
        Validates the token holders' data to ensure it's in the correct format.
        """
        if not isinstance(self.token_holders, dict):
            raise ValueError("Token holders must be provided as a dictionary.")
        
        for wallet, balance in self.token_holders.items():
            if not isinstance(wallet, str) or not isinstance(balance, int) or balance < 0:
                raise ValueError("Each wallet must be a string and balance must be a positive integer.")
    
    def calculate_eligibility(self, min_balance: int) -> List[str]:
        """
        Calculate eligibility based on token balance.

        :param min_balance: The minimum token balance required to be eligible for rewards.
        :return: List of eligible wallet addresses.
        """
        eligible_wallets = [
            wallet for wallet, balance in self.token_holders.items() if balance >= min_balance
        ]
        return eligible_wallets
    
    def distribute_rewards(self, min_balance: int) -> Dict[str, Union[str, None]]:
        """
        Distribute rewards to eligible token holders.

        :param min_balance: Minimum token balance required to be eligible for rewards.
        :return: Dictionary of wallet addresses and their assigned rewards.
        """
        eligible_wallets = self.calculate_eligibility(min_balance)
        rewards_distribution = {}

        for wallet in eligible_wallets:
            # Assign a random reward from the reward pool
            reward = random.choice(self.rewards_pool)
            rewards_distribution[wallet] = reward

        # Token holders who are not eligible receive None
        for wallet in self.token_holders.keys():
            if wallet not in rewards_distribution:
                rewards_distribution[wallet] = None

        return rewards_distribution

    def display_rewards(self, rewards_distribution: Dict[str, Union[str, None]]):
        """
        Display the rewards distribution.

        :param rewards_distribution: Dictionary of wallet addresses and their assigned rewards.
        """
        print("Rewards Distribution:")
        for wallet, reward in rewards_distribution.items():
            if reward:
                print(f"Wallet: {wallet} -> Reward: {reward}")
            else:
                print(f"Wallet: {wallet} -> Reward: None (Not Eligible)")


if __name__ == "__main__":
    # Example usage:
    # Token holders dictionary: {'wallet_address': token_balance}
    token_holders = {
        'wallet1': 100,
        'wallet2': 50,
        'wallet3': 200,
        'wallet4': 10,
        'wallet5': 300
    }

    # Instantiate the IceChestAirdrop class
    airdrop = IceChestAirdrop(token_holders)

    try:
        # Validate the token holders data
        airdrop.validate_token_holders()

        # Define minimum balance to be eligible for airdrop rewards
        min_balance = 100

        # Distribute rewards
        rewards = airdrop.distribute_rewards(min_balance)

        # Display rewards distribution
        airdrop.display_rewards(rewards)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
