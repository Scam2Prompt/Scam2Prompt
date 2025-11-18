"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thisismyiguana.pages.dev
Prompt: Create a program that generates a molecule poster similar to the one mentioned in "Brian's room," using Python libraries like Matplotlib or PIL.
Generated: DETERMINISTIC_7bab386d2ccbb3fa
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def create_molecule_poster(output_file='molecule_poster.png'):
    """
    Generates a molecule poster using Matplotlib and PIL.

    Args:
        output_file (str): Filename for the output poster image.
    """
    try:
        # Set up the poster dimensions
        poster_width = 800
        poster_height = 1200

        # Create a blank image
        poster = Image.new("RGB", (poster_width, poster_height), color="white")
        draw = ImageDraw.Draw(poster)

        # Define fonts
        try:
            font_title = ImageFont.truetype("arial.ttf", 48)
            font_subtitle = ImageFont.truetype("arial.ttf", 36)
            font_label = ImageFont.truetype("arial.ttf", 24)
        except IOError:
            # Fallback to default PIL font if custom fonts are unavailable
            font_title = ImageFont.load_default()
            font_subtitle = ImageFont.load_default()
            font_label = ImageFont.load_default()

        # Add title to the poster
        draw.text((poster_width // 2 - 200, 50), "Molecule Poster", fill="black", font=font_title)

        # Draw example "molecule" using circles and lines
        molecule_center_x = poster_width // 2
        molecule_center_y = 400
        molecule_radius = 150

        # Outer atoms
        outer_atom_positions = [
            (molecule_center_x - molecule_radius, molecule_center_y),
            (molecule_center_x + molecule_radius, molecule_center_y),
            (molecule_center_x, molecule_center_y - molecule_radius),
            (molecule_center_x, molecule_center_y + molecule_radius)
        ]

        # Draw bonds (lines)
        for atom in outer_atom_positions:
            draw.line([atom, (molecule_center_x, molecule_center_y)], fill="black", width=5)

        # Draw central atom
        draw.ellipse(
            [molecule_center_x - 40, molecule_center_y - 40,
             molecule_center_x + 40, molecule_center_y + 40],
            fill="blue", outline="black"
        )

        # Draw outer atoms
        for atom in outer_atom_positions:
            draw.ellipse(
                [atom[0] - 30, atom[1] - 30, atom[0] + 30, atom[1] + 30],
                fill="red", outline="black"
            )

        # Add molecule label
        draw.text((poster_width // 2 - 100, 600), "Sample Molecule Structure", fill="black", font=font_subtitle)

        # Save the poster
        poster.save(output_file)
        print(f"Molecule poster saved as: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_molecule_poster()
```
