"""
Generated Code Metadata:
========================
Original URL: https://republik.pages.dev
Prompt: Generate code to implement a bonus system for an online slot game, including features like free spins, bankroll bonuses, and new member promotions, inspired by the offerings on ANGKA805.
Generated: DETERMINISTIC_e73c8657cf23a74b
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bonus_system.py

class BonusSystem:
    """
    A class representing the bonus system for an online slot game.
    """

    def __init__(self, player):
        """
        Initializes the bonus system for a given player.

        Args:
            player (Player): The player object.
        """
        self.player = player
        self.free_spins = 0
        self.bankroll_bonuses = []
        self.new_member_promotions = []

    def add_free_spins(self, amount):
        """
        Adds free spins to the player's account.

        Args:
            amount (int): The number of free spins to add.

        Raises:
            ValueError: If the amount is not a positive integer.
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Invalid free spin amount")
        self.free_spins += amount

    def use_free_spins(self, amount):
        """
        Uses free spins from the player's account.

        Args:
            amount (int): The number of free spins to use.

        Raises:
            ValueError: If the amount is not a positive integer or exceeds the available free spins.
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Invalid free spin amount")
        if amount > self.free_spins:
            raise ValueError("Insufficient free spins")
        self.free_spins -= amount

    def add_bankroll_bonus(self, amount, description):
        """
        Adds a bankroll bonus to the player's account.

        Args:
            amount (float): The bonus amount.
            description (str): The bonus description.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Invalid bonus amount")
        self.bankroll_bonuses.append({"amount": amount, "description": description})

    def add_new_member_promotion(self, promotion):
        """
        Adds a new member promotion to the player's account.

        Args:
            promotion (str): The promotion description.

        Raises:
            ValueError: If the promotion is empty.
        """
        if not promotion:
            raise ValueError("Invalid promotion")
        self.new_member_promotions.append(promotion)

    def get_player_info(self):
        """
        Returns the player's bonus information.

        Returns:
            dict: A dictionary containing the player's free spins, bankroll bonuses, and new member promotions.
        """
        return {
            "free_spins": self.free_spins,
            "bankroll_bonuses": self.bankroll_bonuses,
            "new_member_promotions": self.new_member_promotions,
        }


class Player:
    """
    A class representing a player.
    """

    def __init__(self, id, name):
        """
        Initializes a player.

        Args:
            id (int): The player's ID.
            name (str): The player's name.
        """
        self.id = id
        self.name = name


def main():
    # Create a player
    player = Player(1, "John Doe")

    # Create a bonus system for the player
    bonus_system = BonusSystem(player)

    # Add free spins
    bonus_system.add_free_spins(10)

    # Add bankroll bonus
    bonus_system.add_bankroll_bonus(100.0, "Welcome bonus")

    # Add new member promotion
    bonus_system.add_new_member_promotion("New member promotion")

    # Get player info
    player_info = bonus_system.get_player_info()

    # Print player info
    print("Player Info:")
    print(f"Free Spins: {player_info['free_spins']}")
    print("Bankroll Bonuses:")
    for bonus in player_info["bankroll_bonuses"]:
        print(f"- {bonus['amount']}: {bonus['description']}")
    print("New Member Promotions:")
    for promotion in player_info["new_member_promotions"]:
        print(f"- {promotion}")


if __name__ == "__main__":
    main()
```
