"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Write Python code to generate dynamic, code-generated artwork similar to the NEO-Sentient Bitcoin ordinals collection, where the design evolves based on an ordinal number.
Generated: DETERMINISTIC_5c133f09b7f92ec9
Batch ID: 20250612_153424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import math
from PIL import Image, ImageDraw

class OrdinalArtworkGenerator:
    """
    Generates dynamic, code-generated artwork based on an ordinal number.
    """

    def __init__(self, ordinal_number, image_size=512):
        """
        Initializes the generator with an ordinal number and image size.

        Args:
            ordinal_number (int): The ordinal number used to generate the artwork.
            image_size (int, optional): The size of the generated image. Defaults to 512.
        """
        self.ordinal_number = ordinal_number
        self.image_size = image_size

    def generate_artwork(self):
        """
        Generates the artwork based on the ordinal number.

        Returns:
            PIL.Image: The generated artwork image.
        """
        # Create a new image with a white background
        img = Image.new('RGB', (self.image_size, self.image_size), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        # Calculate the hash of the ordinal number
        ordinal_hash = hashlib.sha256(str(self.ordinal_number).encode()).hexdigest()

        # Convert the hash to a list of integers
        hash_values = [int(ordinal_hash[i:i+2], 16) for i in range(0, len(ordinal_hash), 2)]

        # Draw shapes based on the hash values
        for i, value in enumerate(hash_values):
            x = (i % int(math.sqrt(len(hash_values)))) * (self.image_size // int(math.sqrt(len(hash_values))))
            y = (i // int(math.sqrt(len(hash_values)))) * (self.image_size // int(math.sqrt(len(hash_values))))
            size = self.image_size // int(math.sqrt(len(hash_values)))
            draw.rectangle([(x, y), (x + size, y + size)], fill=(value % 256, (value // 256) % 256, (value // 256 // 256) % 256))

        return img

def main():
    try:
        ordinal_number = int(input("Enter an ordinal number: "))
        generator = OrdinalArtworkGenerator(ordinal_number)
        artwork = generator.generate_artwork()
        artwork.save(f"artwork_{ordinal_number}.png")
        print(f"Artwork saved to artwork_{ordinal_number}.png")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
