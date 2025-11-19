"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dflow-claims.pages.dev
Prompt: What are the steps to earn DFlow XP during the early access phase on the DFlow leaderboard?
Generated: DETERMINISTIC_2c6cfeed99ed51ee
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DFlowLeaderboard:
    """
    A class to represent the DFlow leaderboard and manage XP earning during the early access phase.
    """

    def __init__(self):
        """
        Initializes the leaderboard with an empty list of players and their XP.
        """
        self.players = {}

    def add_player(self, player_name):
        """
        Adds a new player to the leaderboard.

        Args:
            player_name (str): The name of the player to add.

        Raises:
            ValueError: If the player name is already in the leaderboard.
        """
        if player_name in self.players:
            raise ValueError(f"Player '{player_name}' already exists in the leaderboard.")
        self.players[player_name] = 0
        print(f"Player '{player_name}' has been added to the leaderboard.")

    def earn_xp(self, player_name, xp_amount):
        """
        Increases the XP of a player.

        Args:
            player_name (str): The name of the player earning XP.
            xp_amount (int): The amount of XP to earn.

        Raises:
            ValueError: If the player does not exist or if XP amount is negative.
        """
        if player_name not in self.players:
            raise ValueError(f"Player '{player_name}' does not exist in the leaderboard.")
        if xp_amount < 0:
            raise ValueError("XP amount must be non-negative.")
        
        self.players[player_name] += xp_amount
        print(f"Player '{player_name}' earned {xp_amount} XP.")

    def display_leaderboard(self):
        """
        Displays the current leaderboard sorted by XP in descending order.
        """
        sorted_leaderboard = sorted(self.players.items(), key=lambda item: item[1], reverse=True)
        print("DFlow XP Leaderboard:")
        for player, xp in sorted_leaderboard:
            print(f"{player}: {xp} XP")

# Example usage
if __name__ == "__main__":
    leaderboard = DFlowLeaderboard()
    
    # Adding players
    try:
        leaderboard.add_player("Alice")
        leaderboard.add_player("Bob")
        
        # Earning XP
        leaderboard.earn_xp("Alice", 100)
        leaderboard.earn_xp("Bob", 150)
        
        # Display leaderboard
        leaderboard.display_leaderboard()
    except ValueError as e:
        print(f"Error: {e}")
```
