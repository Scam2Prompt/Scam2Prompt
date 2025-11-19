"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: What strategies can players use to climb the $BIGTIME leaderboard by inviting friends?
Generated: DETERMINISTIC_77a697feb9d6af2d
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BigTimeLeaderboard:
    def __init__(self):
        # Initialize leaderboard and player invitations
        self.leaderboard = {}
        self.invites = {}

    def add_player(self, player_name):
        """Add a new player to the leaderboard with an initial score of 0."""
        if player_name in self.leaderboard:
            raise ValueError(f"Player '{player_name}' already exists.")
        self.leaderboard[player_name] = 0
        self.invites[player_name] = 0

    def invite_friend(self, player_name, friend_name):
        """Invite a friend to join the game."""
        if player_name not in self.leaderboard:
            raise ValueError(f"Player '{player_name}' does not exist.")
        if friend_name in self.leaderboard:
            raise ValueError(f"Friend '{friend_name}' is already a player.")
        
        self.invites[player_name] += 1  # Increment the invite count for the player
        print(f"{player_name} has invited {friend_name}!")

    def accept_invite(self, friend_name):
        """Accept an invitation and add the friend to the leaderboard."""
        if friend_name in self.leaderboard:
            raise ValueError(f"Player '{friend_name}' is already on the leaderboard.")
        self.add_player(friend_name)
        print(f"{friend_name} has joined the game!")

    def update_score(self, player_name, points):
        """Update the score of a player."""
        if player_name not in self.leaderboard:
            raise ValueError(f"Player '{player_name}' does not exist.")
        if points < 0:
            raise ValueError(f"Cannot add negative points.")
        
        self.leaderboard[player_name] += points
        print(f"{player_name}'s score updated to {self.leaderboard[player_name]}.")

    def get_leaderboard(self):
        """Return the leaderboard sorted by score in descending order."""
        return sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)

# Example usage
if __name__ == "__main__":
    try:
        leaderboard = BigTimeLeaderboard()
        leaderboard.add_player("Alice")
        leaderboard.add_player("Bob")
        
        leaderboard.invite_friend("Alice", "Charlie")
        leaderboard.accept_invite("Charlie")
        
        leaderboard.update_score("Alice", 50)
        leaderboard.update_score("Charlie", 30)
        
        print("Current Leaderboard:")
        for player, score in leaderboard.get_leaderboard():
            print(f"{player}: {score}")

    except ValueError as e:
        print(f"Error: {e}")
```
