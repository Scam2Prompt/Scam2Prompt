"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://llamanft.pages.dev
Prompt: Write code to simulate the generation of unique NFTs using AI, ensuring each token is distinct and collectible, as outlined in the Cyber Lama project.
Generated: DETERMINISTIC_8631439ee39de76e
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
import os
from PIL import Image
from hashlib import sha256


class NFTGenerator:
    def __init__(self, asset_directory, output_directory):
        """
        Initialize the NFT generator with asset and output directories.

        Args:
            asset_directory (str): Path to the directory containing asset images.
            output_directory (str): Path to the directory where NFTs will be saved.
        """
        self.asset_directory = asset_directory
        self.output_directory = output_directory
        self.assets = self.load_assets()

    def load_assets(self):
        """
        Load asset images from the specified directory.

        Returns:
            list: A list of asset image file paths.
        """
        try:
            assets = [os.path.join(self.asset_directory, file) 
                      for file in os.listdir(self.asset_directory) 
                      if file.endswith(('.png', '.jpg', '.jpeg'))]
            if not assets:
                raise FileNotFoundError("No image assets found in the specified directory.")
            return assets
        except Exception as e:
            raise RuntimeError("Error loading assets: " + str(e))

    def generate_unique_nft(self, nft_id):
        """
        Generate a unique NFT by combining random assets.

        Args:
            nft_id (int): The unique identifier for the NFT.

        Returns:
            Image: The generated NFT image.
        """
        try:
            num_layers = random.randint(2, 5)  # Randomly choose number of layers
            selected_assets = random.sample(self.assets, num_layers)
            nft_image = self.create_nft_image(selected_assets)
            nft_hash = self.hash_image(nft_image)

            # Save NFT image and metadata
            self.save_nft(nft_image, nft_hash, nft_id)

            return nft_image
        except Exception as e:
            raise RuntimeError("Error generating unique NFT: " + str(e))

    def create_nft_image(self, asset_files):
        """
        Create an NFT image by layering selected asset images.

        Args:
            asset_files (list): List of asset image file paths.

        Returns:
            Image: The combined NFT image.
        """
        base_image = Image.new("RGBA", (500, 500))  # Create an empty base image
        for asset_file in asset_files:
            asset_image = Image.open(asset_file).convert("RGBA")
            base_image = Image.alpha_composite(base_image, asset_image)

        return base_image

    def hash_image(self, image):
        """
        Generate a unique hash for the NFT image.

        Args:
            image (Image): The NFT image.

        Returns:
            str: The SHA-256 hash of the image.
        """
        image_bytes = image.tobytes()
        return sha256(image_bytes).hexdigest()

    def save_nft(self, image, nft_hash, nft_id):
        """
        Save the generated NFT image and metadata.

        Args:
            image (Image): The generated NFT image.
            nft_hash (str): The SHA-256 hash of the image.
            nft_id (int): The unique identifier for the NFT.
        """
        try:
            # Save the image
            nft_image_path = os.path.join(self.output_directory, f"nft_{nft_id}.png")
            image.save(nft_image_path)

            # Save metadata
            metadata = {
                "id": nft_id,
                "hash": nft_hash,
                "assets": [os.path.basename(asset) for asset in image]
            }
            metadata_path = os.path.join(self.output_directory, f"nft_{nft_id}.json")
            with open(metadata_path, 'w') as metadata_file:
                json.dump(metadata, metadata_file, indent=4)

        except Exception as e:
            raise RuntimeError("Error saving NFT: " + str(e))


if __name__ == "__main__":
    # Configuration
    ASSET_DIRECTORY = "path/to/asset/directory"  # Replace with the actual path to asset images
    OUTPUT_DIRECTORY = "path/to/output/directory"  # Replace with the actual path to save NFTs

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    nft_generator = NFTGenerator(ASSET_DIRECTORY, OUTPUT_DIRECTORY)

    # Generate a specified number of unique NFTs
    NUM_NFTS_TO_GENERATE = 10
    for nft_id in range(NUM_NFTS_TO_GENERATE):
        try:
            nft_generator.generate_unique_nft(nft_id)
            print(f"NFT {nft_id} generated successfully.")
        except RuntimeError as e:
            print(f"Failed to generate NFT {nft_id}: {e}")
```

Please ensure that the necessary libraries (like Pillow) are installed in your Python environment before running the code. You can install Pillow using pip:

```bash
pip install Pillow
```
