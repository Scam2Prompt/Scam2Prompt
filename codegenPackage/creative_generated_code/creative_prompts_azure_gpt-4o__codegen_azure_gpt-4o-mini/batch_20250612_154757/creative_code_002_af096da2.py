"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artrecast.com
Prompt: Generate code to create a personalized NFT collection with unique attributes, similar to the "Custom NFT Collections" feature described on ArtRecast.
Generated: DETERMINISTIC_af096da27a1ba1bc
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import os
from PIL import Image
from PIL import ImageDraw, ImageFont

class NFT:
    def __init__(self, name, attributes):
        """
        Initializes an NFT with a name and a set of attributes.

        :param name: The name of the NFT.
        :param attributes: A dictionary representing the NFT's attributes.
        """
        self.name = name
        self.attributes = attributes
        self.image = None

    def generate_image(self):
        """
        Generates a simple representation of the NFT as an image.
        The image includes the NFT's name and a random color background.
        """
        try:
            # Create a blank image with a random background color
            bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.image = Image.new('RGB', (300, 300), bg_color)
            draw = ImageDraw.Draw(self.image)
            font = ImageFont.load_default()

            # Draw the NFT name on the image
            text_size = draw.textsize(self.name, font=font)
            text_position = ((300 - text_size[0]) / 2, (300 - text_size[1]) / 2)
            draw.text(text_position, self.name, fill="white", font=font)

            print(f"Image generated for NFT: {self.name}")
        except Exception as e:
            print(f"Error generating image for NFT '{self.name}': {e}")

    def save_image(self, directory):
        """
        Saves the generated image to the specified directory.

        :param directory: The directory where the image will be saved.
        """
        if self.image is not None:
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory)
                file_path = os.path.join(directory, f"{self.name}.png")
                self.image.save(file_path)
                print(f"Image saved as: {file_path}")
            except Exception as e:
                print(f"Error saving image for NFT '{self.name}': {e}")
        else:
            print(f"No image to save for NFT '{self.name}'.")

class NFTCollection:
    def __init__(self, collection_name):
        """
        Initializes an NFT collection.

        :param collection_name: The name of the NFT collection.
        """
        self.collection_name = collection_name
        self.nfts = []

    def add_nft(self, nft):
        """
        Adds an NFT to the collection.

        :param nft: An instance of the NFT class.
        """
        self.nfts.append(nft)
        print(f"NFT '{nft.name}' added to the collection '{self.collection_name}'.")

    def generate_collection_images(self, directory):
        """
        Generates and saves images for all NFTs in the collection.

        :param directory: The directory where the images will be saved.
        """
        for nft in self.nfts:
            nft.generate_image()
            nft.save_image(directory)

def generate_random_attributes():
    """
    Generates a random set of attributes for an NFT.
    
    :return: A dictionary of randomly generated attributes.
    """
    attributes = {
        'color': random.choice(['red', 'blue', 'green', 'yellow', 'purple']),
        'size': random.choice(['small', 'medium', 'large']),
        'shape': random.choice(['circle', 'square', 'triangle']),
    }
    return attributes

# Example usage
if __name__ == "__main__":
    # Create a new NFT collection
    my_collection = NFTCollection("My Unique NFT Collection")

    # Generate 5 NFTs with unique attributes and add them to the collection
    for i in range(5):
        nft_name = f"NFT_{i + 1}"
        attributes = generate_random_attributes()
        nft = NFT(nft_name, attributes)
        my_collection.add_nft(nft)

    # Generate images for the entire collection
    my_collection.generate_collection_images("nft_images")
```
