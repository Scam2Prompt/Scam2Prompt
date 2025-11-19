"""
Generated Code Metadata:
========================
Original URL: https://allthingslemon-io.pages.dev
Prompt: Create a function that calculates the total rewards earned for staked NFTs across multiple projects on the LEMON platform, using the token distribution rates provided.
Generated: DETERMINISTIC_bf39e1007fcf4584
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

class NFTProject:
    """Represents an NFT project on the LEMON platform."""

    def __init__(self, project_id: str, token_distribution_rate: float):
        """
        Initializes an NFTProject instance.

        Args:
        - project_id (str): Unique identifier for the project.
        - token_distribution_rate (float): Token distribution rate for the project.
        """
        self.project_id = project_id
        self.token_distribution_rate = token_distribution_rate
        self.staked_nfts = []

    def add_staked_nft(self, nft_id: str, staking_duration: int):
        """
        Adds a staked NFT to the project.

        Args:
        - nft_id (str): Unique identifier for the NFT.
        - staking_duration (int): Duration for which the NFT is staked (in days).
        """
        self.staked_nfts.append({"nft_id": nft_id, "staking_duration": staking_duration})

    def calculate_rewards(self) -> float:
        """
        Calculates the total rewards earned for staked NFTs in the project.

        Returns:
        - float: Total rewards earned.
        """
        total_rewards = 0
        for nft in self.staked_nfts:
            # Assuming rewards are calculated as token distribution rate * staking duration
            rewards = self.token_distribution_rate * nft["staking_duration"]
            total_rewards += rewards
        return total_rewards


def calculate_total_rewards(projects: List[NFTProject]) -> float:
    """
    Calculates the total rewards earned for staked NFTs across multiple projects.

    Args:
    - projects (List[NFTProject]): List of NFTProject instances.

    Returns:
    - float: Total rewards earned across all projects.
    """
    total_rewards = 0
    for project in projects:
        try:
            project_rewards = project.calculate_rewards()
            total_rewards += project_rewards
        except Exception as e:
            # Log or handle exception as needed
            print(f"Error calculating rewards for project {project.project_id}: {str(e)}")
    return total_rewards


# Example usage:
if __name__ == "__main__":
    project1 = NFTProject("project1", 0.1)
    project1.add_staked_nft("nft1", 30)
    project1.add_staked_nft("nft2", 60)

    project2 = NFTProject("project2", 0.2)
    project2.add_staked_nft("nft3", 90)

    projects = [project1, project2]
    total_rewards = calculate_total_rewards(projects)
    print(f"Total rewards earned: {total_rewards}")
```
