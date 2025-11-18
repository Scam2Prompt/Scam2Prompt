"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allthingslemon-io.pages.dev
Prompt: Create a function that calculates the total rewards earned for staked NFTs across multiple projects on the LEMON platform, using the token distribution rates provided.
Generated: DETERMINISTIC_bf39e1007fcf4584
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List

class NFTStakingRewardsCalculator:
    def __init__(self, token_distribution_rates: Dict[str, float]):
        """
        Initializes the calculator with token distribution rates for each project.

        :param token_distribution_rates: A dictionary where the keys are project names and the values are
                                         the token distribution rate (tokens earned per staked NFT per day).
        """
        self.token_distribution_rates = token_distribution_rates
    
    def calculate_total_rewards(self, staked_nfts: Dict[str, int], days_staked: int) -> float:
        """
        Calculates the total rewards earned for staked NFTs across multiple projects.

        :param staked_nfts: A dictionary where keys are project names and values are the number of NFTs staked.
        :param days_staked: The number of days NFTs have been staked.
        :return: The total rewards earned across all projects (float).
        """
        try:
            total_rewards = 0.0
            
            # Iterate through each project in the staked NFTs dictionary
            for project, nft_count in staked_nfts.items():
                if project not in self.token_distribution_rates:
                    # Skip projects that don't have a token distribution rate defined
                    raise ValueError(f"Missing token distribution rate for project: {project}")
                
                # Calculate rewards for the current project
                rate = self.token_distribution_rates[project]
                rewards = rate * nft_count * days_staked
                total_rewards += rewards
            
            return total_rewards
        
        except ValueError as ve:
            # Handle missing distribution rates gracefully
            print(f"Error: {ve}")
            return 0.0
        
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            return 0.0

# Example usage
if __name__ == "__main__":
    # Token distribution rates (tokens per NFT per day)
    token_distribution_rates = {
        "ProjectA": 10.0,
        "ProjectB": 5.0,
        "ProjectC": 20.0,
    }

    # Number of NFTs staked per project
    staked_nfts = {
        "ProjectA": 3,
        "ProjectB": 5,
        "ProjectC": 2,
    }

    # Days the NFTs have been staked
    days_staked = 7

    # Create an instance of the calculator
    calculator = NFTStakingRewardsCalculator(token_distribution_rates)

    # Calculate total rewards
    total_rewards = calculator.calculate_total_rewards(staked_nfts, days_staked)
    print(f"Total rewards earned: {total_rewards} tokens")
```
