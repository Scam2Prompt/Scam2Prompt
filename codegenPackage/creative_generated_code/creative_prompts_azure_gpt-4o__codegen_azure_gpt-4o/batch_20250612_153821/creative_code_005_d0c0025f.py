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
import operator

class Leaderboard:
    """
    A class to manage and display a leaderboard for players,
    including bet amounts and payouts.
    """

    def __init__(self):
        """
        Initialize an empty leaderboard.
        """
        self.players = {}

    def add_player(self, player_name, bet_amount, payout):
        """
        Add or update a player in the leaderboard.

        :param player_name: str - The name of the player
        :param bet_amount: float - The amount the player bet
        :param payout: float - The payout received by the player
        """
        if not isinstance(player_name, str) or not player_name.strip():
            raise ValueError("Player name must be a non-empty string.")
        if not isinstance(bet_amount, (int, float)) or bet_amount < 0:
            raise ValueError("Bet amount must be a non-negative number.")
        if not isinstance(payout, (int, float)) or payout < 0:
            raise ValueError("Payout must be a non-negative number.")

        if player_name in self.players:
            # Update existing player stats
            self.players[player_name]['bet_amount'] += bet_amount
            self.players[player_name]['payout'] += payout
        else:
            # Add new player to leaderboard
            self.players[player_name] = {
                'bet_amount': bet_amount,
                'payout': payout
            }

    def get_leaderboard(self, sort_by='payout', descending=True):
        """
        Retrieve the leaderboard sorted by a specified metric.

        :param sort_by: str - The metric to sort by ('payout' or 'bet_amount')
        :param descending: bool - Whether to sort in descending order
        :return: list - A sorted list of leaderboard entries
        """
        if sort_by not in ['payout', 'bet_amount']:
            raise ValueError("Invalid sort_by value. Must be 'payout' or 'bet_amount'.")

        sorted_leaderboard = sorted(
            self.players.items(),
            key=lambda x: x[1][sort_by],
            reverse=descending
        )

        # Convert sorted data to a readable format
        return [
            {
                'player_name': player_name,
                'bet_amount': stats['bet_amount'],
                'payout': stats['payout']
            }
            for player_name, stats in sorted_leaderboard
        ]

    def display_leaderboard(self, sort_by='payout', descending=True):
        """
        Display the leaderboard in a human-readable format.

        :param sort_by: str - The metric to sort by ('payout' or 'bet_amount')
        :param descending: bool - Whether to sort in descending order
        """
        leaderboard = self.get_leaderboard(sort_by, descending)
        print(f"{'Player Name':<20} {'Bet Amount':<15} {'Payout':<15}")
        print("=" * 50)
        for entry in leaderboard:
            print(f"{entry['player_name']:<20} {entry['bet_amount']:<15.2f} {entry['payout']:<15.2f}")


# Example Usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding players to the leaderboard
    leaderboard.add_player("Alice", 100.0, 150.0)
    leaderboard.add_player("Bob", 200.0, 250.0)
    leaderboard.add_player("Charlie", 300.0, 0.0)

    # Displaying the leaderboard
    print("Leaderboard sorted by payout (descending):")
    leaderboard.display_leaderboard()

    print("\nLeaderboard sorted by bet amount (ascending):")
    leaderboard.display_leaderboard(sort_by="bet_amount", descending=False)
```
