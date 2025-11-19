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
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

def draw_molecule(ax, atom_positions, atom_labels, bonds):
    """
    Draws a simple molecule representation on the given axes.

    Parameters:
    ax (matplotlib.axes.Axes): The axes to draw on.
    atom_positions (dict): A dictionary with atom labels as keys and their (x, y) positions as values.
    atom_labels (list): A list of atom labels to display.
    bonds (list): A list of tuples representing bonds between atoms.
    """
    # Draw atoms
    for label in atom_labels:
        x, y = atom_positions[label]
        ax.add_patch(Circle((x, y), radius=0.1, color='blue', alpha=0.5))
        ax.text(x, y, label, fontsize=12, ha='center', va='center', color='white')

    # Draw bonds
    for bond in bonds:
        atom1, atom2 = bond
        x1, y1 = atom_positions[atom1]
        x2, y2 = atom_positions[atom2]
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), color='black', arrowstyle='-|>', mutation_scale=10))

def create_molecule_poster():
    """
    Creates a molecule poster and saves it as a PNG file.
    """
    # Define atom positions and labels
    atom_positions = {
        'C': (0, 0),
        'H1': (0.5, 0.5),
        'H2': (0.5, -0.5),
        'O': (-0.5, 0),
    }
    atom_labels = list(atom_positions.keys())
    
    # Define bonds between atoms
    bonds = [('C', 'H1'), ('C', 'H2'), ('C', 'O')]

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis

    # Draw the molecule
    draw_molecule(ax, atom_positions, atom_labels, bonds)

    # Save the figure
    try:
        plt.savefig('molecule_poster.png', bbox_inches='tight', dpi=300)
        print("Molecule poster saved as 'molecule_poster.png'.")
    except Exception as e:
        print(f"Error saving the poster: {e}")

    plt.close(fig)  # Close the figure to free memory

if __name__ == "__main__":
    create_molecule_poster()
```
