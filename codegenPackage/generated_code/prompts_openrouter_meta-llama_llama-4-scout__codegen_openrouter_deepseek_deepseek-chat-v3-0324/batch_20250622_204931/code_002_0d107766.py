"""
Generated Code Metadata:
========================
Original URL: https://doglibretoken.web.app
Prompt: Develop a basic implementation of a walk-to-earn or play-to-earn gaming mechanism using Python, inspired by DogLibre's gamified NFTs and metaverse plans.
Generated: DETERMINISTIC_0d1077661140c057
Batch ID: 20250622_204931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from dataclasses import dataclass
from typing import Dict, List, Optional
from hashlib import sha256
import uuid
import os

# Error classes
class InsufficientBalanceError(Exception):
    pass

class NFTNotFoundError(Exception):
    pass

class InvalidStepCountError(Exception):
    pass

@dataclass
class NFT:
    """Represents a gamified NFT with walk-to-earn capabilities."""
    id: str
    name: str
    base_earn_rate: float  # Tokens earned per step
    stamina: int  # Max steps per day
    current_stamina: int  # Remaining steps for today
    last_used: float  # Timestamp of last use

@dataclass
class Player:
    """Represents a player in the walk-to-earn game."""
    id: str
    name: str
    token_balance: float
    owned_nfts: Dict[str, NFT]  # NFT ID -> NFT object

class WalkToEarnGame:
    """Main game class implementing walk-to-earn mechanics."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.nft_templates: Dict[str, Dict] = {}  # Template data for NFTs
        self._load_nft_templates()
        
    def _load_nft_templates(self):
        """Load NFT templates from a JSON file or create default ones."""
        try:
            if os.path.exists('nft_templates.json'):
                with open('nft_templates.json', 'r') as f:
                    self.nft_templates = json.load(f)
            else:
                # Default templates if file doesn't exist
                self.nft_templates = {
                    "common": {
                        "name": "Common Walker",
                        "base_earn_rate": 0.01,
                        "stamina": 5000
                    },
                    "rare": {
                        "name": "Rare Runner",
                        "base_earn_rate": 0.03,
                        "stamina": 7500
                    },
                    "legendary": {
                        "name": "Legendary Sprinter",
                        "base_earn_rate": 0.05,
                        "stamina": 10000
                    }
                }
                self._save_nft_templates()
        except Exception as e:
            print(f"Error loading NFT templates: {e}")
            raise

    def _save_nft_templates(self):
        """Save NFT templates to a JSON file."""
        try:
            with open('nft_templates.json', 'w') as f:
                json.dump(self.nft_templates, f, indent=2)
        except Exception as e:
            print(f"Error saving NFT templates: {e}")
            raise

    def register_player(self, name: str) -> Player:
        """Register a new player with an initial balance."""
        player_id = str(uuid.uuid4())
        new_player = Player(
            id=player_id,
            name=name,
            token_balance=0.0,
            owned_nfts={}
        )
        self.players[player_id] = new_player
        return new_player

    def mint_nft(self, player_id: str, nft_type: str) -> NFT:
        """Mint a new NFT for a player based on template type."""
        if player_id not in self.players:
            raise ValueError("Player not found")
        
        if nft_type not in self.nft_templates:
            raise ValueError("Invalid NFT type")
        
        template = self.nft_templates[nft_type]
        nft_id = sha256(str(uuid.uuid4()).encode()).hexdigest()
        
        new_nft = NFT(
            id=nft_id,
            name=template['name'],
            base_earn_rate=template['base_earn_rate'],
            stamina=template['stamina'],
            current_stamina=template['stamina'],
            last_used=0.0
        )
        
        self.players[player_id].owned_nfts[nft_id] = new_nft
        return new_nft

    def _reset_stamina_if_needed(self, nft: NFT):
        """Reset NFT stamina if a new day has passed."""
        current_time = time.time()
        last_reset = time.localtime(nft.last_used)
        current_date = time.localtime(current_time)
        
        if (last_reset.tm_year != current_date.tm_year or
            last_reset.tm_mon != current_date.tm_mon or
            last_reset.tm_mday != current_date.tm_mday):
            nft.current_stamina = nft.stamina

    def walk_with_nft(self, player_id: str, nft_id: str, steps: int) -> float:
        """
        Walk with an NFT to earn tokens.
        Returns the amount of tokens earned.
        """
        if steps <= 0:
            raise InvalidStepCountError("Steps must be positive")
            
        try:
            player = self.players[player_id]
            nft = player.owned_nfts.get(nft_id)
            
            if not nft:
                raise NFTNotFoundError("NFT not found in player's collection")
            
            self._reset_stamina_if_needed(nft)
            
            usable_steps = min(steps, nft.current_stamina)
            if usable_steps <= 0:
                return 0.0
                
            tokens_earned = usable_steps * nft.base_earn_rate
            player.token_balance += tokens_earned
            nft.current_stamina -= usable_steps
            nft.last_used = time.time()
            
            return tokens_earned
        except KeyError:
            raise ValueError("Player not found")

    def transfer_nft(self, from_player_id: str, to_player_id: str, nft_id: str) -> None:
        """Transfer an NFT between players."""
        try:
            from_player = self.players[from_player_id]
            to_player = self.players[to_player_id]
            
            if nft_id not in from_player.owned_nfts:
                raise NFTNotFoundError("NFT not found in sender's collection")
                
            nft = from_player.owned_nfts.pop(nft_id)
            to_player.owned_nfts[nft_id] = nft
        except KeyError:
            raise ValueError("Player not found")

    def get_player_balance(self, player_id: str) -> float:
        """Get a player's token balance."""
        try:
            return self.players[player_id].token_balance
        except KeyError:
            raise ValueError("Player not found")

    def get_player_nfts(self, player_id: str) -> List[NFT]:
        """Get a list of NFTs owned by a player."""
        try:
            return list(self.players[player_id].owned_nfts.values())
        except KeyError:
            raise ValueError("Player not found")

    def spend_tokens(self, player_id: str, amount: float) -> None:
        """Spend tokens from a player's balance."""
        try:
            player = self.players[player_id]
            if player.token_balance < amount:
                raise InsufficientBalanceError("Not enough tokens")
            player.token_balance -= amount
        except KeyError:
            raise ValueError("Player not found")

# Example usage
if __name__ == "__main__":
    game = WalkToEarnGame()
    
    # Register players
    alice = game.register_player("Alice")
    bob = game.register_player("Bob")
    
    # Mint NFTs
    alice_nft = game.mint_nft(alice.id, "rare")
    bob_nft = game.mint_nft(bob.id, "common")
    
    # Walk to earn
    alice_earned = game.walk_with_nft(alice.id, alice_nft.id, 3000)
    print(f"Alice earned {alice_earned} tokens")
    
    # Check balance
    print(f"Alice's balance: {game.get_player_balance(alice.id)}")
    
    # Transfer NFT
    game.transfer_nft(alice.id, bob.id, alice_nft.id)
    print(f"Bob now has {len(game.get_player_nfts(bob.id))} NFTs")
```
