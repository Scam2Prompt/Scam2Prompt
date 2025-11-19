"""
Generated Code Metadata:
========================
Original URL: https://atocha.io
Prompt: "Propose a puzzle game idea for Atocha protocol, incorporating NFTs and a treasure hunt mechanism, similar to NEAR2ATO Treasure Hunt."
Generated: DETERMINISTIC_8692048dd058397d
Batch ID: 20250622_210718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from typing import List, Dict, Any

class NFT:
    """Class representing a Non-Fungible Token (NFT) in the game."""
    
    def __init__(self, token_id: str, owner: str, metadata: Dict[str, Any]):
        self.token_id = token_id
        self.owner = owner
        self.metadata = metadata

    def __repr__(self):
        return f"NFT(token_id={self.token_id}, owner={self.owner}, metadata={self.metadata})"


class TreasureHuntGame:
    """Class representing the Treasure Hunt Game incorporating NFTs."""
    
    def __init__(self):
        self.nfts: List[NFT] = []
        self.treasures: List[str] = []
        self.players: Dict[str, List[NFT]] = {}

    def create_nft(self, token_id: str, owner: str, metadata: Dict[str, Any]) -> NFT:
        """Create a new NFT and add it to the game."""
        nft = NFT(token_id, owner, metadata)
        self.nfts.append(nft)
        return nft

    def add_treasure(self, treasure: str):
        """Add a treasure to the game."""
        self.treasures.append(treasure)

    def register_player(self, player_id: str):
        """Register a new player in the game."""
        if player_id not in self.players:
            self.players[player_id] = []
        else:
            raise ValueError(f"Player {player_id} is already registered.")

    def assign_nft_to_player(self, player_id: str, token_id: str):
        """Assign an NFT to a player."""
        if player_id not in self.players:
            raise ValueError(f"Player {player_id} is not registered.")
        
        nft = next((nft for nft in self.nfts if nft.token_id == token_id), None)
        if nft is None:
            raise ValueError(f"NFT with token_id {token_id} does not exist.")
        
        nft.owner = player_id
        self.players[player_id].append(nft)

    def start_treasure_hunt(self, player_id: str) -> str:
        """Start a treasure hunt for a player and return a random treasure."""
        if player_id not in self.players:
            raise ValueError(f"Player {player_id} is not registered.")
        
        if not self.treasures:
            raise RuntimeError("No treasures available for the hunt.")
        
        treasure = random.choice(self.treasures)
        return treasure

    def save_game_state(self, filename: str):
        """Save the current game state to a JSON file."""
        game_state = {
            "nfts": [nft.__dict__ for nft in self.nfts],
            "treasures": self.treasures,
            "players": {player: [nft.token_id for nft in nfts] for player, nfts in self.players.items()}
        }
        with open(filename, 'w') as f:
            json.dump(game_state, f, indent=4)

    def load_game_state(self, filename: str):
        """Load the game state from a JSON file."""
        try:
            with open(filename, 'r') as f:
                game_state = json.load(f)
                self.nfts = [NFT(**nft) for nft in game_state['nfts']]
                self.treasures = game_state['treasures']
                self.players = {player: [NFT(**nft) for nft in nfts] for player, nfts in game_state['players'].items()}
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the game state file.")


# Example usage
if __name__ == "__main__":
    game = TreasureHuntGame()
    
    # Create NFTs
    nft1 = game.create_nft("nft1", "creator1", {"name": "Golden Key", "description": "Unlocks the treasure."})
    nft2 = game.create_nft("nft2", "creator2", {"name": "Silver Map", "description": "Shows treasure locations."})
    
    # Add treasures
    game.add_treasure("Hidden Cave")
    game.add_treasure("Lost City")
    
    # Register players
    game.register_player("player1")
    
    # Assign NFTs to player
    game.assign_nft_to_player("player1", "nft1")
    
    # Start treasure hunt
    treasure_found = game.start_treasure_hunt("player1")
    print(f"Player found treasure: {treasure_found}")
    
    # Save game state
    game.save_game_state("game_state.json")
    
    # Load game state
    game.load_game_state("game_state.json")
```
