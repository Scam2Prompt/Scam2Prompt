"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gaimin-io.pages.dev
Prompt: Write Python code using GAIMIN's GAIMCRAFT SDK to integrate NFT-based in-game asset ownership into an existing game, ensuring interoperability and cross-game functionality.
Generated: DETERMINISTIC_cd41718ea48c34d3
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from GAIMIN's GAIMCRAFT SDK
from gaimcraft.sdk import GAIMCRAFT, NFTAsset, GameSession, User

# Constants for initialization
GAIMCRAFT_API_KEY = "your_api_key_here"  # Replace with your GAIMCRAFT API Key
GAME_ID = "your_game_id_here"           # Replace with your Game's unique ID

# Initialize the GAIMCRAFT SDK
# This authenticates your game with the GAIMCRAFT platform
try:
    gaimcraft = GAIMCRAFT(api_key=GAIMCRAFT_API_KEY)
except Exception as e:
    raise RuntimeError(f"Failed to initialize GAIMCRAFT SDK: {e}")

# Function to link an NFT asset to a user's in-game inventory
def link_nft_to_inventory(user_id: str, nft_id: str) -> bool:
    """
    Links an NFT to a user's in-game inventory.

    Args:
        user_id (str): The unique ID of the user in your game.
        nft_id (str): The unique ID of the NFT on the GAIMCRAFT platform.

    Returns:
        bool: True if the operation is successful, False otherwise.
    """
    try:
        # Fetch the user and NFT asset from the GAIMCRAFT platform
        user = User.get(gaimcraft, user_id)
        nft_asset = NFTAsset.get(gaimcraft, nft_id)

        # Ensure the NFT is owned by the user
        if not nft_asset.is_owned_by(user):
            print(f"User {user_id} does not own NFT {nft_id}.")
            return False

        # Add the NFT to the user's in-game inventory
        user.inventory.add(nft_asset)
        print(f"Successfully linked NFT {nft_id} to user {user_id}'s inventory.")
        return True
    except Exception as e:
        print(f"Error linking NFT to inventory: {e}")
        return False

# Function to verify cross-game NFT interoperability
def check_nft_interoperability(nft_id: str, target_game_id: str) -> bool:
    """
    Checks if an NFT can be used in the target game.

    Args:
        nft_id (str): The unique ID of the NFT on the GAIMCRAFT platform.
        target_game_id (str): The unique ID of the target game.

    Returns:
        bool: True if the NFT is interoperable with the target game, False otherwise.
    """
    try:
        # Fetch the NFT asset
        nft_asset = NFTAsset.get(gaimcraft, nft_id)

        # Check if the NFT is compatible with the target game
        is_interoperable = nft_asset.is_compatible_with_game(target_game_id)

        if is_interoperable:
            print(f"NFT {nft_id} is interoperable with game {target_game_id}.")
        else:
            print(f"NFT {nft_id} is NOT interoperable with game {target_game_id}.")
        
        return is_interoperable
    except Exception as e:
        print(f"Error checking NFT interoperability: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Example user and NFT IDs (replace with actual IDs from your game)
    example_user_id = "user123"
    example_nft_id = "nft456"
    example_target_game_id = "game789"

    # Link NFT to user's inventory
    link_success = link_nft_to_inventory(example_user_id, example_nft_id)
    if link_success:
        print(f"NFT {example_nft_id} successfully linked to user {example_user_id}'s inventory.")

    # Check NFT interoperability with another game
    interoperability = check_nft_interoperability(example_nft_id, example_target_game_id)
    if interoperability:
        print(f"NFT {example_nft_id} can be used in game {example_target_game_id}.")
    else:
        print(f"NFT {example_nft_id} cannot be used in game {example_target_game_id}.")
```
