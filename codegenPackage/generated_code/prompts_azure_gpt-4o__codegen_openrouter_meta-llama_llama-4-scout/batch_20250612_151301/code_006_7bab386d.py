"""
Generated Code Metadata:
========================
Original URL: https://thisismyiguana.pages.dev
Prompt: Create a program that generates a molecule poster similar to the one mentioned in "Brian's room," using Python libraries like Matplotlib or PIL.
Generated: DETERMINISTIC_7bab386d2ccbb3fa
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

# Function to generate molecule poster
def generate_molecule_poster(width=800, height=600, num_molecules=100):
    # Create a new image with white background
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Set font for molecule labels
    font = ImageFont.load_default()

    # Generate random molecules
    for _ in range(num_molecules):
        # Random molecule properties
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(10, 50)
        num_atoms = random.randint(2, 10)
        atom_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_atoms)]

        # Draw molecule circle
        draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], outline=(0, 0, 0))

        # Draw atoms
        for i in range(num_atoms):
            atom_x = x + int(radius * 0.5 * np.cos(2 * np.pi * i / num_atoms))
            atom_y = y + int(radius * 0.5 * np.sin(2 * np.pi * i / num_atoms))
            draw.ellipse([(atom_x - 5, atom_y - 5), (atom_x + 5, atom_y + 5)], fill=atom_colors[i])
            draw.text((atom_x + 10, atom_y - 5), f'Atom {i+1}', font=font, fill=(0, 0, 0))

        # Draw bonds
        for i in range(num_atoms - 1):
            bond_x1 = x + int(radius * 0.5 * np.cos(2 * np.pi * i / num_atoms))
            bond_y1 = y + int(radius * 0.5 * np.sin(2 * np.pi * i / num_atoms))
            bond_x2 = x + int(radius * 0.5 * np.cos(2 * np.pi * (i + 1) / num_atoms))
            bond_y2 = y + int(radius * 0.5 * np.sin(2 * np.pi * (i + 1) / num_atoms))
            draw.line([(bond_x1, bond_y1), (bond_x2, bond_y2)], fill=(0, 0, 0))

    # Save the image
    img.save('molecule_poster.png')

# Generate and display the poster
generate_molecule_poster()

# Alternatively, use Matplotlib to generate the poster
def generate_molecule_poster_matplotlib(width=8, height=6, num_molecules=100):
    fig, ax = plt.subplots(figsize=(width, height))

    for _ in range(num_molecules):
        x = random.random() * width
        y = random.random() * height
        radius = random.random() * 2 + 1
        num_atoms = random.randint(2, 10)

        circle = patches.Circle((x, y), radius, edgecolor='black', facecolor='none', lw=2)
        ax.add_patch(circle)

        for i in range(num_atoms):
            atom_x = x + radius * 0.5 * np.cos(2 * np.pi * i / num_atoms)
            atom_y = y + radius * 0.5 * np.sin(2 * np.pi * i / num_atoms)
            ax.plot(atom_x, atom_y, 'o', markersize=5, color=[random.random() for _ in range(3)])
            ax.text(atom_x + 0.2, atom_y - 0.2, f'Atom {i+1}', ha='center')

        for i in range(num_atoms - 1):
            bond_x1 = x + radius * 0.5 * np.cos(2 * np.pi * i / num_atoms)
            bond_y1 = y + radius * 0.5 * np.sin(2 * np.pi * i / num_atoms)
            bond_x2 = x + radius * 0.5 * np.cos(2 * np.pi * (i + 1) / num_atoms)
            bond_y2 = y + radius * 0.5 * np.sin(2 * np.pi * (i + 1) / num_atoms)
            ax.plot([bond_x1, bond_x2], [bond_y1, bond_y2], color='black')

    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    plt.savefig('molecule_poster_matplotlib.png', bbox_inches='tight')

generate_molecule_poster_matplotlib()
```
