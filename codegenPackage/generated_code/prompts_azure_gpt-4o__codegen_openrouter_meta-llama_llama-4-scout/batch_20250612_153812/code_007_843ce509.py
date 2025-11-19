"""
Generated Code Metadata:
========================
Original URL: https://stellar-neurongate.xyz
Prompt: Write code to implement a welcome bonus system for an online casino, including features like €450 and 250 free spins, as described on the Zeus Fortune webpage.
Generated: DETERMINISTIC_843ce509cd2886ba
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# welcome_bonus.py

class WelcomeBonus:
    """
    A class representing the welcome bonus system for an online casino.
    """

    def __init__(self, bonus_amount=450, free_spins=250):
        """
        Initializes the WelcomeBonus object.

        Args:
            bonus_amount (int, optional): The welcome bonus amount in euros. Defaults to 450.
            free_spins (int, optional): The number of free spins. Defaults to 250.
        """
        self.bonus_amount = bonus_amount
        self.free_spins = free_spins

    def calculate_welcome_bonus(self, deposit_amount):
        """
        Calculates the welcome bonus based on the deposit amount.

        The welcome bonus is €450 and is given for a minimum deposit of €10.

        Args:
            deposit_amount (float): The player's deposit amount.

        Returns:
            float: The welcome bonus amount.

        Raises:
            ValueError: If the deposit amount is less than €10.
        """
        if deposit_amount < 10:
            raise ValueError("Deposit amount must be at least €10 to receive the welcome bonus.")

        # For simplicity, assume the welcome bonus is a fixed amount
        return self.bonus_amount

    def get_free_spins(self):
        """
        Returns the number of free spins.

        Returns:
            int: The number of free spins.
        """
        return self.free_spins


class Player:
    """
    A class representing a player in the online casino.
    """

    def __init__(self, player_id, deposit_amount):
        """
        Initializes the Player object.

        Args:
            player_id (int): The player's unique ID.
            deposit_amount (float): The player's deposit amount.
        """
        self.player_id = player_id
        self.deposit_amount = deposit_amount
        self.welcome_bonus = None

    def apply_welcome_bonus(self, welcome_bonus):
        """
        Applies the welcome bonus to the player's account.

        Args:
            welcome_bonus (WelcomeBonus): The welcome bonus object.

        Returns:
            dict: A dictionary containing the welcome bonus details.
        """
        try:
            bonus_amount = welcome_bonus.calculate_welcome_bonus(self.deposit_amount)
            free_spins = welcome_bonus.get_free_spins()

            self.welcome_bonus = {
                "bonus_amount": bonus_amount,
                "free_spins": free_spins,
            }

            return self.welcome_bonus

        except ValueError as e:
            print(f"Error applying welcome bonus: {e}")
            return None


def main():
    # Create a welcome bonus object
    welcome_bonus = WelcomeBonus()

    # Create a player object
    player = Player(1, 100)

    # Apply the welcome bonus to the player's account
    bonus_details = player.apply_welcome_bonus(welcome_bonus)

    if bonus_details:
        print("Welcome Bonus Details:")
        print(f"Player ID: {player.player_id}")
        print(f"Bonus Amount: €{bonus_details['bonus_amount']}")
        print(f"Free Spins: {bonus_details['free_spins']}")


if __name__ == "__main__":
    main()
```
