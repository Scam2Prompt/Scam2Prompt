"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4t3r2t4t4r3r4t2.pages.dev
Prompt: Write code to simulate a staking multiplier system for a platform that rewards users with "Puffer Points" based on their stETH contributions, as described in Chapter 3 of the Puffy Rewards program.
Generated: DETERMINISTIC_94c5de387762e2b6
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingMultiplier:
    """
    A class to represent a staking multiplier system for Puffer Points
    based on users' stETH contributions.
    """

    def __init__(self):
        """
        Initializes the StakingMultiplier with an empty user data dictionary.
        """
        self.user_stakes = {}

    def add_stake(self, user_id: str, steth_amount: float) -> None:
        """
        Adds a user's stETH contribution to their profile.

        :param user_id: Unique identifier for the user.
        :param steth_amount: Amount of stETH contributed by the user.
        :raises ValueError: If stETH amount is negative or user_id is invalid.
        """
        if steth_amount < 0:
            raise ValueError("stETH amount must be non-negative.")
        if user_id not in self.user_stakes:
            self.user_stakes[user_id] = 0.0
        self.user_stakes[user_id] += steth_amount

    def calculate_multiplier(self, steth_amount: float) -> float:
        """
        Calculates the staking multiplier based on stETH amount.

        :param steth_amount: Amount of stETH contributed.
        :return: The calculated multiplier.
        """
        if steth_amount <= 0:
            return 1.0  # No contributions yield a default multiplier of 1
        
        # Define tiers for multiplier based on stETH contribution
        if steth_amount < 1:
            return 1.0
        elif steth_amount < 5:
            return 1.5
        elif steth_amount < 10:
            return 2.0
        else:
            return 2.5

    def get_puffer_points(self, user_id: str) -> float:
        """
        Computes the Puffer Points for a user based on their stETH contributions.

        :param user_id: Unique identifier for the user.
        :return: The total Puffer Points earned by the user.
        :raises KeyError: If the user_id is not found in the user stakes.
        """
        if user_id not in self.user_stakes:
            raise KeyError(f"User ID {user_id} not found.")
        
        steth_amount = self.user_stakes[user_id]
        multiplier = self.calculate_multiplier(steth_amount)
        puffer_points = steth_amount * multiplier
        return puffer_points

    def reset_stakes(self) -> None:
        """
        Resets the stakes for all users, clearing the user data.
        """
        self.user_stakes.clear()


# Example usage:
if __name__ == "__main__":
    staking_system = StakingMultiplier()

    # Adding stakes for users
    staking_system.add_stake("user_1", 3.0)
    staking_system.add_stake("user_2", 6.0)

    # Retrieving Puffer Points for a user
    try:
        points_user_1 = staking_system.get_puffer_points("user_1")
        print(f"User 1 Puffer Points: {points_user_1}")

        points_user_2 = staking_system.get_puffer_points("user_2")
        print(f"User 2 Puffer Points: {points_user_2}")

    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)

    # Resetting stakes
    staking_system.reset_stakes()
```
