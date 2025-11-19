"""
Generated Code Metadata:
========================
Original URL: https://flipperzerobase-presales.pages.dev
Prompt: "Write a Python script to create an NFT minting system for a mobile game, inspired by Flipper Zero's community-driven ecosystem."
Generated: DETERMINISTIC_08b52cf69930752f
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
import uuid
from datetime import datetime
from typing import Dict, Any

# Constants
NFT_STORAGE_PATH = "nft_storage.json"  # File to store minted NFTs
MAX_NFTS = 1000  # Maximum number of NFTs that can be minted
GAME_NAME = "Flipper Zero Mobile Game"  # Game name for NFT metadata

# Error classes
class NFTMintingError(Exception):
    """Custom exception for NFT minting errors."""
    pass

# Helper functions
def load_nft_storage() -> Dict[str, Any]:
    """
    Load the NFT storage file. If it doesn't exist, create an empty storage.
    Returns:
        dict: The NFT storage data.
    """
    if not os.path.exists(NFT_STORAGE_PATH):
        return {"nfts": [], "total_minted": 0}
    try:
        with open(NFT_STORAGE_PATH, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        raise NFTMintingError(f"Failed to load NFT storage: {e}")

def save_nft_storage(data: Dict[str, Any]) -> None:
    """
    Save the NFT storage data to a file.
    Args:
        data (dict): The NFT storage data to save.
    """
    try:
        with open(NFT_STORAGE_PATH, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise NFTMintingError(f"Failed to save NFT storage: {e}")

def generate_nft_metadata(player_id: str, attributes: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate metadata for a new NFT.
    Args:
        player_id (str): The ID of the player minting the NFT.
        attributes (dict): Custom attributes for the NFT.
    Returns:
        dict: The generated NFT metadata.
    """
    return {
        "id": str(uuid.uuid4()),  # Unique identifier for the NFT
        "player_id": player_id,
        "game": GAME_NAME,
        "attributes": attributes,
        "minted_at": datetime.utcnow().isoformat()  # Timestamp of minting
    }

# Main minting function
def mint_nft(player_id: str, attributes: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mint a new NFT for a player.
    Args:
        player_id (str): The ID of the player minting the NFT.
        attributes (dict): Custom attributes for the NFT.
    Returns:
        dict: The minted NFT metadata.
    """
    # Load current NFT storage
    nft_storage = load_nft_storage()

    # Check if the maximum number of NFTs has been reached
    if nft_storage["total_minted"] >= MAX_NFTS:
        raise NFTMintingError("Maximum number of NFTs has been minted.")

    # Generate NFT metadata
    new_nft = generate_nft_metadata(player_id, attributes)

    # Update storage
    nft_storage["nfts"].append(new_nft)
    nft_storage["total_minted"] += 1

    # Save updated storage
    save_nft_storage(nft_storage)

    return new_nft

# Example usage
if __name__ == "__main__":
    try:
        # Example player ID and attributes
        player_id = "player123"
        attributes = {
            "rarity": "legendary",
            "power": 9001,
            "element": "fire"
        }

        # Mint an NFT
        minted_nft = mint_nft(player_id, attributes)
        print("NFT successfully minted!")
        print(json.dumps(minted_nft, indent=4))
    except NFTMintingError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
