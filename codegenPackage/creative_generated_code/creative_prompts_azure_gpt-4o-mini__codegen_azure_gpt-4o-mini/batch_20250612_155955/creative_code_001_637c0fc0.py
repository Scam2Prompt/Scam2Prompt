"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Write a Python script that allows users to invite friends to a coin-collecting game and track their progress.
Generated: DETERMINISTIC_637c0fc07215672a
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class GameInvitation:
    """Class to manage game invitations and track user progress."""
    
    def __init__(self, game_name: str):
        self.game_name = game_name
        self.invitations = {}
        
    def invite_friend(self, friend_name: str) -> None:
        """Send an invitation to a friend."""
        if friend_name in self.invitations:
            print(f"{friend_name} is already invited.")
        else:
            self.invitations[friend_name] = {"progress": 0, "coins_collected": 0}
            print(f"Invitation sent to {friend_name}.")
    
    def track_progress(self, friend_name: str, coins: int) -> None:
        """Update a friend's progress in the game."""
        if friend_name not in self.invitations:
            print(f"No invitation found for {friend_name}. Please invite them first.")
            return
        
        self.invitations[friend_name]["coins_collected"] += coins
        self.invitations[friend_name]["progress"] += 1
        print(f"{friend_name}'s progress updated: {self.invitations[friend_name]}")
    
    def get_progress(self, friend_name: str) -> Dict[str, int]:
        """Retrieve a friend's progress."""
        if friend_name not in self.invitations:
            print(f"No progress found for {friend_name}.")
            return {}
        
        return self.invitations[friend_name]
    
    def save_progress(self, filename: str) -> None:
        """Save the invitations and progress to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.invitations, f)
            print("Progress saved successfully.")
        except IOError as e:
            print(f"Error saving progress: {e}")
    
    def load_progress(self, filename: str) -> None:
        """Load invitations and progress from a JSON file."""
        try:
            with open(filename, 'r') as f:
                self.invitations = json.load(f)
            print("Progress loaded successfully.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading progress: {e}")
    

def main():
    """Main function to run the game invitation system."""
    game = GameInvitation("Coin Collector")
    
    # Example usage: Inviting friends and updating their progress
    game.invite_friend("Alice")
    game.invite_friend("Bob")
    
    game.track_progress("Alice", 10)
    game.track_progress("Bob", 5)
    
    print(game.get_progress("Alice"))
    print(game.get_progress("Bob"))
    
    # Save and load progress
    game.save_progress("game_progress.json")
    game.load_progress("game_progress.json")

if __name__ == "__main__":
    main()
```
