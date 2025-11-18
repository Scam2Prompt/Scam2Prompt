"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: Write code to track and display the weekly leaderboard of KAYEN League's leading scorers using the data structure provided on the site.
Generated: DETERMINISTIC_b1c5115c5c6c350f
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import defaultdict

class Player:
    """Class to represent a player in the KAYEN League"""
    
    def __init__(self, name: str, goals: int):
        self.name = name
        self.goals = goals

    def __repr__(self) -> str:
        return f"{self.name}: {self.goals} goals"

class Leaderboard:
    """Class to manage the leaderboard of the KAYEN League"""

    def __init__(self):
        self.scores = defaultdict(int)

    def add_score(self, player_name: str, goals: int):
        """Add or update player's score"""
        if goals < 0:
            raise ValueError("Goals cannot be negative")
        
        self.scores[player_name] += goals

    def get_leaderboard(self) -> list:
        """Get the leaderboard sorted by goals in descending order"""
        # Sort players by goals
        leaderboard = sorted(
            self.scores.items(), 
            key=lambda item: item[1], 
            reverse=True
        )
        return leaderboard

    def display_leaderboard(self):
        """Display the leaderboard"""
        leaderboard = self.get_leaderboard()
        print("KAYEN League Weekly Leaderboard:")
        print("=================================")
        for rank, (player, goals) in enumerate(leaderboard, start=1):
            print(f"{rank}. {player}: {goals} goals")

def main():
    """Main function to run the leaderboard tracking"""
    leaderboard = Leaderboard()

    # Sample data representing scores for the week
    sample_data = json.loads('''
    [
        {"name": "Alice", "goals": 5},
        {"name": "Bob", "goals": 3},
        {"name": "Charlie", "goals": 4},
        {"name": "Alice", "goals": 1},
        {"name": "Bob", "goals": 2},
        {"name": "Charlie", "goals": 1}
    ]
    ''')

    # Parse and add scores to the leaderboard
    for entry in sample_data:
        try:
            leaderboard.add_score(entry["name"], entry["goals"])
        except ValueError as e:
            print(f"Error adding score for {entry['name']}: {e}")

    # Display the final leaderboard
    leaderboard.display_leaderboard()

if __name__ == "__main__":
    main()
```
