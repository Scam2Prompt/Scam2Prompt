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
# player_economy.py

import json
import uuid
from datetime import datetime
from typing import Dict, List

# Simulated blockchain for NFT ownership
class Blockchain:
    def __init__(self):
        self.chain = []

    def create_nft(self, owner: str, item_name: str, metadata: Dict):
        """
        Create a new NFT and add it to the blockchain.
        """
        nft = {
            "id": str(uuid.uuid4()),
            "owner": owner,
            "item_name": item_name,
            "metadata": metadata,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.chain.append(nft)
        return nft

    def transfer_nft(self, nft_id: str, new_owner: str):
        """
        Transfer ownership of an NFT to a new owner.
        """
        for nft in self.chain:
            if nft["id"] == nft_id:
                nft["owner"] = new_owner
                nft["timestamp"] = datetime.utcnow().isoformat()
                return nft
        raise ValueError("NFT not found")

    def get_nft(self, nft_id: str):
        """
        Retrieve an NFT by its ID.
        """
        for nft in self.chain:
            if nft["id"] == nft_id:
                return nft
        raise ValueError("NFT not found")

    def list_nfts(self, owner: str) -> List[Dict]:
        """
        List all NFTs owned by a specific player.
        """
        return [nft for nft in self.chain if nft["owner"] == owner]


# Player-driven economy system
class PlayerEconomy:
    def __init__(self):
        self.blockchain = Blockchain()
        self.marketplace = []

    def create_item(self, player_id: str, item_name: str, metadata: Dict):
        """
        Create a new item as an NFT and assign ownership to the player.
        """
        return self.blockchain.create_nft(player_id, item_name, metadata)

    def list_item_for_sale(self, nft_id: str, price: float):
        """
        List an NFT for sale in the marketplace.
        """
        nft = self.blockchain.get_nft(nft_id)
        listing = {
            "nft_id": nft_id,
            "item_name": nft["item_name"],
            "owner": nft["owner"],
            "price": price,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.marketplace.append(listing)
        return listing

    def purchase_item(self, buyer_id: str, nft_id: str):
        """
        Purchase an NFT from the marketplace.
        """
        for listing in self.marketplace:
            if listing["nft_id"] == nft_id:
                # Transfer ownership
                self.blockchain.transfer_nft(nft_id, buyer_id)
                # Remove listing from marketplace
                self.marketplace.remove(listing)
                return {
                    "message": "Purchase successful",
                    "nft_id": nft_id,
                    "buyer": buyer_id
                }
        raise ValueError("Item not found in marketplace")

    def view_marketplace(self) -> List[Dict]:
        """
        View all items currently listed for sale in the marketplace.
        """
        return self.marketplace


# Example usage
if __name__ == "__main__":
    # Initialize the player economy system
    economy = PlayerEconomy()

    # Create items (NFTs)
    item1 = economy.create_item("player1", "Sword of Destiny", {"rarity": "legendary", "damage": 100})
    item2 = economy.create_item("player2", "Shield of Valor", {"rarity": "epic", "defense": 50})

    # List items for sale
    economy.list_item_for_sale(item1["id"], 500.0)
    economy.list_item_for_sale(item2["id"], 300.0)

    # View marketplace
    print("Marketplace:", json.dumps(economy.view_marketplace(), indent=4))

    # Purchase an item
    try:
        purchase_result = economy.purchase_item("player3", item1["id"])
        print("Purchase Result:", purchase_result)
    except ValueError as e:
        print("Error:", str(e))

    # View updated marketplace
    print("Updated Marketplace:", json.dumps(economy.view_marketplace(), indent=4))

    # View NFTs owned by player3
    print("Player3 NFTs:", json.dumps(economy.blockchain.list_nfts("player3"), indent=4))
```
