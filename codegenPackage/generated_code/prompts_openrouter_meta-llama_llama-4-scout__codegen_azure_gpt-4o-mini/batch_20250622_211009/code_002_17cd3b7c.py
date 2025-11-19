"""
Generated Code Metadata:
========================
Original URL: https://ejelly.web.app
Prompt: "Explain the rarity system in the context of Jelly drop and staking."
Generated: DETERMINISTIC_17cd3b7c7a413ef5
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JellyDrop:
    """
    A class to represent a Jelly Drop in a rarity and staking system.
    """

    rarity_levels = {
        1: "Common",
        2: "Uncommon",
        3: "Rare",
        4: "Epic",
        5: "Legendary"
    }

    def __init__(self, rarity_level):
        """
        Initializes a Jelly Drop with a specified rarity level.

        :param rarity_level: An integer representing the rarity level (1-5).
        :raises ValueError: If rarity_level is not between 1 and 5.
        """
        if rarity_level not in self.rarity_levels:
            raise ValueError("Rarity level must be between 1 and 5.")
        self.rarity_level = rarity_level
        self.staked = False

    def stake(self):
        """
        Stakes the Jelly Drop, marking it as staked.
        """
        if self.staked:
            raise RuntimeError("This Jelly Drop is already staked.")
        self.staked = True

    def unstake(self):
        """
        Unstakes the Jelly Drop, marking it as unstaked.
        """
        if not self.staked:
            raise RuntimeError("This Jelly Drop is not staked.")
        self.staked = False

    def get_rarity(self):
        """
        Returns the rarity description of the Jelly Drop.

        :return: A string representing the rarity of the Jelly Drop.
        """
        return self.rarity_levels[self.rarity_level]

    def is_staked(self):
        """
        Checks if the Jelly Drop is currently staked.

        :return: A boolean indicating whether the Jelly Drop is staked.
        """
        return self.staked


class JellyDropStakingSystem:
    """
    A class to manage the staking of Jelly Drops.
    """

    def __init__(self):
        """
        Initializes the Jelly Drop Staking System with an empty list of Jelly Drops.
        """
        self.jelly_drops = []

    def add_jelly_drop(self, jelly_drop):
        """
        Adds a Jelly Drop to the staking system.

        :param jelly_drop: An instance of JellyDrop to be added.
        """
        if not isinstance(jelly_drop, JellyDrop):
            raise TypeError("Only JellyDrop instances can be added.")
        self.jelly_drops.append(jelly_drop)

    def stake_jelly_drop(self, index):
        """
        Stakes a Jelly Drop at the specified index.

        :param index: The index of the Jelly Drop to stake.
        :raises IndexError: If the index is out of range.
        """
        try:
            self.jelly_drops[index].stake()
        except IndexError:
            raise IndexError("No Jelly Drop found at the specified index.")

    def unstake_jelly_drop(self, index):
        """
        Unstakes a Jelly Drop at the specified index.

        :param index: The index of the Jelly Drop to unstake.
        :raises IndexError: If the index is out of range.
        """
        try:
            self.jelly_drops[index].unstake()
        except IndexError:
            raise IndexError("No Jelly Drop found at the specified index.")

    def get_staked_jelly_drops(self):
        """
        Returns a list of all staked Jelly Drops.

        :return: A list of staked Jelly Drops.
        """
        return [jelly_drop for jelly_drop in self.jelly_drops if jelly_drop.is_staked()]

    def get_all_jelly_drops(self):
        """
        Returns a list of all Jelly Drops in the system.

        :return: A list of all Jelly Drops.
        """
        return self.jelly_drops


# Example usage
if __name__ == "__main__":
    try:
        # Create a staking system
        staking_system = JellyDropStakingSystem()

        # Create Jelly Drops with different rarity levels
        drop1 = JellyDrop(1)  # Common
        drop2 = JellyDrop(3)  # Rare
        drop3 = JellyDrop(5)  # Legendary

        # Add Jelly Drops to the staking system
        staking_system.add_jelly_drop(drop1)
        staking_system.add_jelly_drop(drop2)
        staking_system.add_jelly_drop(drop3)

        # Stake the first Jelly Drop
        staking_system.stake_jelly_drop(0)

        # Print staked Jelly Drops
        staked_drops = staking_system.get_staked_jelly_drops()
        for drop in staked_drops:
            print(f"Staked Jelly Drop: {drop.get_rarity()}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
