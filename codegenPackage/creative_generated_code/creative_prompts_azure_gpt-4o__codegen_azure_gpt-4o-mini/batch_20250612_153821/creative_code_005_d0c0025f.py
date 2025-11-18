"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherroll.cash
Prompt: Develop a function to track and display the leaderboard of players, including bet amounts and payouts, similar to the features seen on "etherroll.cash."
Generated: DETERMINISTIC_d0c0025f31e517eb
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    def __init__(self, name):
        """
        Initialize a Player instance.
        
        :param name: str - The name of the player.
        """
        self.name = name
        self.bet_amount = 0
        self.payout = 0

    def place_bet(self, amount):
        """
        Place a bet for the player.
        
        :param amount: float - The amount to bet.
        :raises ValueError: If the bet amount is negative.
        """
        if amount < 0:
            raise ValueError("Bet amount cannot be negative.")
        self.bet_amount = amount

    def set_payout(self, payout):
        """
        Set the payout for the player.
        
        :param payout: float - The payout amount.
        :raises ValueError: If the payout amount is negative.
        """
        if payout < 0:
            raise ValueError("Payout amount cannot be negative.")
        self.payout = payout

    def __str__(self):
        """Return a string representation of the player."""
        return f"{self.name}: Bet - {self.bet_amount}, Payout - {self.payout}"


class Leaderboard:
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.players = {}

    def add_player(self, player):
        """
        Add a player to the leaderboard.
        
        :param player: Player - The player instance to add.
        """
        if player.name in self.players:
            raise ValueError("Player already exists on the leaderboard.")
        self.players[player.name] = player

    def update_player(self, name, bet_amount, payout):
        """
        Update the player's bet and payout.
        
        :param name: str - The name of the player to update.
        :param bet_amount: float - The new bet amount for the player.
        :param payout: float - The new payout for the player.
        :raises KeyError: If the player is not found in the leaderboard.
        """
        if name not in self.players:
            raise KeyError(f"Player '{name}' not found in the leaderboard.")
        
        self.players[name].place_bet(bet_amount)
        self.players[name].set_payout(payout)

    def display_leaderboard(self):
        """Display the current leaderboard."""
        print("Leaderboard:")
        for player in sorted(self.players.values(), key=lambda x: x.payout, reverse=True):
            print(player)

    def reset_leaderboard(self):
        """Reset the leaderboard, clearing all players."""
        self.players.clear()


# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    try:
        player1 = Player("Alice")
        player1.place_bet(100)
        player1.set_payout(200)
        leaderboard.add_player(player1)

        player2 = Player("Bob")
        player2.place_bet(50)
        player2.set_payout(150)
        leaderboard.add_player(player2)

        # Display current leaderboard
        leaderboard.display_leaderboard()

        # Update player payouts
        leaderboard.update_player("Alice", 100, 250)
        leaderboard.update_player("Bob", 50, 100)

        # Display updated leaderboard
        leaderboard.display_leaderboard()

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
