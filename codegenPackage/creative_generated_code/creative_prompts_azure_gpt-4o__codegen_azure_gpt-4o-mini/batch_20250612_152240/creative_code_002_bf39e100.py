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
class NFTProject:
    def __init__(self, project_name, staked_amount, reward_rate):
        """
        Initialize an NFT project with its name, staked amount, and reward rate.
        
        :param project_name: str - Name of the NFT project
        :param staked_amount: float - Amount of NFTs staked
        :param reward_rate: float - Token distribution rate per staked NFT
        """
        self.project_name = project_name
        self.staked_amount = staked_amount
        self.reward_rate = reward_rate

    def calculate_rewards(self):
        """
        Calculate the total rewards for this NFT project.
        
        :return: float - Total rewards earned
        """
        try:
            if self.staked_amount < 0 or self.reward_rate < 0:
                raise ValueError("Staked amount and reward rate must be non-negative.")
            return self.staked_amount * self.reward_rate
        except Exception as e:
            print(f"Error calculating rewards for {self.project_name}: {e}")
            return 0.0


def total_rewards(nft_projects):
    """
    Calculate the total rewards earned across multiple NFT projects.

    :param nft_projects: list of NFTProject - List of NFTProject instances
    :return: float - Total rewards earned across all projects
    """
    try:
        if not isinstance(nft_projects, list):
            raise TypeError("Input must be a list of NFTProject instances.")
        
        total = 0.0
        for project in nft_projects:
            if not isinstance(project, NFTProject):
                raise TypeError("All items in the list must be instances of NFTProject.")
            total += project.calculate_rewards()
        return total
    except Exception as e:
        print(f"Error calculating total rewards: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    # Create instances of NFT projects
    project1 = NFTProject("Project A", 10, 2.5)
    project2 = NFTProject("Project B", 5, 3.0)
    project3 = NFTProject("Project C", 20, 1.0)

    # List of all NFT projects
    projects = [project1, project2, project3]

    # Calculate total rewards for all projects
    total_earned = total_rewards(projects)
    print(f"Total rewards earned: {total_earned}")
```
