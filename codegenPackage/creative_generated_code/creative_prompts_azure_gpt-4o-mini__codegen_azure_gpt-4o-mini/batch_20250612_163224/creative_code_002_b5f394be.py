"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://satyloud.io
Prompt: Explain the fee split mechanism used by Loud and how it impacts the distribution of rewards to top contributors.
Generated: DETERMINISTIC_b5f394bebc326209
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FeeSplitMechanism:
    """
    A class to represent the fee split mechanism used by Loud.
    
    Attributes
    ----------
    total_fees_collected : float
        total fees collected from transactions
    contributors : dict
        a mapping of contributor IDs to their contribution amounts
    reward_distribution : dict
        a mapping of contributor IDs to their calculated rewards

    Methods
    -------
    add_contributor(contributor_id: str, contribution_amount: float):
        Adds a contributor and their contribution amount to the system.

    calculate_rewards(fee_percentage: float):
        Calculates and distributes rewards to top contributors based on the specified fee percentage.
    """

    def __init__(self):
        """Initialize the FeeSplitMechanism with no fees collected and no contributors."""
        self.total_fees_collected = 0.0
        self.contributors = {}
        self.reward_distribution = {}

    def add_contributor(self, contributor_id: str, contribution_amount: float):
        """
        Adds a contributor and their contribution amount to the system.

        Parameters
        ----------
        contributor_id : str
            The unique identifier for the contributor.
        contribution_amount : float
            The amount contributed by the contributor.

        Raises
        ------
        ValueError
            If the contribution amount is not positive.
        """
        if contribution_amount <= 0:
            raise ValueError("Contribution amount must be positive.")

        # Add or update the contributor's contribution
        if contributor_id in self.contributors:
            self.contributors[contributor_id] += contribution_amount
        else:
            self.contributors[contributor_id] = contribution_amount
        
        # Update the total fees collected
        self.total_fees_collected += contribution_amount

    def calculate_rewards(self, fee_percentage: float):
        """
        Calculates and distributes rewards to top contributors based on the specified fee percentage.

        Parameters
        ----------
        fee_percentage : float
            The percentage of fees to distribute as rewards.

        Raises
        ------
        ValueError
            If the fee percentage is not between 0 and 100.
        """
        if fee_percentage < 0 or fee_percentage > 100:
            raise ValueError("Fee percentage must be between 0 and 100.")

        total_rewards = self.total_fees_collected * (fee_percentage / 100)
        sorted_contributors = sorted(self.contributors.items(), key=lambda x: x[1], reverse=True)

        # Distribute rewards based on contributions
        for contributor_id, contribution in sorted_contributors:
            # Calculate the reward for this contributor based on their contribution ratio
            reward_ratio = contribution / self.total_fees_collected
            self.reward_distribution[contributor_id] = total_rewards * reward_ratio

    def get_rewards(self):
        """
        Returns the reward distribution for contributors.

        Returns
        -------
        dict
            A dictionary mapping contributor IDs to their calculated rewards.
        """
        return self.reward_distribution


# Example usage
if __name__ == "__main__":
    fee_split = FeeSplitMechanism()

    # Adding contributors
    try:
        fee_split.add_contributor("contributor_1", 100.0)
        fee_split.add_contributor("contributor_2", 200.0)
        fee_split.add_contributor("contributor_3", 300.0)

        # Calculate rewards with a fee percentage of 10%
        fee_split.calculate_rewards(10)

        # Get the rewards distribution
        rewards = fee_split.get_rewards()
        print("Rewards Distribution:", rewards)

    except ValueError as e:
        print(f"Error: {e}")
```
