"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearsontheblock.com
Prompt: Generate code to create a custom island on Nifty Island using the platform's in-game toolset, including uploading assets and designing a simple game.
Generated: DETERMINISTIC_109a0a8b0ecae896
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the requested code:

```python
import nifty_island_sdk  # Assuming Nifty Island provides an SDK for development
import os

# Constants
ISLAND_NAME = "MyCustomIsland"
ASSET_FOLDER = "./assets"
GAME_NAME = "SimpleIslandGame"

# Initialize the Nifty Island SDK
try:
    sdk = nifty_island_sdk.initialize(api_key="your_api_key_here")
except nifty_island_sdk.SDKInitializationError as e:
    print(f"Error initializing SDK: {e}")
    exit(1)

# Function to upload assets to Nifty Island
def upload_assets(asset_folder, sdk):
    """
    Uploads assets to Nifty Island from the specified folder.
    """
    try:
        # List all files in the asset folder
        asset_files = [f for f in os.listdir(asset_folder) if os.path.isfile(os.path.join(asset_folder, f))]
        
        # Upload each asset
        for asset_file in asset_files:
            asset_path = os.path.join(asset_folder, asset_file)
            print(f"Uploading asset: {asset_file}")
            sdk.upload_asset(file_path=asset_path)
            print(f"Asset {asset_file} uploaded successfully!")
    except nifty_island_sdk.AssetUploadError as e:
        print(f"Error uploading assets: {e}")
        raise
    except FileNotFoundError as e:
        print(f"Asset folder not found: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error during asset upload: {e}")
        raise

# Function to create a custom island
def create_custom_island(island_name, sdk):
    """
    Creates a custom island with the specified name.
    """
    try:
        print(f"Creating island: {island_name}")
        island = sdk.create_island(name=island_name)
        print(f"Island {island_name} created successfully!")
        return island
    except nifty_island_sdk.IslandCreationError as e:
        print(f"Error creating island: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error during island creation: {e}")
        raise

# Function to design a simple game on the island
def design_simple_game(island, game_name, sdk):
    """
    Designs a simple game on the given island.
    """
    try:
        print(f"Designing game: {game_name}")
        game = sdk.create_game(island_id=island.id, name=game_name)
        
        # Example: Adding objects to the game
        sdk.add_object_to_game(game_id=game.id, object_type="treasure_chest", location={"x": 10, "y": 5, "z": 3})
        sdk.add_object_to_game(game_id=game.id, object_type="tree", location={"x": 20, "y": 10, "z": 0})
        
        # Example: Setting game rules
        sdk.set_game_rules(game_id=game.id, rules={
            "win_condition": "collect_all_treasure",
            "time_limit_seconds": 300
        })
        
        print(f"Game {game_name} designed successfully!")
        return game
    except nifty_island_sdk.GameDesignError as e:
        print(f"Error designing game: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error during game design: {e}")
        raise

# Main script
def main():
    """
    Main script to create a custom island, upload assets, and design a simple game.
    """
    try:
        # Upload assets
        upload_assets(ASSET_FOLDER, sdk)

        # Create island
        island = create_custom_island(ISLAND_NAME, sdk)

        # Design game
        game = design_simple_game(island, GAME_NAME, sdk)

        print("Island and game creation process completed successfully!")
    except Exception as e:
        print(f"An error occurred during the process: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
