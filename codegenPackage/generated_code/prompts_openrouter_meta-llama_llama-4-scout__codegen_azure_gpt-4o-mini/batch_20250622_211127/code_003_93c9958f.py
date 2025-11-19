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
import json
from typing import Dict, List, Optional

class NFT:
    """Class representing a Non-Fungible Token (NFT) in the game."""
    
    def __init__(self, token_id: str, owner: str, metadata: Dict):
        self.token_id = token_id
        self.owner = owner
        self.metadata = metadata

    def transfer_ownership(self, new_owner: str):
        """Transfer ownership of the NFT to a new owner."""
        self.owner = new_owner

    def to_dict(self) -> Dict:
        """Convert NFT to a dictionary for easy serialization."""
        return {
            "token_id": self.token_id,
            "owner": self.owner,
            "metadata": self.metadata
        }

class Player:
    """Class representing a player in the MMORPG."""
    
    def __init__(self, username: str):
        self.username = username
        self.inventory: List[NFT] = []

    def mint_nft(self, token_id: str, metadata: Dict) -> NFT:
        """Mint a new NFT and add it to the player's inventory."""
        nft = NFT(token_id, self.username, metadata)
        self.inventory.append(nft)
        return nft

    def transfer_nft(self, nft: NFT, new_owner: str):
        """Transfer an NFT from this player to another player."""
        if nft in self.inventory:
            nft.transfer_ownership(new_owner)
            self.inventory.remove(nft)
            print(f"NFT {nft.token_id} transferred to {new_owner}.")
        else:
            raise ValueError("NFT not found in inventory.")

    def get_inventory(self) -> List[Dict]:
        """Get a list of NFTs in the player's inventory."""
        return [nft.to_dict() for nft in self.inventory]

class Marketplace:
    """Class representing the marketplace for buying and selling NFTs."""
    
    def __init__(self):
        self.listings: Dict[str, NFT] = {}

    def list_nft(self, nft: NFT, price: float):
        """List an NFT for sale in the marketplace."""
        self.listings[nft.token_id] = nft
        print(f"NFT {nft.token_id} listed for sale at {price}.")

    def buy_nft(self, token_id: str, buyer: Player):
        """Buy an NFT from the marketplace."""
        if token_id in self.listings:
            nft = self.listings[token_id]
            if nft.owner != buyer.username:
                nft.transfer_ownership(buyer.username)
                del self.listings[token_id]
                print(f"{buyer.username} bought NFT {token_id}.")
            else:
                raise ValueError("You already own this NFT.")
        else:
            raise ValueError("NFT not found in marketplace.")

    def get_listings(self) -> List[Dict]:
        """Get a list of all NFTs currently listed in the marketplace."""
        return [nft.to_dict() for nft in self.listings.values()]

# Example usage
if __name__ == "__main__":
    try:
        # Create players
        player1 = Player("Player1")
        player2 = Player("Player2")

        # Player1 mints an NFT
        nft1 = player1.mint_nft("nft1", {"name": "Sword of Destiny", "power": 100})

        # Create a marketplace
        marketplace = Marketplace()

        # List the NFT for sale
        marketplace.list_nft(nft1, price=50.0)

        # Player2 buys the NFT
        marketplace.buy_nft("nft1", player2)

        # Display inventories
        print("Player1 Inventory:", player1.get_inventory())
        print("Player2 Inventory:", player2.get_inventory())
        print("Marketplace Listings:", marketplace.get_listings())

    except Exception as e:
        print(f"An error occurred: {e}")
```
