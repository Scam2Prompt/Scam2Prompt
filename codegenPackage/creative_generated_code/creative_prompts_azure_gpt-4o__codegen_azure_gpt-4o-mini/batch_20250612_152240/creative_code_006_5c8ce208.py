"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appmemekombatclaim.pages.dev
Prompt: Provide code examples for implementing a leaderboard system for Meme Kombat battles, where players can view rankings based on their betting outcomes and rewards earned.
Generated: DETERMINISTIC_5c8ce2081ffddc05
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

class Player:
    """
    A class to represent a player in the Meme Kombat leaderboard.
    """
    def __init__(self, username: str):
        """
        Initialize the player with a username and default stats.
        
        :param username: The player's username.
        """
        self.username = username
        self.wins = 0
        self.losses = 0
        self.total_bets = 0.0
        self.total_rewards = 0.0

    def update_stats(self, win: bool, bet_amount: float, reward: float):
        """
        Update player's win/loss stats and betting outcomes.
        
        :param win: Boolean indicating if the player won the bet.
        :param bet_amount: The amount bet by the player.
        :param reward: The reward earned by the player if they won.
        """
        if win:
            self.wins += 1
            self.total_rewards += reward
        else:
            self.losses += 1
        
        self.total_bets += bet_amount


class Leaderboard:
    """
    A class to manage the leaderboard of players.
    """
    def __init__(self):
        """
        Initialize the leaderboard with an empty player list.
        """
        self.players = {}

    def add_player(self, username: str):
        """
        Add a new player to the leaderboard.
        
        :param username: The username of the player to add.
        """
        if username not in self.players:
            self.players[username] = Player(username)
        else:
            raise ValueError(f"Player {username} already exists.")

    def update_player(self, username: str, win: bool, bet_amount: float, reward: float):
        """
        Update the stats for an existing player.
        
        :param username: The username of the player to update.
        :param win: Boolean indicating if the player won the bet.
        :param bet_amount: The amount bet by the player.
        :param reward: The reward earned by the player if they won.
        """
        if username in self.players:
            self.players[username].update_stats(win, bet_amount, reward)
        else:
            raise ValueError(f"Player {username} does not exist.")

    def get_leaderboard(self):
        """
        Get the leaderboard sorted by total rewards earned.
        
        :return: A list of tuples containing player usernames and their total rewards, sorted by rewards.
        """
        return sorted(
            self.players.items(),
            key=lambda item: item[1].total_rewards,
            reverse=True
        )

    def display_leaderboard(self):
        """
        Display the leaderboard in a readable format.
        """
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for rank, (username, player) in enumerate(leaderboard, start=1):
            print(f"{rank}. {username} - Wins: {player.wins}, Losses: {player.losses}, Total Rewards: {player.total_rewards:.2f}")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding players
    try:
        leaderboard.add_player("Player1")
        leaderboard.add_player("Player2")
    except ValueError as e:
        print(e)

    # Updating players with battle results
    try:
        leaderboard.update_player("Player1", True, 50, 100)
        leaderboard.update_player("Player2", False, 20, 0)
        leaderboard.update_player("Player1", True, 30, 60)
    except ValueError as e:
        print(e)

    # Display the current leaderboard
    leaderboard.display_leaderboard()
```
