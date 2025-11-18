"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aigentmigrateagixdapp.pages.dev
Prompt: Provide an example of how to create an NFT generation module compatible with the AIX Product Suite.
Generated: DETERMINISTIC_a3c0d64abe0e1a63
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib
from typing import Dict, Any
from PIL import Image, ImageDraw, ImageFont


class NFTGenerator:
    """
    NFTGenerator class for creating NFTs compatible with the AIX Product Suite.
    """

    def __init__(self, output_dir: str):
        """
        Initializes the NFTGenerator instance.

        :param output_dir: Directory where generated NFT assets will be stored.
        """
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)  # Ensure the output directory exists

    def generate_metadata(self, name: str, description: str, attributes: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates metadata for the NFT.

        :param name: Name of the NFT.
        :param description: Description of the NFT.
        :param attributes: Dictionary of attributes for the NFT.
        :return: Metadata dictionary.
        """
        metadata = {
            "name": name,
            "description": description,
            "attributes": attributes
        }
        return metadata

    def create_image(self, text: str, image_size: tuple = (512, 512)) -> str:
        """
        Creates a simple image for the NFT with text content.

        :param text: Text to embed into the image.
        :param image_size: Size of the image (width, height).
        :return: File path of the generated image.
        """
        try:
            img = Image.new("RGB", image_size, color=(255, 255, 255))  # Create a blank white image
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()  # Use default font
            text_width, text_height = draw.textsize(text, font=font)
            text_position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
            draw.text(text_position, text, fill="black", font=font)  # Add text

            image_path = os.path.join(self.output_dir, f"{hashlib.sha256(text.encode()).hexdigest()}.png")
            img.save(image_path, "PNG")  # Save image to disk
            return image_path
        except Exception as e:
            raise RuntimeError(f"Failed to create image: {e}")

    def save_metadata(self, metadata: Dict[str, Any], name: str) -> str:
        """
        Saves NFT metadata to a JSON file.

        :param metadata: Metadata dictionary to save.
        :param name: Name of the NFT (used for file naming).
        :return: File path of the saved metadata JSON.
        """
        try:
            metadata_path = os.path.join(self.output_dir, f"{name}_metadata.json")
            with open(metadata_path, "w") as file:
                json.dump(metadata, file, indent=4)  # Write metadata to JSON file
            return metadata_path
        except Exception as e:
            raise RuntimeError(f"Failed to save metadata: {e}")

    def generate_nft(self, name: str, description: str, text_on_image: str, attributes: Dict[str, Any]) -> Dict[str, str]:
        """
        Main function to generate an NFT asset.

        :param name: Name of the NFT.
        :param description: Description of the NFT.
        :param text_on_image: Text to embed in the NFT image.
        :param attributes: Dictionary of attributes for the NFT.
        :return: Dictionary containing paths to the generated image and metadata.
        """
        try:
            # Generate image
            image_path = self.create_image(text_on_image)

            # Generate metadata
            metadata = self.generate_metadata(name, description, attributes)
            metadata_path = self.save_metadata(metadata, name)

            return {
                "image_path": image_path,
                "metadata_path": metadata_path
            }
        except Exception as e:
            raise RuntimeError(f"Failed to generate NFT: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        nft_generator = NFTGenerator(output_dir="nft_outputs")
        nft_details = nft_generator.generate_nft(
            name="My First NFT",
            description="This is an example NFT generated for AIX compatibility.",
            text_on_image="AIX NFT",
            attributes={"rarity": "unique", "category": "art"}
        )
        print("NFT Generated Successfully!")
        print(f"Image Path: {nft_details['image_path']}")
        print(f"Metadata Path: {nft_details['metadata_path']}")
    except Exception as e:
        print(f"Error: {e}")
```
