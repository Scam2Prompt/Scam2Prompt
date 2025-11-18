"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koalamemecoin.pages.dev
Prompt: Generate a play-to-earn game concept where users can earn KoalaKash tokens for completing tasks and competing against other players worldwide.
Generated: DETERMINISTIC_69cd860c437ad608
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

# KoalaKash token system
class KoalaKash:
    def __init__(self):
        # Initialize user balances
        self.balances: Dict[str, int] = {}

    def add_tokens(self, username: str, amount: int):
        """Add tokens to a user's balance."""
        if username not in self.balances:
            self.balances[username] = 0
        self.balances[username] += amount

    def deduct_tokens(self, username: str, amount: int):
        """Deduct tokens from a user's balance."""
        if username not in self.balances or self.balances[username] < amount:
            raise ValueError("Insufficient balance")
        self.balances[username] -= amount

    def get_balance(self, username: str) -> int:
        """Get the token balance of a user."""
        return self.balances.get(username, 0)


# Game system
class PlayToEarnGame:
    def __init__(self):
        self.token_system = KoalaKash()
        self.tasks: List[str] = ["Solve a puzzle", "Win a trivia quiz", "Complete a maze"]
        self.players: List[str] = []

    def register_player(self, username: str):
        """Register a player in the game."""
        if username in self.players:
            raise ValueError("Player already registered")
        self.players.append(username)
        self.token_system.add_tokens(username, 10)  # Initial tokens for joining

    def complete_task(self, username: str):
        """Allow a player to complete a random task."""
        if username not in self.players:
            raise ValueError("Player not registered")

        task = random.choice(self.tasks)
        print(f"{username} is completing the task: {task}")
        reward = random.randint(5, 20)  # Random reward for completing a task
        self.token_system.add_tokens(username, reward)
        return reward

    def compete(self, player1: str, player2: str):
        """Simulate a competition between two players."""
        if player1 not in self.players or player2 not in self.players:
            raise ValueError("Both players must be registered")

        # Randomize competition winner
        winner = random.choice([player1, player2])
        reward = 50  # Fixed reward for winning a competition
        self.token_system.add_tokens(winner, reward)
        print(f"{winner} wins the competition and earns {reward} KoalaKash tokens!")
        return winner

    def get_leaderboard(self) -> List[Dict[str, int]]:
        """Generate a leaderboard of players based on their token balances."""
        leaderboard = [{"username": username, "balance": self.token_system.get_balance(username)} for username in self.players]
        leaderboard.sort(key=lambda x: x["balance"], reverse=True)
        return leaderboard


# Example usage
if __name__ == "__main__":
    game = PlayToEarnGame()

    # Register players
    game.register_player("Alice")
    game.register_player("Bob")
    game.register_player("Charlie")

    # Players complete tasks
    print(f"Alice earned {game.complete_task('Alice')} tokens!")
    print(f"Bob earned {game.complete_task('Bob')} tokens!")
    print(f"Charlie earned {game.complete_task('Charlie')} tokens!")

    # Players compete against each other
    game.compete("Alice", "Bob")

    # Display leaderboard
    print("Leaderboard:")
    for entry in game.get_leaderboard():
        print(f"{entry['username']}: {entry['balance']} KoalaKash tokens")
```
