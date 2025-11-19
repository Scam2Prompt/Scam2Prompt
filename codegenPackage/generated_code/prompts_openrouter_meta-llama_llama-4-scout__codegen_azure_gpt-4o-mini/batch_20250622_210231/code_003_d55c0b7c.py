"""
Generated Code Metadata:
========================
Original URL: https://notcoin-90l.pages.dev
Prompt: Design a data structure to store information about Notcoin players, including their balances, league rankings, and squad affiliations, and write a function to update this information based on new gameplay data.
Generated: DETERMINISTIC_d55c0b7cc43ef62b
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NotcoinPlayer:
    """
    A class to represent a Notcoin player.

    Attributes:
        player_id (str): Unique identifier for the player.
        balance (float): The current balance of the player.
        league_rank (int): The current league ranking of the player.
        squad_affiliation (str): The squad the player is affiliated with.
    """

    def __init__(self, player_id: str, balance: float, league_rank: int, squad_affiliation: str):
        """
        Initializes a NotcoinPlayer instance.

        Args:
            player_id (str): Unique identifier for the player.
            balance (float): Initial balance of the player.
            league_rank (int): Initial league ranking of the player.
            squad_affiliation (str): Initial squad affiliation of the player.
        """
        self.player_id = player_id
        self.balance = balance
        self.league_rank = league_rank
        self.squad_affiliation = squad_affiliation

    def update_info(self, balance_change: float, new_league_rank: int, new_squad_affiliation: str):
        """
        Updates the player's information based on new gameplay data.

        Args:
            balance_change (float): The amount to change the player's balance by (can be negative).
            new_league_rank (int): The new league ranking of the player.
            new_squad_affiliation (str): The new squad affiliation of the player.

        Raises:
            ValueError: If the new league rank is not a positive integer.
            TypeError: If balance_change is not a float.
        """
        if not isinstance(balance_change, (int, float)):
            raise TypeError("balance_change must be a number.")
        
        if new_league_rank <= 0:
            raise ValueError("League rank must be a positive integer.")

        # Update balance
        self.balance += balance_change

        # Update league rank and squad affiliation
        self.league_rank = new_league_rank
        self.squad_affiliation = new_squad_affiliation

    def __str__(self):
        """
        Returns a string representation of the NotcoinPlayer instance.

        Returns:
            str: A string containing player information.
        """
        return (f"Player ID: {self.player_id}, "
                f"Balance: {self.balance:.2f}, "
                f"League Rank: {self.league_rank}, "
                f"Squad Affiliation: {self.squad_affiliation}")


# Example usage
if __name__ == "__main__":
    try:
        player = NotcoinPlayer("player1", 100.0, 1, "Squad A")
        print(player)

        # Update player information
        player.update_info(50.0, 2, "Squad B")
        print(player)

        # Attempt to update with invalid league rank
        player.update_info(-20.0, 0, "Squad C")  # This will raise a ValueError
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
