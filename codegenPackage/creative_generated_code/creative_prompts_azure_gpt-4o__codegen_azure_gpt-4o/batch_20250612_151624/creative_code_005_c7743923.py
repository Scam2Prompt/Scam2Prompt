"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blvckparis-nft.pages.dev
Prompt: Suggest tools or libraries for creating a 3D NFT viewer in a metaverse environment like Blvck City, utilizing Unreal Engine or similar technologies.
Generated: DETERMINISTIC_c77439234c42c87f
Batch ID: 20250612_151624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exampleblockchain.com/nft/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a Python script for creating a 3D NFT viewer using Unreal Engine's Python API. Unreal Engine supports Python scripting for automation, asset management, and more within the editor. This script assumes integration with a blockchain to fetch NFT metadata and utilizes the Unreal Engine environment for rendering 3D assets.

```python
import unreal
import requests

# Constants for the blockchain API and NFT metadata
BLOCKCHAIN_API_URL = "https://api.exampleblockchain.com/nft/"
NFT_ASSET_DIRECTORY = "/Game/NFTAssets/"  # Unreal Engine asset directory

def fetch_nft_metadata(nft_id):
    """
    Fetch metadata for a given NFT from the blockchain API.

    Args:
        nft_id (str): The NFT ID or token identifier.

    Returns:
        dict: A dictionary containing metadata (e.g., 3D model URL).
    """
    try:
        response = requests.get(f"{BLOCKCHAIN_API_URL}{nft_id}")
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()
    except requests.exceptions.RequestException as e:
        unreal.log_error(f"Failed to fetch NFT metadata: {e}")
        return None

def import_nft_asset(nft_metadata):
    """
    Import the NFT 3D model into Unreal Engine.

    Args:
        nft_metadata (dict): Metadata containing the 3D model's URL.

    Returns:
        str: The path to the imported asset in Unreal Engine.
    """
    try:
        model_url = nft_metadata.get("model_url")
        asset_name = nft_metadata.get("name")

        if not model_url or not asset_name:
            unreal.log_error("Invalid NFT metadata or missing required fields.")
            return None

        # Download the 3D model file
        response = requests.get(model_url)
        response.raise_for_status()
        model_file_path = f"/tmp/{asset_name}.fbx"  # Temporary local path

        with open(model_file_path, "wb") as file:
            file.write(response.content)

        # Import the model into Unreal Engine
        task = unreal.AssetImportTask()
        task.set_editor_property("filename", model_file_path)
        task.set_editor_property("destination_path", NFT_ASSET_DIRECTORY)
        task.set_editor_property("automated", True)

        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

        if task.imported_object_paths:
            unreal.log(f"Successfully imported NFT asset: {task.imported_object_paths[0]}")
            return task.imported_object_paths[0]
        else:
            unreal.log_error(f"Failed to import NFT asset: {model_file_path}")
            return None
    except Exception as e:
        unreal.log_error(f"Error during asset import: {e}")
        return None

def display_nft_in_world(asset_path):
    """
    Display the imported NFT asset in the Unreal Engine world.

    Args:
        asset_path (str): Path to the NFT asset in Unreal Engine.
    """
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        if not asset:
            unreal.log_error(f"Unable to load asset from path: {asset_path}")
            return

        # Spawn the asset into the world
        actor_location = unreal.Vector(0.0, 0.0, 100.0)  # Location to spawn
        spawned_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(asset, actor_location)
        if spawned_actor:
            unreal.log(f"Successfully spawned NFT actor: {spawned_actor.get_actor_label()}")
        else:
            unreal.log_error("Failed to spawn NFT actor in the world.")
    except Exception as e:
        unreal.log_error(f"Error during asset spawning: {e}")

def main(nft_id):
    """
    Main function to fetch, import, and display an NFT in Unreal Engine.

    Args:
        nft_id (str): The NFT ID or token identifier.
    """
    nft_metadata = fetch_nft_metadata(nft_id)
    if not nft_metadata:
        return

    asset_path = import_nft_asset(nft_metadata)
    if asset_path:
        display_nft_in_world(asset_path)

# Example usage:
if __name__ == "__main__":
    # Replace with a valid NFT ID
    nft_id = "123456"
    main(nft_id)
```

### Key Notes:
- Replace `BLOCKCHAIN_API_URL` with the actual endpoint for fetching NFT metadata from the blockchain.
- Ensure Unreal Engine Python scripting is enabled and configured in your project.
- This script assumes NFT metadata includes a `model_url` pointing to an `.fbx` file and a `name` field for naming assets. Adjust as necessary based on your actual metadata structure.
