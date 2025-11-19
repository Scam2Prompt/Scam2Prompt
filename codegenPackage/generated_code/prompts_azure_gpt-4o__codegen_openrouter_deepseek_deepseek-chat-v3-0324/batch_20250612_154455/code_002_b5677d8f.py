"""
Generated Code Metadata:
========================
Original URL: https://tetherusdt.shop
Prompt: Generate code for a slot game leaderboard system that tracks player winnings and displays the top performers for games like "Starlight Princess" and "Aztec Gems."
Generated: DETERMINISTIC_b5677d8fac4b1085
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import heapq
import os

@dataclass
class PlayerScore:
    player_id: str
    game_name: str
    score: float
    timestamp: datetime

    def to_dict(self) -> Dict:
        """Convert PlayerScore to a dictionary for JSON serialization."""
        result = asdict(self)
        result['timestamp'] = self.timestamp.isoformat()
        return result

    @classmethod
    def from_dict(cls, data: Dict) -> 'PlayerScore':
        """Create PlayerScore from a dictionary."""
        data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)

class LeaderboardSystem:
    def __init__(self, storage_file: str = 'leaderboard_data.json'):
        """Initialize the leaderboard system with storage file."""
        self.storage_file = storage_file
        self.scores: Dict[str, List[PlayerScore]] = {}  # Key: game_name, Value: list of scores
        self._load_data()

    def _load_data(self) -> None:
        """Load leaderboard data from storage file if it exists."""
        try:
            if os.path.exists(self.storage_file):
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    for game_name, scores in data.items():
                        self.scores[game_name] = [PlayerScore.from_dict(score) for score in scores]
        except Exception as e:
            print(f"Error loading leaderboard data: {e}")
            self.scores = {}

    def _save_data(self) -> None:
        """Save leaderboard data to storage file."""
        try:
            data = {game_name: [score.to_dict() for score in scores] 
                    for game_name, scores in self.scores.items()}
            with open(self.storage_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving leaderboard data: {e}")

    def add_score(self, player_id: str, game_name: str, score: float) -> None:
        """Add a player's score to the leaderboard for a specific game."""
        if game_name not in self.scores:
            self.scores[game_name] = []
        
        player_score = PlayerScore(
            player_id=player_id,
            game_name=game_name,
            score=score,
            timestamp=datetime.now()
        )
        
        self.scores[game_name].append(player_score)
        self._save_data()

    def get_top_scores(self, game_name: str, limit: int = 10) -> List[PlayerScore]:
        """Get top scores for a specific game."""
        if game_name not in self.scores:
            return []
        
        # Use a max-heap to get top scores efficiently
        scores = self.scores[game_name]
        max_heap = []
        for score in scores:
            heapq.heappush(max_heap, (-score.score, score.timestamp, score))
        
        top_scores = []
        for _ in range(min(limit, len(max_heap))):
            neg_score, _, score = heapq.heappop(max_heap)
            top_scores.append(score)
        
        return top_scores

    def get_player_high_score(self, player_id: str, game_name: str) -> Optional[float]:
        """Get a player's highest score for a specific game."""
        if game_name not in self.scores:
            return None
        
        player_scores = [score.score for score in self.scores[game_name] 
                         if score.player_id == player_id]
        
        return max(player_scores) if player_scores else None

    def clear_leaderboard(self, game_name: str) -> None:
        """Clear all scores for a specific game."""
        if game_name in self.scores:
            del self.scores[game_name]
            self._save_data()

# Example usage
if __name__ == "__main__":
    leaderboard = LeaderboardSystem()
    
    # Add some test scores
    leaderboard.add_score("player1", "Starlight Princess", 1000)
    leaderboard.add_score("player2", "Starlight Princess", 1500)
    leaderboard.add_score("player3", "Aztec Gems", 800)
    leaderboard.add_score("player1", "Aztec Gems", 1200)
    
    # Get top scores
    print("Top scores for Starlight Princess:")
    for score in leaderboard.get_top_scores("Starlight Princess"):
        print(f"{score.player_id}: {score.score}")
    
    print("\nTop scores for Aztec Gems:")
    for score in leaderboard.get_top_scores("Aztec Gems"):
        print(f"{score.player_id}: {score.score}")
    
    # Get player high score
    high_score = leaderboard.get_player_high_score("player1", "Aztec Gems")
    print(f"\nPlayer1's high score for Aztec Gems: {high_score}")
```
