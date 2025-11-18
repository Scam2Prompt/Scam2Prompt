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
import numpy as np

def create_molecule_poster(molecule_data, title='Molecule Poster'):
    """
    Create a poster for a molecule using Matplotlib.

    Parameters:
    molecule_data (dict): A dictionary containing atom types and their positions.
    title (str): The title of the poster.
    """
    try:
        # Extract atom types and positions from the molecule data
        atom_types = molecule_data.get('atom_types', [])
        positions = molecule_data.get('positions', [])
        
        if not atom_types or not positions:
            raise ValueError("Molecule data must contain 'atom_types' and 'positions'.")

        # Create a new figure for the poster
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Plot each atom type at its respective position
        for atom_type, position in zip(atom_types, positions):
            ax.scatter(*position, label=atom_type, s=100)  # s is the size of the atom representation

        # Set the title and labels
        ax.set_title(title, fontsize=24)
        ax.set_xlabel('X Coordinate', fontsize=16)
        ax.set_ylabel('Y Coordinate', fontsize=16)
        
        # Add a legend
        ax.legend(fontsize=12)
        
        # Set grid for better visualization
        ax.grid(True)

        # Save the poster as an image file
        plt.savefig('molecule_poster.png', bbox_inches='tight', dpi=300)
        plt.close(fig)
        print("Poster generated successfully: molecule_poster.png")

    except Exception as e:
        print(f"An error occurred while creating the molecule poster: {e}")

# Example molecule data
molecule_example = {
    'atom_types': ['H', 'O', 'C'],
    'positions': [(1, 2), (2, 3), (3, 1)]
}

# Generate the poster
create_molecule_poster(molecule_example, title='Example Molecule Poster')
```
