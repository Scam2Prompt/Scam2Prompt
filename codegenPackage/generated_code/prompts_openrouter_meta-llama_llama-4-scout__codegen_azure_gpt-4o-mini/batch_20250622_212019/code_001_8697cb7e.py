"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: "Write a Python script to generate nail art designs using aerography techniques, incorporating stencils from the Airstyleart collection."
Generated: DETERMINISTIC_8697cb7e0eba1719
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import os
from PIL import Image, ImageDraw

class NailArtGenerator:
    def __init__(self, stencil_directory):
        """
        Initializes the NailArtGenerator with the path to the stencil directory.

        :param stencil_directory: Path to the directory containing stencil images.
        """
        self.stencil_directory = stencil_directory
        self.stencils = self.load_stencils()

    def load_stencils(self):
        """
        Loads stencil images from the specified directory.

        :return: A list of stencil images.
        """
        stencils = []
        try:
            for filename in os.listdir(self.stencil_directory):
                if filename.endswith('.png'):
                    stencil_path = os.path.join(self.stencil_directory, filename)
                    stencil_image = Image.open(stencil_path).convert("RGBA")
                    stencils.append(stencil_image)
        except Exception as e:
            print(f"Error loading stencils: {e}")
        return stencils

    def generate_nail_art(self, base_color=(255, 182, 193), output_size=(100, 100)):
        """
        Generates a nail art design using random stencils.

        :param base_color: The base color of the nail art (RGB tuple).
        :param output_size: The size of the output image.
        :return: An Image object representing the nail art design.
        """
        # Create a blank canvas for the nail art
        nail_art = Image.new("RGBA", output_size, base_color)
        draw = ImageDraw.Draw(nail_art)

        # Randomly select and apply stencils
        for stencil in random.sample(self.stencils, k=min(3, len(self.stencils))):
            # Random position for the stencil
            x = random.randint(0, output_size[0] - stencil.width)
            y = random.randint(0, output_size[1] - stencil.height)

            # Composite the stencil onto the nail art
            nail_art.paste(stencil, (x, y), stencil)

        return nail_art

    def save_nail_art(self, nail_art_image, output_path):
        """
        Saves the generated nail art image to the specified path.

        :param nail_art_image: The Image object to save.
        :param output_path: The file path where the image will be saved.
        """
        try:
            nail_art_image.save(output_path, format='PNG')
            print(f"Nail art saved to {output_path}")
        except Exception as e:
            print(f"Error saving nail art: {e}")

def main():
    # Define the path to the stencil directory and output file
    stencil_directory = 'path/to/stencils'  # Update this path
    output_file = 'nail_art_design.png'

    # Create an instance of the NailArtGenerator
    generator = NailArtGenerator(stencil_directory)

    # Generate a nail art design
    nail_art = generator.generate_nail_art()

    # Save the generated nail art
    generator.save_nail_art(nail_art, output_file)

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have the `Pillow` library installed to run this script. You can install it using `pip install Pillow`. Update the `stencil_directory` variable with the correct path to your stencil images before running the script.
