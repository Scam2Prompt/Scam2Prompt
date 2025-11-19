"""
Generated Code Metadata:
========================
Original URL: https://flipperzerobase-presales.pages.dev
Prompt: "Design a treasure hunt game with hidden objects and NFT rewards, using Flipper Zero's game mechanics as a reference."
Generated: DETERMINISTIC_86ccc2311bc07489
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib
import json
from datetime import datetime
from typing import List, Dict, Optional

class NFT:
    """Represents an NFT reward."""
    def __init__(self, token_id: str, metadata: Dict):
        self.token_id = token_id
        self.metadata = metadata

    def to_dict(self) -> Dict:
        """Convert NFT to dictionary."""
        return {
            'token_id': self.token_id,
            'metadata': self.metadata
        }

class TreasureHuntGame:
    """Main game class for the treasure hunt."""
    def __init__(self):
        self.players = {}
        self.treasures = []
        self.nft_rewards = []
        self.game_state = {}
        self.initialize_game()

    def initialize_game(self):
        """Initialize game with default treasures and NFTs."""
        # Generate some sample treasures
        self.treasures = [
            {"id": 1, "name": "Golden Key", "location": (10, 20), "found": False},
            {"id": 2, "name": "Ancient Coin", "location": (30, 40), "found": False},
            {"id": 3, "name": "Mysterious Map", "location": (50, 60), "found": False}
        ]

        # Generate some sample NFT rewards
        self.nft_rewards = [
            NFT(
                token_id="1",
                metadata={
                    "name": "Treasure Hunter Badge",
                    "description": "Awarded for finding your first treasure",
                    "image": "ipfs://QmX1..."
                }
            ),
            NFT(
                token_id="2",
                metadata={
                    "name": "Master Explorer",
                    "description": "Awarded for finding all treasures",
                    "image": "ipfs://QmX2..."
                }
            )
        ]

    def register_player(self, player_id: str) -> bool:
        """Register a new player."""
        if player_id in self.players:
            return False
        
        self.players[player_id] = {
            "found_treasures": [],
            "nfts": [],
            "last_location": (0, 0)
        }
        return True

    def check_location(self, player_id: str, location: tuple) -> Optional[Dict]:
        """Check if player found a treasure at given location."""
        if player_id not in self.players:
            return None

        self.players[player_id]["last_location"] = location

        for treasure in self.treasures:
            if not treasure["found"] and treasure["location"] == location:
                treasure["found"] = True
                self.players[player_id]["found_treasures"].append(treasure["id"])
                
                # Award NFT if conditions met
                self._check_nft_rewards(player_id)
                
                return treasure
        return None

    def _check_nft_rewards(self, player_id: str):
        """Check and award NFT rewards based on player progress."""
        found_count = len(self.players[player_id]["found_treasures"])
        
        if found_count == 1 and len(self.players[player_id]["nfts"]) == 0:
            # Award first treasure NFT
            self.players[player_id]["nfts"].append(self.nft_rewards[0].to_dict())
        
        if found_count == len(self.treasures):
            # Award all treasures NFT
            self.players[player_id]["nfts"].append(self.nft_rewards[1].to_dict())

    def get_player_state(self, player_id: str) -> Optional[Dict]:
        """Get current player state."""
        if player_id not in self.players:
            return None

        return {
            "found_treasures": self.players[player_id]["found_treasures"],
            "nfts": self.players[player_id]["nfts"],
            "last_location": self.players[player_id]["last_location"]
        }

    def generate_random_treasure(self) -> Dict:
        """Generate a new random treasure location."""
        new_id = max(t["id"] for t in self.treasures) + 1 if self.treasures else 1
        new_treasure = {
            "id": new_id,
            "name": f"Random Treasure {new_id}",
            "location": (random.randint(0, 100), random.randint(0, 100)),
            "found": False
        }
        self.treasures.append(new_treasure)
        return new_treasure

    def save_game_state(self, filename: str = "game_state.json") -> bool:
        """Save current game state to file."""
        try:
            state = {
                "players": self.players,
                "treasures": self.treasures,
                "timestamp": datetime.now().isoformat()
            }
            with open(filename, 'w') as f:
                json.dump(state, f)
            return True
        except Exception as e:
            print(f"Error saving game state: {e}")
            return False

    def load_game_state(self, filename: str = "game_state.json") -> bool:
        """Load game state from file."""
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
                self.players = state.get("players", {})
                self.treasures = state.get("treasures", [])
            return True
        except FileNotFoundError:
            print("No saved game state found.")
            return False
        except Exception as e:
            print(f"Error loading game state: {e}")
            return False

# Example usage
if __name__ == "__main__":
    game = TreasureHuntGame()
    
    # Register players
    game.register_player("player1")
    game.register_player("player2")
    
    # Simulate player movements
    player1_location = (10, 20)  # Golden Key location
    found = game.check_location("player1", player1_location)
    
    if found:
        print(f"Player1 found: {found['name']}")
        print("Player1 NFTs:", game.get_player_state("player1")["nfts"])
    
    # Save game state
    game.save_game_state()
```
