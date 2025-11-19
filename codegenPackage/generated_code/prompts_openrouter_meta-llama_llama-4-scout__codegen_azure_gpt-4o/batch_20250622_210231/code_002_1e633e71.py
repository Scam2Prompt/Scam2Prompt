"""
Generated Code Metadata:
========================
Original URL: https://tabi-9md.pages.dev
Prompt: Generate a Python code example for a simple pirate-themed NFT trading platform, using keywords like "Pirate Island" and "booties for gold".
Generated: DETERMINISTIC_1e633e71da3bd031
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import json
from typing import List, Dict

# Pirate-themed NFT trading platform: Pirate Island

class NFT:
    """
    Represents a Pirate-themed NFT.
    """
    def __init__(self, name: str, description: str, owner: str, value_in_gold: int):
        self.id = str(uuid.uuid4())  # Unique identifier for the NFT
        self.name = name  # Name of the NFT
        self.description = description  # Description of the NFT
        self.owner = owner  # Current owner of the NFT
        self.value_in_gold = value_in_gold  # Value of the NFT in gold

    def to_dict(self) -> Dict:
        """
        Converts the NFT object to a dictionary for serialization.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "owner": self.owner,
            "value_in_gold": self.value_in_gold
        }


class PirateIsland:
    """
    Represents the Pirate Island NFT trading platform.
    """
    def __init__(self):
        self.nfts = []  # List of all NFTs on the platform
        self.users = {}  # Dictionary of users and their gold balance

    def register_user(self, username: str, initial_gold: int):
        """
        Registers a new user with an initial gold balance.
        """
        if username in self.users:
            raise ValueError(f"User '{username}' already exists!")
        self.users[username] = initial_gold
        print(f"Welcome aboard, {username}! You have {initial_gold} gold.")

    def mint_nft(self, name: str, description: str, owner: str, value_in_gold: int):
        """
        Mints a new NFT and assigns it to the owner.
        """
        if owner not in self.users:
            raise ValueError(f"Owner '{owner}' is not registered!")
        new_nft = NFT(name, description, owner, value_in_gold)
        self.nfts.append(new_nft)
        print(f"Ahoy! New NFT '{name}' minted for {owner}.")
        return new_nft

    def trade_nft(self, nft_id: str, buyer: str):
        """
        Facilitates the trade of an NFT between the current owner and a buyer.
        """
        if buyer not in self.users:
            raise ValueError(f"Buyer '{buyer}' is not registered!")

        # Find the NFT by ID
        nft = next((nft for nft in self.nfts if nft.id == nft_id), None)
        if not nft:
            raise ValueError(f"NFT with ID '{nft_id}' not found!")

        if nft.owner == buyer:
            raise ValueError(f"Buyer '{buyer}' already owns this NFT!")

        if self.users[buyer] < nft.value_in_gold:
            raise ValueError(f"Buyer '{buyer}' does not have enough gold!")

        # Perform the trade
        self.users[buyer] -= nft.value_in_gold
        self.users[nft.owner] += nft.value_in_gold
        print(f"Trade successful! {buyer} bought '{nft.name}' from {nft.owner} for {nft.value_in_gold} gold.")
        nft.owner = buyer

    def list_nfts(self) -> List[Dict]:
        """
        Lists all NFTs on the platform.
        """
        return [nft.to_dict() for nft in self.nfts]

    def user_balance(self, username: str) -> int:
        """
        Returns the gold balance of a user.
        """
        if username not in self.users:
            raise ValueError(f"User '{username}' is not registered!")
        return self.users[username]


# Example usage
if __name__ == "__main__":
    # Initialize the Pirate Island platform
    pirate_island = PirateIsland()

    # Register users
    pirate_island.register_user("CaptainJack", 100)
    pirate_island.register_user("BlackBeard", 200)

    # Mint NFTs
    nft1 = pirate_island.mint_nft("Golden Compass", "A rare compass that points to treasure.", "CaptainJack", 50)
    nft2 = pirate_island.mint_nft("Silver Sword", "A sharp blade forged from silver.", "BlackBeard", 75)

    # List NFTs
    print("Available NFTs:")
    print(json.dumps(pirate_island.list_nfts(), indent=4))

    # Trade NFTs
    pirate_island.trade_nft(nft1.id, "BlackBeard")

    # Check user balances
    print(f"CaptainJack's balance: {pirate_island.user_balance('CaptainJack')} gold")
    print(f"BlackBeard's balance: {pirate_island.user_balance('BlackBeard')} gold")

    # List NFTs after trade
    print("NFTs after trade:")
    print(json.dumps(pirate_island.list_nfts(), indent=4))
```
