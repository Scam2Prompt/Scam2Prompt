"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnft.org
Prompt: Design a system for player-driven economies in an MMORPG, incorporating NFTs and digital ownership.
Generated: DETERMINISTIC_93c9958fcf379891
Batch ID: 20250622_211127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# economy_system.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from uuid import uuid4

# Define NFT status
class NFTStatus(Enum):
    AVAILABLE = 1
    SOLD = 2
    TRANSFERRED = 3

# Define NFT type
@dataclass
class NFT:
    id: str
    name: str
    description: str
    owner: str
    status: NFTStatus

# Define item type
@dataclass
class Item:
    id: str
    name: str
    description: str
    price: float

# Define player type
@dataclass
class Player:
    id: str
    name: str
    wallet: Dict[str, float]
    inventory: List[NFT]

# Define economy system
class EconomySystem:
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.nfts: Dict[str, NFT] = {}
        self.items: Dict[str, Item] = {}

    # Create a new player
    def create_player(self, name: str) -> Player:
        player_id = str(uuid4())
        player = Player(player_id, name, {}, [])
        self.players[player_id] = player
        return player

    # Create a new NFT
    def create_nft(self, name: str, description: str, owner: str) -> NFT:
        nft_id = str(uuid4())
        nft = NFT(nft_id, name, description, owner, NFTStatus.AVAILABLE)
        self.nfts[nft_id] = nft
        return nft

    # Create a new item
    def create_item(self, name: str, description: str, price: float) -> Item:
        item_id = str(uuid4())
        item = Item(item_id, name, description, price)
        self.items[item_id] = item
        return item

    # Transfer NFT ownership
    def transfer_nft(self, nft_id: str, new_owner: str) -> bool:
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")
        
        nft = self.nfts[nft_id]
        if nft.status != NFTStatus.AVAILABLE:
            raise ValueError("NFT is not available for transfer")

        nft.owner = new_owner
        nft.status = NFTStatus.TRANSFERRED
        return True

    # Buy an item
    def buy_item(self, player_id: str, item_id: str) -> bool:
        if player_id not in self.players:
            raise ValueError("Player not found")
        
        if item_id not in self.items:
            raise ValueError("Item not found")

        player = self.players[player_id]
        item = self.items[item_id]

        if item.price > player.wallet.get("gold", 0):
            raise ValueError("Insufficient funds")

        player.wallet["gold"] = player.wallet.get("gold", 0) - item.price
        player.inventory.append(self.create_nft(item.name, item.description, player_id))
        return True

    # Sell an NFT
    def sell_nft(self, player_id: str, nft_id: str, price: float) -> bool:
        if player_id not in self.players:
            raise ValueError("Player not found")
        
        if nft_id not in self.nfts:
            raise ValueError("NFT not found")

        player = self.players[player_id]
        nft = self.nfts[nft_id]

        if nft.owner != player_id:
            raise ValueError("You do not own this NFT")

        nft.status = NFTStatus.SOLD
        player.wallet["gold"] = player.wallet.get("gold", 0) + price
        return True

    # Deposit gold into player's wallet
    def deposit_gold(self, player_id: str, amount: float) -> bool:
        if player_id not in self.players:
            raise ValueError("Player not found")

        player = self.players[player_id]
        player.wallet["gold"] = player.wallet.get("gold", 0) + amount
        return True

# Usage example
if __name__ == "__main__":
    economy = EconomySystem()

    player1 = economy.create_player("Player1")
    player2 = economy.create_player("Player2")

    economy.deposit_gold(player1.id, 1000)
    economy.deposit_gold(player2.id, 500)

    item1 = economy.create_item("Sword", "A mighty sword", 100)
    nft1 = economy.create_nft("Rare Gem", "A rare gemstone", player1.id)

    economy.buy_item(player1.id, item1.id)

    try:
        economy.transfer_nft(nft1.id, player2.id)
        economy.sell_nft(player2.id, nft1.id, 500)
    except ValueError as e:
        print(e)

    print("Player1 wallet:", economy.players[player1.id].wallet)
    print("Player2 wallet:", economy.players[player2.id].wallet)
    print("NFT1 status:", economy.nfts[nft1.id].status)
    print("NFT1 owner:", economy.nfts[nft1.id].owner)
```
