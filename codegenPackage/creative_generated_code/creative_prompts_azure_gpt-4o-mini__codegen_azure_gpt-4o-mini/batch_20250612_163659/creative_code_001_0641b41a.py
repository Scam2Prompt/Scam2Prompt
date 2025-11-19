"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olliivveemmaaiinn12893891bndjdbiqw.pages.dev
Prompt: Write a code snippet to calculate total deposits and active restakers for a staking rewards platform.
Generated: DETERMINISTIC_0641b41a74e6e4ee
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsPlatform:
    """
    A class to represent a staking rewards platform.

    Attributes
    ----------
    deposits : list of float
        A list containing the deposit amounts for each user.
    restakers : list of bool
        A list indicating whether each user is an active restaker.
    """

    def __init__(self):
        """Initializes the StakingRewardsPlatform with empty deposits and restakers."""
        self.deposits = []
        self.restakers = []

    def add_user(self, deposit: float, is_restaker: bool) -> None:
        """
        Adds a user to the platform with their deposit amount and restaker status.

        Parameters
        ----------
        deposit : float
            The deposit amount made by the user. Must be non-negative.
        is_restaker : bool
            The status indicating if the user is an active restaker.

        Raises
        ------
        ValueError
            If the deposit is negative.
        """
        if deposit < 0:
            raise ValueError("Deposit amount cannot be negative.")

        self.deposits.append(deposit)
        self.restakers.append(is_restaker)

    def calculate_total_deposits(self) -> float:
        """
        Calculates the total deposits made by all users.

        Returns
        -------
        float
            The total sum of deposits.
        """
        return sum(self.deposits)

    def count_active_restakers(self) -> int:
        """
        Counts the number of active restakers.

        Returns
        -------
        int
            The count of active restakers.
        """
        return sum(1 for restaker in self.restakers if restaker)

    def get_summary(self) -> dict:
        """
        Provides a summary of total deposits and active restakers.

        Returns
        -------
        dict
            A dictionary containing total deposits and active restaker count.
        """
        return {
            "total_deposits": self.calculate_total_deposits(),
            "active_restakers": self.count_active_restakers()
        }


# Example usage
if __name__ == "__main__":
    platform = StakingRewardsPlatform()
    
    # Adding users with their deposit amounts and restaker status
    platform.add_user(1000.0, True)
    platform.add_user(500.0, False)
    platform.add_user(250.0, True)

    # Getting the summary of deposits and restakers
    summary = platform.get_summary()
    print(summary)  # Output: {'total_deposits': 1750.0, 'active_restakers': 2}
```
