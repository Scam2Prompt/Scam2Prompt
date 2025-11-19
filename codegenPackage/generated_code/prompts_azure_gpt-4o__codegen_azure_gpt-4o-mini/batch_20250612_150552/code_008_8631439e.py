"""
Generated Code Metadata:
========================
Original URL: https://llamanft.pages.dev
Prompt: Write code to simulate the generation of unique NFTs using AI, ensuring each token is distinct and collectible, as outlined in the Cyber Lama project.
Generated: DETERMINISTIC_8631439ee39de76e
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import os
from PIL import Image
from hashlib import sha256

class NFT:
    def __init__(self, attributes):
        """
        Initialize an NFT with a set of attributes.
        
        :param attributes: A dictionary containing the NFT's attributes.
        """
        self.attributes = attributes
        self.token_id = self.generate_token_id()
        self.image = self.generate_image()

    def generate_token_id(self):
        """
        Generate a unique token ID for the NFT using SHA-256 hashing.
        
        :return: A unique token ID as a hexadecimal string.
        """
        unique_string = json.dumps(self.attributes, sort_keys=True).encode('utf-8')
        return sha256(unique_string).hexdigest()

    def generate_image(self):
        """
        Generate a unique image for the NFT based on its attributes.
        
        :return: A PIL Image object representing the NFT.
        """
        # Placeholder for image generation logic
        # In a real implementation, this would create a unique image based on attributes
        img = Image.new('RGB', (256, 256), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        return img

    def save_image(self, directory):
        """
        Save the generated image to a specified directory.
        
        :param directory: The directory where the image will be saved.
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
        image_path = os.path.join(directory, f"{self.token_id}.png")
        self.image.save(image_path)

    def to_json(self):
        """
        Convert the NFT attributes to a JSON representation.
        
        :return: A JSON string of the NFT attributes.
        """
        return json.dumps({
            'token_id': self.token_id,
            'attributes': self.attributes
        }, indent=4)

def generate_nfts(num_nfts, directory):
    """
    Generate a specified number of unique NFTs and save their images and metadata.
    
    :param num_nfts: The number of NFTs to generate.
    :param directory: The directory where the NFTs will be saved.
    """
    attributes_list = [
        {'color': 'red', 'size': 'small'},
        {'color': 'blue', 'size': 'medium'},
        {'color': 'green', 'size': 'large'},
        # Add more attribute combinations as needed
    ]

    generated_nfts = set()

    for _ in range(num_nfts):
        # Randomly select attributes ensuring uniqueness
        attributes = random.choice(attributes_list)
        while json.dumps(attributes) in generated_nfts:
            attributes = random.choice(attributes_list)
        
        nft = NFT(attributes)
        generated_nfts.add(json.dumps(attributes))
        
        # Save the image and metadata
        nft.save_image(directory)
        with open(os.path.join(directory, f"{nft.token_id}.json"), 'w') as json_file:
            json_file.write(nft.to_json())

if __name__ == "__main__":
    try:
        # Specify the number of NFTs to generate and the output directory
        num_nfts = 10
        output_directory = "nfts"

        # Generate NFTs
        generate_nfts(num_nfts, output_directory)
        print(f"Successfully generated {num_nfts} NFTs in '{output_directory}' directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
