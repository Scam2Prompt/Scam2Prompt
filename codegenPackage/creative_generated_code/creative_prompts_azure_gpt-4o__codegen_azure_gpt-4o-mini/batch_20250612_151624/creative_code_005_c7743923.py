"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blvckparis-nft.pages.dev
Prompt: Suggest tools or libraries for creating a 3D NFT viewer in a metaverse environment like Blvck City, utilizing Unreal Engine or similar technologies.
Generated: DETERMINISTIC_c77439234c42c87f
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for creating a 3D NFT viewer
import unreal

# Define a class for the 3D NFT viewer within Unreal Engine
class NFTViewer:
    def __init__(self, asset_path):
        """
        Initializes the NFT viewer with the specified asset path.

        Args:
            asset_path (str): The path to the NFT 3D model asset in the Unreal project.
        """
        self.asset_path = asset_path
        self.nft_actor = None
        self.load_nft_asset()

    def load_nft_asset(self):
        """Load the NFT asset from the specified path."""
        try:
            # Load the NFT model asset
            asset = unreal.EditorAssetLibrary.load_asset(self.asset_path)
            if asset is None:
                raise ValueError(f"Asset not found at path: {self.asset_path}")

            # Spawn the NFT actor in the world
            self.nft_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(asset, unreal.Vector(0, 0, 0))
            unreal.EditorLevelLibrary.set_actor_rotation(self.nft_actor, unreal.Rotator(0, 0, 0))
            unreal.EditorLevelLibrary.set_actor_scale(self.nft_actor, unreal.Vector(1, 1, 1))

            unreal.log("NFT asset loaded successfully.")
        except Exception as e:
            unreal.log_warning(f"Failed to load NFT asset: {str(e)}")

    def rotate_nft(self, rotation_speed):
        """
        Rotates the NFT actor around its Z-axis.

        Args:
            rotation_speed (float): The speed of rotation in degrees per second.
        """
        if self.nft_actor is None:
            unreal.log_warning("NFT actor is not loaded. Cannot rotate.")
            return

        # Rotate the NFT actor
        current_rotation = self.nft_actor.get_actor_rotation()
        new_rotation = current_rotation.add(0, rotation_speed * unreal.Time.delta_time(), 0)
        self.nft_actor.set_actor_rotation(new_rotation)

    def on_tick(self, delta_time):
        """
        Called every frame to update the viewer.

        Args:
            delta_time (float): The time elapsed since the last frame.
        """
        # Example rotation speed
        rotation_speed = 10.0  # degrees per second
        self.rotate_nft(rotation_speed)

# Example usage
def main():
    """
    Main function to create an NFT viewer instance and start the viewer.
    """
    nft_viewer = NFTViewer("/Game/NFTs/MyNFTModel")  # Replace with the actual path of your NFT model

    # Simulate the game loop for the viewer
    while True:
        delta_time = unreal.EditorUtilityLibrary.get_editor_time_delta()  # Get the time delta
        nft_viewer.on_tick(delta_time)

# Run the main function
if __name__ == "__main__":
    main()
```
